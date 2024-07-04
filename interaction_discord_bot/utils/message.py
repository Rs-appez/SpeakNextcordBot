async def transfer_message(message, guild, channel_id):
    files = []
    for file in message.attachments:
        files.append(await file.to_file())
    await guild.get_channel(channel_id).send(content=f"**__{message.author} dm me __**: \n{message.content}",embeds=message.embeds,files=files)