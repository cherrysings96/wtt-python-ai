import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "echovault_secret_key_dev"
DB_NAME = "studio.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Table 1: Vocal Projects (Songs/Covers)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            original_artist TEXT NOT NULL,
            original_key TEXT NOT NULL,
            transposed_key TEXT NOT NULL,
            bpm INTEGER NOT NULL,
            status TEXT DEFAULT 'Recording',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Table 2: Recording Takes (Linked to Projects)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS takes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            take_number INTEGER NOT NULL,
            section TEXT NOT NULL,
            mic_chain TEXT NOT NULL,
            pitch_score INTEGER NOT NULL,
            timing_score INTEGER NOT NULL,
            vibe_score INTEGER NOT NULL,
            composite_score REAL NOT NULL,
            vocal_strain TEXT NOT NULL,
            notes TEXT,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
        )
    """)

    # Seed sample data if empty
    cursor.execute("SELECT COUNT(*) FROM projects")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO projects (title, original_artist, original_key, transposed_key, bpm, status)
            VALUES 
            ('Rolling in the Deep (Acoustic Cover)', 'Adele', 'C Minor', 'B Minor (-1)', 105, 'Mixing'),
            ('Valerie (Soul Arrangement)', 'Amy Winehouse', 'Eb Major', 'Eb Major (0)', 106, 'Recording'),
            ('Drivers License (Piano Ballad)', 'Olivia Rodrigo', 'Bb Major', 'A Major (-1)', 72, 'Mastered')
        """)

        cursor.execute("""
            INSERT INTO takes (project_id, take_number, section, mic_chain, pitch_score, timing_score, vibe_score, composite_score, vocal_strain, notes)
            VALUES 
            (1, 1, 'Chorus High Belt', 'Shure SM7B + Cloudlifter (Gain 60%)', 8, 9, 9, 86.5, 'Low', 'Clean chest-mix transition on the high C.'),
            (1, 2, 'Bridge Stacked Harmony', 'AT2020 Condenser (Pop Filter 4 in)', 9, 8, 10, 91.0, 'Moderate', 'Slightly breathy tone works well for the backing track.'),
            (2, 1, 'Verse 1 Groove', 'Shure SM7B (Flat EQ)', 7, 8, 8, 76.5, 'Low', 'Rushed the second bar slightly; good warmth.')
        """)

    conn.commit()
    conn.close()


def calculate_readiness(pitch, timing, vibe):
    """
    Custom weighted studio algorithm:
    Vibe/Delivery (40%), Pitch Accuracy (35%), Pocket/Timing (25%)
    Returns a 0-100 Mix-Readiness Percentage.
    """
    weighted = (pitch * 0.35) + (timing * 0.25) + (vibe * 0.40)
    return round(weighted * 10, 1)


@app.route("/")
def index():
    conn = get_db_connection()

    # Fetch projects with aggregated take metrics using SQL LEFT JOIN
    projects = conn.execute("""
        SELECT 
            p.*,
            COUNT(t.id) AS total_takes,
            ROUND(AVG(t.composite_score), 1) AS avg_readiness,
            MAX(t.composite_score) AS best_take_score
        FROM projects p
        LEFT JOIN takes t ON p.id = t.project_id
        GROUP BY p.id
        ORDER BY p.created_at DESC
    """).fetchall()

    # Fetch recent takes with project names
    recent_takes = conn.execute("""
        SELECT t.*, p.title AS project_title, p.transposed_key
        FROM takes t
        JOIN projects p ON t.project_id = p.id
        ORDER BY t.recorded_at DESC
        LIMIT 10
    """).fetchall()

    # Studio summary metrics
    stats = conn.execute("""
        SELECT 
            (SELECT COUNT(*) FROM projects) AS project_count,
            COUNT(*) AS total_takes,
            ROUND(AVG(composite_score), 1) AS studio_avg_score,
            SUM(CASE WHEN vocal_strain = 'High' THEN 1 ELSE 0 END) AS high_strain_count
        FROM takes
    """).fetchone()

    conn.close()
    return render_template("index.html", projects=projects, takes=recent_takes, stats=stats)


@app.route("/add_project", methods=["POST"])
def add_project():
    title = request.form.get("title")
    original_artist = request.form.get("original_artist")
    original_key = request.form.get("original_key")
    transposed_key = request.form.get("transposed_key")
    bpm = request.form.get("bpm", type=int)
    status = request.form.get("status")

    conn = get_db_connection()
    conn.execute("""
        INSERT INTO projects (title, original_artist, original_key, transposed_key, bpm, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, original_artist, original_key, transposed_key, bpm, status))
    conn.commit()
    conn.close()

    flash(f"Added '{title}' to active studio sessions!", "success")
    return redirect(url_for("index"))


@app.route("/add_take", methods=["POST"])
def add_take():
    project_id = request.form.get("project_id", type=int)
    section = request.form.get("section")
    mic_chain = request.form.get("mic_chain")
    pitch_score = request.form.get("pitch_score", type=int)
    timing_score = request.form.get("timing_score", type=int)
    vibe_score = request.form.get("vibe_score", type=int)
    vocal_strain = request.form.get("vocal_strain")
    notes = request.form.get("notes")

    composite_score = calculate_readiness(pitch_score, timing_score, vibe_score)

    conn = get_db_connection()
    # Auto-increment take number per project
    cur = conn.execute("SELECT COALESCE(MAX(take_number), 0) + 1 FROM takes WHERE project_id = ?", (project_id,))
    next_take_num = cur.fetchone()[0]

    conn.execute("""
        INSERT INTO takes 
        (project_id, take_number, section, mic_chain, pitch_score, timing_score, vibe_score, composite_score, vocal_strain, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (project_id, next_take_num, section, mic_chain, pitch_score, timing_score, vibe_score, composite_score, vocal_strain, notes))
    conn.commit()
    conn.close()

    flash(f"Logged Take #{next_take_num} — Mix-Readiness Score: {composite_score}%", "info")
    return redirect(url_for("index"))


@app.route("/update_status/<int:project_id>", methods=["POST"])
def update_status(project_id):
    new_status = request.form.get("status")
    conn = get_db_connection()
    conn.execute("UPDATE projects SET status = ? WHERE id = ?", (new_status, project_id))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/delete_project/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM takes WHERE project_id = ?", (project_id,))
    conn.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()
    flash("Project removed from studio vault.", "warning")
    return redirect(url_for("index"))


init_db()


if __name__ == "__main__":
    init_db()
    app.run(debug=True)