#this code gives you all the possible combinations of a poker deck
import itertools
rank=list(range(2,11))+['J','K','Q','A']
ranks=[str(ranks) for ranks in rank]
suits=['HEARTS','SPADES','CLUBS','DIAMONDS']
deck=[card for card in itertools.product(ranks,suits)]
hands=[hand for hand in itertools.combinations(deck,5)]
print(len(hands))
