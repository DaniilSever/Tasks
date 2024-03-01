def check_close_brackets(stroke: str) -> bool:
    str_filter = "()"
    for _ in stroke:
        stroke = stroke.replace(str_filter, "")

    if len(stroke) != 0:
        return False
    else:
        return True


set_stroke = ["(())", ")()(", "(()()))"]

for item in set_stroke:
    print(check_close_brackets(item))
