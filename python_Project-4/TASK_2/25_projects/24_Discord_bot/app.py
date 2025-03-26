import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # For message events
intents.guilds = True    # For server info

bot = commands.Bot(
    command_prefix='!',
    intents=intents  # Use modified intents
)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

bot.run("YOUR_TOKEN_HERE")  # Replace with your token