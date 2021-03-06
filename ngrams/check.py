import ngram_extract as ne
from math import log

def gen_unigram_model(train_file, phi = 0):
    return ne.extract_unigram_models(train_file, phi)
    
def gen_bigram_model(train_file):
    return ne.extract_bigram_models(train_file)
    
def unigram_sentence_prob(train_file, test_or_seed_file):
    unigram_model = gen_unigram_model(train_file)
    test_unigrams = ne.extract_unigrams(test_or_seed_file)
    
    total_unigram_freq = sum(unigram_model.values())
    
    unigram_sent_probs = {}
    
    for x in test_unigrams:
        logprob = 0.0
        for y in x[1]:
            logprob += log(unigram_model[y]/total_unigram_freq, 2)
        unigram_sent_probs[x[0]] = round(logprob,4)
    return unigram_sent_probs

def bigram_sentence_prob(train_file,test_or_seed_file, smoothing = 0):
    unigram_model = gen_unigram_model(train_file, 1)
    bigram_model = gen_bigram_model(train_file)
    test_bigrams = ne.extract_bigrams(test_or_seed_file)
        
    bigram_sent_prob = {}
#    total_bigram_freq = sum(bigram_model.values())    
#    total_unigram_freq = sum(unigram_model.values())
    V = len(set(unigram_model))
    
    
    for x in test_bigrams:
        logprob = 0.0
        for y in x[1]:
            prob_bigram = bigram_model[y] + smoothing
            prob_prec_word = unigram_model[y[0]] + smoothing*V
            prob_bigram_cond = prob_bigram/prob_prec_word
            if(prob_bigram_cond == 0 or logprob == "undefined"):
                logprob = "undefined"
            else:
                logprob += log(prob_bigram_cond,2)
        if(logprob == "undefined"):
            bigram_sent_prob[x[0]] = logprob
        else:
            bigram_sent_prob[x[0]] = round(logprob, 4)
    return bigram_sent_prob