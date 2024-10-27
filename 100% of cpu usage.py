#import threading
#
#def my_function(x):
#    return x * x
#
#def my_thread(x):
#    t = threading.Thread(target=my_function, args=(x,))
#    t.start()
#    return t
#
#results = []
#for i in range(1000000):
#    results.append(my_thread(i))
#
#for t in results:
#    t.join()
#
#print(results)

#import concurrent.futures
#
#def my_function(x):
#    return x * x
#
#executor = concurrent.futures.ProcessPoolExecutor(4)
#results = executor.map(my_function, range(10))
#print(results)


import multiprocessing

def my_function(x):
    return x * x

pool = multiprocessing.Pool(400000)
results = pool.map(my_function(0), range(100000000000000))
print(results)