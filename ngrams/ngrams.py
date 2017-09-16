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

if "gen" in mode:
    gen.set_unigram_bigram(train_file, test_or_seed_file)
    gen = gen.gen_function(train_file, test_or_seed_file)