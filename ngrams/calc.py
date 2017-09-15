from collections import Counter

def compute_probabilites(gram, smoothing = 0):
    freq = Counter(gram)
    gram_length = len(gram) + smoothing*len(set(gram))
    for x in freq:
        freq[x] = (freq[x] + smoothing)/gram_length
    return freq