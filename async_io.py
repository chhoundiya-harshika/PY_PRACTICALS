# import asyncio
# async def greet():
#     print("Hello")
# result = greet()
# print(result)

# import asyncio

# async def greet():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("Welcome")

# asyncio.run(greet())

# import time
# print("hello")
# time.sleep(2)
# print("Welcome")

# import asyncio
# async def task1(name):
#     print("t1 started!",name)
#     await asyncio.sleep(2)
#     print("t1 completed!",name)
    
# async def task2():
#     print("t2 started!")
#     await asyncio.sleep(2)
#     print("t2 completed!")
    
# async def task3():
#     print("t3 started!")
#     await asyncio.sleep(2)
#     print("t3 completed!")

# async def main():
#     await asyncio.gather(
#         task1("hey"),
#         task1("hello"),
#         task1("hi")
#     )
# asyncio.run(main)

# import asyncio

# async def greet(name):
#     print("Hello", name)
#     await asyncio.sleep(2)
#     print("Welcome", name)

# async def main():
#     await asyncio.gather(greet("a")

#     )

# asyncio.run(main())

import asyncio
async def square(n):
    await asyncio.sleep(2)
    return n*n
async def main():
    result=await asyncio.gather(
        square(2),
        square(3),
        square(4)
    )
    print(result)
asyncio.run(main())