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
# Usage

To access the API you'll need to login, use:

```python
>>> from musixmatch.musixmatch import Musixmatch

>>> musixmatch = Musixmatch('<apikey>')
```

```python
>>> musixmatch.chart_artists(1, 1)
```

```python
{'message': {
    'header': {
        'status_code': 200,
        'execute_time': 0.011009931564331
    }, 'body': {
            'artist_list': [{
                'artist': {
                    'artist_country': 'GB',
                    'artist_credits': {
                        'artist_list': []
                    },
                    'artist_share_url': 'https://www.musixmatch.com/artist/Ed-Sheeran',
                    'artist_name_translation_list': [],
                    'artist_edit_url': 'https://www.musixmatch.com/artist/Ed-Sheeran?utm_source=application&utm_campaign=api&utm_medium=Code+Rocket',
                    'artist_mbid': 'b8a7c51f-362c-4dcb-a259-bc6e0095f0a6',
                    'artist_name': 'Ed Sheeran',
                    'artist_alias_list': [{
                        'artist_alias': 'エド シーラン'
                    },
                    {'artist_alias': 'ai de xi lan'},
                    {'artist_alias': 'Ed shiran'}],
                    'updated_time': '2017T22:35:37Z',
                    'artist_comment': '',
                    'artist_vanity_id': 'Ed-Sheeran',
                    'primary_genres': {
                        'music_genre_list': [{
                            'music_genre': {
                                'music_genre_id': 10,
                                'music_genre_parent_id': 34,
                                'music_genre_name': 'Singer/Songwriter',
                                'music_genre_vanity': 'Singer-Songwriter',
                                'music_genre_name_extended': 'Singer/Songwriter'
                            }
                        }]
                    },
                    'restricted': 0,
                    'managed': 0,
                    'artist_rating': 100,
                    'artist_twitter_url': 'https://twitter.com/edsheeran',
                    'artist_id': 33111847,
                    'secondary_genres': {
                        'music_genre_list': []
                    }
                }
            }]
        }
    }
}
```
# Features
- [x] [Chart Artists Get](https://developer.musixmatch.com/documentation/api-reference/artist-chart-get)
- [ ] [Chart Track Get](https://developer.musixmatch.com/documentation/api-reference/track-chart-get)
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
