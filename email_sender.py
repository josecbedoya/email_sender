import os
import smtplib
import ssl
import socket
from email.message import EmailMessage


def env_or_default(name: str, fallback: str) -> str:
    value = os.getenv(name, "").strip()
    return value or fallback


def input_required(label: str, default: str = "") -> str:
    while True:
        prompt = f"{label} [{default}]: " if default else f"{label}: "
        value = input(prompt).strip()
        final_value = value or default
        if final_value:
            return final_value
        print(f"{label} is required.")


def send_email() -> None:
    sender_name = input_required("Sender name", env_or_default("EMAIL_FROM_NAME", "Anonymous"))
    sender_email = input_required("Sender email", env_or_default("EMAIL_USERNAME", ""))
    recipient_email = input_required("Recipient email", env_or_default("EMAIL_TO", ""))
    subject = input_required("Email subject", env_or_default("EMAIL_SUBJECT", "Hello"))
    message_body = input("Message: ").strip()

    message = EmailMessage()
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = recipient_email
    message["Subject"] = subject
    message.set_content(message_body or "(No message)")

    smtp_host = input_required("SMTP host", env_or_default("SMTP_HOST", "smtp.gmail.com"))
    smtp_port_raw = input_required("SMTP port", env_or_default("SMTP_PORT", "587"))
    smtp_password = input_required("App password", env_or_default("EMAIL_APP_PASSWORD", ""))

    try:
        smtp_port = int(smtp_port_raw)
    except ValueError:
        print("SMTP port must be a valid number.")
        return

    try:
        with smtplib.SMTP(host=smtp_host, port=smtp_port, timeout=30) as smtp:
            smtp.ehlo()
            smtp.starttls(context=ssl.create_default_context())
            smtp.ehlo()
            smtp.login(sender_email, smtp_password)
            smtp.send_message(message)
    except socket.gaierror:
        print("Type SMTP host value: smtp.gmail.com")
        return
    except smtplib.SMTPAuthenticationError:
        print("Check your email or app password.")
        return

    print("Email sent successfully.")


if __name__ == "__main__":
    send_email()

