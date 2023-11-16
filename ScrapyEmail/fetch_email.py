import imaplib
from email.header import decode_header
import email

def get_email_body(msg):
    # Assuming the email is in plain text
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    # Decode the payload, ignoring or replacing invalid bytes
                    return part.get_payload(decode=True).decode(
                        "utf-8", errors="replace"
                    )
                except UnicodeDecodeError as e:
                    print(f"Error decoding email body: {e}")
    else:
        try:
            # Decode the payload, ignoring or replacing invalid bytes
            return msg.get_payload(decode=True).decode("utf-8", errors="replace")
        except UnicodeDecodeError as e:
            print(f"Error decoding email body: {e}")

    # Return an empty string if decoding fails
    return ""

def fetch_emails(email_address, app_password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    try:
        mail.login(email_address, app_password)

        mailbox = "inbox"
        mail.select(mailbox)

        # Fetch and return emails
        status, messages = mail.search(None, "ALL")
        messages = messages[0].split()

        email_list = []
        for mail_id in messages:
            _, msg_data = mail.fetch(mail_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            # Access other parts of the email, like body, sender, etc.
            body = get_email_body(msg)
            sender = msg.get("From")

            email_data = {"Subject": subject, "Body": body, "Sender": sender}
            email_list.append(email_data)

    except imaplib.IMAP4.error as e:
        print(f"Failed to authenticate or select mailbox: {e}")
        email_list = []

    finally:
        mail.close()
        mail.logout()

    return email_list
