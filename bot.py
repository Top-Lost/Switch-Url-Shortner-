from swibots import BotContext, CommandEvent, filters, BotCommand, MessageEvent
from client import app
from database import add_user, is_user_exist, update_api, update_shortner, update_user, get_user
from plugins import gplink, atglinks, shareus
from loader import load_modules
import re
import logging
logging.basicConfig(filename="logs.txt", filemode="w",format='%(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

app.set_bot_commands(
    [
        BotCommand("start", "Tickle Me!", True),
        BotCommand("set_api", "To set shortner api", True),
        BotCommand("set", "To set default shortner", True),
        BotCommand("settings", "To view Settings", True),
        BotCommand("help", "To get help message", True)
    ]
)

load_modules("plugins")

@app.on_command("start")
async def start(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    user = m.user
    reply = f"Hey {user.name}👋,\n\nI am an URL Shortner Bot🤖\nHit /help for more details"
    
    user_exists = await is_user_exist(user.id)
    
    if user_exists:
        await update_user(id=user.id, name=user.name)
    else:
        await add_user(id=user.id, name=user.name)
        
    await m.reply_text(reply)


@app.on_command("help")
async def help(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    reply = """<b>Available Commands</b>

🚀<b>/start</b> - To start me
🔧<b>/set_api</b> - To set the shortener API
🎯<b>/set</b> - To set the default shortener
👀<b>/settings</b> - To view current settings
📖<b>/help</b> - To see this help message

<i>send commands to see more.</i>
"""
    await m.reply_text(reply)
    
    
@app.on_command("set_api")
async def setapi(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    param = ctx.event.params.split()
    user = m.user

    if len(param) < 2:
        await m.reply_text("""Set API Key in the following:\n
/set_api -gp  <api_id> - For Gplink
/set_api -atg <api_id> - For Atg Links
/set_api -sus <api_id> - For Shareus""")
        return

    type = typeof(param)
    
    if type is None:
        await m.reply_text("Use the appropriate flag.\nCheck /help for details.")
        return
    
    await update_api(id=user.id, type=type, api=param[1])
    await m.reply_text(f"Successfully set your {type} API key!")

def typeof(input):
    types = {"-gp": "gplink", "-atg": "atglinks", "-sus": "shareus"}
    return types.get(input[0]) or None


@app.on_message(filters.regexp(r'https?://[^\s]+'))
async def shorten(ctx: BotContext[MessageEvent]):
    m = ctx.event.message
    url = ctx.event.message.message
    user = m.user
    default = (await get_user(user.id)).get("shortner")

    if default == "gplink":
        shorten = await gplink.gplink(user.id, url)
    elif default == "atglinks":
        shorten = await atglinks.atglinks(user.id, url)
    else:
        shorten = await shareus.shareus(user.id, url)
        
    if re.match(r'https?://[^\s]+',shorten):
        await m.reply_text(f"Your shortened {default} URl\n\n🔗{shorten}")
    else:
        await m.reply_text(f"Failed to genrerate shortened URL\n{shorten}")
    
    
@app.on_command("set")
async def set_shortner(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    param = ctx.event.params
    user = m.user
    shortners = ["gplink", "atglinks", "shareus"]
    
    if not param:
        await m.reply_text("""Usage
/set <value>

values:
gplink - To enable GPLink as default
shareus - To enable Shareus as default
atglinks - To enable ATGLinks as default

example: /set gplink""")
    elif param not in shortners:
        await m.reply_text("Check your input and try again🔃")
    else:
        await update_shortner(id=user.id, shortner=param)     
        await m.reply_text(f"Successfuly set {param} as your default shortner")
        
        
@app.on_command("settings")
async def settings(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    user = m.user
    user_data = await get_user(user.id)
    apis = user_data.get("api")
    reply = f"""⚙️<b>Settings</b>⚙️
    
👤 <b>User ID</b> - {user.id}
🎯 <b>Default</b> - {user_data.get("shortner")}

🔑 <b>API's</b>
🔗 <b>Gplink</b> - {apis.get("gplink")}
🔗 <b>ATGLinks</b> - {apis.get("atglinks")}
🔗 <b>Shareus</b> - {apis.get("shareus")}
    """
    await m.reply_text(reply)
    
app.run()