from flask import Flask
from flask import render_template
from flask import request
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "#
password = "#"

data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
data = data.json()
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html', posts=data)


@app.route('/post/<int:id>')
def post_page(id):
    return render_template('post.html', post=data[id - 1])


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact',methods=['GET','POST'])
def contact_page():
    if request.method == "POST":
        name = request.form['name']
        email_from = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        send_email(name,email_from,phone,message)
        return render_template("contact.html",message="Successfully sent message")
    return render_template("contact.html")


def send_email(name, email_from, phone, message):
    email_message = MIMEMultipart()
    email_message.attach(MIMEText(f"Subject: New Message\n\nName: {name}\nEmail: {email_from}\nPhone: {phone}\nMessage: {message}", 'plain', 'utf-8'))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email, email, email_message.as_string())

@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(name + "\n" + email + "\n" + phone + "\n" + message)
    return "Successefully"


if __name__ == '__main__':
    app.run(debug=True)
