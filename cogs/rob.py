import discord
from discord.ext import commands
import funcs
import random

class rob(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def rob(self, ctx, mention: discord.User):
      user = ctx.author
      await funcs.open_account(user)
      users = await funcs.get_inventory_data()

      event = random.randint(1, 5)

      target_wallet_amount = users[str(mention.id)]["wallet"]
      wallet_amt = users[str(user.id)]["wallet"]
      target_premium = users[str(mention.id)]["premium"]
      payout = random.randint(1, target_wallet_amount)
      gun = users[str(user.id)]["gun"]

      if gun >= 1:
        if wallet_amt >= 2000:
          if target_wallet_amount >= 1000:
            if target_premium:
              await ctx.send("Looks like the person you tried to rob has a shield enabled.")

            else:
              if event < 5:
                await ctx.send(f"{ctx.author.mention}, you robbed {mention} for {payout} coins")

                await funcs.update_inventory(user, payout)
                await funcs.update_inventory(mention, payout, "wallet", add = False)

              elif event == 5:
                if payout > wallet_amt:
                  payout = wallet_amt
                  
                await ctx.send(f"You were caught trying to rob {mention} and had to pay a {funcs.format_commas(payout)} bail to leave prison")

                await funcs.update_inventory(mention, payout)
                await funcs.update_inventory(user, payout, "wallet", add = False)
          else:
            await ctx.send("The player you tried to rob has less than 1,000 coins in their wallet. Don't rob the poor.")
        else:
          await ctx.send("You need to have atleast 2,000 coins in your wallet to rob someone!")
      else:
        await ctx.send("You need a gun to be able to rob someone. Go buy one in the shop.")

    @rob.error
    async def rob_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Chill, the cops are going to get you if you go crazy. The default cooldown for this command is `10mins`.")

def setup(bot):
    bot.add_cog(rob(bot))
        



