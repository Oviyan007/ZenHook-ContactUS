
# Contact Us Form Project

This project implements a simple Contact Us form using Django, allowing users to send messages directly via email.

## Features

- **Contact Form:** Users can fill out their name, email, subject, and message.
- **Email Integration:** Emails are sent using Django's `send_mail` function via SMTP.
- **Feedback:** User receives feedback messages on successful submission or errors.

## Technologies Used

- Django
- HTML/CSS
- Bootstrap
- JavaScript
- SMTP (for email sending)

#Screenshots
![image](https://github.com/user-attachments/assets/fe30e4bd-adf1-45f9-9d04-3a77b995228e)


## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/contact-us-project.git
   cd contact-us-project

   1.  **Install dependencies:**

    bash

    Copy code

    `pip install -r requirements.txt`

2.  **Configure SMTP settings:**

    -   Open `settings.py` and set your email host (`EMAIL_HOST`), port (`EMAIL_PORT`), and authentication details (`EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`).
3.  **Run migrations:**

    bash

    Copy code

    `python manage.py migrate`

4.  **Create a superuser (optional):**

    bash

    Copy code

    `python manage.py createsuperuser`

5.  **Run the development server:**

    bash

    Copy code

    `python manage.py runserver`

6.  **Access the application:** Open your web browser and go to `http://localhost:8000/` to view and interact with the Contact Us form.

Usage
-----

-   Fill out the Contact Us form with your details and message.
-   Click on "Send Message" to submit the form.
-   You will receive a success message if the email is sent successfully.
-   Check your email inbox for the received message.
