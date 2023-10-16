# Flask Authentication Project

This is a simple Flask project that demonstrates how to implement user authentication using Flask-Login and SQLite.

## Getting Started

To get started with this project, you'll need to have Python 3 and pip installed on your machine. You can then install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

You can then start the Flask development server by running the following command:

```
python main.py
```

You should now be able to access the application by visiting http://localhost:5000 in your web browser.

## Project Structure

The project has the following structure:

```
.
├── main.py
├── models.py
├── templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── secrets.html
├── static
│   ├── css
│   │   └── styles.css
│   └── files
│       └── cheat_sheet.pdf
├── requirements.txt
└── README.md
```

The `main.py` file contains the main Flask application code, while the `models.py` file contains the database models for the application. The `templates` directory contains the HTML templates for the application, while the `static` directory contains the static assets (CSS, images, etc.) for the application.

## Features

The application has the following features:

- User registration
- User login
- User logout
- Access control (only authenticated users can access the secrets page)
- File download (authenticated users can download a PDF cheat sheet)

## Dependencies

The application depends on the following Python packages:

- Flask
- Flask-Login
- Flask-SQLAlchemy
- Werkzeug

These packages are listed in the `requirements.txt` file and can be installed using pip.