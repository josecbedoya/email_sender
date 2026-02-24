# SendEmails (Python)

Python SMTP email sender designed with secure defaults and interactive terminal input.

## Overview

This project sends plain-text emails through an SMTP server (Gmail by default) using Python's standard library only.

### Key Features

- Interactive runtime prompts via `input()`.
- Secure transport using `STARTTLS`.
- Validation for required fields.
- User-friendly error messages for common SMTP/network issues.
- No external dependencies.

## Requirements

- Python 3.10+ (tested with Python 3.13)
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

## GitHub Best Practices

- Never commit secrets, app passwords, or sensitive personal data.
- Keep `.env` out of version control (`.gitignore` is already configured).
- Rotate credentials immediately if leaked.

Author: José C. Bedoya. Built with Copilot AI

