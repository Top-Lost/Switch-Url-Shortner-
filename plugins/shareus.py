import aiohttp
import re
import database as db


async def get_shortlink(id, url):
    api_id = (await db.get_api(id))('shareus')
    
    if not api_id:
        return "Set Your API ID"
    else:
        pass

    link = f"https://api.shareus.io/easy_api?key={api_id}&link={url}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                response = await resp.text()

        if re.match(r'https?://[^\s]+',response):
            return response
        else:
            raise Exception
        
    except Exception as e:
        print(f"Failed to get response from API")
        return "Check Your API ID"
    
    