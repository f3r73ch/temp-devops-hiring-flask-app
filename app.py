from flask import Flask, jsonify
import mysql.connector
#
from config import DB_CONFIG  # import configuration



app = Flask(__name__)

@app.route('/users', methods=['GET'])
def list_users():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        # Fetch users
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(users)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


if __name__ == "__main__":
    # Listen on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
