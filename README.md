# assignment-1-6-jonathanjtang-kralgeliy1-backend

[![CircleCI](https://circleci.com/gh/csc301-fall-2020/assignment-1-6-jonathanjtang-kralgeliy1-backend.svg?style=shield&circle-token=899863b30b6a235f3c5cc66bc7ace386ddc8ff88)](https://app.circleci.com/pipelines/github/csc301-fall-2020/assignment-1-6-jonathanjtang-kralgeliy1-backend)

Authors: Team 6, Jonathan Tang (JonathanJTang) and İsmail Atadinç (kralgeliy1)

Our Checkout Calculator backend built using Django, shared by both the mobile and web frontends.

Our assignment report is in the root directory of this repository, the file named `CSC301 A1 Report.pdf` (the same document is in all three of our repositories)

Note on CircleCI sticker: the state is not accurate, since CircleCI tasks refused to run (and give a fail status) after the class organization account ran out of credits.

## Production link
Please see our web and mobile frontend repositories for further setup and testing instructions--links to these repositories are on the second page of our report. Here they are again for convenience:
- [Web Frontend Repo](https://github.com/csc301-fall-2020/assignment-1-6-jonathanjtang-kralgeliy1-web)
- [Mobile Frontend Repo](https://github.com/csc301-fall-2020/assignment-1-6-jonathanjtang-kralgeliy1-mobile)

Our backend is hosted on Heroku.

&nbsp;

&nbsp;

&nbsp;

## Reference: Development Environment Setup Instructions (not needed to test our app)
We ran our code from a Windows Subsystem Linux (WSL) terminal window, but these steps would probably work on Linux machines too.
1. From the command line, install python module `pipenv` (eg using `pip`) and make sure the `pipenv` command can be accessed in the terminal (WSL: might need to restart the terminal)
2. Clone this repository and navigate to the directory, ie `assignment-1-6-jonathanjtang-kralgeliy1-backend` (the location is important for `pipenv` to work properly).
3. Run `pipenv install` to create a virtual environment with the necessary dependencies installed.
4. Run `pipenv shell` to start a shell session under the newly created virtual environment.
5. Run `cd server`
6. Run `python manage.py makemigrations`
7. Run `python manage.py migrate`
8. Run `python manage.py runserver`
