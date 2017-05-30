# Python Musixmatch

Simple integrate of API musixmatch.com with python

[![Build Status](https://travis-ci.org/hudsonbrendon/python-musixmatch.svg?branch=master)](https://travis-ci.org/hudsonbrendon/python-musixmatch)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/python-musixmatch.svg?style=flat)](https://github.com/hudsonbrendon/python-musixmatch/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![Logo](logo.jpg)

# Quick start

```bash
$ pip install pymusixmatch
```
or

```bash
$ python setup.py install
```

# Authentication

Register for an API key:

All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret.

# Usage

With your key in hand, it's time to authenticate, so run:

```python
>>> from musixmatch.musixmatch import Musixmatch

>>> musixmatch = Musixmatch('<apikey>')
```

## Chart Artists Get

This api provides you the list of the top artists of a given country.

Parameters:

- country - A valid country code (default US).
- page - Define the page number for paginated results.
- page_size - Define the page size for paginated results (range 1 - 100).
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.chart_artists_get(1, 1)
```

## Chart Tracks Get

This api provides you the list of the top songs of a given country.

Parameters:

- page - Define the page number for paginated results.
- page_size - Define the page size for paginated results (range 1 - 100).
- f_has_lyrics - When set, filter only contents with lyrics.
- country - A valid country code (default US).
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.chart_tracks_get(1, 1)
```

```
# Features
- [x] [Chart Artists Get](https://developer.musixmatch.com/documentation/api-reference/artist-chart-get)
- [x] [Chart Track Get](https://developer.musixmatch.com/documentation/api-reference/track-chart-get)
- [ ] [Track Search](https://developer.musixmatch.com/documentation/api-reference/track-search)
- [ ] [Track Get](https://developer.musixmatch.com/documentation/api-reference/track-get)
- [ ] [Track Lyrics Get](https://developer.musixmatch.com/documentation/api-reference/track-lyrics-get)
- [ ] [Track Snippet Get](https://developer.musixmatch.com/documentation/api-reference/track-snippet-get)
- [ ] [Track Subtitle Get](https://developer.musixmatch.com/documentation/api-reference/track-subtitle-get)
- [ ] [Track Richsync Get](https://developer.musixmatch.com/documentation/api-reference/track-richsync-get)
- [ ] [Track Lyrics Post](https://developer.musixmatch.com/documentation/api-reference/track-lyrics-post)
- [ ] [Track Lyrics Feedback Post](https://developer.musixmatch.com/documentation/api-reference/track-lyrics-feedback-post)
- [ ] [Matcher Lyrics Get](https://developer.musixmatch.com/documentation/api-reference/matcher-lyrics-get)
- [ ] [Matcher Lyrics Get](https://developer.musixmatch.com/documentation/api-reference/matcher-lyrics-get)
- [ ] [Matcher Track Get](https://developer.musixmatch.com/documentation/api-reference/matcher-track-get)
- [ ] [Matcher Subtitle Get](https://developer.musixmatch.com/documentation/api-reference/matcher-subtitle-get)
- [ ] [Artist Get](https://developer.musixmatch.com/documentation/api-reference/artist-get)
- [ ] [Artist Search](https://developer.musixmatch.com/documentation/api-reference/artist-search)
- [ ] [Artist Albums Get](https://developer.musixmatch.com/documentation/api-reference/artist-albums-get)
- [ ] [Artist Related Get](https://developer.musixmatch.com/documentation/api-reference/artist-related-get)
- [ ] [Album Get](https://developer.musixmatch.com/documentation/api-reference/album-get)
- [ ] [Album Tracks Get](https://developer.musixmatch.com/documentation/api-reference/album-tracks-get)
- [ ] [Tracking Url Get](https://developer.musixmatch.com/documentation/api-reference/tracking-url-get)
- [ ] [Catalogue Dump Get](https://developer.musixmatch.com/documentation/api-reference/catalogue-dump-get)

# Dependencies
- Python 3.5
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [requests](http://docs.python-requests.org/en/latest/)

# License
[MIT](http://en.wikipedia.org/wiki/MIT_License)
