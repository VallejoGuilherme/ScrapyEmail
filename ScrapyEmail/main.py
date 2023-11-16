from auth_method import get_app_password
from fetch_email import fetch_emails
from processing_data import process_data

email_address = "Your e-mail aaddress here"
app_password = get_app_password()

email_list = fetch_emails(email_address, app_password)

if email_list:
    process_data(email_list)
