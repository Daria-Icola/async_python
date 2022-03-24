import requests
import time
import threading


def req():
    return requests.get('https://api.covidtracking.com/v1/us/current.json')


def main():
    begin = time.time()

    r1 = threading.Thread(target=req)
    r2 = threading.Thread(target=req)
    r3 = threading.Thread(target=req)
    r4 = threading.Thread(target=req)
    r5 = threading.Thread(target=req)
    r6 = threading.Thread(target=req)
    r7 = threading.Thread(target=req)
    r8 = threading.Thread(target=req)
    r9 = threading.Thread(target=req)
    r10 = threading.Thread(target=req)

    r1.start()
    r2.start()
    r3.start()
    r4.start()
    r5.start()
    r6.start()
    r7.start()
    r8.start()
    r9.start()
    r10.start()

    r1.join()
    r2.join()
    r3.join()
    r4.join()
    r5.join()
    r6.join()
    r7.join()
    r8.join()
    r9.join()
    r10.join()

    # for i in range(10):
    #     x = threading.Thread(target=req)
    #     x.start()
    #     x.join()

    print(time.time() - begin)


if __name__ == "__main__":
    main()
