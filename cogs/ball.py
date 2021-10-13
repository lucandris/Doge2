import discord
from discord.ext import commands
import funcs
import random

class ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["8ball"])
    async def ball(self, ctx):
      user = ctx.author
      await funcs.open_account(user)

      response = "Yes","No","Probably","Very doubtful", "I don't answer bitches", "Maybe?"

      await ctx.send(f"**:8ball: Answer:** {random.choice(response)}")

def setup(bot):
    bot.add_cog(ball(bot))