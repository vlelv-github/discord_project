import nextcord #pip install nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
TOKEN = 'PUT YOUR DISCORD TOKEN'  # Discord 토큰
prefix = "!"

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents=intents)

bot.run(TOKEN)