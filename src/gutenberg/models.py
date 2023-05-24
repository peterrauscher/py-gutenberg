from dataclasses import dataclass
from typing import Dict, List


class APIException(Exception):
    """Raised when Gutendex API returns some error details."""

    pass


@dataclass
class Person:
    """A class representing an author or contributor to a book."""

    birth_year: int
    death_year: int
    name: str

    @classmethod
    def from_json(cls, person_json):
        return cls(
            birth_year=person_json["birth_year"],
            death_year=person_json["death_year"],
            name=person_json["name"],
        )


@dataclass
class Book:
    """A class representing an individual work from the Project Gutenberg library."""

    id: int
    title: str
    authors: List[Person]
    translators: List[Person]
    subjects: List[str]
    bookshelves: List[str]
    languages: List[str]
    copyright: bool
    media_type: str
    formats: Dict[str, str]
    download_count: int

    def __post_init__(self):
        if self.id < 1:
            raise ValueError("Book IDs must be positive integers.")

    @classmethod
    def from_json(cls, book_json):
        return cls(
            id=book_json["id"],
            title=book_json["title"],
            authors=[
                Person.from_json(person_json) for person_json in book_json["authors"]
            ],
            translators=[
                Person.from_json(person_json)
                for person_json in book_json["translators"]
            ],
            subjects=book_json["subjects"],
            bookshelves=book_json["bookshelves"],
            languages=book_json["languages"],
            copyright=book_json["copyright"],
            media_type=book_json["media_type"],
            formats=book_json["formats"],
            download_count=book_json["download_count"],
        )
