from lxml import html
import requests
import random
site = "https://blkom.com/"

def random_anime(genres=[]):
  first_site = site+ "/anime-list?genres="+"_".join(genres)
  page = requests.get(first_site)
  tree = html.fromstring(page.content)
  pages =  tree.xpath('//li[@class="page-item"]/a/@href')
  if len(pages) == 0:
    tree = tree
  else:
    pages[-1] = first_site
    random_page = random.choice(pages)
    page = requests.get(random_page)
    tree = html.fromstring(page.content)
  anime = tree.xpath('//div[@class="contents text-center"]')[0]
  href = anime.xpath('.//div[@class="poster"]/a/@href')
  if len(href) == 0:
    return 0 , "No Animes"
  random_href = random.choice(href)
  
  return 1, random_href

def home_page():
    page = requests.get(site)
    tree = html.fromstring(page.content)
    anime = tree.xpath('//div[@class="recent-episodes"]')
  
    if len(anime) == 0:
      return 0 , "err"
    for cc in anime:
        href = cc.xpath('.//a/@href')
        name = cc.xpath('.//div[@class="name"]/text()')
        numb = cc.xpath('.//div[@class="episode-number"]/text()')

    return 1, href, name, numb
    
def ep(url):
    search = requests.get(site + url)
    trees = html.fromstring(search.content)
    epi = ""
    try:
      epi = trees.xpath('//div[@class="episode-number"]/text()')[0]
      name = trees.xpath('//div[@class="anime-name"]/a/text()')[0]
    except:
      name = trees.xpath('//div[@class="anime-name"]/text()')[0]
  
    
    eplink = trees.xpath('//iframe/@src')
    dwlinks = trees.xpath('//div[@class="panel-body"]/a/@href')
    cal = trees.xpath('//div[@class="panel-body"]/a/text()')
    tit = trees.xpath('//div[@class="panel-body"]/a/@title')
    size = trees.xpath('//div[@class="panel-body"]/a/small/text()')
    for i in cal:
        if i.endswith("\n"):
            cal.remove(i)
    if len(eplink) == 0:
        return 0, "invalid ep"
    else:
        return 1, eplink[0], name, epi, dwlinks, cal, tit, size

def s__animes(namen):
  name = namen.replace(" ", "+")
  page = requests.get(site + '/search?query=' + name)
  tree = html.fromstring(page.content)
  anime = tree.xpath('//div[@class="name"]/a/@href')
  anime_name = tree.xpath('//div[@class="name"]/a/text()')
  poster = tree.xpath('//div[@class="poster"]/a/img[@class="lazy"]/@data-original')
  storie = tree.xpath('//div[@class="story-text"]/p/text()')


  filmoranime = []
  posters = []
  stories = []
  names = []
  for index,i in enumerate(anime):
    k = i.split("/")[1]
    if k == "anime":
      filmoranime.append(anime[index])
      posters.append(poster[index])
      stories.append(storie[index])
      names.append(anime_name[index])
  
  btbtlen = len(filmoranime)
  return filmoranime , posters , stories , names , btbtlen

def s_animes(namen, ova=False , info=False):
  name = namen.replace(" ", "+")
  page = requests.get(site+'/search?query=' + name)
  tree = html.fromstring(page.content)
  anime = tree.xpath('//div[@class="name"]/a/@href')
  name = tree.xpath('//div[@class="name"]/a/text()')
  poster = tree.xpath('//div[@class="poster"]/a/img[@class="lazy"]/@data-original')
  btbtlen = 0
  filmoranime = []
  names = []
  posters = []
  for index , i in enumerate(anime):
    k = i.split("/")[1]
    if info:
      filmoranime.append(i)
      names.append(name[index])
      btbtlen += 1
      posters.append(poster[index])
    elif k == "anime" and not ova:
      filmoranime.append(i)
      names.append(name[index])
      btbtlen += 1
      posters.append(poster[index])
    elif ova and k == "watch":
      filmoranime.append(i)
      names.append(name[index])
      btbtlen += 1
      posters.append(poster[index])
  return filmoranime , btbtlen , names , posters

