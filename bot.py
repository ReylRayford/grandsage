import discord
from dictionnary import quotes
from discord.ext import commands
from random import randint
from info import token
from discord_slash import SlashCommand

client = commands.Bot(command_prefix='=', help_command=None)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print('Le bot est démarré en tant que {0.user}'.format(client))
    print('==========================')


# Répond "Salut !"
@client.command()
async def hello(ctx):
    await ctx.send(f"Hello {discord.Member}")


# Envoie une citation du dictionnaire aléatoire dans le channel
@slash.slash(name="citation", description="Envoie une citation aléatoire")
async def citation(ctx):
    await ctx.message.delete()
    await ctx.send(f'Un grand sage a dit un jour : ***"{quotes[randint(0, len(quotes)-1)]}"***.')
    print("Citation envoyée.")


# Permet d'afficher le dictionnaire de citations
@slash.slash(name="show_quotes", description="Affiche la liste de citations")
async def show_quotes(ctx):
    await ctx.message.delete()
    file = open("dictionnary.py", "r")
    await ctx.send(file.read())


# Permet d'ajouter une citation au dictionnaire
@slash.slash(name="add_quote", description="Ajoute la citation marquée dans la liste de citations")
async def add_quote(ctx, text: str):
    quotes.append(text)
    await ctx.message.delete()
    file = open("dictionnary.py", 'w')
    file.write(f"quotes = {quotes}")
    await ctx.send("Votre citation a été ajoutée au dictionnaire.")
    print("Citation ajoutée !")


# Permet de supprimer une citation du dictionnaire
@slash.slash(name="del_quote",
             description="Supprime la citation se trouvant à la position inscrite dans la liste de citations")
async def del_quote(ctx, index: int):
    quotes.pop(index-1)
    await ctx.message.delete()
    file = open("dictionnary.py", 'w')
    file.write(f"quotes = {quotes}")
    await ctx.send("Votre citation a bien été enlevé")
    print("Citation supprimé !")


client.run(token)
