from collections import Counter

def extract_unigrams(train_file, phi = 0):
    unigrams = []
    with open(train_file) as f:
        for x in f:
            a = ["phi"]
            if(phi == 0):
                a = []
            a.extend(x.strip().split(" "))
            a = [y.lower() for y in a]
            a = [x for x in a if len(x) > 0]
            unigrams.append((x,a))
    return unigrams

def extract_unigram_models(train_file, phi = 0):
    l = []
    for x in extract_unigrams(train_file, phi):
        l.extend(x[1])
    return Counter(l)


def extract_bigrams(train_file):
    bigrams = []
    with open(train_file) as f:
        for x in f:
            bigram = ["phi"]
            bigram.extend([y.lower() for y in x.strip().split(" ")])
            #bigram = [y for y in bigram if len(y) > 0 and x not in set(string.punctuation)]
            bigram = [y for y in bigram if len(y) > 0]
            bigram_c = bigram[1:]
            bigram = bigram[:-1]
            bigram = list(zip(bigram, bigram_c))
            bigrams.append((x,bigram))
    return bigrams

def extract_bigram_models(train_file):
    l = []
    for x in extract_bigrams(train_file):
        l.extend(x[1])
    return Counter(l)