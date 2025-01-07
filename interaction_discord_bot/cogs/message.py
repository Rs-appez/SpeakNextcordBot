from nextcord.ext import commands
from nextcord import slash_command
from interaction_discord_bot.modal.speakModal import SpeakModal
from interaction_discord_bot.modal.updateModal import UpdateModal

from nextcord import InteractionContextType
class Interaction(commands.Cog):
    """Message command for admin"""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="🎙️",contexts=[InteractionContextType.guild], default_member_permissions=0)
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

    @slash_command(description="🔧🎙️", contexts=[InteractionContextType.guild], default_member_permissions=0)
    async def update_speak(self, interaction, message_id: str):
        """Update a message in a channel"""
        try:
            message = await interaction.channel.fetch_message(message_id)
            await interaction.response.send_modal(
                UpdateModal(self.bot, message)
            )
        except Exception as e:
            await interaction.response.send_message(f"Error : {e}", ephemeral=True)
        
def setup(bot):
    bot.add_cog(Interaction(bot))