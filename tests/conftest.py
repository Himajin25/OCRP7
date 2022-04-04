""" File containing pytest fixtures used in tests """
import pytest
from app import app


def flask_app():
    """ Configuration of flask app to be used in the flask test client """
    app = app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client():
    """ Initiates flask app test client  """
    return app.test_client()


@pytest.fixture()
def mock_mapbox_api_response_failure():
    """ Mocked Mapbox API succesful json response from invalid input query """
    mapbox_api_response = {
        "type": "FeatureCollection",
        "query": ["zfcreoh"],
        "features": [],
        "attribution": "NOTICE: © 2022 Mapbox and its suppliers. All rights reserved. Use of this data is subject to the Mapbox Terms of Service (https://www.mapbox.com/about/maps/). This response and the information it contains may not be retained. POI(s) provided by Foursquare.",
    }
    return mapbox_api_response


@pytest.fixture()
def mock_mapbox_api_response_success():
    """ Mocked Mapbox API succesful json response from a valid input query """
    mapbox_api_response = {
        "type": "FeatureCollection",
        "query": ["the", "eiffel", "tower"],
        "features": [
            {
                "id": "poi.1236950632550",
                "type": "Feature",
                "place_type": ["poi"],
                "relevance": 0.96,
                "properties": {
                    "address": "5 avenue Anatole France",
                    "foursquare": "51a2445e5019c80b56934c75",
                    "wikidata": "Q243",
                    "landmark": True,
                    "category": "monument, landmark, historic",
                },
                "text": "Tour Eiffel",
                "place_name": "Tour Eiffel, 5 avenue Anatole France, Paris, 75007, France",
                "matching_text": "The Eiffel Tower",
                "matching_place_name": "The Eiffel Tower, 5 avenue Anatole France, Paris, 75007, France",
                "center": [2.294786, 48.85877975],
                "geometry": {"coordinates": [2.294786, 48.85877975], "type": "Point"},
            }
        ],
    }
    return mapbox_api_response


@pytest.fixture()
def mock_fetched_invalid_location_data():
    """ Mocked output of "fetch_location_data()" using an invalid location uery """
    zfcreoh_location_data = {"message": "not found"}
    return zfcreoh_location_data


@pytest.fixture()
def mock_fetched_valid_location_data():
    """ Mocked output of "fetch_location_data()" method using a valid location uery """
    eiffel_tower_location_data = {
        "id": "poi.1236950632550",
        "type": "Feature",
        "place_type": ["poi"],
        "relevance": 0.96,
        "properties": {
            "address": "5 avenue Anatole France",
            "foursquare": "51a2445e5019c80b56934c75",
            "wikidata": "Q243",
            "landmark": True,
            "category": "monument, landmark, historic",
        },
        "text": "Tour Eiffel",
        "place_name": "Tour Eiffel, 5 avenue Anatole France, Paris, 75007, France",
        "matching_text": "The Eiffel Tower",
        "matching_place_name": "The Eiffel Tower, 5 avenue Anatole France, Paris, 75007, France",
        "center": [2.294786, 48.85877975],
        "geometry": {"coordinates": [2.294786, 48.85877975], "type": "Point"},
    }
    return eiffel_tower_location_data


@pytest.fixture()
def mock_wikidata_response():
    """ Mocked Wikidata API json response """
    eiffel_tower_wikidata_info = {
        "entities": {
            "Q243": {
                "type": "item",
                "id": "Q243",
                "sitelinks": {
                    "enwiki": {
                        "site": "enwiki",
                        "title": "Eiffel Tower",
                        "badges": [],
                        "url": "https://en.wikipedia.org/wiki/Eiffel_Tower",
                    },
                    "frwiki": {
                        "site": "frwiki",
                        "title": "Tour Eiffel",
                        "badges": [],
                        "url": "https://fr.wikipedia.org/wiki/Tour_Eiffel",
                    },
                },
            }
        }
    }
    return eiffel_tower_wikidata_info


@pytest.fixture()
def mock_wikipedia_response():
    """ Mocked Wikipedia API json response """
    eiffel_tower_wikipedia_raw_extract = {
        "batchcomplete": "",
        "query": {
            "pageids": ["9232"],
            "pages": {
                "9232": {
                    "pageid": 9232,
                    "ns": 0,
                    "title": "Eiffel Tower",
                    "extract": 'The Eiffel Tower ( EYE-fəl; French: tour Eiffel [tuʁ‿ɛfɛl] (listen)) is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.\nLocally nicknamed "La dame de fer" (French for "Iron Lady"), it was constructed from 1887 to 1889 as the centerpiece of the 1889 World\'s Fair and was initially criticized by some of France\'s leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world. The Eiffel Tower is the most visited monument with an entrance fee in the world; 6.91 million people ascended it in 2015. The Tower was made a Monument historique in 1964 and named part of UNESCO World Heritage Site ("Paris, Banks of the Seins") in 1991.The tower is 330 metres (1,083 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris.',
                }
            },
        },
    }
    return eiffel_tower_wikipedia_raw_extract


@pytest.fixture()
def mock_wikipedia_extract():
    """ Mocked output from "get_page_extract()" method """
    extract = 'The Eiffel Tower ( EYE-fəl; French: tour Eiffel [tuʁ‿ɛfɛl] (listen)) is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.\nLocally nicknamed "La dame de fer" (French for "Iron Lady"), it was constructed from 1887 to 1889 as the centerpiece of the 1889 World\'s Fair and was initially criticized by some of France\'s leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world. The Eiffel Tower is the most visited monument with an entrance fee in the world; 6.91 million people ascended it in 2015. The Tower was made a Monument historique in 1964 and named part of UNESCO World Heritage Site ("Paris, Banks of the Seins") in 1991.The tower is 330 metres (1,083 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris.'
    return extract
