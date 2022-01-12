from flask import Flask, request
import sqlite3
import threading

lock = threading.Lock()

app = Flask(__name__)

con = sqlite3.connect('payments.db', check_same_thread=False)
cur = con.cursor()

@app.route('/yoomoney', methods=['POST'])
def hello():
    data = request.values
    amount = data['amount']
    label = data['label']
    with lock:
        cur.execute(f'UPDATE yoomoney SET completed = 1 WHERE comment = "{label}" and amount >= "{amount}"')
        con.commit()
    return {'status': 'OK'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)