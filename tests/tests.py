import pytest
from decouple import config
from musixmatch import Musixmatch

from . import results


class TestMusixmatch:
    @classmethod
    def setup_class(cls):
        cls.musixmatch = Musixmatch("test")
        cls.url = "http://api.musixmatch.com/ws/1.1/"

    def test_get_url(self):
        assert (
            self.musixmatch._get_url(
                "chart.artists.get?" "page=1&page_size=1&country=us" "&format=json"
            )
            == f"{self.url}chart.artists.get?page=1&page_size=1&country=us&format=json&apikey=test"
        )

    def test_apikey(self):
        assert self.musixmatch._apikey == "test"

    def test_chart_artists(self, requests_mock):
        json = results.CHART_ARTISTS
        url = "http://api.musixmatch.com/ws/1.1/chart.artists.get?page=1&page_size=1&country=us&format=json"
        requests_mock.get(url=url, json=json)
        request = self.musixmatch.chart_artists(1, 1)
        assert json == request

    def test_chart_tracks_get(self, requests_mock):
        json = results.TRACKS
        url = "http://api.musixmatch.com/ws/1.1/chart.tracks.get?page=1&page_size=1&country=us&format=json&f_has_lyrics=1"
        requests_mock.get(url=url, json=json)
        request = self.musixmatch.chart_tracks_get(1, 1, 1)
        assert json == request

    @pytest.mark.skip("Refactor test")
    def test_track_search(self):
        self.assertEqual(
            self.musixmatch.track_search(
                q_track="Let Me Love You",
                q_artist="justinbieber",
                page_size=10,
                page=1,
                s_track_rating="desc",
            )["message"]["body"]["track_list"],
            [],
        )

    @pytest.mark.skip("Refactor test")
    def test_track_get(self):
        self.assertEqual(
            self.musixmatch.track_get(15445219)["message"]["body"]["track"][
                "artist_name"
            ],
            "Lady Gaga",
        )
        self.assertEqual(
            self.musixmatch.track_get(15445219)["message"]["body"]["track"][
                "album_name"
            ],
            "The Fame Monster",
        )

    def test_track_lyrics_get(self, requests_mock):
        json = results.TRACKS
        url = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id=12345"
        requests_mock.get(url=url, json=json)
        request = self.musixmatch.track_lyrics_get(12345)
        assert json == request

    def test_track_snippet_get(self, requests_mock):
        json = results.TRACK_SNIPPET
        url = "http://api.musixmatch.com/ws/1.1/track.snippet.get?track_id=12345"
        requests_mock.get(url=url, json=json)
        request = self.musixmatch.track_snippet_get(12345)
        assert json == request

    @pytest.mark.skip("Refactor test")
    def test_track_subtitle_get(self):
        self.assertEqual(
            self.musixmatch.track_subtitle_get(14201829)["message"]["body"], ""
        )

    @pytest.mark.skip("Refactor test")
    def test_track_richsync_get(self):
        self.assertEqual(
            self.musixmatch.track_richsync_get(114837357)["message"]["body"][
                "richsync"
            ]["richsync_id"],
            6,
        )
        self.assertEqual(
            self.musixmatch.track_richsync_get(114837357)["message"]["body"][
                "richsync"
            ]["richsync_length"],
            230,
        )

    @pytest.mark.skip("Refactor test")
    def test_track_lyrics_post(self):
        self.assertEqual(
            self.musixmatch.track_lyrics_post(1471157, "test")["message"]["header"][
                "status_code"
            ],
            200,
        )
        self.assertEqual(
            self.musixmatch.track_lyrics_post(1471157, "test")["message"]["body"], ""
        )

    @pytest.mark.skip("Refactor test")
    def test_track_lyrics_feedback_post(self):
        self.assertEqual(
            self.musixmatch.track_lyrics_post(1471157, 4193713, "wrong_verses")[
                "message"
            ]["body"],
            "",
        )

    @pytest.mark.skip("Refactor test")
    def test_matcher_lyrics_get(self):
        self.assertEqual(
            self.musixmatch.matcher_lyrics_get("Sexy and I know it", "LMFAO")[
                "message"
            ]["body"]["lyrics"]["lyrics_language_description"],
            "English",
        )
        self.assertEqual(
            self.musixmatch.matcher_lyrics_get("Sexy and I know it", "LMFAO")[
                "message"
            ]["body"]["lyrics"]["lyrics_language"],
            "en",
        )

    @pytest.mark.skip("Refactor test")
    def test_matcher_track_get(self):
        self.assertEqual(
            self.musixmatch.matcher_track_get("Lose Yourself (soundtrack)", "Eminem")[
                "message"
            ]["body"]["track"]["track_name"],
            "Lose Yourself - " "Soundtrack Version" " (Explicit)",
        )
        self.assertEqual(
            self.musixmatch.matcher_track_get("Lose Yourself (soundtrack)", "Eminem")[
                "message"
            ]["body"]["track"]["album_name"],
            "Curtain Call",
        )

    @pytest.mark.skip("Refactor test")
    def test_matcher_subtitle_get(self):
        self.assertEqual(
            self.musixmatch.matcher_subtitle_get("Sexy and I know it", "LMFAO", 200, 3)[
                "message"
            ]["body"],
            "",
        )

    @pytest.mark.skip("Refactor test")
    def test_artist_get(self):
        self.assertEqual(
            self.musixmatch.artist_get(118)["message"]["body"]["artist"]["artist_name"],
            "Queen",
        )
        self.assertEqual(
            self.musixmatch.artist_get(118)["message"]["body"]["artist"]["artist_mbid"],
            "5eecaf18-02ec-47af-a4f2-7831db373419",
        )

    @pytest.mark.skip("Refactor test")
    def test_artist_search(self):
        self.assertEqual(
            self.musixmatch.artist_search(
                "prodigy", 1, 1, 16439, "4a4ee089-93b1-4470-af9a-6ff575d32704"
            )["message"]["body"]["artist_list"][0]["artist"]["artist_id"],
            16439,
        )
        self.assertEqual(
            self.musixmatch.artist_search(
                "prodigy", 1, 1, 16439, "4a4ee089-93b1-4470-af9a-6ff575d32704"
            )["message"]["body"]["artist_list"][0]["artist"]["artist_name"],
            "The Prodigy",
        )

    @pytest.mark.skip("Refactor test")
    def test_artist_albums_get(self):
        self.assertEqual(
            self.musixmatch.artist_albums_get(1039, 1, 1, 1, "desc")["message"]["body"][
                "album_list"
            ][0]["album"]["album_id"],
            25660826,
        )
        self.assertEqual(
            self.musixmatch.artist_albums_get(1039, 1, 1, 1, "desc")["message"]["body"][
                "album_list"
            ][0]["album"]["album_name"],
            "Kaleidoscope",
        )

    @pytest.mark.skip("Refactor test")
    def test_artist_related_get(self):
        self.assertEqual(
            self.musixmatch.artist_related_get(56, 1, 1)["message"]["body"][
                "artist_list"
            ][0]["artist"]["artist_id"],
            298,
        )
        self.assertEqual(
            self.musixmatch.artist_related_get(56, 1, 1)["message"]["body"][
                "artist_list"
            ][0]["artist"]["artist_name"],
            "Outkast",
        )

    @pytest.mark.skip("Refactor test")
    def test_album_get(self):
        self.assertEqual(
            self.musixmatch.album_get(14250417)["message"]["body"]["album"]["album_id"],
            14250417,
        )
        self.assertEqual(
            self.musixmatch.album_get(14250417)["message"]["body"]["album"][
                "album_name"
            ],
            "Party Rock",
        )

    @pytest.mark.skip("Refactor test")
    def test_album_tracks_get(self):
        self.assertEqual(
            self.musixmatch.album_tracks_get(13750844, 1, 1, "")["message"]["body"][
                "track_list"
            ][0]["track"]["track_id"],
            30057052,
        )
        self.assertEqual(
            self.musixmatch.album_tracks_get(13750844, 1, 1, "")["message"]["body"][
                "track_list"
            ][0]["track"]["track_name"],
            "Don't Panic",
        )

    @pytest.mark.skip("Refactor test")
    def test_tracking_url_get(self):
        self.assertEqual(
            self.musixmatch.tracking_url_get("www.mylyricswebsite.com")["message"][
                "header"
            ]["status_code"],
            200,
        )

    @pytest.mark.skip("Refactor test")
    def test_catalogue_dump_get(self):
        self.assertEqual(
            self.musixmatch.catalogue_dump_get("test")["message"]["body"], ""
        )
