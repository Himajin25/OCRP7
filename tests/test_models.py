""" File containing the tests for the models.py file """
from grandpy_app.models import (
    ParserClient,
    MapboxClient,
    WikidataClient,
    WikipediaClient,
)


class TestParserClient:
    """ Class testing the Parser class with a dummy input  """

    mock_user_input = "Do you know where the Eiffel Tower is?"
    mock_parser_object = ParserClient(mock_user_input)

    def test_spacy_en(self):
        """ Method testing parsing of user input using spacy """
        expected_parsed_location = "the Eiffel Tower"
        mock_parsed_location = self.mock_parser_object.spacy_en()

        assert expected_parsed_location == mock_parsed_location


class TestMapboxClient:
    """ Tests the code calling the Mapbox API using dummy input and using mocked response """

    mock_location = "the Eiffel Tower"
    mock_mapbox = MapboxClient(mock_location)

    def test_fetch_location_from_valid_query(
        self, mocker, mock_mapbox_api_response_success, mock_fetched_valid_location_data
    ):
        """ Method testing the fetch_location_from_query method using a valid query and a mocked output """
        mocker.patch(
            "grandpy_app.models.MapboxClient.get_json",
            return_value=mock_mapbox_api_response_success,
        )
        expected_location_data = self.mock_mapbox.fetch_location_from_query()

        assert expected_location_data == mock_fetched_valid_location_data

    def test_fetch_location_from_invalid_query(
        self,
        mocker,
        mock_mapbox_api_response_failure,
        mock_fetched_invalid_location_data,
    ):
        """ Method testing the fetch_location_from_query method using an invalid query and a mocked output """
        mocker.patch(
            "grandpy_app.models.MapboxClient.get_json",
            return_value=mock_mapbox_api_response_failure,
        )

        expected_location_data = self.mock_mapbox.fetch_location_from_query()

        assert expected_location_data == mock_fetched_invalid_location_data

    def test_get_wiki_id(self, mock_fetched_valid_location_data):
        """ Method testing the get_wiki_id method using a mocked location data from Mapbox API  """
        expected_id = "Q243"
        mocked_id = self.mock_mapbox.get_wiki_id(mock_fetched_valid_location_data)

        assert expected_id == mocked_id


class TestWikidataClient:
    """ Class testing the code calling the Wikidata API using dummy input and using mocked response """

    mock_id = "Q243"
    mock_wikidata_object = WikidataClient(mock_id)

    def test_get_wikipage_title(self, mocker, mock_wikidata_response):
        """ Method testing the "get_wiki()" method using a mock Wikidata API response """
        mocker.patch(
            "grandpy_app.models.WikidataClient.get_json",
            return_value=mock_wikidata_response,
        )
        expected_title = "Eiffel Tower"
        mock_wikidata_title = self.mock_wikidata_object.get_wikipage_en_title()

        assert expected_title == mock_wikidata_title


class TestWikipediaClient:
    """ Tests the code calling the Wikipedia API using dummy input and using mocked response """

    mock_title = "Eiffel Tower"
    mock_wikipedia_object = WikipediaClient(mock_title)

    def test_get_page_id(self, mocker, mock_wikipedia_response):
        """ Method testing the "get_page_id()" method using a mock Wikipedia API response """
        mocker.patch(
            "grandpy_app.models.WikipediaClient.get_json",
            return_value=mock_wikipedia_response,
        )
        expected_page_id = "9232"
        mock_page_id = self.mock_wikipedia_object.get_page_id()

        assert expected_page_id == mock_page_id

    def test_get_page_extract(self, mocker, mock_wikipedia_response):
        """ Method testing the "get_page_extract()" method using a mock Wikipedia API response """
        mocker.patch(
            "grandpy_app.models.WikipediaClient.get_json",
            return_value=mock_wikipedia_response,
        )
        expected_extract = 'The Eiffel Tower ( EYE-fəl; French: tour Eiffel [tuʁ‿ɛfɛl] (listen)) is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.\nLocally nicknamed "La dame de fer" (French for "Iron Lady"), it was constructed from 1887 to 1889 as the centerpiece of the 1889 World\'s Fair and was initially criticized by some of France\'s leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world. The Eiffel Tower is the most visited monument with an entrance fee in the world; 6.91 million people ascended it in 2015. The Tower was made a Monument historique in 1964 and named part of UNESCO World Heritage Site ("Paris, Banks of the Seins") in 1991.The tower is 330 metres (1,083 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris.'
        mock_page_id = "9232"
        mock_extract = self.mock_wikipedia_object.get_page_extract(mock_page_id)

        assert expected_extract == mock_extract
