from flask import Flask, render_template, request
import wtforms
from wtforms.validators import DataRequired, Length, Email
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    username = wtforms.EmailField(label='Username', validators=[DataRequired(),
                                                                 Length(min=6, max=120),
                                                                 Email(message="Field must contain email like this i.e. saba@example.com",
                                                                       allow_empty_local=True,
                                                                       check_deliverability=True)])
    password = wtforms.PasswordField(label='Password', validators=[DataRequired()])
    submit = wtforms.SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "sdvbfgsdvgfsdvkb13jhbfj342hjbwhjvfh47892fw"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstrap)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if request.method == "POST" :
        print(login_form.username.data)
        print(login_form.password.data)
        if login_form.validate():
            return render_template("success.html", bootstrap=bootstrap)
        else:
            return render_template("denied.html", bootstrap=bootstrap)
    return render_template('login.html', form=login_form, bootstrap=bootstrap)


if __name__ == '__main__':
    app.run(debug=True)
