#!venv/bin/python3
from nextcord.ext import commands
import config
from interaction_discord_bot.init_cog import init_cog

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready")


init_cog(bot)

bot.run(config.TOKEN)
