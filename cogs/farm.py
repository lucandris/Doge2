import discord
from discord.ext import commands
import funcs
import random

class farm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def farm(self, ctx):
      user = ctx.author
      await funcs.open_account(user)

      product = random.randint(1, 2)

      if product == 1:
        milk_amt = random.randint(1, 2)
        await ctx.send(f"You milked {milk_amt} cow(s)!")
        await funcs.update_inventory(user,change = milk_amt,target = "milk")

      elif product == 2:
        eggs_amt = random.randint(6, 12)
        await ctx.send(f"You took {eggs_amt} egg(s)!")
        await funcs.update_inventory(user,change = eggs_amt,target = "egg")     

    @farm.error
    async def farm_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("The farm is curently closed. The default cooldown for this coomand is `45s`.")

def setup(bot):
  bot.add_cog(farm(bot))