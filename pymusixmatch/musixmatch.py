from typing import Optional
import requests

from pymusixmatch.enums import Country, Format, Ordering, Route


class Musixmatch(object):
    BASE_URL = "https://api.musixmatch.com/ws"
    VERSION = "1.1"

    def __init__(self, api_key: str) -> None:
        """Define objects of type Musixmatch.

        Args:
            api_key ([str]): For get your apikey access: https://developer.musixmatch.com
        """
        self.__api_key = api_key
        self.__url = f"{self.BASE_URL}/{self.VERSION}/"

    def _get_url(self, path: str) -> str:
        """Get the url for the request.

        Args:
            path (str): The url for the request.

        Returns:
            str: The url for the request.
        """
        return f"{self.__url}{path}&apikey={self._apikey}"

    @property
    def _apikey(self) -> str:
        """Get the api_key.

        Returns:
            str: The api_key.
        """
        return self.__api_key

    def _request(self, url: str, format: Format = Format.JSON) -> dict:
        """Get the request.

        Args:
            url (str): The url for the request.

        Returns:
            dict: The request.
        """
        request = requests.get(url)
        if format == Format.XML:
            return request.text
        return request.json()

    def _set_page_size(self, page_size: int) -> int:
        """Set the page size.

        Args:
            page_size (int): The page size.

        Returns:
            int: The page size.
        """
        if page_size < 1 or page_size > 100:
            raise ValueError(
                f"Invalid page size: {page_size}, please use a page size between 1 and 100."
            )
        return page_size

    def chart_artists(
        self,
        page: int,
        page_size: int,
        country: Optional[Country] = Country.US.value,
        _format: Optional[Format] = Format.JSON.value,
    ) -> dict:
        """This api provides you the list
        of the top artists of a given country.

        Parameters:

        page (int): Define the page number for paginated results.
        page_size (int): Define the page size for paginated results (range 1 - 100).
        country (Country): A valid country code (default US).
        format (Format): Decide the output type json or xml (default json).
        """
        if country not in Country._value2member_map_:
            raise ValueError(
                f"Invalid country code: {country}, please use a valid country code."
            )

        if _format not in Format._value2member_map_:
            raise ValueError(f"Invalid format: {_format}, please use a valid format.")

        request = self._request(
            self._get_url(
                f"{Route.CHART_ARTISTS_GET.value}?page={page}&page_size={self._set_page_size(page_size)}&country={country}&format={_format}",
            ),
        )
        return request

    def chart_tracks_get(
        self,
        page: int,
        page_size: int,
        f_has_lyrics: bool,
        country: Optional[Country] = Country.US.value,
        _format: Optional[Format] = Format.JSON.value,
    ) -> dict:
        """This api provides you the list
        of the top songs of a given country.

        Parameters:

        page (int): Define the page number for paginated results.
        page_size (int): Define the page size for paginated results (range 1 - 100).
        f_has_lyrics (bool): When set, filter only contents with lyrics.
        country (Country): A valid country code (default US).
        format (Format): Decide the output type json or xml (default json).
        """
        if country not in Country._value2member_map_:
            raise ValueError(
                f"Invalid country code: {country}, please use a valid country code."
            )

        if _format not in Format._value2member_map_:
            raise ValueError(f"Invalid format: {_format}, please use a valid format.")

        request = self._request(
            self._get_url(
                f"chart.tracks.get?page={page}&page_size={self._set_page_size(page_size)}&country={country}&format={_format}&f_has_lyrics={f_has_lyrics}",
            ),
        )
        return request

    def track_search(
        self,
        page: int,
        page_size: int,
        q_track: Optional[str] = "",
        q_artist: Optional[str] = "",
        q_lyrics: Optional[str] = "",
        q_track_artist: Optional[str] = "",
        q_writer: Optional[str] = "",
        q: Optional[str] = "",
        f_artist_id: Optional[int] = "",
        f_music_genre_id: Optional[int] = "",
        f_lyrics_language: Optional[str] = "",
        f_has_lyrics: Optional[bool] = "",
        f_track_release_group_first_release_date_min: Optional[str] = "",
        f_track_release_group_first_release_date_max: Optional[str] = "",
        s_artist_rating: Optional[Ordering] = Ordering.DESC.value,
        s_track_rating: Optional[Ordering] = Ordering.DESC.value,
        quorum_factor: Optional[float] = "",
    ) -> dict:
        """Search for track in our database.

        Parameters:

        q_track (str): The song title
        q_artist (str): The song artist
        q_lyrics (str): Any word in the lyrics
        q_track_artist (str): Any word in the song title or artist name
        q_writer (str): Search among writers
        q (str): Any word in the song title or artist name or lyrics
        f_artist_id (int): When set, filter by this artist id
        f_music_genre_id (int): When set, filter by this music category id
        f_lyrics_language (str): Filter by the lyrics language (en,it,..)
        f_has_lyrics (bool): When set, filter only contents with lyrics
        f_track_release_group_first_release_date_min (str): When set, filter the tracks with release date newer than value, format is YYYYMMDD
        f_track_release_group_first_release_date_max (str): When set, filter the tracks with release date older than value, format is YYYYMMDD
        s_artist_rating (Ordering): Sort by our popularity index for artists (asc|desc)
        s_track_rating (Ordering): Sort by our popularity index for tracks (asc|desc)
        quorum_factor (float): Search only a part of the given query string.Allowed range is (0.1 – 0.9)
        page (int): Define the page number for paginated results
        page_size (int): Define the page size for paginated results. Range is 1 to 100.

        Note: This method requires a commercial plan.
        """

        if s_artist_rating not in Ordering._value2member_map_:
            raise ValueError(
                f"Invalid artist rating: {s_artist_rating}, please use a valid artist rating."
            )

        if s_track_rating not in Ordering._value2member_map_:
            raise ValueError(
                f"Invalid track rating: {s_track_rating}, please use a valid track rating."
            )

        data = self._request(
            self._get_url(
                "track.search?"
                f"q_track={q_track}&"
                f"q_artist={q_artist}&"
                f"q_lyrics={q_lyrics}&"
                f"q_track_artist={q_track_artist}&"
                f"q_writer={q_writer}&"
                f"q={q}&"
                f"f_artist_id={f_artist_id}&"
                f"f_music_genre_id={f_music_genre_id}&"
                f"f_lyrics_language={f_lyrics_language}&"
                f"f_has_lyrics={f_has_lyrics}&"
                f"f_track_release_group_first_release_date_min={f_track_release_group_first_release_date_min}&"
                f"f_track_release_group_first_release_date_max={f_track_release_group_first_release_date_max}&"
                f"s_artist_rating={s_artist_rating}&"
                f"s_track_rating={s_track_rating}&"
                f"quorum_factor={quorum_factor}&"
                f"page={page}&"
                f"page_size={self._set_page_size(page_size)}"
            ),
        )
        return data

    def track_get(
        self,
        commontrack_id: Optional[str] = "",
        track_isrc: Optional[str] = "",
    ) -> dict:
        """Get a track info from our database:
        title, artist, instrumental flag and cover art.

        Parameters:

        commontrack_id (str): The musiXmatch commontrack id.
        track_isrc (str): A valid ISRC identifier.
        """
        data = self._request(
            self._get_url(
                "track.get?commontrack_id={}&track_isrc={}".format(
                    commontrack_id,
                    track_isrc,
                ),
            ),
        )
        return data

    def track_lyrics_get(self, track_id: str = "", commontrack_id: str = "") -> dict:
        """Get the lyrics of a track.

        Parameters:

        track_id (str): The musiXmatch track id.
        track_mbid (str): The musicbrainz track id.
        """
        data = self._request(
            self._get_url(
                f"track.lyrics.get?track_id={track_id}&commontrack_id={commontrack_id}",
            ),
        )
        return data

    def track_snippet_get(self, track_id: str) -> dict:
        """Get the snippet for a given track.

        A lyrics snippet is a very short representation of a song lyrics.
        It’s usually twenty to a hundred characters long and it’s calculated
        extracting a sequence of words from the lyrics.

        Parameters:

        track_id (str): The musiXmatch track id.
        """
        data = self._request(
            self._get_url(f"track.snippet.get?track_id={track_id}"),
        )
        return data

    def track_subtitle_get(
        self,
        track_id: str,
        track_mbid: str = "",
        subtitle_format: str = "",
        f_subtitle_length: str = "",
        f_subtitle_length_max_deviation: str = "",
    ) -> dict:
        """Retreive the subtitle of a track.

        Return the subtitle of a track in LRC or DFXP format.
        Refer to Wikipedia LRC format page or DFXP format on W3c
        for format specifications.

        Parameters:

        track_id (str): The musiXmatch track id.
        track_mbid (str): The musicbrainz track id.
        subtitle_format (str): The format of the subtitle (lrc,dfxp,stledu).
        Default to lrc.
        f_subtitle_length (str): The desired length of the subtitle (seconds).
        f_subtitle_length_max_deviation (str): The maximum deviation allowed.
        from the f_subtitle_length (seconds).
        """
        data = self._request(
            self._get_url(
                "track.subtitle.get?"
                "track_id={}&track_mbid={}"
                "&subtitle_format={}"
                "&f_subtitle_length={}"
                "&f_subtitle_length_max_deviation={}".format(
                    track_id,
                    track_mbid,
                    subtitle_format,
                    f_subtitle_length,
                    f_subtitle_length_max_deviation,
                ),
            ),
        )
        return data

    def track_richsync_get(
        self,
        track_id: str,
        f_sync_length: str = "",
        f_sync_length_max_deviation: str = "",
    ) -> dict:
        """Get the Rich sync for a track.

        A rich sync is an enhanced version of the
        standard sync which allows:

        - position offset by single characther.
        - endless formatting options at single char level.
        - multiple concurrent voices.
        - multiple scrolling direction.

        Parameters:

        track_id (str): The musiXmatch track id.
        f_sync_length (str): The desired length of the sync (seconds).
        f_sync_length_max_deviation (str): The maximum deviation allowed.
        from the f_sync_length (seconds).
        """
        data = self._request(
            self._get_url(
                "track.richsync.get?"
                "track_id={}&f_sync_length={}"
                "&f_sync_length_max_deviation={}".format(
                    track_id,
                    f_sync_length,
                    f_sync_length_max_deviation,
                ),
            ),
        )
        return data

    def matcher_lyrics_get(
        self,
        q_track: str,
        q_artist: str,
        track_isrc: Optional[str] = "",
    ) -> dict:
        """Get the lyrics for track based on title and artist.

        Parameters:

        q_track (str): The song title
        q_artist (str): The song artist
        track_isrc (str): If you have an available isrc id in your catalogue
        you can query using this id only (optional)
        track_isrc - If you have an available musicbrainz recording id
        """
        data = self._request(
            self._get_url(
                "matcher.lyrics.get?q_track={}&q_artist={}&track_isrc={}".format(
                    q_track, q_artist, track_isrc
                ),
            ),
        )
        return data

    def matcher_track_get(
        self, q_track: str, q_artist: str, q_album: Optional[str] = ""
    ) -> dict:
        """Match your song against our database.

        In some cases you already have some informations
        about the track title, artist name, album etc.

        A possible strategy to get the corresponding lyrics could be:
        - search our catalogue with a perfect match,
        - maybe try using the fuzzy search,
        - maybe try again using artist aliases, and so on.

        The matcher.track.get method does all the job for you in
        a single call. This way you dont’t need to worry about the
        details, and you’ll get instant benefits for your application
        without changing a row in your code, while we take care of
        improving the implementation behind. Cool, uh?

        Parameters:

        q_track (str): The song title.
        q_artist (str): The song artist.
        q_album (str): The song album.
        """
        data = self._request(
            self._get_url(
                "matcher.track.get?q_track={}&q_artist={}&q_album={}".format(
                    q_track, q_artist, q_album
                ),
            ),
        )
        return data

    def matcher_subtitle_get(
        self,
        q_track: str,
        q_artist: str,
        f_subtitle_length: int,
        f_subtitle_length_max_deviation: int,
        track_isrc: Optional[str] = "",
    ):
        """Get the subtitles for a song given his title,artist and duration.

        You can use the f_subtitle_length_max_deviation to fetch subtitles
        within a given duration range.

        Parameters:

        q_track (str): The song title.
        q_artist (str): The song artist.
        f_subtitle_length (int): Filter by subtitle length in seconds.
        f_subtitle_length_max_deviation (int): Max deviation for a subtitle
        length in seconds.
        track_isrc (str): If you have an available isrc id in your catalogue
        you can query using this id only (optional).

        Note: This method requires a commercial plan.
        """
        data = self._request(
            self._get_url(
                "matcher.subtitle.get?q_track={}"
                "&q_artist={}&f_subtitle_length={}"
                "&f_subtitle_length_max_deviation={}"
                "&track_isrc={}".format(
                    q_track,
                    q_artist,
                    f_subtitle_length,
                    f_subtitle_length_max_deviation,
                    track_isrc,
                ),
            ),
            format=Format.XML,
        )
        return data

    def artist_get(self, artist_id, artist_mbid=None, _format="json"):
        """Get the artist data from our database.

        Parameters:

        artist_id - Musixmatch artist id.
        artist_mbid - Musicbrainz artist id.
        format - Decide the output type json or xml (default json).
        """
        data = self._request(
            self._get_url(
                "artist.get?artist_id={}&artist_mbid={}&format={}".format(
                    artist_id, artist_mbid, _format
                ),
            ),
        )
        return data

    def artist_search(
        self,
        q_artist,
        page,
        page_size,
        f_artist_id,
        f_artist_mbid,
        _format="json",
    ):
        """Search for artists in our database.

        Parameters:

        q_artist - The song artist.
        f_artist_id - When set, filter by this artist id.
        f_artist_mbid - When set, filter by this artist musicbrainz id.
        page - Define the page number for paginated results.
        page_size - Define the page size for paginated results
        (Range is 1 to 100).
        format - Decide the output type json or xml (default json).
        """
        data = self._request(
            self._get_url(
                "artist.search?q_artist={}"
                "&f_artist_id={}&f_artist_mbid={}"
                "&page={}&page_size={}&format={}".format(
                    q_artist,
                    f_artist_id,
                    f_artist_mbid,
                    page,
                    self._set_page_size(page_size),
                    _format,
                ),
            ),
        )
        return data

    def artist_albums_get(
        self,
        artist_id,
        g_album_name,
        page,
        page_size,
        s_release_date,
        artist_mbid=None,
        _format="json",
    ):
        """Get the album discography of an artist.

        Parameters:

        artist_id - Musixmatch artist id.
        artist_mbid - Musicbrainz artist id.
        g_album_name - Group by Album Name.
        s_release_date - Sort by release date (asc|desc).
        page - Define the page number for paginated results.
        page_size - Define the page size for paginated results
        (range is 1 to 100).
        format - Decide the output type json or xml (default json).
        """
        data = self._request(
            self._get_url(
                "artist.albums.get?artist_id={}"
                "&artist_mbid={}&g_album_name={}"
                "&s_release_date={}&page={}"
                "&page_size={}&format={}".format(
                    artist_id,
                    artist_mbid,
                    g_album_name,
                    s_release_date,
                    page,
                    self._set_page_size(page_size),
                    _format,
                ),
            ),
        )
        return data

    def artist_related_get(
        self,
        artist_id,
        page,
        page_size,
        artist_mbid=None,
        _format="json",
    ):
        """Get a list of artists somehow related to a given one.

        Parameters:

        artist_id - The musiXmatch artist id.
        artist_mbid - The musicbrainz artist id.
        page - Define the page number for paginated results.
        page_size - Define the page size for paginated results.
        (range is 1 to 100).
        format - Decide the output type json or xml (default json).
        """
        data = self._request(
            self._get_url(
                "artist.related.get?artist_id={}"
                "&artist_mbid={}&page={}"
                "&page_size={}&format={}".format(
                    artist_id,
                    artist_mbid,
                    page,
                    self._set_page_size(page_size),
                    _format,
                ),
            ),
        )
        return data

    def album_get(self, album_id, _format="json"):
        """Get an album from our database:
        name, release_date, release_type, cover art.

        Parameters:

        album_id - The musiXmatch album id.
        format - Decide the output type json or xml (default json)
        """
        data = self._request(
            self._get_url("album.get?album_id={}&format={}".format(album_id, _format)),
        )
        return data

    def album_tracks_get(
        self,
        album_id,
        page,
        page_size,
        album_mbid,
        f_has_lyrics=None,
        _format="json",
    ):
        """This api provides you the list of the songs of an album.

        Parameters:

        album_id - Musixmatch album id.
        album_mbid - Musicbrainz album id.
        f_has_lyrics - When set, filter only contents with lyrics.
        page - Define the page number for paginated results.
        page_size - Define the page size for paginated results.
        (range is 1 to 100).
        format - Decide the output type json or xml (default json).
        """
        data = self._request(
            self._get_url(
                "album.tracks.get?album_id={}"
                "&album_mbid={}&f_has_lyrics={}"
                "&page={}&page_size={}&format={}".format(
                    album_id,
                    album_mbid,
                    f_has_lyrics,
                    page,
                    self._set_page_size(page_size),
                    _format,
                ),
            ),
        )
        return data

    def tracking_url_get(self, domain, _format="json"):
        """Get the base url for the tracking script

        With this api you’ll be able to get the base
        url for the tracking script you need to insert in
        your page to legalize your existent lyrics library.
        Read more here: rights-clearance-on-your-existing-catalog

        In case you’re fetching the lyrics by the musiXmatch api
        called track.lyrics.get you don’t need to implement this API call.

        Parameters:

        domain - Your domain name.
        format - Decide the output type json or xml (default json).
        """
        data = self._request(
            self._get_url(
                "tracking.url.get?domain={}&format={}".format(domain, _format),
            ),
        )
        return data

    def catalogue_dump_get(self, url):
        """Get the list of our songs with the lyrics last updated information.

        CATALOGUE_COMMONTRACKS

        Dump of our catalogue in this format:

        {
            "track_name": "Shape of you",
            "artist_name": "Ed Sheeran",
            "commontrack_id":12075763,
            "instrumental": false,
            "has_lyrics": yes,
            "updated_time": "2013-04-08T09:28:40Z"
        }

        Note: This method requires a commercial plan.
        """
        data = self._request(self._get_url(url))
        return data

    def genres_get(self, _format="json"):
        """Get the list of the music genres of our catalogue:
        music_genre_id, music_genre_parent_id, music_genre_name, music_genre_name_extended, music_genre_vanity

        Parameters:

        format - Decide the output type json or xml (default json)
        """
        data = self._request(
            self._get_url("music.genres.get?format={}".format(_format)),
        )
        return data
