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
>>> from musixmatch import Musixmatch

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

## Chart Tracks Get

Search for track in our database.

Parameters:

- q_track - The song title
- q_artist - The song artist
- q_lyrics - Any word in the lyrics
- f_artist_id - When set, filter by this artist id
- f_music_genre_id - When set, filter by this music category id
- f_lyrics_language - Filter by the lyrics language (en,it,..)
- f_has_lyrics - When set, filter only contents with lyrics
- f_track_release_group_first_release_date_min - When set, filter the tracks with release date newer than value, format is YYYYMMDD
- f_track_release_group_first_release_date_max - When set, filter the tracks with release date older than value, format is YYYYMMDD
- s_artist_rating - Sort by our popularity index for artists (asc|desc)
- s_track_rating - Sort by our popularity index for tracks (asc|desc)
- quorum_factor - Search only a part of the given query string.Allowed range is (0.1 – 0.9)
- page - Define the page number for paginated results
- page_size - Define the page size for paginated results. Range is 1 to 100.
- callback - jsonp callback
- format - Decide the output type (json or xml)

```python
>>> musixmatch.track_search(q_artist='twentyonepilots', page_size=10, page=1, s_track_rating='desc')
```

## Track Get

Get a track info from our database: title, artist, instrumental flag and cover art.

Parameters:

- track_id - The musiXmatch track id.
- commontrack_id - The musiXmatch commontrack id.
- track_isrc - A valid ISRC identifier.
- track_mbid - The musicbrainz recording id.
- format - Decide the output type json or xml (default json).


```python
>>> musixmatch.track_get(15445219)
```

## Track Lyrics Get

Get the lyrics of a track.

Parameters:

- track_id - The musiXmatch track id.
- track_mbid - The musicbrainz recording id.
- format - Decide the output type json or xml (default json).


```python
>>> musixmatch.track_lyrics_get(15953433)
```

## Track Snippet Get

Get the snippet for a given track.

A lyrics snippet is a very short representation of a song lyrics. It’s usually twenty to a hundred characters long and it’s calculated extracting a sequence of words from the lyrics.

Parameters:

- track_id - The musiXmatch track id.
- format - Decide the output type json or xml (default json).


```python
>>> musixmatch.track_snippet_get(16860631)
```

## Track Snippet Get

Retreive the subtitle of a track.

Return the subtitle of a track in LRC or DFXP format. Refer to Wikipedia LRC format page or DFXP format on W3c for format specifications.

Parameters:

- track_id - The musiXmatch track id.
- track_mbid - The musicbrainz track id.
- subtitle_format - The format of the subtitle (lrc,dfxp,stledu). Default to lrc.
- f_subtitle_length - The desired length of the subtitle (seconds).
- f_subtitle_length_max_deviation - The maximum deviation allowed from the f_subtitle_length (seconds).
- format - Decide the output type json or xml (default json).


```python
>>> musixmatch.track_subtitle_get(14201829)
```

## Track Richsync Get

Get the Rich sync for a track.

A rich sync is an enhanced version of the standard sync which allows:

- position offset by single characther.
- endless formatting options at single char level.
- multiple concurrent voices.
- multiple scrolling direction.

Parameters:

- track_id - The musiXmatch track id.
- f_sync_length - The desired length of the sync (seconds).
- f_sync_length_max_deviation - The maximum deviation allowed.
- from the f_sync_length (seconds).
- format - Decide the output type json or xml (default json).


```python
>>> musixmatch.track_richsync_get(14201829)
```

## Track Lyrics Post

Submit a lyrics to our database.

It may happen we don’t have the lyrics for a song, you can ask your users to help us sending the missing lyrics. We’ll validate every submission and in case, make it available through our api.

Please take all the necessary precautions to avoid users or automatic software to use your website/app to use this commands, a captcha solution like http://www.google.com/recaptcha or an equivalent one has to be implemented in every user interaction that ends in a POST operation on the musixmatch api.

Parameters:

- track_i - dA valid country code (default US).
- lyrics_body - The lyrics.
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.track_lyrics_post(1471157, 'test')
```

## Track Lyrics Post

This API method provides you the opportunity to help us improving our catalogue.

We aim to provide you with the best quality service imaginable, so we are especially interested in your detailed feedback to help us to continually improve it.

Please take all the necessary precautions to avoid users or automatic software to use your website/app to use this commands, a captcha solution like http://www.google.com/recaptcha or an equivalent one has to be implemented in every user interaction that ends in a POST operation on the musixmatch api.

Parameters:

- lyrics_id - The musiXmatch lyrics id.
- track_id - The musiXmatch track id.
- feedback - The feedback to be reported, possible values are: wrong_lyrics, wrong_attribution, bad_characters,
- lines_too_long, wrong_verses, wrong_formatting
- format - Decide the output type json or xml (default json)

```python
>>> musixmatch.track_lyrics_feedback_post(1471157, 4193713, 'wrong_verses')
```

## Matcher Lyrics Get

Get the lyrics for track based on title and artist.

Parameters:

- q_track - The song title
- q_artist - The song artist
- track_isrc - If you have an available isrc id in your catalogue you can query using this id only (optional)
- format - Decide the output type json or xml (default json)

```python
>>> musixmatch.matcher_lyrics_get('Sexy and I know it', 'LMFAO')
```

## Matcher Track Get

Match your song against our database.

In some cases you already have some informations about the track title, artist name, album etc.
A possible strategy to get the corresponding lyrics could be:
- search our catalogue with a perfect match,
- maybe try using the fuzzy search,
- maybe try again using artist aliases, and so on.

The matcher.track.get method does all the job for you in a single call. This way you dont’t need to worry about the details, and you’ll get instant benefits for your application without changing a row in your code, while we take care of improving the implementation behind. Cool, uh?

Parameters:

- q_track - The song title.
- q_artist - The song artist.
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.matcher_track_get('Lose Yourself (soundtrack)', 'Eminem')
```

# Features

- [x] [Chart Artists Get](https://developer.musixmatch.com/documentation/api-reference/artist-chart-get)
- [x] [Chart Track Get](https://developer.musixmatch.com/documentation/api-reference/track-chart-get)
- [x] [Track Search](https://developer.musixmatch.com/documentation/api-reference/track-search)
- [x] [Track Get](https://developer.musixmatch.com/documentation/api-reference/track-get)
- [x] [Track Lyrics Get](https://developer.musixmatch.com/documentation/api-reference/track-lyrics-get)
- [x] [Track Snippet Get](https://developer.musixmatch.com/documentation/api-reference/track-snippet-get)
- [x] [Track Subtitle Get](https://developer.musixmatch.com/documentation/api-reference/track-subtitle-get)
- [x] [Track Richsync Get](https://developer.musixmatch.com/documentation/api-reference/track-richsync-get)
- [x] [Track Lyrics Post](https://developer.musixmatch.com/documentation/api-reference/track-lyrics-post)
- [x] [Track Lyrics Feedback Post](https://developer.musixmatch.com/documentation/api-reference/track-lyrics-feedback-post)
- [x] [Matcher Lyrics Get](https://developer.musixmatch.com/documentation/api-reference/matcher-lyrics-get)
- [x] [Matcher Track Get](https://developer.musixmatch.com/documentation/api-reference/matcher-track-get)
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
