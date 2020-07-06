import multiprocessing as mp

def job(x):
    return x**2


def multicore():
    # Can take result return
    pool = mp.Pool()
    # map to cores automatically
    res = pool.map(job, range(1, 10))
    print(res)
    # for single variable
    res = pool.apply_async(job, (2,))
    print(res.get())
    multi_res = [pool.apply_async(job, (i,)) for i in range(1, 10)]
    print([res.get() for res in multi_res])


if __name__ == "__main__":
    multicore()