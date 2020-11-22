import discord
import random
import time
import youtube_dl
from time import sleep
from discord.ext import commands

client = commands.Bot(command_prefix='.')



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Comendo cu de curioso'))
    print('bot is ready')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('leon'):
        await message.channel.send('opiniao errada!')

    if message.content.startswith('jair'):
        await message.channel.send('kkk gay!')

    if message.content.startswith('teu pai'):
        await message.channel.send('o teu!')

    if message.content.startswith('cara intrometido'):
        await message.channel.send('MEU PAU TEM VITILIGO')

    if message.content.startswith('cara intrometido'):
        await message.channel.send('MEU PAU TEM VITILIGO')

    if message.content.startswith('hmm'):
        await message.channel.send('https://tenor.com/view/funny-dance-happy-gif-13581492')   

    if message.content.startswith('POG'):
        await message.channel.send('https://tenor.com/view/rise-pieces-pog-is-alive-when-you-say-pog-pog-gif-17519305')      

    if message.content.startswith('agr vai'):
        await message.channel.send("<:zuki:719757832756658247>")


    await client.process_commands(message)


@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *,question):
    responses = ["claro porra.",
                 "sem duvida.",
                 "sem duvida confia.",
                 "Sim - pode apostar fdp.",
                 "vai.",
                 "provavelmente.",
                 "parece bom.",
                 "Sim.",
                 "Pergunta depois.",
                 "a meia noite te conto segredo gigatonico.",
                 "sla porra.",
                 "pergunte denovo mais tarde.",
                 "Não conta com isso.",
                 "eu acho que não.",
                 "minhas fontes dizem que não.",
                 "não parece bom.",
                 "duvidoso."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

players = { }


@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    vc = ctx.voice_client

    if not vc:
        await ctx.send("ta falando sozinho esquizofrenico")
        return

    await vc.disconnect()
    await ctx.send("flw puta")
    
@client.command()
async def trovao(ctx, *, text=None):
    
    channel = ctx.message.author.voice.channel
    await channel.connect()

    vc = ctx.voice_client # We use it more then once, so make it an easy variable


    vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/trovao.mp3'), after=lambda e: print(f"Finished playing: {e}"))

    # Lets set the volume to 1
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 1 
    sleep(7)
    await vc.disconnect()

       

client.run('Nzc5OTUwODk2ODU1MTIxOTMw.X7n_4A.27VUzlWi8RkaJ3QLhfdxmso5DV8')
