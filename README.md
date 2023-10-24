# Teacher Data Management System

The Teacher Data Management System is a Django-based web application that simplifies the process of managing and distributing teacher's data and their individual Excel sheets. It automates the extraction of teacher data from uploaded Excel files, generates PDFs for each teacher's sheet, and sends them via email.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Description

The Teacher Data Management System simplifies the yearly process of collecting Excel sheets from teachers, extracting data, and distributing the individual sheets to each teacher via email. It streamlines this process through the following key features:

## Features

- **Automatic Data Extraction:** The system extracts teacher data from uploaded Excel files.
- **PDF Generation:** It generates PDF files for each teacher's Excel sheet.
- **Email Distribution:** PDFs are sent to respective teachers via email.
- **Admin Panel Integration:** All operations, including Excel file upload, are performed through the Django admin panel.

## Getting Started

### Prerequisites

Before setting up the Teacher Data Management System, make sure you have Python and pip installed on your system. 

If not, you can download and install Python from the [official website](https://www.python.org/downloads/).

### Installation

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/mr-robot369/Excel-Email-Send.git
    ```

2. Create a virtual environment for the project. Replace your-env-name with your preferred name.
    ```bash
    python -m venv your-env-name
    ```
3. Activate the virtual environment.
* On Windows:
    ```bash
    your-env-name\Scripts\activate
    ```
* On macOS and Linux:
    ```bash
    source your-env-name/bin/activate
    ```

4. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Django migration and migrate command.

    To apply database migrations, use the following command:
    ```bash
    python manage.py makemigrations
    ```
    This command generates the SQL migrations for your models and prepares the changes to be applied to the database.

    To apply the pending migrations to the database, use the following command:
    ```bash
    python manage.py migrate
    ```

6. Creating a Superuser
    ```bash
    python manage.py createsuperuser
    ```
You will be prompted to enter a username, email address, and password for the superuser. Fill in the requested information.

Once you've provided the required details, the superuser will be created, and you'll see a confirmation message.

7. Run the Django development server.
    ```bash
    python manage.py runserver
    ```
    
### Usage

1. Access the Django admin panel at `http://localhost:8000/admin/` and log in with admin credentials.

2. Upload Excel files containing teacher data.

3. Utilize the "Generate PDFs and Send Emails" admin action to automatically process and send sheets to teachers.

## Configuration
The following environment variables can be configured in a .env file:
    
    EMAIL_USER=<your-email>
    EMAIL_PASS=<your-email-password>
    EMAIL_FROM=<your-email>

## Dependencies
The project relies on the following main dependencies:
* Django (version 3.2.5)
* openpyxl (for Excel file processing)
* ReportLab (for PDF generation)

## Authors

- [Anubhav Shukla](https://github.com/mr-robot369/)

## Acknowledgments

This project wouldn't have been possible without the contributions of the following open-source libraries and frameworks:

- [Django](https://www.djangoproject.com/): A high-level Python web framework that encourages rapid development and clean, pragmatic design.

- [openpyxl](https://openpyxl.readthedocs.io/en/stable/): A Python library for reading and writing Excel (xlsx) files.

- [ReportLab](https://www.reportlab.com/): An open-source Python library that lets you create and modify PDF documents.

We are grateful for the developers and communities behind these fantastic tools that made this project successful. 🙌


Have fun managing teacher data efficiently!