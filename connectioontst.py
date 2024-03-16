import imaplib
import email
from email.header import decode_header

# Gmail IMAP server settings
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

# Your Gmail credentials
EMAIL = "varunmsaji01@gmail.com"
PASSWORD = "wpsh jidu eysb qdfw"  # Update with your actual password

# Connect to Gmail IMAP server
imap_conn = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

# Login to your Gmail account
imap_conn.login(EMAIL, PASSWORD)

# Select the inbox
imap_conn.select("INBOX")

# Search for all unseen emails from the specified email address
status, email_ids = imap_conn.search(None, '(UNSEEN FROM "varunms322@gmail.com")')

if status == "OK":
    email_ids = email_ids[0].split()
    for email_id in email_ids:
        # Fetch the email
        status, email_data = imap_conn.fetch(email_id, "(RFC822)")
        if status == "OK":
            raw_email = email_data[0][1]
            # Parse the raw email
            msg = email.message_from_bytes(raw_email)
            # Extract sender information
            sender_name, sender_email = decode_header(msg["From"])[0]
            if isinstance(sender_name, bytes):
                sender_name = sender_name.decode()
            sender_details = f"{sender_name} <{sender_email}>"
            # Extract email text
            if msg.is_multipart():
                text = ""
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        try:
                            text += part.get_payload(decode=True).decode("utf-8")
                        except UnicodeDecodeError:
                            text += part.get_payload(decode=True).decode("latin1", errors="replace")
            else:
                text = msg.get_payload(decode=True).decode()

            print("Sender:", sender_details)
            print("Text:", text.strip())
            print("-" * 50)

# Close the IMAP connection
imap_conn.logout()
