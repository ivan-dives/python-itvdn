from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def fact(started=1, finished=1):
    factor = started
    for i in range(started, finished):
        i += 1
        factor = factor * i
    result = factor
    return result


def executor_map(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()

    future1 = executor.submit(fact, started=1, finished=100)
    future2 = executor.submit(fact, started=1, finished=5)

    result = future2.result() + future1.result()
    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def main():
    executor_map(ThreadPoolExecutor)
    executor_map(ProcessPoolExecutor)


if __name__ == "__main__":
    main()
