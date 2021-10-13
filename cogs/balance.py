import discord
from discord.ext import commands
import funcs

class balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["bal"])
    async def balance(self, ctx, mention: discord.User = None):
      user = ctx.author
      await funcs.open_account(user)
      users = await funcs.get_inventory_data()

      if mention == None:
        wallet_amt = await funcs.format_commas(users[str(user.id)]["wallet"])
        bank_amt = await funcs.format_commas(users[str(user.id)]["bank"])
        bankmax_amt = await funcs.format_commas(users[str(user.id)]["bankmax"])

        em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.from_rgb(47, 49, 54), description = f"**Wallet:** {wallet_amt} coins \n**Bank:** {bank_amt} / {bankmax_amt} coins")
        await ctx.send(embed = em)

      else:
        await funcs.open_account(mention)
        
        wallet_amt = await funcs.format_commas(users[str(mention.id)]["wallet"])
        bank_amt = await funcs.format_commas(users[str(mention.id)]["bank"])
        bankmax_amt = await funcs.format_commas(users[str(mention.id)]["bankmax"])

        em = discord.Embed(title = f"{mention}'s balance",color = discord.Color.from_rgb(47, 49, 54), description = f"**Wallet:** {wallet_amt} coins \n**Bank:** {bank_amt} / {bankmax_amt} coins")
        await ctx.send(embed=em)

def setup(bot):
  bot.add_cog(balance(bot))