#!/usr/bin/env python3.6
import sys
import calc
import string
from math import log
import ngram_extract as ne

train_file = sys.argv[1]
test_or_seed_file = sys.argv[3]
mode = sys.argv[2]

unigram_log_probs = {}
bigram_log_probs = {}
bigram_smoothing_probs = {}

def gen_unigram_model():
    return calc.compute_probabilites(ne.extract_unigrams(train_file))

def gen_bigram_model(smoothing = 0):
    return calc.compute_probabilites(ne.extract_bigrams(train_file), smoothing)

def unigram_sent_prob(test):
    unigram_model = gen_unigram_model()
    logprob = 0.0
    for y in test:
        logprob += log(unigram_model[y],2)
    return logprob

def bigram_sent_prob(test):
    bigram_model = gen_bigram_model()
    logprob = 0.0
    for y in test:
        if(bigram_model[y] == 0.0):
            return "undefined"
        logprob += log(bigram_model[y],2)
    return logprob

def compute_sentence_prob():
    test_unigrams = []
    test_bigrams = []
        
    with open(test_or_seed_file) as f:
        for x in f:
            u = x.strip().split(" ")
            u = [y.lower() for y in u]
            u = [y for y in u if len(y) > 0]
            #u = [y for y in u if len(y) > 0 and y not in set(string.punctuation)]
            test_unigrams.append((x,u))
            
            b = ["phi"]
            b.extend(y.lower() for y in x.strip().split(" "))
            b = [y for y in b if len(y) > 0]
            #b = [y for y in b if len(y) > 0 and y not in set(string.punctuation)]
            b_c = b[1:]
            b = b[:-1]
            b = list(zip(b,b_c))
            test_bigrams.append((x,b))
            
    for x in test_unigrams:
        unigram_log_probs[x[0]] = unigram_sent_prob(x[1])
        
    for x in test_bigrams:
        bigram_log_probs[x[0]] = bigram_sent_prob(x[1])          
    
    
    
def ngram_lang_gen():
    print("gen")


# Main run routine. Decides if to compute probabilites of generate language    
if (mode == "-test"):
    compute_sentence_prob()
    print(unigram_log_probs)
    print()
    print(bigram_log_probs)
    print()
    print(bigram_smoothing_probs)
if(mode == "-gen"):
    ngram_lang_gen()
    