# 🎙️ EchoVault — Vocal Take & Studio Telemetry System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Relational_SQL-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

**EchoVault** is a specialized full-stack studio production and vocal telemetry web application built for recording vocalists, music producers, and audio creators. Rather than relying on scattered spreadsheets or voice memos during recording sessions, EchoVault tracks song repertoire, key transpositions, microphone/preamp signal chains, and individual vocal takes—dynamically computing a weighted **Mix-Readiness Score** and monitoring vocal strain across sessions.

---

## ✨ Key Features

* **Weighted Mix-Readiness Algorithm:** Automatically calculates a composite readiness percentage (`0–100%`) for every logged vocal take using a weighted studio formula:
  * **Emotional Delivery / Vibe:** `40%`
  * **Pitch Accuracy:** `35%`
  * **Pocket & Timing:** `25%`
* **Repertoire & Transposition Vault:** Tracks original keys alongside custom transposed studio vocal keys, tempos (BPM), and production workflow stages (`Recording`, `Mixing`, `Mastered`).
* **Signal Chain & Take Logging:** Logs specific song sections (e.g., *Chorus High Belt*, *Bridge Stacked Harmony*), microphone/preamp gain settings, and timestamped producer notes with automatic per-project take numbering.
* **Vocal Fatigue Telemetry:** Monitors session strain levels (`Low`, `Moderate`, `High`) and triggers dashboard alerts when high-strain takes accumulate, helping vocalists prevent burnout and schedule vocal rest.
* **Relational SQL Aggregations:** Uses raw SQL `LEFT JOIN`, `GROUP BY`, `COALESCE`, and conditional `CASE` aggregations to compute real-time studio statistics without ORM overhead.

---

## 🛠️ Tech Stack & Architecture

* **Backend:** Python, Flask (Routing, Jinja2 Templating, Flash Messaging)
* **Database:** SQLite3 with Relational Foreign Key Constraints (`ON DELETE CASCADE`)
* **Frontend:** HTML5, CSS3 (Custom Dark-Mode Studio Theme), Bootstrap 5.3, Vanilla JavaScript

### Database Schema (`studio.db`)

1. **`projects` Table:**
   * `id` (Primary Key), `title`, `original_artist`, `original_key`, `transposed_key`, `bpm`, `status`, `created_at`
2. **`takes` Table:**
   * `id` (Primary Key), `project_id` (Foreign Key -> `projects.id`), `take_number`, `section`, `mic_chain`, `pitch_score`, `timing_score`, `vibe_score`, `composite_score`, `vocal_strain`, `notes`, `recorded_at`

---

## 🚀 Getting Started (Run Locally)

### 1. Clone the repository
```bash
git clone [https://github.com/cherrysings96/echovault-studio.git](https://github.com/cherrysings96/echovault-studio.git)
cd echovault-studio
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```
*Note: On first launch, `app.py` automatically initializes `studio.db` and seeds it with sample studio arrangements and vocal takes so you can explore the dashboard immediately.*

### 4. Open in browser
Navigate to `http://127.0.0.1:5000` in your browser.

---

## 📂 Project Structure

```text
echovault-studio/
│
├── app.py                  # Flask server, SQL schema initialization & scoring engine
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Excluded environment and local database files
└── templates/
    └── index.html          # Dark-mode studio UI, telemetry cards & modals
```

---

## 💡 Future Enhancements
* Audio snippet upload (`.wav` / `.mp3`) attached to individual takes with an embedded waveform player.
* Interactive Chart.js vocal pitch and readiness trendlines across multi-day recording sessions.
* Exportable PDF session sheets for mixing and mastering engineers.

---

## 👩‍💻 Author
**Sherene Antony**  
[GitHub Profile](https://github.com/cherrysings96)