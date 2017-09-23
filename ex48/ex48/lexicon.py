def scan(string):
    words = string.lower().split()

    directions = ['north', 'south', 'east', 'west', 'up', 'down', 'left',
                  'right', 'back', 'forward']
    verbs = ['go', 'stop', 'kill', 'eat', 'punch', 'kick', 'poke', 'stay',
             'run', 'walk', 'open', 'prod', 'yell', 'scream', 'panic', 'fight']
    stops = ['the', 'in', 'of', 'from', 'at', 'it', 'for', 'to', 'a', 'an',
             'and']
    nouns = ['door', 'bear', 'princess', 'cabinet', 'monster', 'snakes', 'pit']

    sentence = []

    for word in words:
        if word in directions:
            item = ('direction', word)
        elif word in verbs:
            item = ('verb', word)
        elif word in stops:
            item = ('stop', word)
        elif word in nouns:
            item = ('noun', word)
        else:
            try:
                num = int(word)
                item = ('number', num)
            except ValueError:
                item = ('error', word)

        sentence.append(item)

    return sentence
