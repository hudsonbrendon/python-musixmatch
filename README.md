# Python Musixmatch

Simple integrate of API musixmatch.com with python

[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/python-musixmatch.svg?style=flat)](https://github.com/hudsonbrendon/python-musixmatch/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)
[![Python package](https://github.com/hudsonbrendon/python-musixmatch/actions/workflows/pythonpackage.yml/badge.svg)](https://github.com/hudsonbrendon/python-musixmatch/actions/workflows/pythonpackage.yml)
[![Upload Python Package](https://github.com/hudsonbrendon/python-musixmatch/actions/workflows/python-publish.yml/badge.svg)](https://github.com/hudsonbrendon/python-musixmatch/actions/workflows/python-publish.yml)

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
>>> musixmatch.chart_artists(1, 1)
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
>>> musixmatch.track_search(q_track='Stressed Out', q_artist='twentyonepilots', page_size=10, page=1, s_track_rating='desc')
```

## Track Get

Get a track info from our database: title, artist, instrumental flag and cover art.

Parameters:

- commontrack_id - The musiXmatch commontrack id.
- track_isrc - A valid ISRC identifier.

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

## Matcher Subtitle Get

You can use the f_subtitle_length_max_deviation to fetch subtitles within a given duration range.

Parameters:

- q_track - The song title
- q_artist - The song artist
- f_subtitle_length - Filter by subtitle length in seconds
- f_subtitle_length_max_deviation - Max deviation for a subtitle length in seconds
- track_isrc - If you have an available isrc id in your catalogue you can query using this id only (optional)
- format - Decide the output type json or xml (default json)

Note: This method requires a commercial plan.

```python
>>> musixmatch.matcher_subtitle_get('Sexy and I know it', 'LMFAO', 200, 3)
```

## Artist Get

Get the artist data from our database.

Parameters:

- artist_id - Musixmatch artist id
- artist_mbid - Musicbrainz artist id
- format - Decide the output type json or xml (default json)

```python
>>> musixmatch.artist_get(118)
```

## Artist Search

Search for artists in our database.

Parameters:

- q_artist - The song artist.
- f_artist_id - When set, filter by this artist id.
- f_artist_mbid - When set, filter by this artist musicbrainz id.
- page - Define the page number for paginated results.
- page_size - Define the page size for paginated results (range is 1 to 100).
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.artist_search('prodigy', 1, 1, 16439, '4a4ee089-93b1-4470-af9a-6ff575d32704')
```

## Artist Album Get

Get the album discography of an artist.

Parameters:

- artist_id - Musixmatch artist id.
- artist_mbid - Musicbrainz artist id.
- g_album_name - Group by Album Name.
- s_release_date - Sort by release date (asc|desc).
- page - Define the page number for paginated results.
- page_size - Define the page size for paginated results (range is 1 to 100).
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.artist_albums_get(1039, 1, 1, 1, 'desc')
```

## Artist Related Get

Get a list of artists somehow related to a given one.

Parameters:

- artist_id - Musixmatch artist id.
- artist_mbid - Musicbrainz artist id.
- page - Define the page number for paginated results.
- page_size - Define the page size for paginated results (range is 1 to 100).
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.artist_related_get(56, 1, 1)
```

## Album Get

Get an album from our database: name, release_date, release_type, cover art.

Parameters:

- album_id - The musiXmatch album id
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.album_get(14250417)
```

## Album Tracks Get

This api provides you the list of the songs of an album.

Parameters:

- album_id - Musixmatch album id.
- album_mbid - Musicbrainz album id.
- f_has_lyrics - When set, filter only contents with lyrics.
- page - Define the page number for paginated results.
- page_size - Define the page size for paginated results (range is 1 to 100).
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.album_tracks_get(13750844, 1, 1, '')
```

## Tracking Url Get

Get the base url for the tracking script

With this api you’ll be able to get the base url for the tracking script you need to insert in your page to legalize your existent lyrics library.

Read more here: rights-clearance-on-your-existing-catalog

In case you’re fetching the lyrics by the musiXmatch api called track.lyrics.get you don’t need to implement this API call.

Parameters:

- domain - Your domain name.
- format - Decide the output type json or xml (default json).

```python
>>> musixmatch.album_tracks_get(13750844, 1, 1, '')
```

## Catalogue Dump Get

Get the list of our songs with the lyrics last updated information

CATALOGUE_COMMONTRACKS

Dump of our catalogue in this format:

```python
{
    "track_name": "Shape of you",
    "artist_name": "Ed Sheeran",
	"commontrack_id": 12075763,
    "instrumental": false,
    "has_lyrics": yes,
    "updated_time": "2013-04-08T09:28:40Z"
}
```

Note: This method requires a commercial plan.

```python
>>> musixmatch.catalogue_dump_get('test')
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
- [x] [Matcher Subtitle Get](https://developer.musixmatch.com/documentation/api-reference/matcher-subtitle-get)
- [x] [Artist Get](https://developer.musixmatch.com/documentation/api-reference/artist-get)
- [x] [Artist Search](https://developer.musixmatch.com/documentation/api-reference/artist-search)
- [x] [Artist Albums Get](https://developer.musixmatch.com/documentation/api-reference/artist-albums-get)
- [x] [Artist Related Get](https://developer.musixmatch.com/documentation/api-reference/artist-related-get)
- [x] [Album Get](https://developer.musixmatch.com/documentation/api-reference/album-get)
- [x] [Album Tracks Get](https://developer.musixmatch.com/documentation/api-reference/album-tracks-get)
- [x] [Tracking Url Get](https://developer.musixmatch.com/documentation/api-reference/tracking-url-get)
- [x] [Catalogue Dump Get](https://developer.musixmatch.com/documentation/api-reference/catalogue-dump-get)

# Dependencies

- Python 3.5
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [requests](http://docs.python-requests.org/en/latest/)

# License

[MIT](http://en.wikipedia.org/wiki/MIT_License)
