#!/usr/bin/env python3.6
import sys
import gen
import test
from random import *

train_file = sys.argv[1]
test_or_seed_file = sys.argv[3]
mode = sys.argv[2]

if "test" in mode:
    a = test.unigram_sentence_prob(train_file, test_or_seed_file)
    b = test.bigram_sentence_prob(train_file, test_or_seed_file)
    c = test.bigram_sentence_prob(train_file, test_or_seed_file,1)

    for x in a.keys():
        print("S = " + x.strip())
        print()
        print("Unsmoothed Unigrams, logprob(S) = " + str(a[x]))
        print("Unsmoothed Bigrams, logprob(S) = "+ str(b[x]))
        print("Smoothed Bigrams, logprob(S) = "+ str(c[x]))
        print()
        
if "gen" in mode:
    gen.set_unigram_bigram(train_file, test_or_seed_file)
    gen = gen.gen_function(train_file, test_or_seed_file)
    
    for x in gen:
        print("Seed = " + x[0].strip())
        print()
        count = 1
        for y in x[1]:
            print("Sentence " + str(count) +": " + y)
            count += 1
        print()