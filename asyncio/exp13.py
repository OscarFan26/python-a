import asyncio
import time


async def testa(x):
    print("in test a")
    await asyncio.sleep(3)
    print("Resuming a")
    return x


async def testb(x):
    print("in test b")
    await asyncio.sleep(1)
    print('Resuming b')
    return x


async def main():

    start = time.time()
    # method 1
    taska = asyncio.create_task(testa(1))
    taskb = asyncio.create_task(testb(2))

    # method 2
    # taska = asyncio.ensure_future(testa(1))
    # taskb = asyncio.ensure_future(testb(2))
    print("task a is %s" % taska)
    print("task b is %s" % taskb)
    print("task a is done? %s" % taska.done())
    print("task b is done? %s" % taskb.done())
    await taskb
    await taska
    print("task a is done? %s" % taska.done())
    print("task b is done? %s" % taskb.done())
    print("test a result is %d" % taska.result())
    print("test b result is %d" % taskb.result())
    print("use %s time" % (time.time()-start))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
