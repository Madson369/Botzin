import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cog is on.')


    @commands.command()
    async def cogtest(self,ctx):
        await ctx.send('pego')

        

def setup(client):
    client.add_cog(Example(client))



    









