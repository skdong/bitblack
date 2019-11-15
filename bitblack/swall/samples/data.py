import json
import random

def generate(times=1):
    for _ in range(0, times):
        print(random.randint(1,100))

def main():
    generate(100)

if __name__ == "__main__":
    main()