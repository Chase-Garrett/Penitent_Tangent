# Penitent Tangent

## Installation
Clone the repository, navigate to the project directory and run the project locally
with the django command "python manage.py runserver". Alternatively you can host it 
elsewhere if you don't want to run it locally.

## Usage
Copy a URL to a reddit thread and paste it in the text box, click submit. After a short period
of time you will be redirected to a page showing the results related to the sentiment of the
associated subreddit with the score of your thread added to correct category.

## Design
Django was used to create the framework of this web application. On the backend I used SQLite to hold the data
from the results of the sentiment analysis. The analysis itself is done by the use of a project called VADER.
