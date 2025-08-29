import asyncio
import aiofiles

async def main():
    async with aiofiles.open('file.txt', mode='w') as f:
        await f.write('data')

    async with aiofiles.open('file.txt', mode='r') as f:
        contents = await f.read()
    print(contents)

asyncio.run(main())
