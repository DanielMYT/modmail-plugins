import discord
from discord.ext import commands
from datetime import datetime
from dateutil import tz

class Time(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def time(self, ctx, *, timezone):
		"""Time command by DanielMYT - get the current date and time in any timezone."""

		output = ""

		try:
			zone = tz.gettz(timezone)

			if not zone:
				zone = tz.tzoffset(None, int(timezone[:3]) * 3600 + int(timezone[0] + timezone[3:]) * 60)

			output = ":clock4: The current date and time in " + timezone + " is " + datetime.now(zone).strftime("%Y-%m-%d %H:%M:%S %Z (%z)") + "."

		except Exception:
			output = ":x: I was unable to determine the current date time in " + timezone + ".\n\n:bulb: Recognized timezone formats include common abreviations (`UTC`, `GMT`, `EST`, `CET`), POSIX timezones (`America/New_York`, `Europe/London`, `Etc/UTC`), and UTC offsets (`+0000`, `+0100`, `-0500`)."

		await ctx.send(output)

async def setup(bot):
	await bot.add_cog(Time(bot))
