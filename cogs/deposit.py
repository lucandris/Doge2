import discord
from discord.ext import commands
import funcs

class deposit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["dep"])
    async def deposit(self, ctx, amount = 0):
      user = ctx.author
      await funcs.open_account(user)
      users = await funcs.get_inventory_data()

      wallet_amt = users[str(user.id)]["wallet"]
      bank_amt = users[str(user.id)]["bank"]
      bankmax_amt = users[str(user.id)]["bankmax"]

      if amount <= wallet_amt:
        total = amount + bank_amt

        if total <= bankmax_amt:
          await funcs.update_inventory(user,change = amount, target = "wallet", add = False)
          await funcs.update_inventory(user,change = amount,target = "bank")

          await ctx.send(f"{ctx.author.mention}, you successfully deposited {await funcs.format_commas(amount)} coins!")
          
        else:
          await ctx.send(f"{ctx.author.mention}, your bank is too full too deposit that much!")
        
      else:
        await ctx.send(f"{ctx.author.mention}, you don't have enough coins to deposit that much!")

def setup(bot):
  bot.add_cog(deposit(bot))
