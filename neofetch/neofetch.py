import discord
from discord.ext import commands
from os import popen

cmd = "/bin/bash plugins/DanielMYT/modmail-plugins/neofetch-master/neofetch 2>&1"

class Neofetch(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def neofetch(self, ctx):
		"Neofetch for Modmail! Neofetch program taken from Hyfetch project."
		stream = popen(cmd)
		output = stream.read()
		await ctx.send(output)

async def setup(bot):
	await bot.add_cog(Neofetch(bot))
