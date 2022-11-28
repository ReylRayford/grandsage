import discord
from discord import app_commands
from dictionnary import quotes
from discord import FFmpegPCMAudio
from random import randint
from info import token
import youtube_dl
import os


class GrandSage(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'Le bot est démarré en tant que {self.user}')
        print('==========================')


client = GrandSage()
tree = app_commands.CommandTree(client)


# =====================================================================
#                           Partie citation
# =====================================================================


# Envoie une citation du dictionnaire aléatoire dans le channel
@tree.command(name="citation", description="Envoie une citation aléatoire")
async def citation(interaction: discord.Interaction):
    await interaction.response.send_message(f'Un grand sage a dit un jour : ***"{quotes[randint(0, len(quotes) - 1)]}"***.')
    print("Citation envoyée.")


# Permet d'afficher le dictionnaire de citations
@tree.command(name="show_quotes", description="Affiche la liste de citations")
async def show_quotes(interaction: discord.Interaction):
    file = open("dictionnary.py", "r")
    await interaction.response.send_message(file.read())


# Permet d'ajouter une citation au dictionnaire
@tree.command(name="add_quote", description="Ajoute la citation marquée dans la liste de citations")
async def add_quote(interaction: discord.Interaction, text: str):
    quotes.append(text)
    file = open("dictionnary.py", 'w')
    file.write(f"quotes = {quotes}")
    await interaction.response.send_message("Votre citation a été ajoutée au dictionnaire.")
    print("Citation ajoutée !")


# Permet de supprimer une citation du dictionnaire
@tree.command(name="del_quote",
             description="Supprime la citation se trouvant à la position inscrite dans la liste de citations")
async def del_quote(interaction: discord.Interaction, index: int):
    quotes.pop(index - 1)
    file = open("dictionnary.py", 'w')
    file.write(f"quotes = {quotes}")
    await interaction.response.send_message("Votre citation a bien été enlevé")
    print("Citation supprimé !")


# =====================================================================
#                           Partie citation
# =====================================================================


@tree.command(name="play", description="Permet de jouer la musique inscrite")



client.run(token)
