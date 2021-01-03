class SELFBOT():
    __linecount__ = 2624
    __version__ = 3.7
     
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS

ctypes.windll.kernel32.SetConsoleTitleW(f'Execard v{SELFBOT.__version__} | Loading...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
dankmemer_sniper = config.get('dankmemer_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')
bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled" 
    
    print(f'''{Fore.RESET}
                                

                        {Fore.YELLOW}     ███████╗██╗░░██╗███████╗░█████╗░░█████╗░██████╗░██████╗░
                        {Fore.YELLOW}     ██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
                        {Fore.YELLOW}     █████╗░░░╚███╔╝░█████╗░░██║░░╚═╝███████║██████╔╝██║░░██║
                        {Fore.YELLOW}     ██╔══╝░░░██╔██╗░██╔══╝░░██║░░██╗██╔══██║██╔══██╗██║░░██║
                        {Fore.YELLOW}     ███████╗██╔╝╚██╗███████╗╚█████╔╝██║░░██║██║░░██║██████╔╝
                        {Fore.YELLOW}     ╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
                                                   
                                                   
                                        
                       {Fore.GREEN}Execard {SELFBOT.__version__} | {Fore.RED}Logged in as: {Fore.CYAN} {Execard.user.name}#{Execard.user.discriminator} {Fore.RED}| ID: {Fore.CYAN}{Execard.user.id}   
                       {Fore.RED}Privnote Sniper | {Fore.CYAN}{privnote}{Fore.RED}|  
                       {Fore.RED}Nitro Sniper    | {Fore.CYAN}{nitro}{Fore.RED}|
                       {Fore.RED}Giveaway Sniper | {Fore.CYAN}{giveaway}{Fore.RED}|
                       {Fore.RED}SlotBot Sniper  | {Fore.CYAN}{slotbot}{Fore.RED}|
                       {Fore.RED}Prefix: {Fore.CYAN}{prefix}
                       {Fore.RED}Creator: {Fore.CYAN}coats.#4321 / Ecys#1337
    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Execard.run(token, bot=False, reconnect=True)
            os.system(f'title (Execard Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Execard = discord.Client()
Execard = commands.Bot(
    description='Execard Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Execard.msgsniper = False
Execard.slotbot_sniper = True
Execard.giveaway_sniper = True
Execard.mee6 = False
Execard.mee6_channel = None
Execard.yui_kiss_user = None
Execard.yui_kiss_channel = None
Execard.yui_hug_user = None
Execard.yui_hug_channel = None
Execard.snipe_history_dict = {}
Execard.sniped_message_dict = {}
Execard.sniped_edited_message_dict = {}
Execard.whitelisted_users = {}
Execard.copycat = None
Execard.wave = token
Execard.remove_command('help') 

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url="https://www.twitch.tv/monstercat", 
    )
    await Execard.change_presence(activity=btc_stream)

@Execard.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Execard.event
async def on_message_delete(message):
    if message.author.id == Execard.user.id:
        return
    if Execard.msgsniper:
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Execard.sniped_message_dict) > 1000:
        Execard.sniped_message_dict.clear()
    if len(Execard.snipe_history_dict) > 1000:
        Execard.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Execard.sniped_message_dict.update({channel_id: message_content})
        if channel_id in Execard.snipe_history_dict:
            pre = Execard.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Execard.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Execard.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        Execard.sniped_message_dict.update({channel_id: message_content})


@Execard.event
async def on_message_edit(before, after):
    if before.author.id == Execard.user.id:
        return
    if Execard.msgsniper:
        if before.content is after.content:
            return
        # if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(before.channel, discord.DMChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Execard.sniped_edited_message_dict) > 1000:
        Execard.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Execard.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Execard.sniped_edited_message_dict.update({channel_id: message_content})

@Execard.event
async def on_message(message):
    if Execard.copycat is not None and Execard.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
     	    f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
            +Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            +Fore.RESET)

    def PrivnoteData(code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
            +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
    
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == true:
            if message.author.id == 346353957029019648:
                try:
                    await asyncio.sleep(5)
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009 or message.author.id == 673918978178940951 or message.author.id == 582537632991543307 or message.author.id == 396464677032427530 or message.author.id == 649604306596528138 or message.author.id == 716967712844414996:
                try:
                    await asyncio.sleep(25)    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Execard.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009 or message.author.id == 673918978178940951 or message.author.id == 582537632991543307 or message.author.id == 396464677032427530 or message.author.id == 649604306596528138 or message.author.id == 716967712844414996:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Execard.process_commands(message)

@Execard.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    
    
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Execard v{SELFBOT.__version__}] | Logged in as {Execard.user.name} ')

@Execard.command()
async def bhelp(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(color=0xFFA500, timestamp=ctx.message.created_at)
        embed.set_author(name="𝙴𝚇𝙴𝙲𝙰𝚁𝙳 𝚟𝟹.𝟽", icon_url=Execard.user.avatar_url)
        embed.set_thumbnail(url=Execard.user.avatar_url)
        embed.add_field(name="😈 `HELP GENERAL`", value="Shows all general commands", inline=False)
        embed.add_field(name="😈 `HELP ACCOUNT`", value="Shows all account commands", inline=False)
        embed.add_field(name="😈 `HELP TEXT`", value="Shows all text commands", inline=False)
        embed.add_field(name="😈 `HELP IMAGE`", value="Shows all image manipulation commands", inline=False)
        embed.add_field(name="😈 `HELP NSFW`", value="Shows all nsfw commands", inline=False)
        embed.add_field(name="😈 `HELP MISC`", value="Shows all miscellaneous commands", inline=False)
        embed.add_field(name="😈 `HELP NUKE`", value="Shows all nuke commands", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        await ctx.send(embed=embed)
    elif str(category).lower() == "general":
        embed = discord.Embed(color=0xFFA500, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        embed.description = f"\uD83D\uDCB0 `GENERAL COMMANDS`\n`> help <category>` - returns all commands of that category\n`> uptime` - return how long the selfbot has been running\n`> prefix <prefix>` - changes the bot's prefix\n`> ping` - returns the bot's latency\n`> av <user>` - returns the user's pfp\n`> whois <user>` - returns user's account info\n`> tokeninfo <token>` - returns information about the token\n`> copyserver` - makes a copy of the server\n`> rainbowrole <role>` - makes the role a rainbow role (ratelimits)\n`> serverinfo` - gets information about the server\n`> serverpfp` - returns the server's icon\n`> banner` - returns the server's banner\n`> shutdown` - shutsdown the selfbot\n`> getroles` - lists all roles on the server"
        await ctx.send(embed=embed)
    elif str(category).lower() == "account":
        embed = discord.Embed(color=0xFFA500, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        embed.description = f"\uD83D\uDCB0 `ACCOUNT COMMANDS`\n`> ghost` - makes your name and pfp invisible\n`> pfpsteal <user>` - steals the users pfp\n`> setpfp <link>` - sets the image-link as your pfp\n`> hypesquad <hypesquad>` - changes your current hypesquad\n`> leavegroups` - leaves all groups that you're in\n`> cyclenick <text>` - cycles through your nickname by letter\n`> stopcyclenick` - stops cycling your nickname\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> acceptfriends` - accepts all friend requests\n`> delfriends` - removes all your friends\n`> ignorefriends` - ignores all friends requests\n`> clearblocked` - clears your block-list\n`> read` - marks all messages as read\n`> leavegc` - leaves the current groupchat\n`> adminservers` - lists all servers you have perms in\n`> slotbot <on/off>` - snipes slotbots ({Execard.slotbot_sniper})\n`> giveaway <on/off>` - snipes giveaways ({Execard.giveaway_sniper})\n`> mee6 <on/off>` - auto sends messages in the specified channel ({Execard.mee6}) <#{Execard.mee6_channel}>\n`> yuikiss <user>` - auto sends yui kisses every minute <@{Execard.yui_kiss_user}> <#{Execard.yui_kiss_channel}>\n`> yuihug <user>` - auto sends yui hugs every minute <@{Execard.yui_hug_user}> <#{Execard.yui_hug_channel}>\n`> yuistop` - stops any running yui loops"
        await ctx.send(embed=embed)
    elif str(category).lower() == "text":
        embed = discord.Embed(color=0xFFA500, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        embed.description = f"\uD83D\uDCB0 `TEXT COMMANDS`\n`> logo` - sends the selfbot logo\n`> snipehistory` - shows a history of deleted messages\n`> clearsnipehistory` - clears snipe history of current channel\n`> snipe` - shows the last deleted message\n`> editsnipe` - shows the last edited message\n`> msgsniper <on/off> ({Execard.msgsniper})` - enables a message sniper for deleted messages in DMs\n`> clear` - sends a large message filled with invisible unicode\n`> del <message>` - sends a message and deletes it instantly\n`> 1337speak <message>` - talk like a hacker\n`> minesweeper` - play a game of minesweeper\n`> spam <amount>` - spams a message\n`> dm <user> <content>` - dms a user a message\n`> reverse <message>` - sends the message but in reverse-order\n`> shrug` - returns ¯\_(ツ)_/¯\n`> lenny` - returns ( ͡° ͜ʖ ͡°)\n`> fliptable` - returns (╯°□°）╯︵ ┻━┻\n`> unflip` - returns ┬─┬ ノ( ゜-゜ノ)\n`> bold <message>` - bolds the message\n`> censor <message>` - censors the message\n`> underline <message>` - underlines the message\n`> italicize <message>` - italicizes the message\n`> strike <message>` - strikethroughs the message\n`> quote <message>` - quotes the message\n`> code <message>` - applies code formatting to the message\n`> purge <amount>` - purges the amount of messages\n`> empty` - sends an empty message\n`> tts <content>` - returns an mp4 file of your content\n`> firstmsg` - shows the first message in the channel history\n`> ascii <message>` - creates an ASCII art of your message\n`> wizz` - makes a prank message about wizzing \n`> 8ball <question>` - returns an 8ball answer\n`> slots` - play the slot machine\n`> everyone` - pings everyone through a link\n`> abc` - cyles through the alphabet\n`> cum` - makes you cum lol?\n`> 9/11` - sends a 9/11 attack\n`> massreact <emoji>` - mass reacts with the specified emoji"
        await ctx.send(embed=embed)
    elif str(category).lower() == "image":
        embed = discord.Embed(color=0xFFA500, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        embed.description = f"\uD83D\uDCB0 `IMAGE MANIPULATION COMMANDS`\n`> tweet <user> <message>` makes a fake tweet\n`> magik <user>` - distorts the specified user\n`> fry <user>` - deep-fry the specified user\n`> blur <user>` - blurs the specified user\n`> pixelate <user>` - pixelates the specified user\n`> Supreme <message>` - makes a *Supreme* logo\n`> darksupreme <message>` - makes a *Dark Supreme* logo\n`> fax <text>` - makes a fax meme\n`> blurpify <user>` - blurpifies the specified user\n`> invert <user>` - inverts the specified user\n`> gay <user>` - makes the specified user gay\n`> communist <user>` - makes the specified user a communist\n`> snow <user>` - adds a snow filter to the specified user\n`> jpegify <user>` - jpegifies the specified user\n`> Execard <logo-word 1> <logo-word 2>` - makes a Execard logo\n`> phcomment <user> <message>` - makes a fake Execard comment\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nsfw":
        embed = discord.Embed(color=0xFFA500, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        embed.description = f"\uD83D\uDCB0 `NSFW COMMANDS`\n`> anal` - returns anal pics\n`> erofeet` - returns erofeet pics\n`> feet` - returns sexy feet pics\n`> hentai` - returns hentai pics\n`> boobs` - returns booby pics\n`> tits` - returns titty pics\n`> blowjob` - returns blowjob pics\n`> neko` - returns neko pics\n`> lesbian` - returns lesbian pics\n`> cumslut` - returns cumslut pics\n`> pussy` - returns pussy pics\n`> waifu` - returns waifu pics"
        await ctx.send(embed=embed)
    elif str(category).lower() == "misc":
        embed = discord.Embed(color=0xFFA500, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        embed.description = f"\uD83D\uDCB0 `MISCELLANEOUS COMMANDS`\n`> copycat <user>` - copies the users messages ({Execard.copycat})\n`> stopcopycat` - stops copycatting\n`> fakename` - makes a fakename with other members's names\n`> geoip <ip>` - looks up the ip's location\n`> pingweb <website-url>` pings a website to see if it's up\n`> anticatfish <user>` - reverse google searches the user's pfp\n`> stealemoji` - <emoji> <name> - steals the specified emoji\n`> hexcolor <hex-code>` - returns the color of the hex-code\n`> dick <user>` - returns the user's dick size\n`> bitcoin` - shows the current bitcoin exchange rate\n`> hastebin <message>` - posts your message to hastebin\n`> rolecolor <role>` - returns the role's color\n`> nitro` - generates a random nitro code\n`> feed <user>` - feeds the user\n`> tickle <user>` - tickles the user\n`> slap <user>` - slaps the user\n`> hug <user>` - hugs the user\n`> cuddle <user>` - cuddles the user\n`> smug <user>` - smugs at the user\n`> pat <user>` - pat the user\n`> kiss <user>` - kiss the user\n`> topic` - sends a conversation starter\n`> wyr` - sends a would you rather\n`> gif <query>` - sends a gif based on the query\n`> sendall <message>` - sends a message in every channel\n`> poll <msg: xyz 1: xyz 2: xyz>` - creates a poll\n`> bots` - shows all bots in the server\n`> image <query>` - returns an image\n`> hack <user>` - hacks the user\n`> token <user>` - returns the user's token\n`> cat` - returns random cat pic\n`> sadcat` - returns a random sad cat\n`> dog` - returns random dog pic\n`> fox` - returns random fox pic\n`> bird` - returns random bird pic\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nuke":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/784561225458778172/792435183236284416/oRKHqciYdcn4.gif")
        embed.description = f"\uD83D\uDCB0 `NUKE COMMANDS`\n`> tokenfuck <token>` - disables the token\n`> nuke` - nukes the server\n`> massban` - bans everyone in the server\n`> dynoban` - mass bans with dyno one message at a time\n`> masskick` - kicks everyone in the server\n`> spamroles` - spam makes 250 roles\n`> spamchannels` - spam makes 250 text channels\n`> delchannels` - deletes all channels in the server\n`> delroles` - deletes all roles in the server\n`> purgebans` - unbans everyone\n`> renamechannels <name>` - renames all channels\n`> servername <name>` - renames the server to the specified name\n`> nickall <name>` - sets all user's nicknames to the specified name\n`> changeregion <amount>` - spam changes regions in groupchats\n`> kickgc` - kicks everyone in the gc\n`> spamgcname` - spam changes the groupchat name\n`> massmention <message>` - mass mentions random people\n`> giveadmin` - gives all admin roles in the server\n"
        await ctx.send(embed=embed)

@Execard.command(aliases=["automee6"])
async def mee6(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify True/false.", delete_after=0.1)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
            await ctx.send("You can't bind Auto-MEE6 to a DM or GC", delete_after=0.1)
            return
        else:
            Execard.mee6 = True
            await ctx.send("Auto-MEE6 Successfully bound to `" + ctx.channel.name + "`", delete_after=0.1)
            Execard.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Execard.mee6 = False
        await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=0.1)
    while Execard.mee6 is True:
        sentences = ['Stop waiting for exceptional things to just happen.',
                     'The lyrics of the song sounded like fingernails on a chalkboard.',
                     'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
                     'He had a hidden stash underneath the floorboards in the back room of the house.',
                     'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
                     'People generally approve of dogs eating cat food but not cats eating dog food.',
                     'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
                     'She was the type of girl who wanted to live in a pink house.',
                     'The bees decided to have a mutiny against their queen.',
                     'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
                     'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
                     'They desperately needed another drummer since the current one only knew how to play bongos.',
                     'He waited for the stop sign to turn to a go sign.',
                     'His thought process was on so many levels that he gave himself a phobia of heights.',
                     'Her hair was windswept as she rode in the black convertible.',
                     'Karen realized the only way she was getting into heaven was to cheat.',
                     'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
                     'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
                     'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
                     'You probably shouldn\'t look at your feet.',
                     'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
                     'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
                     'The three-year-old girl ran down the beach as the kite flew behind her.',
                     'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
                     'They improved dramatically once the lead singer left.',
                     'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
                     'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
                     'People keep telling me "orange" but I still prefer "pink".',
                     'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                     'I liked their first two albums but changed my mind after that charity gig.',
                     'Plans for this weekend include turning wine into water.',
                     'A kangaroo is really just a rabbit on steroids.',
                     'He played the game as if his life depended on it and the truth was that it did.',
                     'He\'s in a boy band which doesn\'t make much sense for a snake.',
                     'She let the balloon float up into the air with her hopes and dreams.',
                     'There was coal in his stocking and he was thrilled.',
                     'This made him feel like an old-style rootbeer float smells.',
                     'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                     'The light in his life was actually a fire burning all around him.',
                     'Truth in advertising and dinosaurs with skateboards have much in common.',
                     'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                     'The view from the lighthouse excited even the most seasoned traveler.',
                     'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                     'It\'s difficult to understand the lengths he\'d go to remain short.',
                     'Nobody questions who built the pyramids in Mexico.',
                     'They ran around the corner to find that they had traveled back in time.',
                     'A sudden warm rainstorm washes down in sweet hyphens.',
                     'We were all a little drunk with spring, like the fat bees reeling from flower to flower, and a strange insurrectionary current ran among us.',
                     'Lizards skit like quick beige sticks.',
                     'The sky, at sunset, looked like a carnivorous flower.',
                     'Inside us there is something that has no name, that something is what we are.',
                     'As he crossed toward the pharmacy at the corner he involuntarily turned his head because of a burst of light that had ricocheted from his temple, and saw, with that quick smile with which we greet a rainbow or a rose, a blindingly white parallelogram of sky being unloaded from the van—a dresser with mirrors across which, as across a cinema screen, passed a flawlessly clear reflection of boughs sliding and swaying not arboreally, but with a human vacillation, produced by the nature of those who were carrying this sky, these boughs, this gliding façade.',
                     'They were all scarecrows, blown about under the murdering sunball with empty ribcages.',
                     'We all owe death a life',
                     'Love is the extremely difficult realization that something other than oneself is real.',
                     'In the deep gloom he could see the electric white gashes where the water boiled over the boulders.',
                     'We are souls shut inside a cage of bones; souls squeezed into a parcel of flesh.',
                     'I want to sleep in her uterus with my foot hanging out.',
                     'Sometimes to understand a word\'s meaning you need more than a definition.',
                     'Oh, and tell him I swear not to look at what other girl\'s he\'s been calling... cross my heart, like fun!',
                     'The light beyond the solid French doors made her flinch, but she forced herself to cross the doorway.'
                     'Are you blaming a little boy for what his mother did?',
                     'The blue parrot drove by the hitchhiking mongoose.',
                     'Most shark attacks occur about 10 feet from the beach since that\'s where the people are.',
                     'The two walked down the slot canyon oblivious to the sound of thunder in the distance.',
                     'My dentist tells me that chewing bricks is very bad for your teeth.',
                     'At that moment he wasn\'t listening to music, he was living an experience.',
                     'He figured a few sticks of dynamite were easier than a fishing pole to catch fish.',
                     'With a single flip of the coin, his life changed forever.',
                     'She wondered what his eyes were saying beneath his mirrored sunglasses.',
                     'He barked orders at his daughters but they just stared back with amusement.',
                     'Watching the geriatric men’s softball team brought back memories of 3 yr olds playing t-ball.']
        await Execard.get_channel(Execard.mee6_channel).send(random.choice(sentences), delete_after=0.1)
        await asyncio.sleep(45)

@Execard.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")

@Execard.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"exeter_anal.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")

@Execard.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Execard.msgsniper = True
        await ctx.send('Execard Message-Sniper is now **enabled**', delete_after=0.1)
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Execard.msgsniper = False
        await ctx.send('Execard Message-Sniper is now **disabled**', delete_after=0.1)

@Execard.command()
async def supreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Execard_supreme.png"))
    except:
        await ctx.send(endpoint)


@Execard.command(aliases=['dsupreme'])
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20") + "&dark=true"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Execard_dark_supreme.png"))
    except:
        await ctx.send(endpoint)


@Execard.command(aliases=["facts"])
async def fax(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/facts?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Execard_facts.png"))
    except:
        await ctx.send(endpoint)


@Execard.command(aliases=["blurp"])
async def blurpify(ctx, user: discord.User = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_blurpify.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_blurpify.png"))
        except:
            await ctx.send(res['message'])


@Execard.command()
async def invert(ctx, user: discord.User = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/invert?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)


@Execard.command()
async def gay(ctx, user: discord.User = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)

@Execard.command()
async def crash(ctx): # b'\xfc'
    await ctx.message.delete()
    Crash = urlopen(Request("https://pastebin.com/raw/Ht1qyz6W")).read().decode()
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    
@Execard.command()
async def communist(ctx, user: discord.User = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/communist?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)


@Execard.command()
async def snow(ctx, user: discord.User = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/snow?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)


@Execard.command(aliases=["jpeg"])
async def jpegify(ctx, user: discord.User = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/jpegify?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Execard_invert.png"))
        except:
            await ctx.send(endpoint)


@Execard.command(aliases=["Pornhublogo", "logo"])
async def Pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/Execard?text={text-1}&text2={text-2}".replace("{text-1}", word1).replace(
        "{text-2}", word2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Execard_Execard_logo.png"))
    except:
        await ctx.send(endpoint)

@Execard.command()
async def token(ctx, user: discord.User = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@Execard.command()
async def hack(ctx, user: discord.User = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

@Execard.command()
async def lmgtfy(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@Execard.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@Execard.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Execard-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Execard.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@Execard.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Execard.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Execard.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Execard.command() 
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Execard.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@Execard.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])    

@Execard.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@Execard.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Execard.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@Execard.command()
async def pingweb(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=0.1)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=0.1)       

@Execard.command()
async def revav(ctx, user: discord.User=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Execard.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))      

@Execard.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@Execard.command()
async def whois(ctx, *, user: discord.User = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@Execard.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Execard.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)       

@Execard.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Execard.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@Execard.command()
async def blank(ctx): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:  
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:      
             await Execard.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Execard.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Execard.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Execard.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Execard.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Execard.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.User = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@Execard.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "a:"):str.find(arguments, "a:")]).replace(
        "a:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "b:")]).replace(
        "b:", "")
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')

@Execard.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Execard.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        print(list(ctx.guild.members))
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)

@Execard.command()
async def typing(ctx): # b'\xfc'
    await ctx.message.delete()
    headers = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v6/channels/{ctx.message.channel.id}/typing', headers=headers)

@Execard.command(aliases=['tokenfucker', 'disable',]) 
async def tokenfuck(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Execard",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   

@Execard.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)

@Execard.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5) 
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@Execard.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None): # b'\xfc'
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 0.1)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 0.1)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 0.1)

@Execard.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@Execard.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Execard.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(Execard.copycat))
    Execard.copycat = None

@Execard.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    Execard.copycat = user
    await ctx.send("Now copying " + str(Execard.copycat)) 

@Execard.command(aliases=['del'])
async def delmsg(ctx,*,message):
	await ctx.message.delete()
	await ctx.send(message, delete_after=0.1)

@Execard.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await Execard.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Execard.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Execard.command()
async def yuikiss(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Kiss in DMs or GCs", delete_after=0.1)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Kiss", delete_after=0.1)
            return
        Execard.yui_kiss_user = user.id
        Execard.yui_kiss_channel = ctx.channel.id
        if Execard.yui_kiss_user is None or Execard.yui_kiss_channel is None:
            await ctx.send('An impossible error occured, try again later or contact eooe')
            return
        while Execard.yui_kiss_user is not None and Execard.yui_kiss_channel is not None:
            await Execard.get_channel(Execard.yui_kiss_channel).send('yui kiss ' + str(Execard.yui_kiss_user),
                                                                   delete_after=0.1)
            await asyncio.sleep(60)


@Execard.command()
async def yuihug(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Hug in DMs or GCs", delete_after=0.1)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Hug", delete_after=0.1)
            return
        Execard.yui_hug_user = user.id
        Execard.yui_hug_channel = ctx.channel.id
        if Execard.yui_hug_user is None or Execard.yui_hug_channel is None:
            await ctx.send('An impossible error occured, try again later or contact swag')
            return
        while All.yui_hug_user is not None and Execard.yui_hug_channel is not None:
            await Execard.get_channel(Execard.yui_hug_channel).send('yui hug ' + str(Execard.yui_hug_user),
                                                                  delete_after=0.1)
            await asyncio.sleep(60)


@Execard.command()
async def yuistop(ctx):
    await ctx.message.delete()
    Execard.yui_kiss_user = None
    Execard.yui_kiss_channel = None
    Execard.yui_hug_user = None
    Execard.yui_hug_channel = None
    await ctx.send('Successfully **disabled** Yui Loops', delete_after=0.1)

@Execard.command()
async def destroy(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="https://Execard.wtf",
            reason="https://Execard-selfbot.github.io",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@Execard.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(2)    
            await user.send(message)
        except:
            pass

@Execard.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Execard.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Execard.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Execard.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Execard.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Execard.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Execard.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Execard.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Execard.command()
async def dm(ctx, user : discord.User, *, message): # b'\xfc'
    await ctx.message.delete()
    user = Execard.get_user(user.id)
    if ctx.author.id == Execard.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass       

@Execard.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour): # b'\xfc'
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em) 

@Execard.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Execard.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@Execard.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@Execard.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@Execard.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Execard.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Execard.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Execard.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Execard.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@Execard.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Execard.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf', 'backup'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in Execard.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Execard.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@Execard.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@Execard.command()
async def mac(ctx, mac): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@Execard.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(1)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(1)

@Execard.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Execard.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@Execard.command()
async def topic(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Execard.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@Execard.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Execard.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Execard.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Execard.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Execard.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Execard.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()  
async def feed(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def tickle(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def slap(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def hug(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def smug(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def pat(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command()
async def kiss(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Execard.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@Execard.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Execard.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Execard.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Execard.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Execard.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Execard.command()
async def help(ctx): # b'\xfc'
    await ctx.message.delete()
    url = 'https://Alucard-selfbot.github.io/commands'
    r = requests.get(url)
    if r.status_code == 200:
        webbrowser.open(url)
    else:
        print('Page is currently under maintenance, our team will announce when the page is back online')    

@Execard.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await Execard.change_presence(activity=stream)    

@Execard.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Execard.change_presence(activity=game)

@Execard.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Execard.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@Execard.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Execard.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@Execard.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Execard.command()
async def shrug(ctx): # b'\xfc'
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@Execard.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@Execard.command()
async def tableflip(ctx): # b'\xfc'
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@Execard.command()
async def unflip(ctx): # b'\xfc'
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@Execard.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Execard.command()
async def secret(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('||'+message+'||')

@Execard.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@Execard.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f"HWID: {Fore.YELLOW}{hwid}"+Fore.RESET)

@Execard.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))

@Execard.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@Execard.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    await Execard.logout()

@Execard.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()   
    btc_status.start()        

@Execard.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx): # b'\xfc'
    await ctx.message.delete()
    Dump(ctx)

@Execard.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    Clear()
    startprint()

@Execard.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

@Execard.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()

if __name__ == '__main__':
    Init()
