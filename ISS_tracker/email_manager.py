# class responsible for sending emails
import smtplib

class EmailManager:
    """
    managing the sending of emails
    """
    def __init__(self, email_app_password: str, email_from: str) -> None:
        self.email_app_password = email_app_password
        self.email_from = email_from


    def send_gmail_mail(self, email_title: str, message_to_send: str, email_to: str) -> None:
        """
        sends email from a gmail account
        """
        email_message = lambda title, content: f"Subject:{title}\n\n{content}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls() # making the conection secure
            connection.login(user=self.email_from, password=self.email_app_password)
            connection.sendmail(from_addr=self.email_from, to_addrs=email_to, \
                msg=email_message(title=email_title,content=message_to_send))