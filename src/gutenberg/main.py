import requests

from .models import APIException, Book


class GutenbergAPI:
    # DISCLAIMER: PLEASE READ !!!
    # This library is built on the amazing Gutendex project,
    # but the public instance has limited bandwidth and the developer
    # does not make money on the project. If you are able, I HIGHLY encourage
    # you to host your own instance of the API, you will save the developers
    # lots of money and response times will be much faster for you.
    # The instructions for self-hosting can be found here:
    # https://github.com/garethbjohnson/gutendex/wiki/Installation-Guide
    def __init__(self, instance_url="https://gutendex.devbranch.co"):
        self.instance_url = instance_url

    # Methods for getting or searching for lists of books
    def __get_books(
        self,
        author_year_start: int = None,
        author_year_end: int = None,
        copyright: str = None,
        ids: list[int] = None,
        languages: list[str] = None,
        mime_type: str = None,
        search: str = None,
        sort: str = None,
        topic: str = None,
    ):
        endpoint = self.instance_url + "/books"
        response = requests.get(
            endpoint,
            params={
                "author_year_start": author_year_start,
                "author_year_end": author_year_end,
                "copyright": copyright,
                "ids": ids,
                "languages": languages,
                "mime_type": mime_type,
                "search": search,
                "sort": sort,
                "topic": topic,
            },
            timeout=30,
        )
        response.raise_for_status()
        response = response.json()
        if response.get("detail"):
            raise APIException(str(response["detail"]))
        return [Book.from_json(book_json) for book_json in response["results"]]

    def get_all_books(self):
        """Gets all books by the default sorting."""
        return self.__get_books()

    def get_public_domain_books(self):
        return self.__get_books(copyright="false")

    def get_copyrighted_books(self):
        return self.__get_books(copyright="true")

    def get_books_by_ids(self, ids: list[int]):
        return self.__get_books(ids=ids)

    def get_books_by_language(self, languages: list[str]):
        return self.__get_books(languages=",".join(languages))

    def get_books_by_search(self, query: str):
        return self.__get_books(search=query)

    def get_books_by_mime_type(self, mime_type: str):
        return self.__get_books(mime_type=mime_type)

    def get_books_ascending(self):
        return self.__get_books(sorted="ascending")

    def get_oldest(self):
        return self.__get_books(sorted="descending")

    def get_latest(self, topic):
        return self.__get_books(topic=topic)

    # Methods for getting or searching for individual books, their texts, and their metadata
    def __get_book(self, id: int):
        endpoint = self.instance_url + "/books/" + str(id)
        response = requests.get(endpoint, timeout=30)
        response.raise_for_status()
        reponse = response.json()
        if response.detail != None:
            raise APIException(str(response.detail))
        return Book.from_json(response)

    def get_book(self, id: int):
        return self.__get_book(id)

    def get_book_metadata(self, id: int):
        return self.__get_book(id)

    def get_book_text(self, id: int):
        return self.__get_book(id)