def borba(ep, anime,cali):
  
    search = requests.get(site+ anime + "/" + ep)
    trees = html.fromstring(search.content)
    name = trees.xpath('//div[@class="anime-name"]/a/text()')
    if len(name) == 0:
        return 0, "لا توجد نتائج في البحث"
    eplink = trees.xpath('//iframe/@src')
    dwlinks = trees.xpath('//div[@class="panel-body"]/a/@href')
    cal = trees.xpath('//div[@class="panel-body"]/a/text()')
    for i in cal:
      if i.endswith("\n"):
        cal.remove(i)
    calit = []
    for i in cal:
      calit.append(i.replace("\n", ""))
    for i in calit:
      if not "p" in i:
        calit.remove(i)
    if len(calit) == 0:
      return 0, "No download links"
    for i in range(len(calit)):
      if cali in calit[i]:
        dwlinks = dwlinks[i]
        break

    if isinstance(dwlinks, list):
      dwlinks = dwlinks[0]

    
      

        
    if len(eplink) == 0:
        return 0, "invalid ep", 0
    else:
        return 1, dwlinks

def multidw(namen , st, en,cali):
  links = []
  errs = []
  for i in range(st,en+1):
    lara = borba(str(i),namen,cali)
    if lara[0] == 0:
      errs.append(str(i))
    elif lara[0] == 1:
      links.append(lara[1])

  

  return links , errs

def anime_ep(ep, anime):
    if len(anime) == 0:
        return 0, "لا توجد نتائج في البحث", 0
    search = requests.get(site + anime + "/" + ep)
    trees = html.fromstring(search.content)
    name = trees.xpath('//div[@class="anime-name"]/a/text()')
    if len(name) == 0:
        return 0, "لا توجد نتائج في البحث", 0
    eplink = trees.xpath('//iframe/@src')
    dwlinks = trees.xpath('//div[@class="panel-body"]/a/@href')
    cal = trees.xpath('//div[@class="panel-body"]/a/text()')
    tit = trees.xpath('//div[@class="panel-body"]/a/@title')
    size = trees.xpath('//div[@class="panel-body"]/a/small/text()') 
    for i in cal:
        if i.endswith("\n"):
            cal.remove(i)
    if len(eplink) == 0:
        return 0, "invalid ep", 0
    else:
        return 1, eplink[0], name[0], ep, dwlinks, cal, tit, size 


def anime_info(href):
    search = requests.get(href)
    link = href
    anpage = html.fromstring(search.content)
    aniname = anpage.xpath('//div[@class="name col-xs-12"]/span/h1/text()')[0]
    poster_link = anpage.xpath('//div[@class="poster"]/img[@class="lazy"]/@data-original')[0]
    story = anpage.xpath('//div[@class="story"]/p/text()')
    genres = anpage.xpath('//p[@class="genres"]/a/text()')
    test = anpage.xpath('//span[@class="head"]/text()')
    test1 = anpage.xpath('//span[@class="info"]/text()')
    test3 = anpage.xpath('//div[@class="info-cards"]/div[1]/span/text()')[0]
    test5 = anpage.xpath('//div[@class="info-cards"]//span/a/text()')
    
    if len(test5) == 0:
      nono = "-"
    else:
      nono = test5[0]
    test4 = anpage.xpath('//div[@class="info-cards"]/div[2]/span/text()')
    ratt = anpage.xpath(
        '//button[@class="rating-box pull-left dropdown-toggle"]/span/text()')
    other_names = anpage.xpath('//div[@class="names"]/span/text()')
    namees = []
    if len(story) == 0:
      try:
        story = anpage.xpath('//div[@class="story"]/text()')[0]
      except:
        story = ""
      if len(story) == 0:
        story = " - "
    else:
      story = "\n".join(story)
    for name in other_names:
      if not len(name) <= 2:
        namees.append(name)
    return 1, site+poster_link, story, genres, test1, test, ratt, aniname, link, test3, test4, nono , namees
