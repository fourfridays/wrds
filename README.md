Solution to Question 1 can be found in wrds/polymorphism.py

# Rationales

## Language Rationale for Abstract Classes
I have chosen Python for the coding tasks for the following reasons:
- It's easy to learn, read and write
- In my experience I haven't come across a challenge I haven't been able to resolve using its libraries, and frameworks
- Python's history and more recent advances in AI, specifically ML libraries built on Python provides a sense of long term validity of the language
- Highly supportive community! There are numerous solutions on Stackoverflow for various Python challenges

## Rationale for ORM
For the ORM part of the tasks I have selected Django for the following reasons:
- excellent documentation
- established over a number of years
- plenty of open source support
- QuerySets
- reduced development time
- easier to change databases
    - The basics from [Django docs](https://docs.djangoproject.com/en/4.1/topics/db/models/):
- A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
        - Each model is a Python class that subclasses django.db.models.Model.
        - Each attribute of the model represents a database field.
        - With all of this, Django gives you an automatically-generated database-access API; see Making queries.

## Rationale for Template engine
I picked Django's built-in templating language for the following reasons:
1. Separationg of program logic from presentation
2. Template inheritance where you can build elements in blocks that child templates can override of use as is
3.Tags for looping such as if, for, and filters
4. Extensable by adding your own extensions to the language
5. One template language for any text-based formats such as emails, Javascript, CSV. ([Django Docs](https://docs.djangoproject.com/en/4.1/ref/templates/language/))

# Docker Setup

## Prerequisites for running Docker:
1. Latest version of Docker is installed locally on your computer
2. All the following terminal commands should be run when in /wrds folder

## To build docker:
1. Clone this repo
2. Navigate to cloned wrds folder in terminal
3. Run `docker-compose build`
4. Run `docker-compose run web python manage.py migrations`

## To run Docker container:
1. Run `docker-compose up`

## Create Super User:
1. In another tab/window of terminal run `docker-compose run web python manage.py createsuperuser`

## Logging in to admin:
1. For Django admin visit: http://localhost:8000/django-admin
2. You can login using the user credentials you created in Create Super User section

