from urllib.parse import urlparse
import aiohttp

types = {"-gp": "gplink", 
         "-atg": "atglinks", 
         "-sus": "shareus", 
         "-gl": "gyanilinks"}

def typeof(input):
    for short, long in types.items():
        if input[0] == short:
            return long
        elif input[0] == long:
            return long
        else:
            return None
        
        
async def isvalidurl(url):
    try:
        parsed = urlparse(url)
        
        if parsed.netloc:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    
                    if response.status // 100 == 2:
                        return True
                    else:
                        return False
        else:
            return False
    except ValueError:
        return False
        

