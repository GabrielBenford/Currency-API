import discord
from discord.ext import commands,tasks
intents=discord.Intents.all()
bot=commands.Bot('.', intents=intents)
bad_words=['Pizza','Hamburger','Cocacola']
works=['Talk to your adms','Analyse your program system','Interact with your discord members','If there is a bug, fix it']
@bot.event
async def on_ready():
    print('The bot is now online!')
@bot.event
async def on_member_join(member: discord.Member):
     chanel=bot.get_channel(1395883075988230290)
     await chanel.send(f'{member.mention} has joined the server!')
@bot.event
async def on_member_update(before:discord.Member, after:discord.Member):
    if before.avatar !=after.avatar:
     chanel=bot.get_channel(1395883075988230290)
     await chanel.send(f'the {after.name} has changed the avatar to {after.avatar.url}')
@bot.event
async def on_message(message:discord.Message):
    if message.author.bot:
        return
    for word in bad_words:
        if word.lower() in message.content.lower():
         await message.delete()
         await message.channel.send(f"{message.author.mention} said '{word}', please do not use these kind of words in this server!")
         break
    await bot.process_commands(message)
@bot.command()
async def hello(ctx: commands.Context):
    await ctx.reply(f'Hello {ctx.author}!')
@bot.command()
async def task(ctx: commands.Context):
    if ctx.author.bot:
        return
    if works:
        task_list='\n'.join(f'-{work}'for work in works)
        await ctx.send(f'Here is your task lists:\n{task_list}')


bot.run('token')