import time
from functools import lru_cache

@lru_cache(maxsize=3)
def sum_work(n):
    #SOME TASK TAKING IN SECONDS
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    sum_work(3)
    print("Calling Again")
    sum_work(3)
    print("Called again")
    sum_work(3)
