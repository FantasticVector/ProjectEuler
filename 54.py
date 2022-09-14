with open('ProjectEuler/54_testinput.txt', 'r') as f:
  plays = f.read().splitlines()

def royalFlush(cards):
  return sorted([card[0] for card in cards]) == ['A', 'J', 'K', 'Q', 'T']

def straightFlush(cards):
  values = [card[:-1] for card in cards]
  suits = [cards[-1] for card in cards]
  return len(suits) == 1 and ''.join(sorted(values)) in '23456789TJQKA'

def fourOfKind(cards):
  values = [card[:-1] for card in cards]
  for val in set(values):
    if values.count(val) == 4: return True
  return False

def fullHouse(cards):
  values = [card[:-1] for card in cards]
  valuePair = {values.count(i):i for i in set(values)}
  return (valuePair[3], sorted(valuePair.keys()) == [2, 3])

def flush(cards):
  suits = [card[-1] for card in cards]
  return len(set(suits)) == 1

def straight(cards):
  values = [card[:-1] for card in cards]
  return ''.join(sorted(values)) in '23456789TJQKA'

def threeOfAKind(cards):
  values = [card[:-1] for card in cards]
  for val in set(values):
    if values.count(val) == 3: return True
  return False

def twoPairs(cards):
  values = [card[:-1] for card in cards]
  return sorted([values.count(i) for i in set(values)]) == [1, 2, 2]

def onePair(cards):
  values = [card[:-1] for card in cards]
  for val in set(values):
    if values.count(val) == 2: return True
  return False

def highCard(player1, player2):
  p1 = [' 23456789TJQKA'.index(card[:-1]) for card in player1]
  p2 = [' 23456789TJQKA'.index(card[:-1]) for card in player2]
  for i, j in zip(reversed(sorted(p1)), reversed(sorted(p2))):
    if i > j: return 'p1'
    if i < j: return 'p2'

hands = {'9': royalFlush, 
        '8': straightFlush, 
        '7': fourOfKind, 
        '6': fullHouse, 
        '5': flush, 
        '4': straight, 
        '3': threeOfAKind, 
        '2': twoPairs, 
        '1': onePair}

# p1Wins = 0
# for play in plays:
#   player1 = play.split()[:5]
#   player2 = play.split()[5:]
#   val1 = max([int(hand) if hands[hand](player1) else 0 for hand in hands])
#   val2 = max([int(hand) if hands[hand](player2) else 0 for hand in hands])
#   print(val1, val2)
#   if val1 > val2:
#     p1Wins += 1
#     print("1 wins")
#   elif val1 == val2 and highCard(player1, player2) == 'p1':
#     p1Wins += 1
#     print("1 wins")
print(fullHouse(plays[4].split()[:5]))
print(fullHouse(plays[4].split()[5:]))
