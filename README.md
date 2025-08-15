# OIBSIP_WebDevelopment_4
## Flask Login-Authentication App

This is a simple Flask web application that demonstrates user authentication, including registration, login, and a protected dashboard page. It uses `Flask-SQLAlchemy` for database management and `Werkzeug` for secure password hashing.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [Prerequisites](#prerequisites)
- [File Structure](#file-structure)
- [Live Demo](#live-demo)


<img width="1416" height="567" alt="image" src="https://github.com/user-attachments/assets/bb8251ea-92ab-47c1-94de-7160cb0bc4ef" />


## Features

- **User Registration**: Users can create a new account with a unique username and password. The application checks for existing usernames to prevent duplicates.
- **Secure Password Hashing**: Passwords are not stored in plain text. `Werkzeug.security` is used to hash passwords with a strong `pbkdf2:sha256` method before saving them to the database.
- **User Login**: Existing users can log in with their username and password. The application verifies the provided credentials against the stored hashed password.
- **Session Management**: Once a user logs in, their session is managed using Flask's built-in session object. This allows the application to remember the user's logged-in state across different pages.
- **Protected Dashboard**: A specific route (`/dashboard`) is protected and can only be accessed by authenticated users. If a non-logged-in user tries to access it, they are redirected to the login page.
- **Logout Functionality**: A simple logout route clears the user's session, effectively logging them out and redirecting them to the login page.
- **Flash Messages**: The application provides informative flash messages for user feedback, such as successful registration, login errors, or a warning for trying to access a protected page.

## Technologies Used

- **Flask**: A micro web framework for Python, used to handle routes, requests, and templates.
- **Flask-SQLAlchemy**: An extension for Flask that simplifies database interactions by providing an ORM (Object-Relational Mapper) to work with a database like SQLite.
- **Werkzeug**: A comprehensive WSGI utility library. The `werkzeug.security` module is used specifically for password hashing and checking.
- **SQLite**: A lightweight, file-based database used to store user information.

## Database Schema

The `users.db` database contains a single table, `user`, with the following schema:

- `id`: An integer primary key, automatically incremented for each new user.
- `username`: A string with a maximum length of 80 characters, required to be unique and not null.
- `password`: A string with a maximum length of 200 characters, used to store the hashed password.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## File Structure
 #### Main Flask application file
- ── app.py
- #### SQLite database file (created automatically)
  ── users.db
  #### CSS for styling the application         
- ── static/
-   └── style.css       
- ── templates/
- ── acc.html         Registration page template
- ── base.html        Base template with navigation and flash messages
- ── dashboard.html   User dashboard template
- ── index.html       Home page template
- ── login.html       Login page template

## Live Demo

*You can see a live version of this app here:* [Live Demo Link](https://oibsip-webdevelopment-4-3.onrender.com/)
