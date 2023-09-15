import discord
import os
import datetime
from discord import app_commands
from discord.ext import tasks

DTOKEN = os.getenv("DTOKEN")

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

DCHAT = 1133688257419419668

@bot.event
async def on_ready():
  print("起動完了")
  time_loop.start()
  await tree.sync()
  await bot.change_presence(activity=discord.Activity(
    name="???", type=discord.ActivityType.watching))


@tree.command(name="test",description="テスト")
async def test_command(interaction: discord.Interaction):
  await interaction.response.send_message("う！")


@tasks.loop(seconds=60)
async def time_loop():
  dt = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M')
  channel = bot.get_channel(DCHAT)
  await channel.send(dt)

bot.run(DTOKEN)