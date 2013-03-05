import os
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return redirect('/current')

@app.route('/profile')
def profile():
    return render_template('profile.html', **{'current_tab': 'profile'})

@app.route('/current')
def current():
    return render_template('current.html', **{'current_tab': 'current'})

@app.route('/plan')
def plan():
    return render_template('plan.html', **{'current_tab': 'plan'})

@app.route('/what_if')
def what_if():
    return render_template('what_if.html', **{'current_tab': 'whatif'})


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
