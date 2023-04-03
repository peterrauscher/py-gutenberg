# py-gutenberg

[![Install from pip](https://img.shields.io/badge/pip%20install-py--gutenberg-orange)](https://pypi.org/project/py-gutenberg/) [![Tests Status](https://img.shields.io/github/actions/workflow/status/peterrauscher/py-gutenberg/test.yml?branch=main&label=tests)](https://github.com/peterrauscher/py-gutenberg/actions) [![Build Status](https://img.shields.io/github/actions/workflow/status/peterrauscher/py-gutenberg/release.yml?branch=main&label=build)](https://github.com/peterrauscher/py-gutenberg/actions) [![License](https://img.shields.io/github/license/peterrauscher/py-gutenberg)](https://github.com/peterrauscher/py-gutenberg/blob/main/LICENSE) [![Latest Release Version Number](https://img.shields.io/pypi/v/py-gutenberg)](https://pypi.org/project/py-gutenberg/releases) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/py-gutenberg)](https://pypi.org/project/py-gutenberg)

## Overview

The **py-gutenberg** package is a Python library that provides methods to access the [Project Gutenberg](https://www.gutenberg.org/) library. Users can search for books based on a variety of metadata, get full texts in various formats, and retrieve metadata for books by their ID number.

## Installation

> **_⚠️_** This package has only been tested on Python 3.7 and above. There are no plans for a Python 2 version.

The package can be installed using the pip package manager:

```sh
pip install py-gutenberg
```

## Usage

You should import the module like so:

```python
from gutenberg import GutenbergAPI
```

> The `GutenbergAPI` constructor defaults to using the public instance of the Gutendex API, `https://gutendex.com`. If you are [self-hosting the API](#thanks), you can specify the IP address or URL of your instance with the `instance_url` parameter.

```python
# Uses the public instance
gb = GutenbergAPI()
# Uses a self-hosted instance
gb_private = GutenbergAPI(instance_url="https://gutendex-two.com")
```

### Book Lists and Searching

Here's a simple example to get a list of the most recently uploaded books:

```python
gb.get_all_books()
```

Or, to get only public domain books:

```python
gb.get_public_domain_books()
```

### Individual Books

To get an individual book's metadata:

```python
gb.get_book_metadata()
```

Or, to get the full text of a book:

```python
gb.get_book_text()
```

Full usage information is available in [the documentation](https://github.com/peterrauscher/py-gutenberg/wiki/Documentation)

## Thanks

This module is built on the **wonderful** but unofficial API built by [@garethbjohnson](https://github.com/garethbjohnson) over at [gutendex.com](https://gutendex.com). I have no reason to believe the hosting they've setup is meant to sustain more than a few concurrent users, so please be kind a limit your requests where possible. Additionally, if you intend to use this in a production environment, it is highly encouraged that you self-host.

### Read about [self-hosting the API here!](https://github.com/garethbjohnson/gutendex/wiki/Installation-Guide)
