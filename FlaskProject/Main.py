from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html' )

@app.route('/charts')
def charts():
    return render_template('charts.html' )

@app.route('/tables')
def tables():
    return render_template('tables.html' )

@app.route('/ridedetails')
def ridedetails():
    return render_template('ridedetails.html' )

@app.route('/navbar')
def navbar():
    return render_template('navbar.html' )

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html' )

@app.route('/cards')
def cards():
    return render_template('cards.html' )

@app.route('/blank/')
def blank():
    return render_template('blank.html' )

@app.route('/register')
def register():
    return render_template('register.html' )

@app.route('/driver_profile')
def driver_profile():
    return render_template('Driver_Profile.html' )

if __name__ == "__main__":
    app.run(debug=True)
