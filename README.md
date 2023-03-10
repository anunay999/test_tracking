# Test Case Tracking Tool
The Test Case Tracking Tool is a Django web application designed to help teams track their progress in completing test cases for a project. It provides a simple interface for engineers to log completed test cases based on module and also provides an embedded data visualization dashboard to track progress on test cases completed by engineers.

## Requirements
- Python 3.x
- Django 3.x
- PostgreSQL

## Installation
Clone the repository:

```bash
$ git clone https://github.com/anunay999/test-tracking.git
$ cd test-tracking
```

## Install the required packages:

```bash
$ pip install -r requirements.txt
```

Create a PostgreSQL database and add the database configuration to the settings.py file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database-name>',
        'USER': '<database-username>',
        'PASSWORD': '<database-password>',
        'HOST': '<database-host>',
        'PORT': '<database-port>',
    }
}
```

Run the migrations to create the necessary database tables:

```bash
$ python manage.py migrate
```

Start the Django development server:

```bash
$ python manage.py runserver
```

Navigate to http://localhost:8000 in your web browser to access the Test Case Tracking Tool.

## Usage
The Test Case Tracking Tool provides a simple interface for engineers to log completed test cases based on module and also provides an embedded data visualization dashboard to track progress on test cases completed by engineers.

To log completed test cases:
- Log in to the Test Case Tracking Tool using your credentials.
- Select the module you want to log completed test cases for.
- Enter the number of test cases completed and click "Submit".
- The Test Case Tracking Tool will automatically update the progress on the embedded data visualization dashboard.

### To view the embedded data visualization dashboard:

- Navigate to the "Dashboard" page.
- The embedded data visualization dashboard will display the progress on test cases completed by engineers.

## Contributing
Contributions to the Test Case Tracking Tool are welcome. To contribute, please fork the repository, create a new branch, and submit a pull request.

## License
The Test Case Tracking Tool is licensed under the MIT License. See the LICENSE file for more information.
