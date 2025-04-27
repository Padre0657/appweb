from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = psycopg2.connect(dbname="testdb", user="user", password="password", host="postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
