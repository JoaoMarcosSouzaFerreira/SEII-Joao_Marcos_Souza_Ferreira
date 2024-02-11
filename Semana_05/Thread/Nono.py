import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
  print('Sleeping {seconds} second(s)...')
  time.sleep(seconds)
  return f'Done Sleeping...{seconds}' 


with concurrent.futures.ThreadPoolExecutor() as executor:
  secs = [5,4,3,2,1]
  results = executor.map(do_something, secs)

for result in results:
  print(result)
