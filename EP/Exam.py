from discord.ext import commands
import random
import os
from os.path import isfile, join

Q = 3   #預設題數

async def print_quiz_data(channel):
  await channel.trigger_typing()
  await channel.send('請選擇題庫：')
  quiz_data = []
  path = 'sentences'
  files = os.listdir(path)
  for i, f in enumerate(files):
    fullpath = join(path, f)
    if isfile(fullpath):
      quiz_data.append(f)
      await channel.send('{index}: {file_name}'.format(index=i+1, file_name=f[:-4]))
  return quiz_data

def get_data(name):
  voc = []
  with open('vocabulary/'+name, 'r', encoding="utf-8") as f:
    for v in f:
      voc.append(v.strip('\n'))
  que = []
  randSen = [random.randint(0, 9)+i*10 for i in range(len(voc))]
  allSen = []
  with open('sentences/'+name, 'r', encoding="utf-8") as f:
    allSen = [s.strip('\n') for s in f]
  for i in randSen:
    que.append(allSen[i])
  return voc, que

def hollow_sentence(voc, sen, name):
  processed = []
  for i in range(len(voc)):
    if voc[i] not in sen[i]:
      processed.append(sen[i].replace(voc[i][0].upper()+voc[i][1:], '\_'*4) + '\n')  
    else:
      processed.append(sen[i].replace(voc[i], '\_'*4) + '\n')
  with open('questions/'+name, '+w', encoding="utf-8") as f:
    for s in processed:
      f.write(s)
  return processed

def generate_question(voc, sen):
  size = len(voc)
  ans = []
  que = []
  opt = []
  ansNum = []
  rand = [i for i in range(size)]
  random.shuffle(rand)
  for i in rand:
    ans.append(voc[i])
    que.append(sen[i])
  k = 0
  while k < size:
    random.shuffle(rand)
    tmp = []
    for index, a in enumerate(['(1)', '(2)', '(3)', '(4)']):
      tmp.append("{} {}\n".format(a, voc[rand[index]]))
    notAppear = True
    for c in [s for s in tmp]:
      if ans[k] in c:
        notAppear = False
        break
    if notAppear:
      rPos = random.randint(0, 3)
      tmp[rPos] = "({}) {}\n".format(rPos+1, ans[k])
      ansNum.append(rPos)
    opt.append(tmp)
    k += 1
  return ans, que, opt, ansNum

async def print_question(que, opt, channel, bot, playerId):
  sel = []
  q = ''
  for i in range(Q):
    s = 'Q{}.\n{}'.format(i+1, que[i])
    for j in opt[i]:
      s += j
    if q == '':
      q = await channel.send(s)
    else:
      await q.edit(s)
    while True:
        choose = await bot.wait_for('message', timeout=300.0)
        if choose.channel == channel and choose.author.id == playerId and (choose.content in [str(i) for i in range(1,5)]):
          break
        else:
          await choose.delete()
    sel.append(int(choose.content)-1)
    await choose.delete()
  await q.delete()
  return sel

async def review(ans, ansNum, sel, opt, sen, channel):
  correct = 0
  for i in range(Q):
    if sel[i] == ansNum[i]:
      correct += 1
    s = 'Q{}.\n{}'.format(i+1, sen[i].replace('\_\_\_\_', '{}'.format(ans[i])))
    for j in range(len(opt[i])):
      if j == sel[i] and sel[i] != ansNum[i]:
        s += '~~{}~~'.format(opt[i][j])
      else:
        s += opt[i][j]
    s = s.replace(ans[i], '**{}**'.format(ans[i])) + '\n'
    await channel.send(s)
  s = '\_'*30 + '\n\n'
  s += 'correct: {}\nwrong: {}'.format(correct, Q-correct)
  await channel.send(s)

class Exam(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(
      help = '''
        time for exam~
        ''',
      #brief = "Print satellite cloud chart"
  )
  async def exam(self, ctx):
    thread = await ctx.message.create_thread(name='EXAM!')
    channel = self.bot.get_channel(thread.id)
    await channel.trigger_typing()
    quiz_data = await print_quiz_data(channel)
    playerId = ctx.author.id
    while True:
      choose = await self.bot.wait_for('message', timeout=200.0)
      if choose.channel == channel and choose.author.id == playerId:
        try:
          fileName = quiz_data[int(choose.content)-1]
          break
        except Exception as e:
          print(e)
    voc, sen = get_data(fileName)
    global Q
    await channel.send('請輸入遊玩題數，需小於等於{}題'.format(str(len(voc))))
    while True:
      n = await self.bot.wait_for('message', timeout=300.0)
      print(n.channel, channel)
      if n.channel == channel and n.author.id == playerId and (n.content > '0' and n.content < str(len(voc))):
        Q = int(n.content)
        break
      else:
        await n.delete()
    hollow = hollow_sentence(voc, sen, fileName)
    ans, que, opt, ansNum = generate_question(voc, hollow)
    sel = await print_question(que, opt, channel, self.bot, playerId)
    await review(ans, ansNum, sel, opt, que, channel)
    await channel.send('\n輸入**exit**離開')
    while True:
      try:
        exit = await self.bot.wait_for('message', timeout=1000.0)
        if choose.channel == channel and choose.author.id == playerId:
          if exit.content.lowercase == 'exit':
            await channel.delete()
            break
      except:
        await channel.delete()
        break
      

def setup(bot):
    bot.add_cog(Exam(bot))