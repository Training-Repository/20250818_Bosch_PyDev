from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app)


##-------------------------------------
## Client

import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    try:
        async with async_timeout.timeout(10):
            async with session.get(url) as response:
                return await response.text()
    except asyncio.TimeoutError:
        return "Request timed out"

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

# Use asyncio.run() to properly manage the event loop
asyncio.run(main())