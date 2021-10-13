import discord
from discord.ext import commands
import funcs

class withdraw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["with"])
    async def withdraw(self, ctx, amount = 0):
      user = ctx.author
      await funcs.open_account(user)
      users = await funcs.get_inventory_data()

      wallet_amt = users[str(user.id)]["wallet"]
      bank_amt = users[str(user.id)]["bank"]
      bankmax_amt = users[str(user.id)]["bankmax"]

      if amount <= bank_amt:
        total = amount + bank_amt

        await funcs.update_inventory(user,change = amount, target = "bank", add = False)
        await funcs.update_inventory(user,change = amount,target = "wallet")

        await ctx.send(f"{ctx.author.mention}, you successfully withdrew {await funcs.format_commas(amount)} coins!")
        
      else:
        await ctx.send(f"{ctx.author.mention}, you don't have enough coins in your bank to withdraw that much!")

def setup(bot):
  bot.add_cog(withdraw(bot))
