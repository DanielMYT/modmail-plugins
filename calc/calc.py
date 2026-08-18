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
                output = check_output(["bash", "plugins/DanielMYT/modmail-plugins/calc/bc.sh", expression], stderr=STDOUT, timeout=3, text=True)
                plain_output = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', output)
                await ctx.send(plain_output)

async def setup(bot):
        await bot.add_cog(Calc(bot))
