try:
    1/0
except ArithmeticError as e:
    print(f"{e}, {e.__class__}")