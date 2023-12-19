from multiprocessing import Pool
import time


def square(x):
    time.sleep(1)
    return x**2


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        print(pool.map(square, range(10)))
