import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config 

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create the email headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body to the message
        message.attach(MIMEText(body, "plain"))

        # Set up the SMTP server (Gmail's SMTP server is used here)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # TLS port

        # Start the server and log in
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close the connection to the SMTP server
        server.quit()

        print(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    # Sender's email credentials (replace these with real credentials)
    sender_email = config('EMAIL_SENDER')
    sender_password = config('EMAIL_PASSWORD')

    # Recipient's email address
    recipient_email = config('EMAIL_REC')

    # Email subject and body
    subject = "Test Email from Python"
    body = "Hello, this is a test email sent using Python! sent from docker and deployed on k8s"

    # Send the email
    send_email(sender_email, sender_password, recipient_email, subject, body)
