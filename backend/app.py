from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# 設定資料庫路徑
DB_PATH = 'order.db'

def init_db():
    try:
        # 確保資料庫目錄存在
        db_dir = os.path.dirname(DB_PATH)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                drink_name TEXT NOT NULL,
                sugar TEXT NOT NULL,
                ice TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                order_time TIMESTAMP NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("資料庫初始化成功")
    except Exception as e:
        print("資料庫初始化錯誤:", str(e))

@app.route('/api/submit-order', methods=['POST'])
def submit_order():
    try:
        data = request.get_json()
        print("收到的訂單資料:", data)  # 偵錯用
        
        if not data or 'orders' not in data:
            return jsonify({
                "status": "error",
                "message": "無效的訂單資料"
            }), 400

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        for order in data['orders']:
            print("正在處理訂單:", order)  # 偵錯用
            try:
                c.execute('''
                    INSERT INTO orders 
                    (drink_name, sugar, ice, quantity, order_time) 
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    order['name'],
                    order['sugar'],
                    order['ice'],
                    order['quantity'],
                    datetime.now().isoformat()
                ))
                print(f"成功插入訂單: {order['name']}")  # 偵錯用
            except sqlite3.Error as e:
                print(f"插入訂單時發生錯誤: {str(e)}")
                raise e

        conn.commit()
        print("所有訂單已提交到資料庫")  # 偵錯用
        conn.close()
        
        return jsonify({
            "status": "success",
            "message": "訂單已成功儲存"
        })
    except Exception as e:
        print("訂單處理錯誤:", str(e))
        return jsonify({
            "status": "error",
            "message": f"訂單處理錯誤: {str(e)}"
        }), 500

# 新增一個測試路由來確認資料庫連接
@app.route('/api/test-db', methods=['GET'])
def test_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM orders')
        count = c.fetchone()[0]
        conn.close()
        return jsonify({
            "status": "success",
            "message": f"資料庫連接成功，目前有 {count} 筆訂單"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"資料庫測試錯誤: {str(e)}"
        }), 500

# 初始化資料庫
init_db()

if __name__ == '__main__':
    app.run(debug=True, port=5000) 