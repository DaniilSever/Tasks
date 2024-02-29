def del_space_stroke(stroke: str):
    tmp = []
    for word in stroke:
        tmp.append(word)

    while " " in tmp:
        tmp.remove(" ")

    return "".join(str(element) for element in tmp)


print(del_space_stroke(" Hello World !  "))
