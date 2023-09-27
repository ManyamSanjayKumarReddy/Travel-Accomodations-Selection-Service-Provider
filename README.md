
# WorldXplorer - Hotel Booking Platform

WorldXplorer is a web-based hotel booking platform that allows users to explore and book premium accommodations in various destinations.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Custom Filters](#custom-filters)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

WorldXplorer is a Django-based hotel booking platform designed to provide users with an easy and convenient way to discover and book premium hotel rooms. With a user-friendly interface and a wide range of accommodation options, WorldXplorer aims to make the travel experience enjoyable and hassle-free.

## Features

- User registration and authentication system.
- Browse and search for hotel rooms by location and category.
- View detailed information and images of hotel rooms.
- Add hotel rooms to the cart for booking.
- Secure checkout process with payment integration.
- User profiles with booking history.
- User ratings and reviews for hotel rooms.
- Admin dashboard for managing rooms, orders, and users.

## Installation

To run WorldXplorer locally on your machine, follow these steps:

```bash
# Clone the repository
git clone 

# Change directory to the project folder
cd worldxplorer

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the development server
python manage.py runserver
```

Visit `http://localhost:8000` in your web browser to access the application.

## Usage

1. **User Registration and Login**: Users can create accounts or log in using their credentials.

2. **Browse and Search**: Users can browse hotel rooms by location and category. They can also search for specific rooms.

3. **View Room Details**: Clicking on a room displays detailed information, images, and user ratings.

4. **Booking**: Users can add rooms to their cart and proceed to checkout securely.

5. **User Profile**: Registered users can view their booking history and update their profiles.

## Custom Filters

WorldXplorer provides custom filters to help users find rooms easily:

- **Price Adjuster**: Users can adjust the price range to filter rooms based on their budget.

- **Categories and Subcategories**: Users can filter rooms by categories and subcategories.

## Technologies Used

- Django
- HTML/CSS
- JavaScript
- Bootstrap
- SQLite (for development, consider using PostgreSQL or MySQL for production)

## Contributing

Contributions to WorldXplorer are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request following our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
