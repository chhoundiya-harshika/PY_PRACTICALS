# import asyncio
# async def greet():
#     print("Hello")
# result = greet()
# print(result)

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Welcome")

asyncio.run(greet())