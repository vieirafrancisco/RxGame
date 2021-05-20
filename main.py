import multiprocessing
import random
import time
from threading import current_thread

import rx
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops

def intense_calculation(value):
    time.sleep(random.randint(5, 20) * 0.1)
    return value

optimal_thread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

rx.range(1, 10).pipe(
    ops.map(lambda i: i*100),
    ops.subscribe_on(pool_scheduler)
).subscribe(
    on_next=lambda i: print("PROCESS 1: {0}".format(i)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("PROCESS 1 done!"),
)

rx.of('Yeyy', 'uhuu', 'teste').pipe(
    ops.map(lambda s: len(s)),
    ops.subscribe_on(pool_scheduler)
).subscribe(
    on_next=lambda s: print("PROCESS 2: {0}".format(s)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("PROCESS 2 done!"),
)
