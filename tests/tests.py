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
                         '2U (feat. Justin Bieber)')
        self.assertEqual(self.musixmatch.chart_tracks_get(1, 1, 1)
                         ['message']['body']['track_list'][0]
                         ['track']['track_name'],
                         '2U')

    def test_track_search(self):
        self.assertEqual(self.musixmatch
                             .track_search(q_track='Let Me Love You',
                                           q_artist='justinbieber',
                                           page_size=10, page=1,
                                           s_track_rating='desc')['message']
                                           ['body']['track_list'], [])

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

    def test_track_subtitle_get(self):
        self.assertEqual(self.musixmatch.track_subtitle_get(14201829)
                         ['message']['body'], '')

    def test_track_richsync_get(self):
        self.assertEqual(self.musixmatch.track_richsync_get(114837357)
                         ['message']['body']['richsync']['richsync_id'], 6)
        self.assertEqual(self.musixmatch.track_richsync_get(114837357)
                         ['message']['body']['richsync']
                         ['richsync_length'], 230)

    def test_track_lyrics_post(self):
        self.assertEqual(self.musixmatch.track_lyrics_post(1471157, 'test')
                         ['message']['header']['status_code'], 200)
        self.assertEqual(self.musixmatch.track_lyrics_post(1471157, 'test')
                         ['message']['body'], '')

    def test_track_lyrics_feedback_post(self):
        self.assertEqual(self.musixmatch.track_lyrics_post(1471157, 4193713,
                         'wrong_verses')['message']['body'], '')

    def test_matcher_lyrics_get(self):
        self.assertEqual(self.musixmatch
                         .matcher_lyrics_get('Sexy and I know it', 'LMFAO')
                         ['message']['body']['lyrics']
                         ['lyrics_language_description'], 'English')
        self.assertEqual(self.musixmatch
                         .matcher_lyrics_get('Sexy and I know it', 'LMFAO')
                         ['message']['body']['lyrics']
                         ['lyrics_language'], 'en')

    def test_matcher_track_get(self):
        self.assertEqual(self.musixmatch
                         .matcher_track_get('Lose Yourself (soundtrack)',
                                            'Eminem')['message']['body']
                                                     ['track']['track_name'],
                                                     'Lose Yourself - '
                                                     'Soundtrack Version'
                                                     ' (Explicit)')
        self.assertEqual(self.musixmatch
                         .matcher_track_get('Lose Yourself (soundtrack)',
                                            'Eminem')['message']['body']
                                                     ['track']['album_name'],
                                                     'Curtain Call')

    def test_matcher_subtitle_get(self):
        self.assertEqual(self.musixmatch
                         .matcher_subtitle_get('Sexy and I know it',
                                               'LMFAO', 200, 3)
                                               ['message']['body'], '')

    def test_artist_get(self):
        self.assertEqual(self.musixmatch.artist_get(118)
                         ['message']['body']['artist']['artist_name'], 'Queen')
        self.assertEqual(self.musixmatch.artist_get(118)
                         ['message']['body']['artist']['artist_mbid'],
                         '5eecaf18-02ec-47af-a4f2-7831db373419')

    def test_artist_search(self):
        self.assertEqual(self.musixmatch.artist_search('prodigy',
                         1, 1, 16439, '4a4ee089-93b1-4470-af9a-6ff575d32704')
                         ['message']['body']['artist_list'][0]['artist']
                         ['artist_id'], 16439)
        self.assertEqual(self.musixmatch.artist_search('prodigy',
                         1, 1, 16439, '4a4ee089-93b1-4470-af9a-6ff575d32704')
                         ['message']['body']['artist_list'][0]['artist']
                         ['artist_name'], 'The Prodigy')

    def test_artist_albums_get(self):
        self.assertEqual(self.musixmatch
                         .artist_albums_get(1039, 1, 1, 1, 'desc')
                         ['message']['body']['album_list'][0]['album']
                         ['album_id'], 25660826)
        self.assertEqual(self.musixmatch
                         .artist_albums_get(1039, 1, 1, 1, 'desc')
                         ['message']['body']['album_list'][0]['album']
                         ['album_name'], 'Kaleidoscope')

    def test_artist_related_get(self):
        self.assertEqual(self.musixmatch.artist_related_get(56, 1, 1)
                         ['message']['body']['artist_list'][0]
                         ['artist']['artist_id'], 298)
        self.assertEqual(self.musixmatch.artist_related_get(56, 1, 1)
                         ['message']['body']['artist_list'][0]
                         ['artist']['artist_name'], 'Outkast')

    def test_album_get(self):
        self.assertEqual(self.musixmatch.album_get(14250417)
                         ['message']['body']['album']
                         ['album_id'], 14250417)
        self.assertEqual(self.musixmatch.album_get(14250417)
                         ['message']['body']['album']
                         ['album_name'], 'Party Rock')

    def test_album_tracks_get(self):
        self.assertEqual(self.musixmatch.album_tracks_get(13750844, 1, 1, '')
                         ['message']['body']['track_list'][0]['track']
                         ['track_id'], 30057052)
        self.assertEqual(self.musixmatch.album_tracks_get(13750844, 1, 1, '')
                         ['message']['body']['track_list'][0]['track']
                         ['track_name'], "Don't Panic")

    def test_tracking_url_get(self):
        self.assertEqual(self.musixmatch
                             .tracking_url_get('www.mylyricswebsite.com')
                             ['message']['header']['status_code'], 200)

    def test_catalogue_dump_get(self):
        self.assertEqual(self.musixmatch.catalogue_dump_get('test')
                         ['message']['body'], '')


if __name__ == '__main__':
    unittest.main()
