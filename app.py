from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

# [생략된 init_db 함수는 동일]

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        
        conn = sqlite3.connect('urls.db')
        conn.execute('INSERT INTO urls (short_code, long_url) VALUES (?, ?)', (short_code, long_url))
        conn.commit()
        conn.close()
        
        short_url = f"http://127.0.0.1:5000/{short_code}"
    
    return render_template('index.html', short_url=short_url)

# [생략된 redirect_url 함수는 동일]

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
