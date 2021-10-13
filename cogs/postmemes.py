import discord
from discord.ext import commands
import funcs
import random

class postmemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["pm"])
    @commands.cooldown(1, 35, commands.BucketType.user)
    async def postmemes(self, ctx):
      user = ctx.author
      await funcs.open_account(user)
      users = await funcs.get_inventory_data()

      multi_amt = users[str(user.id)]["multi"]
      amount = random.randint(1, 100)
      amount = amount * multi_amt

      laptopstatus = users[str(user.id)]["laptop"]
      
      event = random.randint(1, 20)

      if laptopstatus >= 1:
        if event == 20:
          await ctx.send("Your meme was so terrible your computer broke!")
          await funcs.update_inventory(user,change = 1,target = "laptop", add = False)
        
        else:
          earnings = await funcs.format_commas(amount)
          await ctx.send(f"You posted a meme and earned {earnings} coin(s) from the ads")

          await funcs.update_inventory(user,change = amount,target = "wallet")

        bankupgrade = 10
        await funcs.update_inventory(user,change = bankupgrade,target = "bankmax")
        
      else: 
        await ctx.send("You need a laptop to post memes, go buy one from the shop.")
    
    @postmemes.error
    async def postmemes_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You're being rate limited by Reddit! The default cooldown for this command is `35s`.")

def setup(bot):
  bot.add_cog(postmemes(bot))