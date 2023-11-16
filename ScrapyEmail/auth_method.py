from google.auth import exceptions
from google.auth.transport.requests import Request

def get_app_password():
    return "Your App Password Here"

def get_access_token():
    credentials, _ = google.auth.default()
    try:
        credentials.refresh(Request())
        return credentials.token
    except exceptions.RefreshError:
        return None
