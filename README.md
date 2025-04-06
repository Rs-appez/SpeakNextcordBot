# Interaction Discord Bot
![Version](https://img.shields.io/pypi/v/interaction_discord_bot?color=blue) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/interaction_discord_bot)

A python package for adding basic interaction slash command to a discord bot ( who use [Nextcord](https://github.com/nextcord/nextcord) )

## Key Features

**The package provides 3 features :**

  * ```/speak``` to make your bot send message in a channel
  * ```/update_speak``` to edit a message send by your bot
  * ```/reply``` to make your bot reply to a message

## Requirements

* Python 3.12 or higher is required
* [Nextcord](https://github.com/nextcord/nextcord) 3.0.1 or higher is required

## Installation

Using pip :

```
pip install interaction-discord-bot
```

## Setup
**Simple example how to setup**
Call init_cog() with your bot in argument :

```py
from nextcord.ext import commands
from interaction_discord_bot.init_cog import init_cog

bot = commands.Bot()

init_cog(bot)

bot.run("YOUR_TOKEN")
```
