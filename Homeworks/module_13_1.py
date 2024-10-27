import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    number = 0
    for i in range(5):
        number += 1
        sleep_time = 6 - power
        await asyncio.sleep(sleep_time)
        print(f'Силач {name} поднял {number}')
    print(f'Силач {name} закончил соревнования.')
async def competition():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3
    print('Соревнования окончены!')
asyncio.run(competition())