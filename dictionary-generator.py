#!/usr/bin/python
# coding: utf-8
import DictionaryServices, re, operator, json

start = "love"
max_depth = 100
min_word_len = 3

visited = dict()

def visit(word, depth):
    if depth > max_depth:
        return
    if word in visited:
        return

    text = DictionaryServices.DCSCopyTextDefinition(None, word, (0, len(word)))
    if not text or len(text) == 0:
        return

    pos_pieces = filter(lambda x: u'▶' in x, text.split())
    pos = pos_pieces[0].replace(u'▶', '') if len(pos_pieces) > 0 else None

    visited[word] = pos

    # We don't care about any of the origin/etymology data, so remove it
    text = text.split('ORIGIN')[0]
    # Remove any punctuation, weird characters, etc.
    filtered_text = re.sub(r'[\W\d]+', ' ', text).lower()
    words = filtered_text.split()

    for w in words:
        if len(w) > 2:
            visit(w, depth + 1)

visit(start, 1)

words = dict((k, v) for k, v in visited.items() if v == 'noun' or v == 'adjective')

print json.dumps(words, sort_keys=True)
