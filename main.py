from discord.ext    import commands

bot = commands.Bot(command_prefix='%')

bot.lava_nodes = [
    {'host' : 'lava.link',
     'port' : '80',
     'password' : 'anything',
     'rest_uri' : f'http://lava.link:80',
     'identifier' : 'MAIN',
     'region': 'singapore'
    }
]

@bot.event
async def on_ready():
    print(f'bot is ready na madapaker')

bot.load_extension('dismusic')

bot.run("OTA4MjEwNTYzNjI3MjUzNzkw.YYybAA.X0eCufPWrglKjLfNozhcw8Ta4Gg")