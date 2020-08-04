class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subj, verb, obj):
        self.subj = subj[1]
        self.verb = verb[1]
        self.obj = obj[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expected):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expected:
            return word[0]
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_type = peek(word_list)
    if next_type == 'noun':
        return match(word_list, 'noun')
    if next_type == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next")


def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')
    start = peek(word_list)
    print(word_list)
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)
