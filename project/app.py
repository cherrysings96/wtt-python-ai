from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import numpy as np
import joblib

app = Flask(__name__)
app.secret_key = 'super_secret_ecommerce_key'

# Load trained ML model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Replace with your MySQL password
    'database': 'ecommerce_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    prob_score = None
    alert_style = "info"

    if request.method == 'POST':
        try:
            # 1. Fetch form inputs
            customer_name = request.form['customer_name']
            admin_pages = int(request.form['admin_pages'])
            info_pages = int(request.form['info_pages'])
            product_pages = int(request.form['product_pages'])
            product_duration = float(request.form['product_duration'])
            bounce_rate = float(request.form['bounce_rate'])
            exit_rate = float(request.form['exit_rate'])
            page_value = float(request.form['page_value'])
            visitor_type = request.form['visitor_type']
            weekend = request.form['weekend']

            # 2. Encode categorical inputs for ML model
            visitor_numeric = 1 if visitor_type == 'Returning Visitor' else 0
            weekend_numeric = 1 if weekend == 'Yes' else 0

            # 3. Scale features and predict
            input_features = np.array([[
                admin_pages, info_pages, product_pages, product_duration,
                bounce_rate, exit_rate, page_value, visitor_numeric, weekend_numeric
            ]])
            input_scaled = scaler.transform(input_features)
            
            pred_class = model.predict(input_scaled)[0]
            pred_prob = round(float(model.predict_proba(input_scaled)[0][1]) * 100, 2)

            if pred_class == 1:
                prediction_text = "Likely to Purchase"
                alert_style = "success"
            else:
                prediction_text = "Unlikely to Purchase"
                alert_style = "warning"

            prob_score = pred_prob

            # 4. Save record to MySQL
            conn = get_db_connection()
            cursor = conn.cursor()
            sql_insert = """
                INSERT INTO prediction_logs 
                (customer_name, admin_pages, info_pages, product_pages, product_duration, 
                 bounce_rate, exit_rate, page_value, visitor_type, weekend, prediction_result, probability)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_insert, (
                customer_name, admin_pages, info_pages, product_pages, product_duration,
                bounce_rate, exit_rate, page_value, visitor_type, weekend, prediction_text, prob_score
            ))
            conn.commit()
            cursor.close()
            conn.close()

        except Exception as e:
            flash(f"Error processing prediction: {str(e)}", "danger")

    # Fetch recent predictions from MySQL to display in table
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM prediction_logs ORDER BY created_at DESC LIMIT 10")
    history = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        'index.html',
        prediction_text=prediction_text,
        prob_score=prob_score,
        alert_style=alert_style,
        history=history
    )

@app.route('/delete/<int:log_id>')
def delete_log(log_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prediction_logs WHERE id = %s", (log_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)