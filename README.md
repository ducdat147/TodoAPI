# TodoAPI

This is a Django-based Todo API project.

## Prerequisites

- Python 3.12
- pip
- virtualenv

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ducdat147/TodoAPI.git
    cd TodoAPI
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser (optional but recommended for accessing the admin site):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Running Tests

To run the tests, use the following command:

```sh
python manage.py test
```
