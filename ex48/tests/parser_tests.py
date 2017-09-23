from nose.tools import *
from ex48 import parser

# an alternate way to use assert_raises:
# def test_exception():
    # with assert_raises(parser.ParserError) as cm:
        # parser.parse_sentence([('error', 'help')])
    # ex = cm.exception
    # can't get this part to work:
    # ok_(ex.args == "Expected a verb next.")
    # test fails with AssertionError: None

def test_exception():
    case = [('error', 'help')]
    assert_raises(parser.ParserError, parser.parse_sentence, case)
    case1 = [('noun', 'bear')]
    assert_raises(parser.ParserError, parser.parse_verb, case1)
    case2 = [('verb', 'go')]
    assert_raises(parser.ParserError, parser.parse_object, case2)
    case3 = [('error', 'help'), ('error', 'me')]
    assert_raises(parser.ParserError, parser.parse_subject, case3)

def test_peek():
    assert_equal(parser.peek([('verb', 'go')]), 'verb')
    assert_equal(parser.peek([]), None)

def test_match():
    assert_equal(parser.match([('verb', 'go')], 'verb'), ('verb', 'go'))
    assert_equal(parser.match([('noun', 'bear')], 'verb'), None)
    assert_equal(parser.match([], 'stop'), None)

def test_parse_verb():
    assert_equal(parser.parse_verb([('verb', 'kill')]), ('verb', 'kill'))
    case = [('verb', 'eat'), ('stop', 'in'), ('noun', 'door')]
    assert_equal(parser.parse_verb(case), ('verb', 'eat'))

def test_parse_object():
    assert_equal(parser.parse_object([('noun', 'door')]), ('noun', 'door'))
    case = [('stop', 'to'), ('direction', 'north'), ('noun', 'bear')]
    assert_equal(parser.parse_object(case), ('direction', 'north'))
    case1 = [('stop', 'to'), ('stop', 'the'), ('direction', 'south')]
    assert_equal(parser.parse_object(case1), ('direction', 'south'))

def test_parse_subject():
    assert_equal(parser.parse_subject([('verb', 'go')]), ('noun', 'player'))
    case = [('noun', 'I'), ('verb', 'go'), ('direction', 'left')]
    assert_equal(parser.parse_subject(case), ('noun', 'I'))
    case1 = [('verb', 'punch'), ('noun', 'bear')]
    assert_equal(parser.parse_subject(case1), ('noun', 'player'))

def test_parse_sentence():
    case = [('verb', 'punch'), ('noun', 'bear')]
    sentence = parser.parse_sentence(case)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'punch')
    assert_equal(sentence.obj, 'bear')

    case1 = [('noun', 'bear'), ('verb', 'goes'), ('direction', 'south')]
    sentence1 = parser.parse_sentence(case1)
    assert_equal(sentence1.subject, 'bear')
    assert_equal(sentence1.verb, 'goes')
    assert_equal(sentence1.obj, 'south')

    case2 = [('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('direction', 'left')]
    sentence2 = parser.parse_sentence(case2)
    assert_equal(sentence2.subject, 'player')
    assert_equal(sentence2.verb, 'go')
    assert_equal(sentence2.obj, 'left')
