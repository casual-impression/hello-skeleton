directions = [
    'north', 'south', 'east', 'west',
    'up', 'down', 'right', 'left', 'back'
]
verbs = [
    'go', 'stop', 'kill', 'eat'
]
stops = [
    'the', 'in', 'of', 'from', 'at', 'it'
]
nouns = [
    'door', 'bear', 'princess', 'cabinet'
]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(saying):
    dictionary = []
    words = saying.split()

    for word in words:
        if word.lower() in directions:
            dictionary.append(('direction', word))
        elif word.lower() in verbs:
            dictionary.append(('verb', word))
        elif word.lower() in stops:
            dictionary.append(('stop', word))
        elif word.lower() in nouns:
            dictionary.append(('noun', word))
        else:
            maybe_num = convert_number(word)
            if not (maybe_num is None):
                dictionary.append(('number', maybe_num))
            else:
                dictionary.append(('error', word))
    return dictionary
