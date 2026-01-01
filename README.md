# Mail Free Games

A python script that uses GamerPower API to collect the current free games from Epic Games and send them to the specified email.

---

## Environment variables

| Variable Name        | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| EPIC_EMAIL_USER_FROM | The email address that sends the email about the free games. |
| EPIC_EMAIL_PASS      | The app password of the sender email.                        |
| EPIC_EMAIL_USER_TO   | The target email address that should receive the report.     |

---

## Setup

- Install requirements using requirements.txt
- Add the listed environment variables
- Setup a scheduled task on your PC to run the script
