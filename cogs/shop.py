import discord
from discord.ext import commands
import funcs
import random

class shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx, category=None):
      user = ctx.author
      await funcs.open_account(user)
      users = await funcs.get_inventory_data()

      if category == None:
        info = "To buy an item use: buy ID", "To get more info on an item use: shop ID"
        em = discord.Embed(title = "Shop", color = discord.Color.from_rgb(47, 49, 54), description = "<:DogeLaptop:896512998720544800> **Laptop** — [2,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `laptop` \n \n<:DogeGun:896512935688540170> **Gun** — [5,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `gun` \n \n<:DogeCoin:896512710500565043> **Doge Coin** — [500,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `coin` \n \n<:DogeMedal:896508910100414537> **Doge Medal** — [1,000,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `medal` \n \n<:DogeEgg:896514393427292241> **Egg** — [3 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `egg` \n \n<:DogeMilk:896514393628606474> **Milk** — [20 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `milk`", inline=False)
        em.set_footer(text=f"{random.choice(info)}")

        await ctx.send(embed = em)
        return

      if category == "medal":
        medal_amt = users[str(user.id)]["medal"]
        em = discord.Embed(title = f"Doge Medal ({medal_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Used to mega flex on poor players. That's it.")
        em.add_field(name="Value:", value="Buy: 1,000,000 coins \nSell: Not sellable")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/896394788289527818/896516047992127488/Untitled_design__2_-removebg-preview.png")

        await ctx.send(embed = em)
        return

      if category == "egg":
        egg_amt = users[str(user.id)]["egg"]
        em = discord.Embed(title = f"Egg ({egg_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Item obtained from farming.")
        em.add_field(name="Value:", value="Buy: Not buyable \nSell: 3 coins")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/896394788289527818/896515886666620958/9664-egg.png")

        await ctx.send(embed = em)
        return

      if category == "milk":
        milk_amt = users[str(user.id)]["milk"]
        em = discord.Embed(title = f"Milk Carton ({milk_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Item obtained from farming.")
        em.add_field(name="Value:", value="Buy: Not buyable \nSell: 20 coins")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/896394788289527818/896515883667714079/9629_milk.png")

        await ctx.send(embed = em)
        return

      if category == "coin":
        coin_amt = users[str(user.id)]["coin"]
        em = discord.Embed(title = f"Doge Coin ({coin_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Used to flex on poor players. That's it.")
        em.add_field(name="Value:", value="Buy: 500,000 coins \nSell: Not sellable")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/896394788289527818/896516050613567528/Untitled_design__3_-removebg-preview.png")

        await ctx.send(embed = em)
        return

      if category == "laptop":
        laptop_amt = users[str(user.id)]["laptop"]
        em = discord.Embed(title = f"Laptop ({laptop_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Allows you to postmemes on reddit for coins. ```+postmemes```")
        em.add_field(name="Value:", value="Buy: 2000 coins \nSell: 1000 coins")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/896394788289527818/896517143447863336/1447_laptop.png")

        await ctx.send(embed = em)
        return

      if category == "gun":
        gun_amt = users[str(user.id)]["gun"]
        em = discord.Embed(title = f"Gun ({gun_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Allows you to rob other players of their wallets. ```+rob MENTION```")
        em.add_field(name="Value:", value="Buy: 5000 coins \nSell: 2500")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/896394788289527818/896516155248877578/1426_pistol.png")

        await ctx.send(embed = em)
        return

def setup(bot):
    bot.add_cog(shop(bot))