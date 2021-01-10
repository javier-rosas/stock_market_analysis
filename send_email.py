import smtplib, ssl

def send_email():
    port = 465  # For SSL
    password = "Javierbot1"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("javier.rosas.bot@gmail.com", password)
        # Send email here
        subject = "BUY STONKS"
        text = "buy specific stonks"
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server.sendmail("javier.rosas.bot@gmail.com", "javier.rosas.bot@gmail.com", message)

