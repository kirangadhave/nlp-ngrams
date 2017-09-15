def extract_unigrams(train_file):
    unigrams = []
    with open(train_file) as f:
        for x in f:
            unigrams.extend(x.strip().split(" "))
    unigrams = [y.lower() for y in unigrams]
    unigrams = [x for x in unigrams if len(x) > 0]
    return unigrams

def extract_bigrams(train_file):
    bigrams = []
    with open(train_file) as f:
        for x in f:
            bigram = ["phi"]
            bigram.extend([y.lower() for y in x.strip().split(" ")])
            bigram = [y for y in bigram if len(y) > 0]        
            bigram_c = bigram[1:]
            bigram = bigram[:-1]
            bigram = list(zip(bigram, bigram_c))
            bigrams.extend(bigram)
    return bigrams