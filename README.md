# Checkout Calculator Backend (Django)

A simple web backend built using Django and a simple SQLite database, for a checkout calculator designed for stores in Ontario, Canada.

This was part of a 2-week course project done together with İsmail Atadinç (kralgeliy1).

## Production link
Our backend is hosted on Fly.io, with automated CI/CD through Github actions.

- A web frontend that works with this backend: [Web Frontend Repo](https://github.com/JonathanJTang/Checkout-Calculator-Frontend)

&nbsp;

&nbsp;

&nbsp;

## Reference: Development Environment Setup Instructions (not needed to test our app)
We ran our code from a Windows Subsystem Linux (WSL) terminal window, but these steps would probably work on Linux machines too.
1. From the command line, install python module `pipenv` (eg using `pip3`) and make sure the `pipenv` command can be accessed in the terminal (WSL: might need to restart the terminal)
2. Clone this repository and navigate to the directory containing the `Pipfile` (the location is important for `pipenv` to work properly).
3. Run `pipenv install` to create a virtual environment with the necessary dependencies installed.
4. Run `pipenv shell` to start a shell session under the newly created virtual environment.
5. Run `cd server`
6. Run `python3 manage.py makemigrations`
7. Run `python3 manage.py migrate`
8. Run `python3 manage.py runserver`
