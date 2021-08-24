from lxml import html
import requests
from random import randint
from random import choice
from modules.peta import anime_info
with open('db/animedb.txt','r') as f:
  b = f.read().splitlines()
site = "https://blkom.com"
def randomanime():
  anime = choice(b)

  return anime
