import time
from multiprocessing import Process


def countdown():
    i = 0
    begin = time.time()
    while i < 5_000_000:
        i += 1
    print(f"duration: {time.time() - begin}")


def main():
    begin = time.time()

    p1 = Process(target=countdown)
    p2 = Process(target=countdown)
    p3 = Process(target=countdown)
    p4 = Process(target=countdown)
    p5 = Process(target=countdown)
    p6 = Process(target=countdown)
    p7 = Process(target=countdown)
    p8 = Process(target=countdown)
    p9 = Process(target=countdown)
    p10 = Process(target=countdown)

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


if __name__ == "__main__":
    main()