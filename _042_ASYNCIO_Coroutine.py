import asyncio, time

async def Hello():
    print("Hello")
    await asyncio.sleep(5)
    print("World")
    print("waiting for result1")
    result1 = await subtask1()
    print("waiting for result2")
    result2 = await subtask2(result1)
    return (result1, result2)

async def subtask1():
    print("perform subtask1")
    return 'result1'

async def subtask2(arg):
    print("perform subtask2")
    return f'result2 relies on {arg}'


result = asyncio.run(Hello())
print(result)