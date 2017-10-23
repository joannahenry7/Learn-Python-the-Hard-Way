from nose.tools import *
from bin.app import app
from tests.tools import assert_response
from gothonweb.map import *


def test_index():
    # check that we got a 404 on the /h URL
    resp = app.request("/h")
    assert_response(resp, status="404")

    # check that we got a 303 on the / URL
    resp = app.request("/")
    assert_response(resp, status="303")

    # test GET request to /game
    resp1 = app.request("/game")
    assert_response(resp1)

    # make sure default values work for the form
    #resp = app.request("/hello", method="POST")
    #assert_response(resp, contains="Nobody")

    # test that we get expected values
    #data = {'name': 'Zed', 'greet': 'Hola'}
    #resp = app.request("/hello", method="POST", data=data)
    #assert_response(resp, contains="Zed")

def get_session_id(resp):
    cookies_str = resp.headers['Set-Cookie']
    if cookies_str:
        for kv in cookies_str.split(';'):
            if 'webpy_session_id=' in kv:
                return kv

def test_engine():
    resp = app.request('/')
    session_id = get_session_id(resp)
    header = {'Cookie': session_id}

    resp1 = app.request('/game', headers=header)
    assert_response(resp1, contains='Central Corridor')

    data = {'action': 'tell a joke'}
    resp2 = app.request('/game', headers=header, method='POST', data=data)
    assert_response(resp2, status='303')
    resp3 = app.request('/game', headers=header)
    assert_response(resp3, contains='Laser Weapon Armory')

    data1 = {'action': stuff.code}
    resp4 = app.request('/game', headers=header, method='POST', data=data1)
    assert_response(resp4, status='303')
    resp5 = app.request('/game', headers=header)
    assert_response(resp5, contains='The Bridge')

    data2 = {'action': 'slowly place the bomb'}
    resp6 = app.request('/game', headers=header, method='POST', data=data2)
    assert_response(resp6, status='303')
    resp7 = app.request('/game', headers=header)
    assert_response(resp7, contains='Escape Pod')

    data3 = {'action': stuff.pod}
    resp8 = app.request('/game', headers=header, method='POST', data=data3)
    assert_response(resp8, status='303')
    resp9 = app.request('/game', headers=header)
    assert_response(resp9, contains='You won!')

def test_death():
    resp = app.request('/')
    session_id = get_session_id(resp)
    header = {'Cookie': session_id}

    data = {'action': 'shoot!'}
    resp1 = app.request('/game', headers=header, method='POST', data=data)
    assert_response(resp1, status='303')
    resp2 = app.request('/game', headers=header)
    assert_response(resp2, contains='Quick on the draw you yank out your blaster')

    resp3 = app.request('/')
    session_id1 = get_session_id(resp3)
    header1 = {'Cookie': session_id1}

    data1 = {'action': 'dodge!'}
    resp4 = app.request('/game', headers=header1, method='POST', data=data1)
    assert_response(resp4, status='303')
    resp5 = app.request('/game', headers=header1)
    assert_response(resp5, contains='Like a world class boxer you dodge')

    resp6 = app.request('/')
    session_id2 = get_session_id(resp6)
    header2 = {'Cookie': session_id2}

    data2 = {'action': 'tell a joke'}
    data3 = {'action': '000'}
    app.request('/game', headers=header2, method='POST', data=data2)
    # skip testing response because this was already tested
    resp7 = app.request('/game', headers=header2, method='POST', data=data3)
    assert_response(resp7, status='303')
    resp8 = app.request('/game', headers=header2)
    assert_response(resp8, contains='BZZZZEDDD')
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    app.request('/game', headers=header2, method='POST', data=data3)
    resp8_1 = app.request('/game', headers=header2)
    assert_response(resp8_1, contains='The lock buzzes one last time')

    resp9 = app.request('/')
    session_id3 = get_session_id(resp9)
    header3 = {'Cookie': session_id3}

    data4 = {'action': stuff.code}
    data5 = {'action': 'throw the bomb'}
    app.request('/game', headers=header3, method='POST', data=data2)
    app.request('/game', headers=header3, method='POST', data=data4)
    resp10 = app.request('/game', headers=header3, method='POST', data=data5)
    assert_response(resp10, status='303')
    resp11 = app.request('/game', headers=header3)
    assert_response(resp11, contains='In a panic you throw the bomb')

    resp12 = app.request('/')
    session_id4 = get_session_id(resp12)
    header4 = {'Cookie': session_id4}

    data6 = {'action': 'slowly place the bomb'}
    data7 = {'action': '*'}
    app.request('/game', headers=header4, method='POST', data=data2) # tell a joke
    app.request('/game', headers=header4, method='POST', data=data4) # enter correct code
    app.request('/game', headers=header4, method='POST', data=data6) # slowly place the bomb
    resp13 = app.request('/game', headers=header4, method='POST', data=data7) # wrong pod
    assert_response(resp13, status='303')
    resp14 = app.request('/game', headers=header4)
    assert_response(resp14, contains='You jump into a random pod')
