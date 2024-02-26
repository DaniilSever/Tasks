from time import perf_counter
from numba import njit, prange

@njit(fastmath=True, parallel=True)
def all_divisors(value: int) -> list: 
    res = []
    for i in prange(1, value+1):
        if not value % i:
            res.append(i)
    return sorted(res)

set_values = [23436, 190187200, 380457890232]

for value in set_values:
    result = all_divisors(value)
    print(result)