import discord
from discord.ext import commands
from subprocess import check_output,STDOUT

class Fastfetch(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def fastfetch(self, ctx):
		"Fastfetch plugin by DanielMYT."
		output = check_output(["bash", "plugins/DanielMYT/modmail-plugins/fastfetch-master/fastfetch"], stderr=STDOUT, timeout=10, text=True)
		await ctx.send("```\n" + output + "\n```")

async def setup(bot):
	await bot.add_cog(Fastfetch(bot))
