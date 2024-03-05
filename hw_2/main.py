from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def user_input():
    return render_template('user_input.html')


@app.route('/welcome')
def welcome():
    if 'user_name' in request.cookies:
        user_name = request.cookies.get('user_name')
        return render_template('welcome.html', user_name=user_name)
    else:
        return redirect(url_for('user_input'))


@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form['user_name']
    user_email = request.form['user_email']
    response = make_response(redirect(url_for('welcome')))
    response.set_cookie('user_name', user_name)
    return response


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('user_input')))
    response.delete_cookie('user_name')
    return response


if __name__ == '__main__':
    app.run(debug=True)
