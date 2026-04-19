from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

AZURE_PRICES = {
    "Standard_B1": 0.01,
    "Standard_B2": 0.09,
    "Basic_mySQL": 0.05
}

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS estimates 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 resource TEXT, hours REAL, total REAL)''')
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.json
    resource = data.get('resource')
    
    try:
        hours = float(data.get('hours', 0))
    except (ValueError, TypeError):
        hours = 0
    
    unit_price = AZURE_PRICES.get(resource, 0)
    total_cost = round(unit_price * hours, 2)
    
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO estimates (resource, hours, total) VALUES (?, ?, ?)",
                 (resource, hours, total_cost))
    conn.commit()
    conn.close()
    
    return jsonify({
        "cost": total_cost, 
        "template_hint": f"az vm create --name {resource}..."
    })
@app.route('/history_data')
def history_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT resource, hours, total FROM estimates ORDER BY id DESC LIMIT 5")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
