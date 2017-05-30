import requests
import json

from .utils import _set_page_size


class Musixmatch(object):

    def __init__(self, apikey):
        ''' Define objects of type Musixmatch.

        Parameters:
        apikey - For get your apikey access: https://developer.musixmatch.com
        '''
        self.__apikey = apikey
        self.__url = 'http://api.musixmatch.com/ws/1.1/'

    def _get_url(self, url):
        return self.__url + '{}&apikey={}'.format(url, self._apikey)

    @property
    def _apikey(self):
        return self.__apikey

    def _request(self, url):
        data = requests.get(url).json()
        return data

    def chart_artists(self, page, page_size, country='us', _format='json'):
        ''' This api provides you the list
        of the top artists of a given country.

        Parameters:

        page - Define the page number for paginated results.
        page_size - Define the page size for paginated results (range 1 - 100).
        country - A valid country code (default US).
        format - Decide the output type json or xml (default json).
        '''
        data = self._request(self._get_url('chart.artists.get?'
                                           'page={}&page_size={}'
                                           '&country={}&format={}'
                                           .format(page,
                                                   _set_page_size(page_size),
                                                   country, _format)))
        return data

    def chart_tracks_get(self, page, page_size, f_has_lyrics,
                         country='us', _format='json'):
        ''' This api provides you the list
        of the top songs of a given country.

        Parameters:

        page - Define the page number for paginated results.
        page_size - Define the page size for paginated results (range 1 - 100).
        f_has_lyrics - When set, filter only contents with lyrics.
        country - A valid country code (default US).
        format - Decide the output type json or xml (default json).
        '''
        data = self._request(self._get_url('chart.tracks.get?'
                                           'page={}&page_size={}'
                                           '&country={}&format={}'
                                           '&f_has_lyrics={}'
                                           .format(page,
                                                   _set_page_size(page_size),
                                                   country, _format,
                                                   f_has_lyrics)))
        return data

    def track_search(self, q_artist, page_size, page,
                     s_track_rating, _format='json'):
        ''' Search for track in our database.

        Parameters:

        q_track - The song title
        q_artist - The song artist
        q_lyrics - Any word in the lyrics
        f_artist_id - When set, filter by this artist id
        f_music_genre_id - When set, filter by this music category id
        f_lyrics_language - Filter by the lyrics language (en,it,..)
        f_has_lyrics - When set, filter only contents with lyrics
        f_track_release_group_first_release_date_min - When set, filter
        the tracks with release date newer than value, format is YYYYMMDD
        f_track_release_group_first_release_date_max - When set, filter
        the tracks with release date older than value, format is YYYYMMDD
        s_artist_rating - Sort by our popularity index for artists (asc|desc)
        s_track_rating - Sort by our popularity index for tracks (asc|desc)
        quorum_factor - Search only a part of the given query string.
        Allowed range is (0.1 – 0.9)
        page - Define the page number for paginated results
        page_size - Define the page size for paginated results.
        Range is 1 to 100.
        callback - jsonp callback
        format - Decide the output type (json or xml)
        '''
        data = self._request(self._get_url('track.search?'
                                           'q_artist={}'
                                           '&page_size={}'
                                           '&page={}'
                                           '&s_track_rating={}'
                                           .format(q_artist, page_size, page,
                                                   s_track_rating, _format)))
        return data
