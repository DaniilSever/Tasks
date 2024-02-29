def check_simple_number(value: int) -> str:
    res = [1, value]
    for i in range(2, value-1):
        if i**2 == value:
            break
        
        if not value % i:
            res.append(i)
    if len(res) == 2:
        return "Простое число"
    else:
        return "Сложное число"
    
print(check_simple_number(100))