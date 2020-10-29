def series(start, step, operator="+"):
    while True:
        yield start

        if operator == "+":
            start += step
        elif operator == "*":
            start *= step
        else:
            raise ValueError(f"Bad value for operator {operator}")


if __name__ == "__main__":
    g = series(1, 2, "/")

    for one_value in g:
        if one_value > 100:
            break
        print(one_value, end=" ")

