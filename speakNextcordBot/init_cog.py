from speakNextcordBot.cogs.message import Interaction


def init_cog(bot):
    bot.add_cog(Interaction(bot))

