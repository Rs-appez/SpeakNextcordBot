from nextcord.ui import Modal, TextInput
from nextcord import TextInputStyle


class UpdateModal(Modal):
    def __init__(self, bot,message):
        super().__init__("Speak Update Modal")
        self.bot = bot
        self.old_message = message

        self.msg = TextInput(
            "Message",
            placeholder="Message",
            required=True,
            style=TextInputStyle.paragraph,
            default_value=message.content
        )

        self.add_item(self.msg)

    async def callback(self, interaction):
        try:
            await self.old_message.edit(content=self.msg.value)
            return await interaction.response.send_message(
                "Message updated !", ephemeral=True
            )
        except Exception as e:
            return await interaction.response.send_message(
                f"Error : {e}", ephemeral=True
            )
