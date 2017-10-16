from nose.tools import *
from bin.app import app
from tests.tools import assert_response


def test_index():
    # check that we got a 404 on the /h URL
    resp = app.request("/h")
    assert_response(resp, status="404")

    # test our first GET request to /
    resp = app.request("/")
    assert_response(resp, status="303")

    # test GET request to /game
    resp1 = app.request("/game")
    assert_response(resp1, contains="Gothons")

    # make sure default values work for the form
    #resp = app.request("/hello", method="POST")
    #assert_response(resp, contains="Nobody")

    # test that we get expected values
    #data = {'name': 'Zed', 'greet': 'Hola'}
    #resp = app.request("/hello", method="POST", data=data)
    #assert_response(resp, contains="Zed")

def test_engine():
    pass
