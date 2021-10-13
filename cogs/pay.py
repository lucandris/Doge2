import discord
from discord.ext import commands
import funcs

class pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pay(self, ctx, mention: discord.User, amount = 0):
      user = ctx.author
      await funcs.open_account(user)
      await funcs.open_account(mention)
      users = await funcs.get_inventory_data()

      if amount <= users[str(user.id)]["wallet"]:
        await funcs.update_inventory(user,change = amount,target = "wallet", add = False)
        await funcs.update_inventory(mention,change = amount,target = "wallet")

        await ctx.send(f"{ctx.author.mention}, you gave {total} coins to {mention}")
        
      else:
        await ctx.send("You don't have enough money in your wallet to send that much!")
    
    @pay.error
    async def pay_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You're going on a giving rampage. The default cooldown for this command is `5s`.")

def setup(bot):
  bot.add_cog(pay(bot))