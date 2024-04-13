from src.decorator import run_time


@run_time
def check_close_brackets(stroke: str) -> bool:
    str_filter = "()"
    for _ in stroke:
        stroke = stroke.replace(str_filter, "")
        if len(stroke) == 0 or len(stroke) == 1:
            break

    if len(stroke) != 0:
        return False
    else:
        return True


set_stroke = ["(())", ")()(", "(()()))"]

new_set = ["((()()(()()()())))", "()(()()()(()()()()()()(()()()()()))))"]

for item in new_set:
    print(check_close_brackets(item))
