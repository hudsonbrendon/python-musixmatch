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

        country - A valid country code (default US).
        page - Define the page number for paginated results.
        page_size - Define the page size for paginated results (range 1 - 100).
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
        data = self._request(self._get_url('chart.tracks.get?'
                                           'page={}&page_size={}'
                                           '&country={}&format={}'
                                           '&f_has_lyrics={}'
                                           .format(page,
                                                   _set_page_size(page_size),
                                                   country, _format,
                                                   f_has_lyrics)))
        return data
