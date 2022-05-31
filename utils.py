import random
from string import punctuation
import pyautogui as pg
import time

word_lists = ["one_letter_words.txt", "two_letter_words.txt", "three_letter_words.txt"]
words = []
punctuation = [".", "!", "?"]

for i in range(len(word_lists)):
  file = open("./word_lists/" + word_lists[i], 'r')
  words.append(file.read().splitlines())
  file.close()

# file = open("./word_lists_three_letter_words.txt", 'w')
# for word in words[2]:
#   file.write(word.lower() + '\n')
# file.close()

def choose_word():
  index = random.randrange(0, 20)
  if index > 7:
    index = 2
  elif index > 0:
    index = 1

  return random.choice(words[index])

def make_sentence():
  arr = [str(choose_word()) for i in range(random.randrange(4, 12))]
  # sentence = []
  # for word in arr:
  #   sentence.append(word)
  #   sentence.append(" ")

  return " ".join(arr).strip()

def key_press(key, delay):
  pg.typewrite(key)
  time.sleep(random.choice(delay))

def type_sentence(sentence):
  delay = [x / 100.0 for x in range(5, 10, 1)]
  key_press(" ", delay)
  pg.keyDown("shift")
  random.choice(delay)
  key_press(sentence[0], delay)
  pg.keyUp("shift")
  random.choice(delay)
  sentence = sentence[1::]
  [key_press(key, delay) for word in sentence for key in word]
  key_press(random.choice(punctuation), delay)
