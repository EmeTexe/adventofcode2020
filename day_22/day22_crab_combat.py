import time

start = time.time()
n_game = 0
deck1, deck2 = [], []
is_player2 = False
with open('day22_crab_combat.txt', 'r') as f:
    for line in f:
        if 'Player 2' in line:
            is_player2 = True
        elif line == '\n' or 'Player 1' in line:
            continue
        else:
            if is_player2:
                deck2.append(int(line.rstrip()))
            else:
                deck1.append(int(line.rstrip()))

part1_deck1, part1_deck2 = deck1[:], deck2[:]
while len(part1_deck1) > 0 and len(part1_deck2) > 0:
    card1, card2 = part1_deck1[0], part1_deck2[0]
    del part1_deck1[0]
    del part1_deck2[0]
    if card1 > card2:
        part1_deck1 += [card1, card2]
    else:
        part1_deck2 += [card2, card1]

final1 = sum([card * (n + 1) for n, card in enumerate(part1_deck1[::-1])]) if len(part1_deck2) == 0 else sum(
    [card * (n + 1) for n, card in enumerate(part1_deck2[::-1])])
print(f"part1 result : {final1}")


def play_game(deck1, deck2, depth):
    global n_game
    i = 0
    n_game += 1
    # print(f"New Game {n_game}! in depth {depth}")
    decks = {1: [], 2: []}
    while len(deck1) > 0 and len(deck2) > 0:
        i += 1
        if deck1 in decks[1] and deck2 in decks[2]:
            # print('deck already in previous decks')
            return deck1, deck2, True
        decks[1].append(deck1[:])
        decks[2].append(deck2[:])
        card1, card2 = deck1[0], deck2[0]
        del deck1[0]
        del deck2[0]
        if len(deck1) >= card1 and len(deck2) >= card2:
            d1, d2, win = play_game(deck1[0:card1], deck2[0:card2], depth + 1)
            if win:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        else:
            if card1 > card2:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]

    return deck1, deck2, True if len(deck1) > len(deck2) else False


d1, d2, winner = play_game(deck1, deck2, 0)

final2 = sum([card * (n + 1) for n, card in enumerate(d1[::-1])]) if winner else sum(
    [card * (n + 1) for n, card in enumerate(d2[::-1])])
print(f"part 2 result = {final2}")
print(f"compute time = {time.time() - start}")
