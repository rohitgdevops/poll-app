from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = psycopg2.connect(
        host="postgres-db",  # Docker Compose service name for the DB
        port=5432,
        user="postgres",
        password="mysecretpassword",
        dbname="pollapp"
    )
    return conn

# Home page route
@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM polls;')  # Get all polls
    polls = cur.fetchall()
    conn.close()
    return render_template('index.html', polls=polls)

# Poll creation route
@app.route('/create', methods=['POST'])
def create_poll():
    poll_title = request.form['title']
    option_1 = request.form['option_1']
    option_2 = request.form['option_2']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO polls (title, option_1, option_2) VALUES (%s, %s, %s)', 
                (poll_title, option_1, option_2))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

# Voting route
@app.route('/vote/<int:poll_id>', methods=['POST'])
def vote(poll_id):
    choice = request.form['choice']
    conn = get_db_connection()
    cur = conn.cursor()

    if choice == '1':
        cur.execute('UPDATE polls SET votes_1 = votes_1 + 1 WHERE id = %s', (poll_id,))
    elif choice == '2':
        cur.execute('UPDATE polls SET votes_2 = votes_2 + 1 WHERE id = %s', (poll_id,))
    
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # Change 127.0.0.1 to 0.0.0.0

