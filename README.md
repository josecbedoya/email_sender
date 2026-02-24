# SendEmails (Python)

This is a Python SMTP email sender. I used Copilot as a tool for advancing faster the proyect.

## Overview

This project sends emails through an SMTP server using Python's standard library only.

## Requirements

- Python 3.10+ 
- Gmail account with an App Password

## Run the Script

From the project folder:

```powershell
python email_sender.py
```

The script prompts for:

- Sender name
- Sender email
- Recipient email
- Email subject
- Message
- SMTP host (default: `smtp.gmail.com`)
- SMTP port (default: `587`)
- App password

Press Enter to accept default values when available.

## Troubleshooting

- `Could not resolve SMTP host...`
  - Verify `SMTP host` (example: `smtp.gmail.com`).
- `SMTP authentication failed...`
  - Verify sender email and app password.
  - For Gmail, use an App Password (not your regular account password).
- `SMTP port must be a valid number.`
  - Enter a numeric port (for example, `587`).


Author: José C. Bedoya. Built with Copilot AI


