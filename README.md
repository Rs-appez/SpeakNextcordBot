# SpeakNextcordBot
![Version](https://img.shields.io/pypi/v/SpeakNextcordBot?color=blue) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/SpeakNextcordBot)

A python package for adding speak interaction slash commands to a [Nextcord](https://github.com/nextcord/nextcord) bot

## Key Features

**The package provides 5 features :**

  * ```/speak``` to make your bot send message in a channel
  * ```/update_speak``` to edit a message send by your bot
  * ```/reply``` to make your bot reply to a message

  * ```/add_vote``` to add a number of vote reaction
  * ```/remove_vote``` to remove all votes reactions

## Usage

*By default all slash commands are only available for server admin*

* ### The speak command
     Enter your message in the ```message``` parameter :  
     ![image](https://github.com/user-attachments/assets/9966647d-a425-4110-a0e3-1e26f7cc779c)  
     If no message is provided, a modal is open to enter your message *(recommended for formated messages)*  
     *You can also edit the channel id, if you want send your message in another channel (default is the current channel)*  
     ![image](https://github.com/user-attachments/assets/c5270ca0-63d2-4e80-b4c5-d47c76c19960)

* ### The update_speak command
     Enter the ID of your bot message you want to edit :  
     ![image](https://github.com/user-attachments/assets/657f892d-c14f-48d5-b034-77cff1045543)  
     A modal will open, allowing you to edit the message.

* ### The reply command
     Enter the ID of the message you want your bot to reply :    
     ![image](https://github.com/user-attachments/assets/1da546a0-aac1-4636-a351-5b5f4b5eaaef)  
     A modal will open, allowing you to enter the reply message.

* ### The add_vote command
     Enter the ID of the message you want to add reaction votes to, and the number of reactions you want (between 1-10)  
    ![image](https://github.com/user-attachments/assets/1e8f4676-337d-4e43-93f5-ee97675e2ad7)

* ### The remove_vote
     Enter the ID of the message you want to remove all reaction votes to  
     ![image](https://github.com/user-attachments/assets/f5c972be-c062-4f76-a687-12b930903be2)

## Requirements

* Python 3.12 or higher is required
* [Nextcord](https://github.com/nextcord/nextcord) 3.0.1 or higher is required

## Installation

Using pip :

```
pip install SpeakNextcordBot
```

## Setup
**Simple setup example**  
Call init_cog() with your bot in argument :

```py
from nextcord.ext import commands
from speakNextcordBot.init_cog import init_cog

bot = commands.Bot()

init_cog(bot)

bot.run("YOUR_TOKEN")
```
