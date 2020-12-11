def decode_bf(seq):
    upper = 127
    lower = 0
    for c in seq[:7]:
        half = (upper - lower + 1) / 2
        if c == "F":
            upper -= half
        elif c == "B":
            lower += half
    print(upper, lower)
    if lower == upper:
        return lower
    else:
        raise


def decode_lr(seq):
    upper = 7
    lower = 0
    for c in seq[7:]:
        half = (upper - lower + 1) / 2
        if c == "L":
            upper -= half
        elif c == "R":
            lower += half
    if lower == upper:
        return lower
    else:
        raise


def find_score(seq):
    return decode_bf(seq) * 8 + decode_lr(seq)


def all_scores(seqs):
    scores = []
    for seq in seqs:
        scores.append(find_score(seq))
    return sorted(scores)


def find_seat(scores):
    for i in range(int(scores[0])+1, int(scores[-1])-1):
        if i-1 in scores and i+1 in scores and i not in scores:
            return i
    return 0


with open('day5_binary_boarding.txt', 'r') as f:
    lines = f.read().splitlines()


print(find_seat(all_scores(lines)))

"""7<score<1016"""
