from app import app
from extensions import mail
from flask_mail import Message

msg = Message(
    subject="Test Email",
    sender="mohsanali1510@gmail.com",
    recipients=["arslanbhatti2960@gmail.com"]
)

msg.body = "Hello Bilal!\nThis is my first email."

msg.html = """
<h2>Hello Bilal!</h2>
<p>This is my <b>first email</b>.</p>
"""

with app.app_context():
    mail.send(msg)