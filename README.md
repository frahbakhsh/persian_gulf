# Persian Gulf Historical API

<div dir="rtl">

## خلیج فارس | Persian Gulf API

این پروژه یک API برای ارائه اطلاعات تاریخی در مورد خلیج فارس است که با هدف نمایش مستندات و شواهد تاریخی مبنی بر اصالت نام "خلیج فارس" ایجاد شده است.

</div>

## Overview

This project provides a RESTful API for accessing historical documentation about the Persian Gulf, including historical maps, quotes from historians and travelers, and positions of international organizations on the name "Persian Gulf". The API aims to provide factual historical evidence about the longstanding use of the name "Persian Gulf".

The project includes:
- RESTful API endpoints for retrieving historical data
- Administrative panel for managing content
- Documentation page for API consumers
- Authentication system for admin users

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Admin Access](#admin-access)
- [Contributing](#contributing)

## Features

- **Historical Maps API**: Access information about historical maps showing the Persian Gulf
- **Historical Quotes API**: Access quotes from historians and travelers about the Persian Gulf
- **Organizations' Positions API**: Access information about international organizations' official positions on the name "Persian Gulf"
- **Admin Panel**: Secure administrative interface for managing content
- **API Documentation**: Interactive documentation for API consumers
- **Multilingual Support**: Interface that supports both English and Persian

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite (SQLAlchemy ORM)
- **Authentication**: Flask-Login
- **Admin Panel**: Flask-Admin
- **Frontend**: HTML, CSS, JavaScript
- **Typography**: Vazir Font for Persian text support
- **API**: RESTful JSON API
- **CORS Support**: Cross-Origin Resource Sharing enabled

## Installation

### Prerequisites
- Python 3.6+
- pip (Python package manager)

### Setup Steps

1. Clone the repository
```bash
git clone https://github.com/frahbakhsh/persian_gulf.git
cd persian_gulf
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
```

3. Activate the virtual environment
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Set environment variables (optional for development)
```bash
# For Windows
set SECRET_KEY=your_secure_secret_key

# For macOS/Linux
export SECRET_KEY=your_secure_secret_key
```

## Running the Application

1. Start the Flask application
```bash
python app.py
```

2. Access the application
- Main website: http://localhost:5000/
- API Documentation: http://localhost:5000/documentation
- Admin Panel: http://localhost:5000/admin

## API Documentation

### API Endpoints

#### Maps API
- `GET /api/maps` - Retrieve all historical maps
- `GET /api/maps/{map_id}` - Retrieve a specific historical map by ID

#### Quotes API
- `GET /api/quotes` - Retrieve all historical quotes
- `GET /api/quotes/{quote_id}` - Retrieve a specific historical quote by ID

#### Organizations API
- `GET /api/organizations` - Retrieve all organization positions
- `GET /api/organizations/{org_id}` - Retrieve a specific organization's position by ID

### Response Format

All API responses are in JSON format.

**Example response from `/api/maps`:**
```json
[
  {
    "id": 1,
    "title": "Map by Ptolemy, 150 AD",
    "text": "One of the earliest maps showing the Persian Gulf",
    "year": "150",
    "source": "Claudius Ptolemy",
    "image_url": "https://example.com/maps/ptolemy.jpg"
  }
]
```

For detailed API documentation, visit the `/documentation` endpoint when the application is running.

## Project Structure

```
persian_gulf/
├── app.py                  # Main application file with routes and setup
├── models.py               # Database models
├── requirements.txt        # Python dependencies
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
│   ├── home.html           # Homepage template
│   ├── document.html       # API documentation template
│   └── login.html          # Admin login template
└── README.md               # Project documentation
```

## Admin Access

The application creates a default admin user on first run:
- Username: `admin`
- Password: `admin1234`

It is recommended to change these credentials after first login by updating the database or through the admin interface if such functionality is implemented.

To access the admin panel:
1. Navigate to `/login`
2. Enter the admin credentials
3. Once logged in, you'll be redirected to the admin panel where you can manage maps, quotes, and organizational positions

## Database Models

### Map
- `id`: Integer (Primary Key)
- `title`: String (150 characters)
- `text`: Text
- `year`: String (10 characters)
- `source`: String (200 characters)
- `image_url`: String (300 characters)

### Quote
- `id`: Integer (Primary Key)
- `text`: Text
- `source`: String (150 characters)

### OrganizationPosition
- `id`: Integer (Primary Key)
- `organization`: String (100 characters)
- `position`: Text

### User
- `id`: Integer (Primary Key)
- `username`: String (80 characters)
- `password_hash`: String (200 characters)

## Security Notes

- This application uses Flask's built-in development server which is not suitable for production use
- For production deployment, consider using a WSGI server like Gunicorn or uWSGI
- Change the default admin credentials and use a strong SECRET_KEY in production
- Configure HTTPS for production deployments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

<div dir="rtl">

## توسعه و همکاری

از مشارکت شما استقبال می‌کنیم! لطفاً برای مشارکت، یک Pull Request ارسال کنید.

</div>

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
