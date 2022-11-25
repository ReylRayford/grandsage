from dictionnary import quotes
from discord.ext import commands
import discord
from random import randint
from info import token

client = commands.Bot(command_prefix='=', help_command=None)


@client.event
async def on_ready():
    print('Le bot est démarré en tant que {0.user}'.format(client))
    print('==========================')


# Répond "Salut !"
@client.command()
async def hello(ctx):
    await ctx.send(f"Hello {discord.Member}")


# Envoie une citation du dictionnaire aléatoire dans le channel
@client.command(pass_context=True)
async def citation(ctx):
    await ctx.message.delete()
    await ctx.send(f'Un grand sage a dit un jour : ***"{quotes[randint(0, len(quotes)-1)]}"***.')
    print("Citation envoyée.")


# Permet d'afficher le dictionnaire de citations
@client.command()
async def show_quotes(ctx):
    file = open("dictionnary.py", "r")
    await ctx.send(file.read())


# Permet d'ajouter une citation au dictionnaire
@client.command()
async def add_quote(ctx, text: str):
    quotes.append(text)
    file = open("dictionnary.py", 'w')
    file.write(f"quotes = {quotes}")
    await ctx.send("Votre citation a été ajoutée au dictionnaire.")
    print("Citation ajoutée !")


# Permet de supprimer une citation du dictionnaire
@client.command()
async def del_quote(ctx, index: int):
    quotes.pop(index-1)
    file = open("dictionnary.py", 'w')
    file.write(f"quotes = {quotes}")
    await ctx.send("Votre citation a bien été enlevé")
    print("Citation supprimé !")


client.run(token)
