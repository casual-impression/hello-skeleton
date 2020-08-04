from nose.tools import *
from ex49 import parsing




def test_peek_ability():
    assert_equal(parsing.peek([('error', 'NONSENSE')]), 'error')
    word_list = [('noun', 'door'), ('noun', 'bear'), ('number', 1)]
    assert_equal(parsing.peek(word_list), 'noun')


def test_match_correct():
    test_list = [('verb', 'look'), ('stop', 'at'), ('noun', 'me')]
    assert_equal(parsing.match([('verb', 'go')], 'verb'), 'verb')
    assert_equal(parsing.match([('stop', 'at')], 'verb'), None)
    assert_equal(parsing.match(test_list, 'verb'), 'verb')

# it skips until requirement is met. elements are going away
# one by one. when it stops, it positions at the next element
def test_skip_right():
    test_list = [('verb', 'look'), ('stop', 'at'), ('noun', 'me')]
    assert_equal(parsing.skip(test_list, 'verb'), None)


def test_verb_parser():
    assert_equal(parsing.parse_verb([('verb', 'go')]), 'verb')


def test_object_parser():
    test_list = [('verb', 'look'), ('stop', 'at'), ('noun', 'me')]

    with assert_raises(parsing.ParserError):
        parsing.parse_object(test_list)
    # assert_equal(parsing.parse_object(test_list), 'direction')


def test_wrong_sentence():
    with assert_raises(parsing.ParserError):
        parsing.parse_subject([('direction', 'right')], ('noun', 'player'))


def test_right_creation():
    test_list = [('verb', 'look'), ('stop', 'at'), ('noun', 'me')]
    isinstance(parsing.parse_sentence(test_list), parsing.Sentence)
