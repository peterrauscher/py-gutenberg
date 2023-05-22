import requests

from .models import APIException, Book


class GutenbergAPI:
    # === DISCLAIMER ===
    # This library is built on the amazing Gutendex project, but the only two
    # public instances are hosted by me (https://gutendex.devbranch.co) and by
    # the developer of Gutendex (https://gutendex.com). If you can, PLEASE self-host.
    # The instructions for doing so can be found here:
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
        limit=32,
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
        if not response:
            raise APIException("No response from server")
        response.raise_for_status()
        res_json = response.json()
        if res_json.get("detail", None):
            raise APIException(str(res_json.get("detail")))
        return [Book.from_json(book_json) for book_json in res_json.get("results", [])]

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
        if not response:
            raise APIException("No response from server")
        response.raise_for_status()
        res_json = response.json()
        if res_json.get("detail", None):
            raise APIException(str(res_json.get("detail")))
        return Book.from_json(res_json)

    def get_book(self, id: int):
        return self.__get_book(id)

    def get_book_metadata(self, id: int):
        return self.__get_book(id)

    def get_book_text(self, id: int):
        return self.__get_book(id)
