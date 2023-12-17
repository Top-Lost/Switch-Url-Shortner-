import aiohttp
import json
import database as db


async def atglinks(id, url):
    api_id = (await db.get_api(id))['atglinks']
    
    if not api_id:
        return "Set Your API ID"
    else:
        pass
    
    link = f"https://atglinks.com/api?api={api_id}&url={url}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                response = await resp.text()
        
        data = json.loads(response)

        if data['status'] == "error":
            raise Exception
        else:
            return data.get("shortenedUrl", "")
        
    except Exception as e:
        print(f"Failed to get response from API")
        return data['message']
    
    