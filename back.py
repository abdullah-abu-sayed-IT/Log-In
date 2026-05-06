from flask import Flask, request

app = Flask(__name__)

# demo correct credentials
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pwd = request.form['password']

    if user == USERNAME and pwd == PASSWORD:
        return "Login Successful ✔️"
    else:
        return "Login Failed ❌"

if __name__ == '__main__':
    app.run(debug=True)
