#!/usr/bin/env python3.6
import sys
from collections import Counter

train_file = sys.argv[1]
test_file = sys.argv[3]
unigram_prob = []
bigram_prob = []

        
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

def compute_probabilites(gram):
    prob_list = Counter(gram)
    gram_length = len(gram)
    return prob_list

u = extract_unigrams(train_file)
b = extract_bigrams(train_file)

unigram_prob = compute_probabilites(u)
bigram_prob = compute_probabilites(b)