import discord
from discord.ext import commands
from subprocess import check_output

class Neofetch(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def neofetch(self, ctx):
		"Neofetch plugin by DanielMYT. Neofetch program taken from Hyfetch project."
		output = check_output(["bash", "plugins/DanielMYT/modmail-plugins/neofetch-master/neofetch"], stderr=subprocess.STDOUT, timeout=10, text=True)
		await ctx.send("```\n" + output + "\n```")

async def setup(bot):
	await bot.add_cog(Neofetch(bot))
