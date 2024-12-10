**Project Status**: This project is currently a work in progress and is being updated regularly.


# Car dealer project [WIP]
### Self-presentation Project
Tato webová aplikace byla vytvořena jako simulace stránek autobazaru, zaměřená na rozvoj programovacích dovedností.
Aplikace není určena pro reálné inzerování, nakupování ani prodávání vozidel.

This web application was created as a simulation of a car dealership website, focused on developing programming skills.
The application is not intended for real advertising, buying, or selling of vehicles.

## Project Goals
### The project allows users to:

- List a car for sale.
- Search and browse car listings based on specified parameters.
- Manage demand and supply listings.
- Register, manage their listings, add new ones, edit or delete them.

## On the homepage, there are sections for:

- Top Offers: Highlighted listings.
- Most Viewed Listings: Listings with the highest view count.
- Search: Allows users to search for listings based on specific parameters.

# Mockup and UI Design
## Project Design and Structure

- [x] GIT - version control and repository management
- [ ] Wireframe design
- [ ] UI elements design
- [ ] User scenarios
- [ ] Mockup presentation

### Basic Features
- Base HTML: Basic structure of the website.
- Additional HTML pages: Templates for various sections and pages of the application.
- Key functions: Registration, ad management, search, and matching of demand and supply.
- Basic functionality testing: Verification of the main components.

# Full Version
- [ ] Advanced features
- [ ] Performance optimization
- [ ] Responsive design
- [ ] Test coverage
- [ ] Final testing

# Installation Instructions
### Step 1 - Create and activate the virtual environment
    python -m venv venv
    venv\Scripts\activate

### Step 2 - Install package
    pip install -r requirements.txt

### Step 3 - Create migrations
    python manage.py makemigrations

### Step 4 - Migration application
    python manage.py migrate

### Step 5 - Create a superuser
    python manage.py createsuperuser

### Step 6 - Start the development server
    python manage.py runserver

### Voluntary Step - Run the Tests
To run the tests, install `selenium` as it is required for automated browser testing.
Some of the tests involve browser interactions, which `selenium` handles.

```bash
pip install selenium
python manage.py test
# Alternatively, to run specific tests
python manage.py test viewer.tests
```

![ER Diagram](...)

### For questions or suggestions, feel free to reach out to me at michael.belka.mb@gmail.com