import unittest
import os

from musixmatch import Musixmatch


class TestMusixmatch(unittest.TestCase):

    def setUp(self):
        self.musixmatch = Musixmatch(os.environ.get('APIKEY'))
        self.url = 'http://api.musixmatch.com/ws/1.1/'

    def test_get_url(self):
        self.assertEqual(self.musixmatch
                         ._get_url('chart.artists.get?'
                                   'page=1&page_size=1&country=us'
                                   '&format=json'),
                         self.url + 'chart.artists.get?'
                                    'page=1&page_size=1'
                                    '&country=us&format=json&apikey={}'
                                    .format(os.environ.get('APIKEY')))

    def test_apikey(self):
        self.assertEqual(self.musixmatch._apikey, os.environ.get('APIKEY'))

    def test_chart_artists(self):
        self.assertEqual(self.musixmatch.chart_artists(1, 1)
                         ['message']['body']['artist_list'][0]
                         ['artist']['artist_vanity_id'], 'Ed-Sheeran')
        self.assertEqual(self.musixmatch.chart_artists(1, 1)
                         ['message']['body']['artist_list'][0]
                         ['artist']['artist_mbid'],
                         'b8a7c51f-362c-4dcb-a259-bc6e0095f0a6')

    def test_chart_tracks_get(self):
        self.assertEqual(self.musixmatch.chart_tracks_get(1, 1, 1)
                         ['message']['body']['track_list'][0]
                         ['track']['album_name'],
                         'Despacito Feat. Justin Bieber (Remix)')
        self.assertEqual(self.musixmatch.chart_tracks_get(1, 1, 1)
                         ['message']['body']['track_list'][0]
                         ['track']['track_name'],
                         'Despacito - Remix')


if __name__ == '__main__':
    unittest.main()
