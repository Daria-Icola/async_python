import requests
import time

def main():
    begin = time.time()

    for i in range(10):
        requests.get('https://api.covidtracking.com/v1/us/current.json')

    print(time.time() - begin)


if __name__ == "__main__":
    main()