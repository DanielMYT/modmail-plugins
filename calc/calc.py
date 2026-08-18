import discord
from discord.ext import commands
from subprocess import check_output,STDOUT
from re import compile

class Calc(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.command()
        async def calc(self, ctx, *, expression):
                "Fast and accurate calculator plugin by DanielMYT using bc."
                try:
                        output = check_output(["bash", "plugins/DanielMYT/modmail-plugins/calc-master/bc.sh", expression], stderr=STDOUT, timeout=3, text=True)
                except:
                        output = "Sorry, calculations containing non-ASCII characters cannot be processed."
                plain_output = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', output)
                if len(plain_output) > 2000:
                        plain_output = "Please specify a lower precision. Discord can't handle this!"
                await ctx.send(plain_output)

async def setup(bot):
        await bot.add_cog(Calc(bot))
