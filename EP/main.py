from discord.ext import commands

bot = commands.Bot(command_prefix=';')

with open("info/token.txt", 'r') as f:
  token = f.read().strip("\n")

with open("info/extensions.txt", 'r') as f:
  for extension in f:
    bot.load_extension(extension.strip('\n')) 

@bot.event
async def on_ready():
  print("Ready!")

@bot.event
async def on_message(message):
  if message.author.id == bot.user.id:
    return
  await bot.process_commands(message)


bot.run(token)