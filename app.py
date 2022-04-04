""" File from wich app is launched """
from grandpy_app import app


if __name__ == "__main__":
    app.run(debug=True, load_dotenv=True, host="0.0.0.0")
