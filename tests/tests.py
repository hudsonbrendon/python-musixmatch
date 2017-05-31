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

    def test_track_search(self):
        self.assertEqual(self.musixmatch.track_search(q_artist='justinbieber',
                                                      page_size=10, page=1,
                                                      s_track_rating='desc')
                                                      ['message']['body']
                                                      ['track_list'], [])

    def test_track_get(self):
        self.assertEqual(self.musixmatch.track_get(15445219)
                         ['message']['body']['track']['artist_name'],
                         'Lady Gaga')
        self.assertEqual(self.musixmatch.track_get(15445219)
                         ['message']['body']['track']['album_name'],
                         'The Fame Monster')

    def test_track_lyrics_get(self):
        self.assertEqual(self.musixmatch.track_lyrics_get(15953433)
                         ['message']['body']['lyrics']['lyrics_language'],
                         'en')
        self.assertEqual(self.musixmatch.track_lyrics_get(15953433)
                         ['message']['body']['lyrics']
                         ['lyrics_language_description'], 'English')
        self.assertEqual(self.musixmatch.track_lyrics_get(15953433)
                         ['message']['body']['lyrics']
                         ['lyrics_id'], 15912802)

    def test_track_snippet_get(self):
        self.assertEqual(self.musixmatch.track_snippet_get(16860631)
                         ['message']['body']['snippet']['snippet_id'],
                         16229519)
        self.assertEqual(self.musixmatch.track_snippet_get(16860631)
                         ['message']['body']['snippet']['snippet_body'],
                         "You shoot me down, but I won't fall")


if __name__ == '__main__':
    unittest.main()
