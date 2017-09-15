#!/usr/bin/env python3.6
import sys
import calc
from math import log
import ngram_extract as ne

train_file = sys.argv[1]
test_or_seed_file = sys.argv[3]
mode = sys.argv[2]

def gen_unigram_model():
    return calc.compute_probabilites(ne.extract_unigrams(train_file))

def gen_bigram_model(smoothing = 0):
    return calc.compute_probabilites(ne.extract_bigrams(train_file), smoothing)

#unigram_prob = gen_unigram_model()
#bigram_prob = gen_bigram_model
#bigram_prob_smooth = gen_bigram_model(1)




def compute_sentence_prob():
    unigram_model = gen_unigram_model()
    bigram_model = gen_bigram_model()
    
    unigram_log_probs = {}
    bigram_log_probs = {}
    
    sp_bigram = 0.0
    sp_bigram_smooth = 0.0
    
    test_unigrams = []
    test_bigrams = []
    with open(test_or_seed_file) as f:
        for x in f:
            unigram = (x.strip().split(" "))
            unigram = [y.lower() for y in unigram]
            unigram = [x for x in unigram if len(x) > 0]
            test_unigrams.append((x, unigram))
            
            bigram = ["phi"]
            bigram.extend([y.lower() for y in x.strip().split(" ")])
            bigram = [y for y in bigram if len(y) > 0]        
            bigram_c = bigram[1:]
            bigram = bigram[:-1]
            bigram = list(zip(bigram, bigram_c))
            test_bigrams.append((x, bigram))
    
    for x in test_unigrams:
        sp_unigram = 0.0
        for y in x[1]:
            if(unigram_model[y] == 0.0):
                unigram_log_probs[x[0]] = logprob
                break
            sp_unigram += log(unigram_model[y],2)
        unigram_log_probs[x[0]] = sp_unigram
        
    for x in test_bigrams:
        sp_bigram = 0.0
        for y in x[1]:
            logprob = "undefined"
            if(bigram_model[y] != 0.0 and sp_bigram != "undefined"):
                sp_bigram += log(bigram_model[y],2)
            else:
                sp_bigram = "undefined"
        bigram_log_probs[x[0]] = sp_bigram
    
    for x in bigram_log_probs:
        print(x+ str(bigram_log_probs[x]))
        
    
            
        
    
    
def ngram_lang_gen():
    print("gen")


# Main run routine. Decides if to compute probabilites of generate language    
if (mode == "-test"):
    compute_sentence_prob()
    
if(mode == "-gen"):
    ngram_lang_gen()
    