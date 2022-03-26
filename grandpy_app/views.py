""" File containing Flask app routes and methods """
from flask import Flask, render_template, request
from .models import ParserClient, MapboxClient, WikidataClient, WikipediaClient


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/api")
def api():
    ui = request.args.get("q")
    spacy = ParserClient(ui)
    query = spacy.spacy_en()
    mapbox = MapboxClient(query)
    mapbox_response = mapbox.fetch_location_from_query()

    try:
        wikidata_id = mapbox.get_wiki_id(mapbox_response)
    except:
        api_response = mapbox_response
        return api_response
    else:
        wikidata = WikidataClient(wikidata_id)
        wikipedia_page_title = wikidata.get_wikipage_en_title()
        wikipedia = WikipediaClient(wikipedia_page_title)
        wikipedia_extract = wikipedia.get_page_extract()
        mapbox_response["wiki"] = wikipedia_extract
        api_response = mapbox_response

        return api_response
