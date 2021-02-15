import discord
import time
import random
from time import sleep
from aiohttp import request
from discord.ext import commands
from itertools import cycle


class animais(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('animais is on.')

    @commands.command(name="fact")
    async def fact(self, ctx):  # async def fact(ctx,animal:str):
        URL = "https://some-random-api.ml/facts/dog"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                await ctx.send(data["fact"])

            else:
                await ctx.send(f"API RETURNED A {response.status} status.")

    @commands.command(name="meme")
    async def meme(self, ctx):  # async def fact(ctx,animal:str):
        URL = "https://some-random-api.ml/meme"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                await ctx.send(data["image"])

            else:
                await ctx.send(f"API RETURNED A {response.status} status.")

    @commands.command(name="pat")
    async def pat(self, ctx):
        URL = "https://some-random-api.ml/animu/pat"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                await ctx.send(data["link"])

            else:
                await ctx.send(f"API RETURNED A {response.status} status.")

    @commands.command(name="fox")
    async def fox(self, ctx):
        URL = "https://some-random-api.ml/img/fox"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                await ctx.send(data["link"])

            else:
                await ctx.send(f"API RETURNED A {response.status} status.")

    @commands.command(name="panda")
    async def panda(self, ctx):
        URL = random.choice(['https://some-random-api.ml/img/red_panda', 'https://some-random-api.ml/img/panda']) 
        
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                await ctx.send(data["link"])

            else:
                await ctx.send(f"API RETURNED A {response.status} status.")



                


def setup(client):
    client.add_cog(animais(client))
