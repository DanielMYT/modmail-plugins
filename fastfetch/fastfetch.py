import discord
from discord.ext import commands
from subprocess import check_output,STDOUT
from re import compile

class Fastfetch(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def fastfetch(self, ctx):
		"Fastfetch plugin by DanielMYT."
		output = check_output(["bash", "plugins/DanielMYT/modmail-plugins/fastfetch-master/fastfetch"], stderr=STDOUT, timeout=10, text=True)
		clean_output = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', output)
		await ctx.send("```\n" + clean_output + "\n```")

async def setup(bot):
	await bot.add_cog(Fastfetch(bot))
