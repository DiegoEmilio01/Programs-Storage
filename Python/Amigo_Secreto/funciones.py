# https://oeis.org/A000166
# https://oeis.org/A038205

from random import shuffle
from math import factorial
from cmath import e
import itertools

def regalo_al_que_me_regala_2(list: list):
  if len(list) == 0 or len(list) == 1: return None
  if len(list) == 2: return [[list[0], list[1]], [list[1], list[0]]]
  shuffle(list)
  if len(list) % 2 == 1:
    ans = [[list[0], list[1]], [list[1], list[2]], [list[2], list[0]]]
    for i in range(3, len(list), 2):
      ans.append([list[i], list[i + 1]])
      ans.append([list[i + 1], list[i]])
    return ans
  ans = []
  for i in range(0, len(list), 2):
    ans.append([list[i], list[i + 1]])
    ans.append([list[i + 1], list[i]])
  return ans

def regalo_al_que_me_regala(list: list):
  if len(list) == 0 or len(list) == 1: return None
  if len(list) == 2: return [[list[0], list[1]], [list[1], list[0]]]
  shuffle(list)
  if len(list) % 2 == 1: ans, start = [[list[0], list[1]], [list[1], list[2]], [list[2], list[0]]], 3
  else: ans, start = [], 0
  for i in range(start, len(list), 2):
    ans.append([list[i], list[i + 1]])
    ans.append([list[i + 1], list[i]])
  return ans

def correct(l1, l2):
  for a, b in list(zip(l1, l2)): # O(n)
    if a == b: return False
  return True

def random(buyers: list):
  if len(buyers) == 0 or len(buyers) == 1: return None
  if len(buyers) == 2: return [[buyers[0], buyers[1]], [buyers[1], buyers[0]]]
  receivers = buyers.copy() # O(n)
  shuffle(receivers)
  while not correct(buyers, receivers): shuffle(receivers) # E(X) = e
  return list(zip(buyers, receivers)) # O(n)

def correct_minimum_cycle_3(l1, l2):
  pairs = set()
  for a, b in list(zip(l1, l2)): # O(n)
    if a == b or (b, a) in pairs: return False
    pairs.add((a,b))
  return True

def random_minimum_cycle_3(buyers: list):
  if len(buyers) == 0 or len(buyers) == 1: return None
  if len(buyers) == 2: return [[buyers[0], buyers[1]], [buyers[1], buyers[0]]]
  receivers = buyers.copy() # O(n)
  shuffle(receivers)
  while not correct_minimum_cycle_3(buyers, receivers): shuffle(receivers) # E(X) = e**3/2
  return list(zip(buyers, receivers)) # O(n)

def random3(list: list):
  if len(list) == 0 or len(list) == 1: return None
  if len(list) == 2: return [[list[0], list[1]], [list[1], list[0]]]
  people = list.copy()
  shuffle(people)
  total = 0
  for i in range(100):
    if correct(list, people): total += 1
    shuffle(people)
  return total / 100

def prob_perm(l1):
  total = 0
  for elem in list(itertools.permutations(l1)):
    if correct_minimum_cycle_3(elem, l1): total +=1
  return total # / factorial(len(l1))

def recursive_derangements(n):
  f, s = 1, 2
  for i in range(4, n + 1): s, f = (i - 1) * (s + f), s
  return s

def derangements(n):
  return int((factorial(n)/e + 1/2) // 1)

def prob_recursive_derangements(n):
  s = 2
  for i in range(4, n + 1): s = i * s + (-1) ** (i % 2)
  return s / factorial(n)

if __name__ == "__main__":
  # print(regalo_al_que_me_regala([1, 2, 3, 4]))
  
  # print(random3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
  print(prob_perm([1, 2, 3, 4, 5, 6, 7]), 1/e)
  print(e**1.5)
  # print(random2([1, 2, 3, 4]))
  #n = 20
  #print(prob_recursive_derangements(n))
  #print(e)
  #print("2.71828 18284 59045 23536 02874 71352 66249 77572 47093 69995 95749 66967 62772 40766 30353 54759 45713 82178 52516 64274 27466 39193 20030 59921 81741 35966 29043 57290 03342 95260 59563 07381 32328 62794 34907 63233 82988 07531 95251 01901 15738 34187 93070 21540 89149 93488 41675 09244 76146 06680 82264 80016 84774 11853 74234 54424 37107 53907 77449 92069 55170 27618 38606 26133 13845 83000 75204 49338 26560 29760 67371 13200 70932 87091 27443 74704 72306 96977 20931 01416 92836 81902 55151 08657 46377 21112 52389 78442 50569 53696 77078 54499 69967 94686 44549 05987 93163 68892 30098 79312 77361 78215 42499 92295 76351 48220 82698 95193 66803 31825 28869 39849 64651 05820".replace(" ", ""))