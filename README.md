# ML Bank Loan Approval API

![Django](https://img.shields.io/badge/Django-5.1.1-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Description

This project is a RESTful API built with Django and Django REST Framework that enables loan applications and predicts their approval using a Machine Learning model. The application is designed for easy deployment on Railway and utilizes a database management system configured via `dj_database_url`.

## Features

- User-friendly interface for submitting loan applications.
- Loan approval predictions using a trained Machine Learning model.
- Input validation to ensure data quality.
- Easy deployment on Railway.

## Project Structure

```plaintext
API DJANGO
 ├── data
 ├── ml_bank_loan
 │   ├── bankAPI
 │   ├── manage.py
 │   ├── requirements.txt
 ├── notebooks
 ├── venv
 ├── Procfile
 ├── railway.toml
 └── runtime.txt
```

## Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/DannyDataScience/loan-app.git
```
2. Navigate to the project directory:

```bash
cd ml_bank_loan
```
3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```
4. Install the dependencies:

```bash
pip install -r requirements.txt
```
5. Set up your environment variables in a .env file:

```bash
#.env file
SECRET_KEY='your_secret_key_here'
DATABASE_URL='your_database_url_here'
```
6. Run database migrations:

```bash
python manage.py migrate
```
7. Start the development server:

```bash
python manage.py runserver
```

## Usage
Once the server is running, you can access the API at http://127.0.0.1:8000/ and use the user interface to submit loan applications.

### Example Request

Usage
Once the server is running, you can access the API at http://127.0.0.1:8000/ and use the user interface to submit loan applications.

```json
{
  "firstname": "John",
  "lastname": "Doe",
  "dependants": 2,
  "applicantincome": 50000,
  "coapplicantincome": 0,
  "loanamt": 20000,
  "loanterm": 360,
  "credithistory": 1,
  "gender": "Male",
  "married": "Yes",
  "graduatededucation": "Graduate",
  "selfemployed": "No",
  "area": "Urban"
}
```

## Contribution
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Make your changes and commit (git commit -m 'Add new feature').
4. Push your changes (git push origin feature/new-feature).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For more information, you can contact:

- Daniel Aguilar - daniel272aguilar@gmail.com

Thank you for your interest in the project!