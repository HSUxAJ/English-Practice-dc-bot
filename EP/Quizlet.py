from concurrent.futures.process import _ExceptionWithTraceback
from multiprocessing.connection import wait
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

def write_quizlet_data(url):
  r = requests.get(url, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
  soup = BeautifulSoup(r.text, 'html.parser')
  title = soup.find(class_ = 'UIHeading UIHeading--one').text.replace(' ', '') + '.txt'
  for i in '\\/:*?\'"<>|':
    title = title.replace(i, '')
  v = soup.find_all(class_ = 'TermText notranslate lang-en')
  with open('vocabulary/' + title, '+w', encoding="utf-8") as f:
    for i in v:
      t = str(i.text)
      if len(t.split()) > 1:
        continue
      if t.find('/') != -1:
        t = t[:t.find('/')]
      f.write(t.lower() + '\n')
  return title

def write_dictionary_data(title, voc):
  sen = []
  for v in voc:
    r = requests.get("https://sentence.yourdictionary.com/" + v, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    soup = BeautifulSoup(r.text, 'html.parser')
    info = soup.find_all(class_ = 'sentence-item__text')
    size = 10
    if len(info) < size:
      size = len(info)
    for i in range(size):
      sen.append(info[i].text.replace(u'\xa0', u' '))
  with open('sentences/' + title, '+w', encoding="utf-8") as f:
    for s in sen:
      f.write(s + '\n')

def generate_sentence(title):
  voc = []
  with open('vocabulary/' + title, 'r', encoding="utf-8") as file:
    for v in file:
      voc.append(v.strip('\n'))
  write_dictionary_data(title, voc)

class Quizlet(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(
      help = '''
        plz enter the Quizlet's url
        ''',
      #brief = "Print satellite cloud chart"
  )
  async def add(self, ctx, url):
    title=''
    try:
      title = write_quizlet_data(url)
    except Exception as e:
      await ctx.send('Query error: ' + str(e))
    try:
      print('executing')
      await ctx.send('executing')
      generate_sentence(title)
      await ctx.send('add successfully')
    except Exception as e:
      await ctx.send('adding error: ' + str(e))
    print('completed')


def setup(bot):
    bot.add_cog(Quizlet(bot))