from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.events import get_events, get_event_by_id
from models.bookings import get_bookings_by_user_id, add_booking, display_bookings_by_user_id
from models.users import get_users, get_user_by_id, add_user
from utils.date import check_valid_date

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    # TODO: Menampilkan halaman utama dan data seluruh acara
    events = get_events()
    return render_template('index.html', events=events)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Menampilkan halaman login dan melakukan proses login
    if request.method == 'POST':
        email = request.form['surel']
        password = request.form['kata_sandi']
        # user = get_users

        if email == 'admin@mail.com' and password == 'admin1234#':
            session['email'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')


    #     if request.method == 'POST':
    #     email = request.form['surel']
    #     password = request.form['kata_sandi']
    #     cur = mysql.connection.cursor()
    #     cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    #     user = cur.fetchone()
    #     cur.close()
    #     if user:
    #         if check_password_hash(user[2], password):
    #             session['is_logged_in'] = True
    #             session['user_id'] = user[0]
    #             return redirect(url_for('index'))
    #         flash("Kata sandi salah")
    #         return redirect(url_for('login'))
    #     flash("Email tidak terdaftar")
    #     return redirect(url_for('login'))
    # return render_template('login.html')

        
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # TODO: Menampilkan halaman register dan melakukan proses register
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # TODO: Menampilkan seluruh acara dan tiket yang telah dibeli oleh user
    events = get_events()
    return render_template('dashboard.html', events=events)

@app.route('/booking/<int:event_id>')
def booking(event_id: int):
    # TODO: Membeli tiket pada event tertentu

    return None

@app.route('/logout')
def logout():
    # TODO: Keluar akun dan menghapus session yang disimpan
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)