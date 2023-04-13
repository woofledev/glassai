import discord, json
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response

bot = ChatBot('GlassAI')
bot.response_selection_method = get_most_frequent_response
intents=discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)
ownerid = 807643858867322900 # replace this with your user id if you want the ?!? commands
ostart=datetime.now().strftime("logs/log_%Y-%m-%d_%H-%M-%S.txt")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="discord.gg/2rBDSf2MCJ"))
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    lastmsg = None
    if message.author == client.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        log = open(ostart,"a")
        user_input = message.content.strip()
        print(f'user {message.author.name}#{message.author.discriminator} said:',user_input)
        log.write(f'[{datetime.now()}] user {message.author.name}#{message.author.discriminator} said: {user_input}\n')
        lastmsg = datetime.now()
        with open('banned.json', 'r') as f:
                banned = json.load(f)
        if message.author.id in banned:
            print('a banned user ('+message.author.name+'#'+message.author.discriminator+') said: '+message.content.strip())
            return
        if user_input.startswith('?!?send') and (message.author.id == ownerid):
            _, recipient_id, *message_parts = user_input.split()
            recipient_id = int(recipient_id)
            message_content = ' '.join(message_parts)
            recipient = client.get_user(recipient_id)
            if recipient is not None:
                await recipient.send(message_content)
            else:
                await message.channel.send(f'Invalid recipient user ID: {recipient_id}')
        elif user_input.startswith('?!?eval') and (message.author.id == ownerid):
            try:
                _, code = user_input.split(maxsplit=1)
                await message.channel.send(eval(code))
            except Exception as e:
                await message.channel.send(f'ERR: {e}')
        elif user_input.startswith('?!?ban') and (message.author.id == ownerid):
            try:
                banned_ids = list(map(int, user_input.split()[1:]))
                banned += banned_ids
                with open('banned.json', 'w') as f:
                    json.dump(banned, f)
                await message.channel.send(f'Banned user IDs: {banned_ids}')
            except Exception as e:
                await message.channel.send(f'ERR: {e}')
        else:
            bot_response = bot.get_response(user_input)
            await message.channel.send(str(bot_response))
            print('bot response:',bot_response)
            log.write(f'[{datetime.now()}] bot response: {bot_response}\n')
client.run(open("token.txt","r").read())
