import asyncio

async def main():
  print('tim')
  task = asyncio.creat_task( foo('text'))
  await asyncio.sleep(0.5)
  print('finished')
  
async def foo(text):
  print(text)
  await asyncio.sleep(10)

asyncio.run(main())
