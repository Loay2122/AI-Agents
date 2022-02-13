import nltk

sentence = "I Have Orange and Apple and Kiwi"
is_noun = lambda pos: pos[:2] == "NN"
tokenized = nltk.word_tokenize(sentence)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
for i in range(len(nouns)):
    noun= nouns[i]
    if noun[0]=="A" or noun[0]=="E" or noun[0]=="I" or noun[0]=="O" or noun[0]=="U":
        sentence = sentence.replace(noun[0], "An " + noun[0])
    else:
        sentence = sentence.replace(noun[0], "A " + noun[0])

print(sentence)