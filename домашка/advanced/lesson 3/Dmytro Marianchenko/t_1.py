from concurrent.futures import ProcessPoolExecutor
import time


def factorial_fun(x):
    start_t = time.time()
    factorial = 1
    for i in range(2, x + 1):
        factorial *= i
    end_t = time.time()
    print(f"{factorial} in {str(end_t - start_t)} sec")


def main():
    with ProcessPoolExecutor(max_workers=2) as exe:
        task1 = exe.submit(factorial_fun(10))
        task2 = exe.submit(factorial_fun(10000))


if __name__ == "__main__":
    main()
