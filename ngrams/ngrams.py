#!/usr/bin/env python3.6
import sys
import calc
import string
from math import log
import ngram_extract as ne

train_file = sys.argv[1]
test_or_seed_file = sys.argv[3]
mode = sys.argv[2]

def gen_unigram_model(train_file):
    return ne.extract_unigrams(train_file)
    
def gen_bigram_model(train_file):
    return ne.extract_bigrams(train_file)
    
a = gen_unigram_model(train_file)
b = gen_bigram_model(train_file)