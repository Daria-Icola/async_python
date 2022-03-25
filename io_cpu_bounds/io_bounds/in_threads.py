import requests
import time
import threading


def req():
    return requests.get('https://api.covidtracking.com/v1/us/current.json')


def main():
    begin = time.time()

    for i in range(10):
        x = threading.Thread(target=req)
        x.start()
        x.join()

    print(time.time() - begin)


if __name__ == "__main__":
    main()
