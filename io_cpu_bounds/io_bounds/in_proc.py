from multiprocessing import Process
import time
import requests


def proc():
    return requests.get('https://api.covidtracking.com/v1/us/current.json')


def main():
    begin = time.time()

    p1 = Process(target=proc)
    p2 = Process(target=proc)
    p3 = Process(target=proc)
    p4 = Process(target=proc)
    p5 = Process(target=proc)
    p6 = Process(target=proc)
    p7 = Process(target=proc)
    p8 = Process(target=proc)
    p9 = Process(target=proc)
    p10 = Process(target=proc)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()

    print(time.time() - begin)

    # begin = time.time()
    # for i in range(10):
    #     x = Process(target=proc)
    #     x.start()
    #     x.join()
    #
    # print(time.time() - begin)
    #

if __name__ == "__main__":
    main()
