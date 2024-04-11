from nextcord.ext import commands
from nextcord import slash_command
from nextcord.ui import UserSelect
from interaction_discord_bot.modal.speakModal import SpeakModal


class Interaction(commands.Cog):
    """Message command for admin"""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="🎙️", dm_permission=False, default_member_permissions=0)
    async def speak(self, interaction, message: str = None):
        """Send a message in a channel"""
        if message:
            try:
                await interaction.channel.send(message)
                await interaction.response.send_message(
                    "Message sent !", ephemeral=True
                )
            except Exception as e:
                await interaction.response.send_message(f"Error : {e}", ephemeral=True)
        else:
            await interaction.response.send_modal(
                SpeakModal(self.bot, interaction.channel.id)
            )

    # @slash_command(description="💭", default_member_permissions=0)
    # async def dm(self, interaction, user : UserSelect, message: str = None):
    #     """Send a message to a user"""
    #     if message:
    #         try:
    #             await interaction.channel.send(message)
    #             await interaction.response.send_message(
    #                 "Message sent !", ephemeral=True
    #             )
    #         except Exception as e:
    #             await interaction.response.send_message(f"Error : {e}", ephemeral=True)
    #     else:
    #         await interaction.response.send_modal(
    #             SpeakModal(self.bot, interaction.channel.id)
    #         )
        
def setup(bot):
    bot.add_cog(Interaction(bot))