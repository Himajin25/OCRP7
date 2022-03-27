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

With GrandPy Bot, ask him for informations about a location.
After a little thinking, if he knows anything about this place, he will give you the address, show you the place in a Google Map, and tell you a story about the spot.

Different ways to use GrandPy Bot :

=> Locally:
1/ Download the repo.
2/ Initialize the virtual environment by indicating : pipenv install
3/ Position yourself in the virtual environment by typing : pipenv shell
4/ Run the app with command : python main.py

=> Online:
Feel free to use it: "https://grandpybotoc.herokuapp.com/"

Enjoy it! ;-)


7th project of the Python/Django Openclassrooms training The goal was to create a web application using Python, Flask and Javascript

If you want to run this app on your local machine:
Go place yourself in a console
Create a folder
Create a virtual environement with python3 -m venv env
Activate it with source env/bin/activate
Init git on this folder
Download or clone this repository
Install dependenties: pip3 install -r requirements.txt
Run the app with python run.py, Flask will run a server on your local machine
Open your browser, you'll see the app running


exigence projet:
clé api en variable env
inclure dans read me
charg via os.getenv
exec flake8
(fichier conf flake8 pour inclure )
github! faire plusieurs commit pre validation
readme extensif