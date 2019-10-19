import discord
import os
from keep_alive import keep_alive

from discord.ext import commands

client = commands.Bot(command_prefix='!')
roless = []
@client.event
async def on_ready():
	print("I'm in")
	print(client.user)



@client.command(pass_context=True)
async def teststuff(ctx, *role: discord.Role):
	print(ctx.message.guild.roles)
	print(role[0])
	print(ctx.message.guild.roles[1])
	if role[0] == ctx.message.guild.roles[1]:
		print("works")
		

@client.command(pass_context=True)
async def role(ctx, *role: discord.Role):
	"""
	Toggle whether or not you have a role. Usage: `!role DivinityPing`. Can take roles with spaces.
	:param role: Anything after "role"; should be the role name.
	"""
	if len(role) == 0:
		await ctx.send("You haven't specified a role! ")
	else:
		for i in range(len(role)):

		#	if role[i] not in ctx.message.guild.roles:
		#		await ctx.send("That role doesn't exist.")

			if role[i] not in ctx.message.author.roles:				
					await ctx.author.add_roles(role[i])
					await ctx.send("{} role has been added to {}.".format(role[i], ctx.message.author.mention))
				
			elif role[i] in ctx.message.author.roles:
				await ctx.author.remove_roles(role[i])
				await ctx.send("{} role has been removed from {}.".format(role[i], ctx.message.author.mention))

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)