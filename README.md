# Interaction Discord Bot
![Version](https://img.shields.io/pypi/v/interaction_discord_bot?color=blue) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/interaction_discord_bot)

A python package for adding speak interaction slash command to a discord bot ( who use [Nextcord](https://github.com/nextcord/nextcord) )

## Key Features

**The package provides 3 features :**

  * ```/speak``` to make your bot send message in a channel
  * ```/update_speak``` to edit a message send by your bot
  * ```/reply``` to make your bot reply to a message

## Usage

* ### The speak command
     Enter your message in the ```message``` parameter :  
     ![image](https://github.com/user-attachments/assets/9966647d-a425-4110-a0e3-1e26f7cc779c)  
     If no message is provided, a modal is open to enter your message *(recommended for formated messages)*  
     *You can also edit the channel id, if you want send your message in another channel (default is the current channel)*  
     ![image](https://github.com/user-attachments/assets/c5270ca0-63d2-4e80-b4c5-d47c76c19960)

* ### The update_speak command
     Enter the id of your bot message you want to edit :  
     ![image](https://github.com/user-attachments/assets/657f892d-c14f-48d5-b034-77cff1045543)  
     A modal will open, allowing you to edit the message.

* ### The reply command
     Enter the id of the message you want your bot to reply :    
     ![image](https://github.com/user-attachments/assets/1da546a0-aac1-4636-a351-5b5f4b5eaaef)  
     A modal will open, allowing you to enter the reply message.

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
