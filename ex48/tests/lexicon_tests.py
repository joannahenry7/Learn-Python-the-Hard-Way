from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])
    result1 = lexicon.scan("west up down back")
    assert_equal(result1, [('direction', 'west'),
                           ('direction', 'up'),
                           ('direction', 'down'),
                           ('direction', 'back')])
    result2 = lexicon.scan("left right")
    assert_equal(result2, [('direction', 'left'),
                           ('direction', 'right')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])
    assert_equal(lexicon.scan("stop"), [('verb', 'stop')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])
    result1 = lexicon.scan("from at it")
    assert_equal(result1, [('stop', 'from'),
                           ('stop', 'at'),
                           ('stop', 'it')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])
    result1 = lexicon.scan("door cabinet")
    assert_equal(result1, [('noun', 'door'),
                           ('noun', 'cabinet')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'asdfadfasdf')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'ias'),
                          ('noun', 'princess')])

def test_downcase():
    result = lexicon.scan("Fight Bear")
    assert_equal(result, [('verb', 'fight'),
                          ('noun', 'bear')])
