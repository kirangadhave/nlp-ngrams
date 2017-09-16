from random import *
import check as test

unigram_model = None
bigram_model = None

def set_unigram_bigram(train_file, test_file):
    global unigram_model
    global bigram_model
    unigram_model = test.gen_unigram_model(train_file, 1)
    bigram_model = test.gen_bigram_model(train_file)


def get_sentences(train_file, seed):
    
    s = []
    for x in range(10):
        sent = get_one(train_file, seed)
        sent = " ".join(sent)
        s.append(sent)
    return s


def get_one(train_file, seed):
    sentence = [seed.strip()]
    count = 0
    while count != 10:  
        next_word = get_next(seed, train_file)
        if (next_word == -1 or type(next_word) is not str):
            return sentence
        sentence.append(next_word)
        if next_word.strip() in [".","?","!"]:
            return sentence
        count += 1
        seed = next_word
    return sentence

def get_next(seed, train_file):
    bigrams_for_seed = [x[0] for x in list(bigram_model.items()) if x[0][0] == seed.strip().lower()]
    if(len(bigrams_for_seed) == 0):
        return -1
    bi_probs = {}
    for x in bigrams_for_seed:
        bi_probs[x] = bigram_model[x]/unigram_model[x[0]]
    bi_probs = sorted(bi_probs.items(), key = lambda x: x[1])
    word = []
    
    while word == []:
        random_no = random()
        cm_prob = 0.0
        for x in bi_probs:
            cm_prob += x[1]
            if (random_no < cm_prob) :
                word = x
                break
    try:
        return word[0][1]
    except:
        print("Error at ")
        print(word)
        
def gen_function(train_file, test_or_seed_file):
    seeds =[]
    with open(test_or_seed_file) as f:
        seeds = f.readlines()    
    sentences = []
    for seed in seeds:
        a = (seed, get_sentences(train_file, seed))
        sentences.append(a)
    return sentences
