import time
import threading


def countdown():
    i = 0
    begin = time.time()
    while i < 5_000_000:
        i += 1
    print(f"duration: {time.time() - begin}")


def main():
    begin = time.time()

    r1 = threading.Thread(target=countdown)
    r2 = threading.Thread(target=countdown)
    r3 = threading.Thread(target=countdown)
    r4 = threading.Thread(target=countdown)
    r5 = threading.Thread(target=countdown)
    r6 = threading.Thread(target=countdown)
    r7 = threading.Thread(target=countdown)
    r8 = threading.Thread(target=countdown)
    r9 = threading.Thread(target=countdown)
    r10 = threading.Thread(target=countdown)

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

    print(time.time() - begin)


if __name__ == "__main__":
    main()
