import requests
import time

def countdown():
    i = 0
    begin = time.time()
    while i < 5_000_000:
        i += 1
    print(f"duration: {time.time() - begin}")

def main():
    begin = time.time()
    for i in range(10):
        countdown()
    print(time.time() - begin)


if __name__ == "__main__":
    main()
