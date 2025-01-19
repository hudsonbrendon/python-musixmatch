import pytest

from pymusixmatch import Musixmatch


class TestMusixmatch:
    @classmethod
    def setup_class(cls) -> None:
        cls.musixmatch = Musixmatch("test")
        cls.url = "https://api.musixmatch.com/ws/1.1/"

    def test_get_url(self) -> None:
        assert (
            self.musixmatch._get_url(
                "chart.artists.get?page=1&page_size=1&country=us&format=json",
            )
            == f"{self.url}chart.artists.get?page=1&page_size=1&country=us&format=json&apikey=test"
        )

    @pytest.mark.parametrize(
        "page_size, expected",
        [(1, 1), (10, 10), (100, 100)],
    )
    def test_set_page_size(self, page_size: int, expected: int) -> None:
        assert self.musixmatch._set_page_size(page_size) == expected

    @pytest.mark.parametrize("page_size", [0, -1, 101, 200])
    def test_set_page_size_with_invalid_page_size(
        self,
        page_size: int,
    ) -> None:
        with pytest.raises(ValueError) as excinfo:
            self.musixmatch._set_page_size(page_size)

        assert (
            str(excinfo.value)
            == f"Invalid page size: {page_size}, please use a page size between 1 and 100."
        )

    def test_chart_artists(self, requests_mock, chart_artists: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/chart.artists.get?page=1&page_size=1&country=us&format=json"
        requests_mock.get(url=url, json=chart_artists)
        assert chart_artists == self.musixmatch.chart_artists(1, 1)

    def test_chart_artists_with_invalid_country(
        self, requests_mock, chart_artists: dict
    ) -> None:
        url = "https://api.musixmatch.com/ws/1.1/chart.artists.get?page=1&page_size=1&country=invalid&format=json&apikey=test"
        requests_mock.get(url=url, json=chart_artists)
        with pytest.raises(ValueError):
            self.musixmatch.chart_artists(1, 1, country="invalid")

    def test_chart_artists_with_invalid_format(
        self, requests_mock, chart_artists: dict
    ) -> None:
        url = "https://api.musixmatch.com/ws/1.1/chart.artists.get?page=1&page_size=1&country=us&format=invalid&apikey=test"
        requests_mock.get(url=url, json=chart_artists)
        with pytest.raises(ValueError):
            self.musixmatch.chart_artists(1, 1, _format="invalid")

    def test_chart_tracks_get(self, requests_mock, tracks: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get?page=1&page_size=1&country=us&format=json&f_has_lyrics=1"
        requests_mock.get(url=url, json=tracks)
        assert tracks == self.musixmatch.chart_tracks_get(1, 1, 1)

    def test_chart_tracks_get_with_invalid_country(
        self, requests_mock, tracks: dict
    ) -> None:
        url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get?page=1&page_size=1&country=invalid&format=json&f_has_lyrics=1&apikey=test"
        requests_mock.get(url=url, json=tracks)
        with pytest.raises(ValueError):
            self.musixmatch.chart_tracks_get(1, 1, 1, country="invalid")

    def test_chart_tracks_get_with_invalid_format(
        self, requests_mock, tracks: dict
    ) -> None:
        url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get?page=1&page_size=1&country=us&format=invalid&f_has_lyrics=1&apikey=test"
        requests_mock.get(url=url, json=tracks)
        with pytest.raises(ValueError):
            self.musixmatch.chart_tracks_get(1, 1, 1, _format="invalid")

    def test_track_search(self, requests_mock, track_search: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.search?q_track=Let%20Me%20Love%20You&q_artist=justinbieber&q_lyrics=&q_track_artist=&q_writer=&q=&f_artist_id=&f_music_genre_id=&f_lyrics_language=&f_has_lyrics=&f_track_release_group_first_release_date_min=&f_track_release_group_first_release_date_max=&s_artist_rating=desc&s_track_rating=desc&quorum_factor=&page=1&page_size=10&apikey=test"
        requests_mock.get(url=url, json=track_search)

        assert (
            self.musixmatch.track_search(
                q_track="Let Me Love You",
                q_artist="justinbieber",
                page_size=10,
                page=1,
                s_track_rating="desc",
            )
            == track_search
        )

    def test_track_search_with_invalid_page_size(
        self, requests_mock, track_search: dict
    ) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.search?q_track=Let%20Me%20Love%20You&q_artist=justinbieber&q_lyrics=&q_track_artist=&q_writer=&q=&f_artist_id=&f_music_genre_id=&f_lyrics_language=&f_has_lyrics=&f_track_release_group_first_release_date_min=&f_track_release_group_first_release_date_max=&s_artist_rating=desc&s_track_rating=desc&quorum_factor=&page=1&page_size=101&apikey=test"
        requests_mock.get(url=url, json=track_search)

        with pytest.raises(ValueError):
            self.musixmatch.track_search(
                q_track="Let Me Love You",
                q_artist="justinbieber",
                page_size=101,
                page=1,
                s_track_rating="desc",
            )

    def test_track_search_with_invalid_s_artist_rating(
        self, requests_mock, track_search: dict
    ) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.search?q_track=Let%20Me%20Love%20You&q_artist=justinbieber&q_lyrics=&q_track_artist=&q_writer=&q=&f_artist_id=&f_music_genre_id=&f_lyrics_language=&f_has_lyrics=&f_track_release_group_first_release_date_min=&f_track_release_group_first_release_date_max=&s_artist_rating=invalid&s_track_rating=desc&quorum_factor=&page=1&page_size=10&apikey=test"
        requests_mock.get(url=url, json=track_search)

        with pytest.raises(ValueError):
            self.musixmatch.track_search(
                q_track="Let Me Love You",
                q_artist="justinbieber",
                page_size=10,
                page=1,
                s_artist_rating="invalid",
            )

    def test_track_search_with_invalid_s_track_rating(
        self, requests_mock, track_search: dict
    ) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.search?q_track=Let%20Me%20Love%20You&q_artist=justinbieber&q_lyrics=&q_track_artist=&q_writer=&q=&f_artist_id=&f_music_genre_id=&f_lyrics_language=&f_has_lyrics=&f_track_release_group_first_release_date_min=&f_track_release_group_first_release_date_max=&s_artist_rating=desc&s_track_rating=invalid&quorum_factor=&page=1&page_size=10&apikey=test"
        requests_mock.get(url=url, json=track_search)

        with pytest.raises(ValueError):
            self.musixmatch.track_search(
                q_track="Let Me Love You",
                q_artist="justinbieber",
                page_size=10,
                page=1,
                s_track_rating="invalid",
            )

    def test_track_get(self, requests_mock, track_get: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.get?commontrack_id=12345&track_isrc=&apikey=test"
        requests_mock.get(url=url, json=track_get)
        request = self.musixmatch.track_get(12345)
        assert track_get == request

    def test_track_lyrics_get(self, requests_mock, tracks: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id=12345&commontrack_id=12345"
        requests_mock.get(url=url, json=tracks)
        request = self.musixmatch.track_lyrics_get(12345, 12345)
        assert tracks == request

    def test_track_snippet_get(self, requests_mock, track_snippet: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.snippet.get?track_id=12345"
        requests_mock.get(url=url, json=track_snippet)
        request = self.musixmatch.track_snippet_get(12345)
        assert track_snippet == request

    def test_track_subtitle_get(self, requests_mock, track_subtitle_get: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.subtitle.get?track_id=14201829"
        requests_mock.get(url=url, json=track_subtitle_get)
        request = self.musixmatch.track_subtitle_get(14201829)
        assert track_subtitle_get == request

    def test_track_richsync_get(self, requests_mock, track_richsync_get: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/track.richsync.get?track_id=114837357"
        requests_mock.get(url=url, json=track_richsync_get)
        request = self.musixmatch.track_richsync_get(114837357)
        assert track_richsync_get == request

    def test_matcher_lyrics_get(self, requests_mock, matcher_lyrics_get) -> None:
        url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track=Let%20Me%20Love%20You&q_artist=justinbieber"
        requests_mock.get(url=url, json=matcher_lyrics_get)
        request = self.musixmatch.matcher_lyrics_get("Let Me Love You", "justinbieber")
        assert matcher_lyrics_get == request

    def test_matcher_track_get(self, requests_mock, matcher_track_get: dict) -> None:
        url = "https://api.musixmatch.com/ws/1.1/matcher.track.get?q_artist=justinbieber&q_track=Let%20Me%20Love%20You&"
        requests_mock.get(url=url, json=matcher_track_get)
        request = self.musixmatch.matcher_track_get("Let Me Love You", "justinbieber")
        assert matcher_track_get == request

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
                "prodigy",
                1,
                1,
                16439,
                "4a4ee089-93b1-4470-af9a-6ff575d32704",
            )["message"]["body"]["artist_list"][0]["artist"]["artist_id"],
            16439,
        )
        self.assertEqual(
            self.musixmatch.artist_search(
                "prodigy",
                1,
                1,
                16439,
                "4a4ee089-93b1-4470-af9a-6ff575d32704",
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
            self.musixmatch.catalogue_dump_get("test")["message"]["body"],
            "",
        )
