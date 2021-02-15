import discord
import time
from time import sleep
from discord.ext import commands


class barulhos(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('barulhos is on.')

    path = 'C:/Users/Madso/Desktop/Bot/trovao.mp3'

    @commands.command(aliases=['Trovao', 'TROVAO'])
    async def trovao(self, ctx, *, text=None):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/trovao.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 10
        sleep(7)
        await vc.disconnect()

    @commands.command(aliases=['Respect', 'RESPECT'])
    async def respect(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/respect.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        sleep(1.2)
        await vc.disconnect()

    @commands.command(aliases=['Bababui', 'BABABUI'])
    async def bababui(self, ctx, *, text=None):

        vc = ctx.voice_client

        if discord.Member.voice == False:
            await ctx.send("tem que ta conectado a canal de voz animal")
            pass

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/bababui.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 3
        sleep(1.2)
        await vc.disconnect()

    @commands.command(aliases=['Barroso', 'BARROSO'])
    async def barroso(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/barroso.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        sleep(40)
        await vc.disconnect()

    @commands.command(aliases=['Barroso1', 'BARROSO1'])
    async def barroso1(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/barroso.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        sleep(3)
        await vc.disconnect()

    @commands.command(aliases=['Miau', 'MIAU'])
    async def miau(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/miau.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 5
        sleep(6)
        await vc.disconnect()

    @commands.command(aliases=['Almeda', 'ALMEDA'])
    async def almeda(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/almeda.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(6)
        await vc.disconnect()

    @commands.command(aliases=['Calaboca', 'CALABOCA'])
    async def calaboca(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/calaboca.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 4
        sleep(2)
        await vc.disconnect()

    @commands.command(aliases=['Bonk', 'BONK'])
    async def bonk(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/bonk.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        await ctx.channel.send('https://tenor.com/view/bonk-meme-dog-doge-gif-14889944')

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 4
        sleep(2)
        await vc.disconnect()

    @commands.command(aliases=['Miau1', 'MIAU1'])
    async def miau1(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/miau1.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(2)
        await vc.disconnect()

    @commands.command(aliases=['Nao', 'NAO'])
    async def nao(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/nao.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(2)
        await vc.disconnect()

    @commands.command(aliases=['Kpop', 'KPOP'])
    async def kpop(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/kpop.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(7)
        await vc.disconnect()

    @commands.command(aliases=['Uepa', 'UEPA'])
    async def uepa(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/uepa.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        sleep(2)
        await vc.disconnect()

    @commands.command(aliases=['Queisso', 'QUEISSO'])
    async def queisso(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/queisso.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        sleep(3)
        await vc.disconnect()

    @commands.command(aliases=['Pau', 'PAU'])
    async def pau(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/pau.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(6)
        await vc.disconnect()

    @commands.command(aliases=['Cavalo', 'CAVALO'])
    async def cavalo(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/cavalo.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(3)
        await vc.disconnect()

    @commands.command(aliases=['Parapara', 'PARAPARA'])
    async def parapara(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/parapara.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        sleep(5)
        await vc.disconnect()

    @commands.command(aliases=['QUEBRAS', 'Quebras'])
    async def quebras(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/quebras.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(5)
        await vc.disconnect()

    @commands.command(aliases=['PORTA', 'Porta'])
    async def porta(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/porta.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(30)
        await vc.disconnect()


    @commands.command(aliases=['PRIMEIRA', 'Primeira'])
    async def primeira(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/primeira.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(3)
        await vc.disconnect()



    @commands.command(aliases=['MACACO', 'Macaco'])
    async def macaco(self, ctx, *, text=None):

        channel = ctx.message.author.voice.channel
        await channel.connect()

        vc = ctx.voice_client  # We use it more then once, so make it an easy variable

        vc.play(discord.FFmpegPCMAudio('C:/Users/Madso/Desktop/Bot/macaco.mp3'),
                after=lambda e: print(f"Finished playing: {e}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 2
        sleep(5)
        await vc.disconnect()      
           

def setup(client):
    client.add_cog(barulhos(client))
