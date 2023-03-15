import asyncio

# async def main():
    # return await add(2)
    
    
async def add(x: int) -> int:
    print("async func add")
    return x+3

print(asyncio.get_event_loop().run_until_complete(add(2)))

