from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time


def factorial_fun(x):
    start_t = time.time()
    factorial = 1
    for i in range(2, x + 1):
        factorial *= i
    end_t = time.time()
    print(f"{end_t - start_t} sec")


def main():
    with ProcessPoolExecutor(max_workers=4) as exe_p:
        print()
        print(f"By using ProcessPoolExecutor factorial of 10 in", end=" ")
        exe_p.submit(factorial_fun(10))
        print("By using ProcessPoolExecutor factorial of 100 in", end=" ")
        exe_p.submit(factorial_fun(100))
        print("By using ProcessPoolExecutor factorial of 1000 in", end=" ")
        exe_p.submit(factorial_fun(1000))
        print("By using ProcessPoolExecutor factorial of 10000 in", end=" ")
        exe_p.submit(factorial_fun(10000))
        print()
    with ThreadPoolExecutor (max_workers=4) as exe_t:
        print("By using ThreadPoolExecutor factorial of 10 in", end=" ")
        exe_t.submit(factorial_fun(10))
        print("By using ThreadPoolExecutor factorial of 100 in", end=" ")
        exe_t.submit(factorial_fun(100))
        print("By using ThreadPoolExecutor factorial of 1000 in", end=" ")
        exe_t.submit(factorial_fun(1000))
        print("By using ThreadPoolExecutor factorial of 10000 in", end=" ")
        exe_t.submit(factorial_fun(10000))

if __name__ == "__main__":
    main()
