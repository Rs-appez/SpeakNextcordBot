from nextcord.ext import commands
from nextcord import slash_command
from speakNextcordBot.modal.speakModal import SpeakModal
from speakNextcordBot.modal.updateModal import UpdateModal
from speakNextcordBot.modal.replyModal import ReplyModal

from nextcord import (
    InteractionContextType,
    SlashOption,
    Interaction as NextcordInteraction,
)


class Interaction(commands.Cog):
    """Message command for admin"""

    vote_emoji = {
        1: "1️⃣",
        2: "2️⃣",
        3: "3️⃣",
        4: "4️⃣",
        5: "5️⃣",
        6: "6️⃣",
        7: "7️⃣",
        8: "8️⃣",
        9: "9️⃣",
        10: "🔟",
    }

    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        description="🎙️",
        contexts=[InteractionContextType.guild],
        default_member_permissions=0,
    )
    async def speak(
        self,
        interaction: NextcordInteraction,
        message: str = SlashOption(
            description="Message to send",
            required=False,
            default=None,
        ),
    ):
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

    @slash_command(
        description="🔧🎙️",
        contexts=[InteractionContextType.guild],
        default_member_permissions=0,
    )
    async def update_speak(
        self,
        interaction: NextcordInteraction,
        message_id: str = SlashOption(
            description="Message ID to update",
        ),
    ):
        """Update a message in a channel"""
        try:
            message = await interaction.channel.fetch_message(message_id)
            await interaction.response.send_modal(UpdateModal(self.bot, message))
        except Exception as e:
            await interaction.response.send_message(f"Error : {e}", ephemeral=True)

    @slash_command(
        description="💬",
        contexts=[InteractionContextType.guild],
        default_member_permissions=0,
    )
    async def reply(
        self,
        interaction: NextcordInteraction,
        message_id: str = SlashOption(description="Message ID to reply to"),
    ):
        """Reply to a message in a channel"""
        try:
            message = await interaction.channel.fetch_message(message_id)
            await interaction.response.send_modal(ReplyModal(message))
        except Exception as e:
            await interaction.response.send_message(f"Error : {e}", ephemeral=True)

    @slash_command(
        description="Vote 🔢",
        contexts=[InteractionContextType.guild],
        default_member_permissions=0,
    )
    async def add_vote(
        self,
        interaction: NextcordInteraction,
        message_id: str = SlashOption(
            description="Message ID to add a vote to",
        ),
        number: int = SlashOption(
            description="Number of votes to add (1-10)",
            min_value=1,
            max_value=10,
        ),
    ):
        """Add a vote to a message in a channel"""
        if number < 1 or number > 10:
            await interaction.response.send_message(
                "Number must be between 1 and 10", ephemeral=True
            )
            return
        try:
            message = await interaction.channel.fetch_message(message_id)
            await interaction.response.defer(ephemeral=True, with_message=True)
            for i in range(1, number + 1):
                await message.add_reaction(self.vote_emoji.get(i))
            await interaction.followup.send("Vote added !", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Error : {e}", ephemeral=True)

    @slash_command(
        description="Remove votes",
        contexts=[InteractionContextType.guild],
        default_member_permissions=0,
    )
    async def remove_vote(
        self,
        interaction: NextcordInteraction,
        message_id: str = SlashOption(
            description="Message ID to remove votes from",
        ),
    ):
        """Remove all votes from a message in a channel"""
        try:
            message = await interaction.channel.fetch_message(message_id)
            await interaction.response.defer(ephemeral=True, with_message=True)
            for reaction in message.reactions:
                if reaction.emoji in self.vote_emoji.values():
                    await message.clear_reaction(reaction.emoji)
            await interaction.followup.send("Votes removed !", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Error : {e}", ephemeral=True)


def setup(bot):
    bot.add_cog(Interaction(bot))
