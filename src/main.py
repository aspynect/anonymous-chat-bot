import discord
from discord import app_commands
from os import getenv

DISCORD_TOKEN = getenv("DISCORD_TOKEN", "NO TOKEN PROVIDED")

client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)


@tree.command(name = "anon", description = "Send a message anonymously")
@app_commands.describe(input="Message")
async def anon(interaction: discord.Interaction, input: str):
    await interaction.channel.send(input)
    await interaction.response.send_message("Sent!", ephemeral = True)

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@tree.command(name="sync",description="sync")
async def sync(interaction: discord.Interaction):
    if interaction.user.id != 439441145466978305:
        await interaction.response.send_message("u arent aspyn", ephemeral = True)
        return
    await tree.sync()
    await interaction.response.send_message("sunk!", ephemeral = True)
    print("Sunk!")

client.run(DISCORD_TOKEN)