import discord
from discord.ext import commands
import funcs
import random

class beg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def beg(self, ctx):
      user = ctx.author
      await funcs.open_account(user)
      users = await funcs.get_inventory_data()

      multi_amt = users[str(user.id)]["multi"]

      amount = random.randint(1, 30)
      amount = amount * multi_amt

      earnings = await funcs.format_commas(amount)
      await ctx.send(f"Someone gave you {earnings} coins!")

      await funcs.update_inventory(user,change = amount,target = "wallet")

      bankupgrade = 10
      await funcs.update_inventory(user, change = bankupgrade, target = "bankmax")

    @beg.error
    async def beg_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Whoa there buddy, you gotta wait before asking someone more money. The default cooldown for this coomand is `45s`.")

def setup(bot):
  bot.add_cog(beg(bot))