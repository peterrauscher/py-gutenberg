from dataclasses import dataclass
from typing import Dict, List


class APIException(Exception):
    """Raised when Gutendex API returns some error details."""

    pass


@dataclass
class Person:
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
    """A class for individual books"""

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


langs = {
    "en": "English",
    "nl": "Dutch",
    "de": "German",
    "it": "Italian",
    "zh": "Chinese",
    "da": "Danish",
    "eo": "Esperanto",
    "fi": "Finnish",
    "fr": "French",
    "el": "Greek",
    "hu": "Hungarian",
    "la": "Latin",
    "pt": "Portuguese",
    "es": "Spanish",
    "sv": "Swedish",
    "tl": "Tagalog",
    "af": "Afrikaans",
    "ale": "Aleut",
    "ar": "Arabic",
    "arp": "Arapaho",
    "brx": "Bodo",
    "br": "Breton",
    "bg": "Bulgarian",
    "rmr": "Caló",
    "ca": "Catalan",
    "ceb": "Cebuano",
    "cs": "Czech",
    "et": "Estonian",
    "fa": "Farsi",
    "fy": "Frisian",
    "fur": "Friulian",
    "gla": "Gaelic, Scottish",
    "gl": "Galician",
    "kld": "Gamilaraay",
    "grc": "Greek, Ancient",
    "he": "Hebrew",
    "is": "Icelandic",
    "ilo": "Iloko",
    "ia": "Interlingua",
    "iu": "Inuktitut",
    "ga": "Irish",
    "ja": "Japanese",
    "csb": "Kashubian",
    "kha": "Khasi",
    "ko": "Korean",
    "lt": "Lithuanian",
    "mi": "Maori",
    "myn": "Mayan Languages",
    "enm": "Middle English",
    "nah": "Nahuatl",
    "nap": "Napoletano-Calabrese",
    "nav": "Navajo",
    "nai": "North American Indian",
    "no": "Norwegian",
    "oc": "Occitan",
    "oji": "Ojibwa",
    "ang": "Old English",
    "pl": "Polish",
    "ro": "Romanian",
    "ru": "Russian",
    "sa": "Sanskrit",
    "sr": "Serbian",
    "sl": "Slovenian",
    "bgs": "Tagabawa",
    "te": "Telugu",
    "bo": "Tibetan",
    "cy": "Welsh",
    "yi": "Yiddish",
}
