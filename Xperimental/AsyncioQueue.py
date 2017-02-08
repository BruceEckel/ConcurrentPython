import asyncio
import random

async def do_work(task_name, work_queue):
    while not work_queue.empty():
        queue_item = await work_queue.get()
        print('{0} got: {1}'.format(task_name, queue_item))
        await asyncio.sleep(random.random())

def execute(tasks):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == "__main__":
    q = asyncio.Queue()

    [q.put_nowait(i) for i in range(20)]

    print(q)

    execute([asyncio.async(do_work('task' + str(t), q))
             for t in range(3)])
