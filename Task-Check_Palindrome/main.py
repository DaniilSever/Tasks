def check_palindrome(word: str) -> str:
    tmp, revers_tmp = [], []
    for i in word:
        tmp.append(i)

    while " " in tmp:
        tmp.remove(" ")

    while "," in tmp:
        tmp.remove(",")

    tmp = [i.lower() for i in tmp]
    revers_tmp = tmp[::-1]

    if revers_tmp == tmp:
        return "Строка является полиндромом"
    else:
        return "Строка не является полиндромом"


print(check_palindrome("Яд Ефрему, а умер Федя"))
