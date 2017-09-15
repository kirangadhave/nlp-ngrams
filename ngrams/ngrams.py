#!/usr/bin/env python3.6
import sys
import test

train_file = sys.argv[1]
test_or_seed_file = sys.argv[3]
mode = sys.argv[2]

#a = test.unigram_sentence_prob(train_file, test_or_seed_file)
#b = test.bigram_sentence_prob(train_file, test_or_seed_file)
#c = test.bigram_sentence_prob(train_file, test_or_seed_file,1)

def get_sentences(train_file, test_file, seed):
    unigram_model = test.gen_unigram_model(train_file, 1)
    bigram_model = test.gen_bigram_model(train_file)
    
    








seeds =[]
with open(test_or_seed_file) as f:
    seeds = f.readlines()
    
sentences = []

for seed in seeds:
    a = (seed, get_sentences(train_file, test_or_seed_file, seed))
    sentences.append(a)
    
