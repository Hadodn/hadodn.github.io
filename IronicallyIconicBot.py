import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot has started")

@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)}ms")


@client.command(aliases=['praise','helix'])
async def helix(ctx):
    await ctx.send("!ping")











@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has been removed the server.')


client.run('Njg2OTU5NzU2ODMzMDYyOTgz.Xmez1Q.QoJA8m6t2NAqRLEMKLeUsVFj3Ms')
