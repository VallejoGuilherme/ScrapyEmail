## Overview

This project is designed to fetch and process emails from a Gmail account using Python. It modularizes the functionality into different parts to enhance readability and maintainability.

### Project Structure

- **auth_method.py**: Contains functions for obtaining authentication details.
- **fetch_email.py**: Fetches emails from the specified mailbox.
- **processing_data.py**: Processes the fetched emails and performs data operations.
- **main.py**: Executes the main workflow by importing functions from other modules.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `google-auth`, `imaplib`, `pandas`

Install the required packages using:
  pip install google-auth imaplib pandas

Usage
  Set up a Gmail account and enable "Less secure app access."
  Generate an app password for authentication.
  Update the get_app_password function in auth_method.py with the generated app password.
  Run the main.py script to fetch and process emails.

Customization
  Update the email_address variable in main.py with your Gmail address.
  Modify the functions in each module to suit specific requirements.

Acknowledgments
  The project uses the google-auth library for authentication and imaplib for handling IMAP connections.
  Special thanks to the Python community for creating and maintaining these libraries.
  
License
  This project is licensed under the MIT License.
