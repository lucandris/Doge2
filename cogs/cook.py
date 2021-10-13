import discord
from discord.ext import commands
import funcs
import random

class cook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def cook(self, ctx):
      user = ctx.author
      await funcs.open_account(user)

      product = random.randint(1, 2)

      if product == 1:
        cookies_amt = random.randint(1, 5)
        await ctx.send(f"You made {cookies_amt} cookie(s)!")
        await funcs.update_inventory(user,change = cookies_amt,target = "cookie")

      elif product == 2:
        pies_amt = random.randint(1, 2)
        await ctx.send(f"You made {pies_amt} pie(s)!")
        await funcs.update_inventory(user,change = pies_amt,target = "pie")

    @cook.error
    async def cook_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You need to wait for the oven to reheat. The default cooldown for this coomand is `45s`.")

def setup(bot):
  bot.add_cog(cook(bot))