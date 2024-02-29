from time import perf_counter
from math import sqrt

def all_divisors(value: int) -> list:
    res = [1, value]
    for i in range(2, int(sqrt(value))+1):
        if not value % i:
            res.append(int(value / i))
            res.append(i)

    return sorted(res)

def main():
    set_values = [23436, 190187200, 380457890232]

    for i in set_values:
        result = all_divisors(i)
        print(result)

if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print("\n",end - start)
