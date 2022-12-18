import multiprocessing 
def func(i):
    print(i)
if __name__=="__main__":
    # for i in range(10):
        # func(i)
    procs=[]
    for i in range(10):
        procs=[multiprocessing.Process(func,args=(i))]
    for i in range(10):
        procs[i].start()
    for i in range(10):
        procs[i].join()
        
