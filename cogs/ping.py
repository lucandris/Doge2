import discord
from discord.ext import commands
import funcs

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["delay"])
    async def ping(self, ctx):
        user = ctx.author
        await funcs.open_account(user)
        await ctx.send(f':ping_pong: Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(ping(bot))