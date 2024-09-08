from discord.ext import commands
import asyncio  


TOKEN = 'YOUR_BOT_TOKEN'


intents = discord.Intents.default()
intents.message_content = True  


bot = commands.Bot(command_prefix=':b ', intents=intents)

@bot.event
async def on_ready():
    print("Connected to Discord")

@bot.command(name='roast', help='List of cool one-liners')
async def roast(ctx):
    roasts = [
        
    ]

    response = random.choice(roasts)
    await ctx.send(response)

@bot.command(name='toss', help='Tosses a coin')
async def toss(ctx):
    await ctx.send("Tossing....")
    await asyncio.sleep(3.5) 
    results = ['Heads', 'Tails']
    res = random.choice(results)
    await ctx.send(res)

@bot.command(name='dice', help='Rolls a dice')
async def dice(ctx):
    await ctx.send("Rolling....")
    await asyncio.sleep(3.5) 
    results = ['1', '2', '3', '4', '5', '6']
    res = random.choice(results)
    await ctx.send(res)

@bot.command(name='ping', help='Pong!')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='echo', help='Repeats what you say')
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command(name='clear', help='Clears the chat')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command(name='kick', help='Kicks a member')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command(name='ban', help='Bans a member')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command(name='unban', help='Unbans a member')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
        
@bot.command(name='join', help='Joins a voice channel')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='Leaves a voice channel')
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name='game', help='Play a game with the bot')
async def game(ctx):
    await ctx.send("Let's play a game! Guess a number between 1 and 10.")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            guess = await bot.wait_for('message', check=check, timeout=10)
            guess = int(guess.content)

            if guess == number:
                await ctx.send("Congratulations! You guessed the correct number.")
                return
            elif guess < number:
                await ctx.send("Too low! Try again.")
            else:
                await ctx.send("Too high! Try again.")

            attempts -= 1

        except asyncio.TimeoutError:
            await ctx.send("Time's up! You ran out of time.")
            return

    await ctx.send(f"Game over! The correct number was {number}.")

@bot.command(name='sticker', help='Get a sticker, duh')
async def stik(ctx):
    stickers = [
        
    ]

    await ctx.send(random.choice(stickers))


bot.run(TOKEN)
