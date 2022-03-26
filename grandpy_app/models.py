""" File containing the classes used in the app """
import requests
import spacy


class ParserClient:
    """ Class processing user input to extract location string  """

    def __init__(self, user_input):
        self.user_input = user_input

    def spacy_en(self) -> str:
        """ Uses spacy to parse user input """
        nlp = spacy.load("en_core_web_lg")
        doc = nlp(self.user_input)
        query_list = []
        for ent in doc.ents:
            if ent.label_ == "GPE" or "ORG" or "FAC" or "LOC":
                query_list.append(ent.text)
        final_query = " ".join(query_list)
        print("final query is :", final_query)
        return final_query


class MapboxClient:
    """ Requests location data from Mapbox API using parsed user query  """

    def __init__(self, query: str):
        self.url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json"
        self.mapbox_token = "pk.eyJ1IjoibmNiIiwiYSI6ImNrejN2NXFiNDA5NTMyb2sycGw0OWRyNWYifQ.HRSod30-jASUMraNtuxc-A"
        self.params = {"access_token": self.mapbox_token}

    def get_json(self):
        """ Returns json response from Mapbox API """
        mapbox_geocoding_request = requests.get(self.url, params=self.params)
        mapbox_geocoding_json = mapbox_geocoding_request.json()
        print("API RETURNS: ", mapbox_geocoding_json)
        return mapbox_geocoding_json

    def fetch_location_from_query(self):
        """ Extracts relevant location data from API json response """
        mapbox_geocoding_json = self.get_json()
        try:
            mapbox_location_data = mapbox_geocoding_json["features"][0]
        except:
            mapbox_location_data = {"message": "not found"}
        return mapbox_location_data

    def get_wiki_id(self, mapbox_location_data):
        """ Extracts Wikidata id from API json response """
        wikidata_id = mapbox_location_data["properties"]["wikidata"]
        return wikidata_id


class WikidataClient:
    """ Requests Wikidata page title from Wikidata API using wikidata id  """

    def __init__(self, wikidata_id):
        self.url = "https://www.wikidata.org/w/api.php"
        self.params = {
            "action": "wbgetentities",
            "props": "sitelinks/urls",
            "ids": wikidata_id,
            "format": "json",
        }
        self.wikidata_id = wikidata_id

    def get_json(self):
        """ Returns json response from Wikidata API """
        wikidata_request = requests.get(self.url, params=self.params)
        wikidata_json_response = wikidata_request.json()
        return wikidata_json_response

    def get_wikipage_en_title(self):
        """ Extracts Wikipedia english page title from json response """
        wikipages = self.get_json()
        wikipage_en_title = wikipages["entities"][self.wikidata_id]["sitelinks"][
            "enwiki"
        ]["title"]
        return wikipage_en_title


class WikipediaClient:
    """ Requests Wikipedia page extract from Wikipedia API using retrieved Wikipedia page title """

    def __init__(self, wikipage_en_title):
        self.url = "https://en.wikipedia.org/w/api.php?"
        self.params = {
            "action": "query",
            "titles": wikipage_en_title,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "indexpageids": True,
            "exsentences": 5,
            "format": "json",
        }

    def get_json(self):
        """ Return json response from Wikipedia API """
        wikipedia_request = requests.get(self.url, params=self.params)
        wikipedia_json = wikipedia_request.json()
        return wikipedia_json

    def get_page_id(self):
        """ Extracts Wikipedia english page id from json response """
        wikipedia_json = self.get_json()
        wikipedia_page_id = wikipedia_json["query"]["pageids"][0]
        return wikipedia_page_id

    def get_page_extract(self, page_id):
        """ Extracts Wikipedia english page extract from json response """
        wikipedia_json = self.get_json()
        extract = wikipedia_json["query"]["pages"][page_id]["extract"]
        return extract

        # lib mypy librairie pour verif de type coté ide
        # pydentik gestion de modele en mvc; verif le params d'entree et sortie en temps reel
        # note: p11 cmodif avec combo box pour chgt de langue
        # flake8 + docstring
        # readme
        # dotenv pour clé api
        # deploiement sur heroku (suggestion : dockers)
        # TODO check if all elements in grandpy api response
