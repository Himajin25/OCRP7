Projet7 : Grandpy Bot, a geopedia chatbot for OpenClassrooms
Features
AJAX interactions: answer to question submitted by user is displayed directly on the screen, without page reloading.
Mapbox API, Wikidata API and Wikipedia API are used along with Spacy to parse the user input.
Conversation history is lost upon page reload, nothing is saved.
Several different answers from GrandPy are coded

User experience
The user connects to the chatbot on this url from his preferred browser. 
The chat window is then divided from top to bottom into a header, a chatbox, an input field and a footer.
header: logo and catchphrase
chatbox: vertical chat room with text. Grandpy messages appear from top to bottom on the left side in green and user messages appear from top to bottom on the right side in red. 
input field bar and send button beneath 
footer: the developper first & last name, and a link to the project Github repository.
use: user types "Hi Grandpy! Do you know where the Eiffel Tower is?" in input field and presses Enter to submit his message. The message then appears beneath the last message in the chatbox. The screen then freezes and a loader appears while GrandPy's answer is being loaded.

GrandPy's replies then appear containing the address, general info about the location and a map with a marker.

Kanban of the project is given to see the roadmap.

Setup
Setup consist in creating a .env file in the main folder with this syntax :

GMAP_API_KEY=YourApiKeyWithoutQuote 
A Pipfile is provided to install all dependencies with this command in root folder :

pipenv install
Flask
To test the app in the Project folder:

export FLASK_APP=app
python -m flask run
Useful ressources about Flask :

quick Start
flask_sqlalchemy but no DB is required for this project
Jinja 2
lesson OpenClassroom
TDD
This project is codded using Test Driven Development (tests are written before the main code). Here are 2 videos about testing programs :

Rails Conf 2013 The Magic Tricks of Testing
Advanced Test Driven Development
To launch the tests use pytest command in root folder.

Deployment
This app is deployed through Heroku

he Procfile is build as follow: web: gunicorn run:app. Procfile specifies the commands that are executed by the app on startup. Here: WSGI gunicorn is ran

gunicorn [OPTIONS] APP_MODULE
Where APP_MODULE is of the pattern $(MODULE_NAME):$(VARIABLE_NAME) here : run:app.