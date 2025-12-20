import discord
from discord.ext import commands
from subprocess import check_output,STDOUT,CalledProcessError,TimeoutExpired
from re import compile,sub

class System(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def system(self, ctx, *, cmd):
		"Run GNU/Linux system programs (in a restrictive sandbox)."
		# Strip out bad characters.
		clean_cmd = sub(r"[ ;&|]", "", cmd)
		# Do nothing if the user command is empty.
		if not clean_cmd:
			await ctx.send("Sorry, the command is malformed and could not be processed.")
			return
		# Define the base minsandbox command.
		bwrap_command = ["bash", "plugins/DanielMYT/modmail-plugins/system-master/minsandbox.sh"]
		# Set up the user command by splitting into an array.
		user_command = cmd.split(" ")
		# Combine base command and user command for the full command.
		full_command = bwrap_command + user_command
		# Run the thing. Inform if the command times out.
		output = ""
		try:
			output = check_output(full_command, stderr=STDOUT, timeout=30, text=True)
		except TimeoutExpired as e:
			output = e.output
			await ctx.send("WARNING: The command timed out.")
		except CalledProcessError as e:
			output = e.output
			await ctx.send("WARNING: The command exited with an unsuccessful exit code.")
		# Strip out ANSI terminal characters from any output.
		clean_output = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', output)
		# Send the output.
		if not clean_output:
			# No output. Display a message.
			await ctx.send("The command produced no output.")
		elif len(clean_output) > 2000:
			# Too long output. Attach as a file.
			outfile = open("SystemOutput.txt", "w")
			outfile.write(clean_output)
			outfile.close()
			await ctx.send("The command produced too much output. I have attached the output as a text document.")
			await ctx.send(file=discord.File(f"SystemOutput.txt"))
		else:
			await ctx.send("```\n" + clean_output + "\n```")

async def setup(bot):
	await bot.add_cog(System(bot))
