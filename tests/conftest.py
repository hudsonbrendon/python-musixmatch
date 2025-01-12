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


@pytest.fixture
def track_richsync_get() -> dict:
    return {
        "message": {
            "header": {
                "status_code": 200,
                "available": 1,
                "execute_time": 0.023973941802979,
            },
            "body": {
                "richsync": {
                    "richsync_id": 6,
                    "restricted": 0,
                    "richsync_body": '[{"ts":16.426,"te":18.261,"l":[{"c":"I","o":0},{"c":"\'","o":0.013},{"c":"m","o":0.025},{"c":" ","o":0.088},{"c":"t","o":0.114},{"c":"r","o":0.137},{"c":"y","o":0.163},{"c":"n","o":0.213},{"c":"a","o":0.276},{"c":" ","o":0.299},{"c":"p","o":0.311},{"c":"u","o":0.348},{"c":"t","o":0.386},{"c":" ","o":0.399},{"c":"y","o":0.399},{"c":"o","o":0.424},{"c":"u","o":0.45},{"c":" ","o":0.489},{"c":"i","o":0.501},{"c":"n","o":0.512},{"c":" ","o":0.549},{"c":"t","o":0.562},{"c":"h","o":0.587},{"c":"e","o":0.626},{"c":" ","o":0.688},{"c":"w","o":0.7},{"c":"o","o":0.813},{"c":"r","o":0.888},{"c":"s","o":0.911},{"c":"t","o":0.963},{"c":" ","o":1.026},{"c":"m","o":1.076},{"c":"o","o":1.212},{"c":"o","o":1.288},{"c":"d","o":1.386},{"c":",","o":1.489},{"c":" ","o":1.512},{"c":"a","o":1.563},{"c":"h","o":1.65}],"x":"I\'m tryna put you in the worst mood, ah"},{"ts":18.934,"te":21.218,"l":[{"c":"P","o":0},{"c":"1","o":0.013},{"c":" ","o":0.298},{"c":"c","o":0.4},{"c":"l","o":0.536},{"c":"e","o":0.575},{"c":"a","o":0.612},{"c":"n","o":0.65},{"c":"e","o":0.687},{"c":"r","o":0.786},{"c":" ","o":0.85},{"c":"t","o":0.875},{"c":"h","o":0.911},{"c":"a","o":0.991},{"c":"n","o":1.049},{"c":" ","o":1.112},{"c":"y","o":1.137},{"c":"o","o":1.188},{"c":"u","o":1.249},{"c":"r","o":1.287},{"c":" ","o":1.325},{"c":"c","o":1.338},{"c":"h","o":1.4},{"c":"u","o":1.474},{"c":"r","o":1.536},{"c":"c","o":1.575},{"c":"h","o":1.637},{"c":" ","o":1.702},{"c":"s","o":1.725},{"c":"h","o":1.8},{"c":"o","o":1.875},{"c":"e","o":1.914},{"c":"s","o":1.95},{"c":",","o":2},{"c":" ","o":2.025},{"c":"a","o":2.038},{"c":"h","o":2.062}],"x":"P1 cleaner than your church shoes, ah"},{"ts":21.441,"te":23.35,"l":[{"c":"M","o":0},{"c":"i","o":0.011},{"c":"l","o":0.05},{"c":"l","o":0.11},{"c":"i","o":0.198},{"c":" ","o":0.222},{"c":"p","o":0.248},{"c":"o","o":0.286},{"c":"i","o":0.324},{"c":"n","o":0.349},{"c":"t","o":0.374},{"c":" ","o":0.399},{"c":"t","o":0.412},{"c":"w","o":0.436},{"c":"o","o":0.474},{"c":" ","o":0.513},{"c":"j","o":0.525},{"c":"u","o":0.549},{"c":"s","o":0.601},{"c":"t","o":0.662},{"c":" ","o":0.762},{"c":"t","o":0.811},{"c":"o","o":0.864},{"c":" ","o":0.937},{"c":"h","o":0.961},{"c":"u","o":1.036},{"c":"r","o":1.1},{"c":"t","o":1.15},{"c":" ","o":1.187},{"c":"y","o":1.212},{"c":"o","o":1.275},{"c":"u","o":1.376},{"c":",","o":1.501},{"c":" ","o":1.565},{"c":"a","o":1.587},{"c":"h","o":1.675}],"x":"Milli point two just to hurt you, ah"},{"ts":23.949,"te":26.224,"l":[{"c":"A","o":0},{"c":"l","o":0.013},{"c":"l","o":0.075},{"c":" ","o":0.103},{"c":"r","o":0.15},{"c":"e","o":0.249},{"c":"d","o":0.402},{"c":" ","o":0.477},{"c":"L","o":0.512},{"c":"a","o":0.598},{"c":"m","o":0.661},{"c":"b","o":0.748},{"c":"\'","o":0.853},{"c":" ","o":0.863},{"c":"j","o":0.887},{"c":"u","o":0.936},{"c":"s","o":1.05},{"c":"t","o":1.1},{"c":" ","o":1.15},{"c":"t","o":1.188},{"c":"o","o":1.263},{"c":" ","o":1.325},{"c":"t","o":1.35},{"c":"e","o":1.4},{"c":"a","o":1.45},{"c":"s","o":1.512},{"c":"e","o":1.575},{"c":" ","o":1.637},{"c":"y","o":1.687},{"c":"o","o":1.775},{"c":"u","o":1.825},{"c":",","o":1.9},{"c":" ","o":1.925},{"c":"a","o":1.949},{"c":"h","o":2.001}],"x":"All red Lamb\' just to tease you, ah"},{"ts":26.666,"te":28.754,"l":[{"c":"N","o":0},{"c":"o","o":0},{"c":"n","o":0.075},{"c":"e","o":0.127},{"c":" ","o":0.163},{"c":"o","o":0.176},{"c":"f","o":0.201},{"c":" ","o":0.226},{"c":"t","o":0.239},{"c":"h","o":0.263},{"c":"e","o":0.316},{"c":"s","o":0.387},{"c":"e","o":0.426},{"c":" ","o":0.476},{"c":"t","o":0.501},{"c":"o","o":0.538},{"c":"y","o":0.599},{"c":"s","o":0.663},{"c":" ","o":0.768},{"c":"o","o":0.816},{"c":"n","o":0.888},{"c":" ","o":0.991},{"c":"l","o":1.063},{"c":"e","o":1.115},{"c":"a","o":1.186},{"c":"s","o":1.273},{"c":"e","o":1.361},{"c":" ","o":1.436},{"c":"t","o":1.475},{"c":"o","o":1.565},{"c":"o","o":1.663},{"c":",","o":1.775},{"c":" ","o":1.813},{"c":"a","o":1.85},{"c":"h","o":1.929}],"x":"None of these toys on lease too, ah"}]',
                    "lyrics_copyright": "Writer(s): Henry Walter, Guillaume de Homem-Christo, Martin Mckinney, Thomas Bangalter, Abel Tesfaye\nLyrics powered by www.musixmatch.com",
                    "richsync_length": 233,
                    "richsync_language": "en",
                    "richsync_language_description": "English",
                    "script_tracking_url": "http:\/\/tracking.musixmatch.com\/t1.0\/m_js\/e_0\/sn_0\/l_0\/su_6\/tr_YslpI3lSWtY0cZG7Mjz64xQyTfhkeWDh4PnQ70MOfMT7-UrMbspN_3J2697kRvv2iD4psBvcJ1y3-5QDL-ETX_41cEP17LuiRSdiLg/",
                    "updated_time": "2017-02-08T13:34:47Z",
                }
            },
        }
    }
