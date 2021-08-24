from lxml import html
import requests
site='https://www.premierleague.com/tables'
def pos():
  page = requests.get(site)
  tree = html.fromstring(page.text)
  name = tree.xpath('//span[@class="long"]/text()')
  pos  = tree.xpath('//span[@class="value"]/text()')
  pts  = tree.xpath('//td[@class="points"]/text()')
  Gd   = tree.xpath('//td[@class="hideSmall"]/text()')
  return name,pos,pts,Gd