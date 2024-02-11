import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
  print('Sleeping {seconds} second(s)...')
  time.sleep(seconds)
  return 'Done Sleeping...' 

with concurrent.futures.ThreadPoolExecutor() as executor:
  f1 = executor.sumbmit(do_something, 1)
  f2 = executor.sumbmit(do_something, 1)
  print(f1.result())
  print(f2.result())

finish= time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
