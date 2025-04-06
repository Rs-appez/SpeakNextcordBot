from nextcord.ui import Modal, TextInput
from nextcord import TextInputStyle


class ReplyModal(Modal):
    def __init__(self, replied):
        super().__init__(f"Reply to {replied.author.name}")
        self.replied = replied

        self.reply = TextInput(
            "Reply",
            placeholder="Reply",
            required=True,
            style=TextInputStyle.paragraph,
        )

        self.add_item(self.reply)

    async def callback(self, interaction):
        try:
            await self.replied.reply(self.reply.value)
            return await interaction.response.send_message(
                "I replied", ephemeral=True
            )
        except Exception as e:
            return await interaction.response.send_message(
                f"Error : {e}", ephemeral=True
            )
