import pytest


@pytest.fixture
def chart_artists() -> dict:
    return {
        "message": {
            "header": {"status_code": 200, "execute_time": 0.093447923660278},
            "body": {
                "artist_list": [
                    {
                        "artist": {
                            "artist_id": 13916103,
                            "artist_mbid": "",
                            "artist_name": "Maroon 5 feat. Wiz Khalifa",
                            "artist_alias_list": [],
                            "artist_rating": 81,
                            "updated_time": "2012-04-17T10:22:35Z",
                        }
                    },
                    {
                        "artist": {
                            "artist_id": 13639930,
                            "artist_mbid": "ec6eaf55-d743-46ce-89b6-014943a2773c",
                            "artist_name": "Emma",
                            "artist_alias_list": [],
                            "artist_rating": 66,
                            "updated_time": "2011-06-03T09:43:10Z",
                        }
                    },
                    {
                        "artist": {
                            "artist_id": 13834953,
                            "artist_mbid": "",
                            "artist_name": "Gotye feat. Kimbra",
                            "artist_alias_list": [],
                            "artist_rating": 84,
                            "updated_time": "2012-04-07T18:22:16Z",
                        }
                    },
                ]
            },
        }
    }


@pytest.fixture
def tracks() -> dict:
    return {
        "message": {
            "header": {"status_code": 200, "execute_time": 0.00136, "available": 646},
            "body": {
                "track_list": [
                    {"track": "track'"},
                    {"track": "track'"},
                    {"track": "track'"},
                ]
            },
        }
    }


@pytest.fixture
def track_snippet() -> dict:
    return {
        "message": {
            "header": {"status_code": 200, "execute_time": 0.04367995262146},
            "body": {
                "lyrics": {
                    "lyrics_id": 7260188,
                    "restricted": 0,
                    "instrumental": 0,
                    "lyrics_body": "Now and then I think of when we were together\r\n...",
                    "lyrics_language": "en",
                    "script_tracking_url": "http:\/\/tracking.musixmatch.com\/t1.0\/m42By\/J7rv9z",
                    "pixel_tracking_url": "http:\/\/tracking.musixmatch.com\/t1.0\/m42By\/J7rv9z6q9he7AA",
                    "lyrics_copyright": "Lyrics powered by www.musiXmatch.com",
                    "backlink_url:"
                    "https://www.musixmatch.com/lyrics/Gotye-feat-Kimbra/Somebody-That-I-Used-to-Know"
                    "updated_time": "2012-04-26T02:09:39Z",
                }
            },
        }
    }


@pytest.fixture
def track_search() -> dict:
    return {
        "message": {
            "header": {"status_code": 200, "execute_time": 0.00136, "available": 646},
            "body": {
                "track_list": [
                    {"track": "track'"},
                    {"track": "track'"},
                    {"track": "track'"},
                ]
            },
        }
    }


@pytest.fixture
def track_get() -> dict:
    return {
        "message": {
            "header": {"status_code": 200, "execute_time": 0.00136},
            "body": {"track": "track"},
        }
    }
