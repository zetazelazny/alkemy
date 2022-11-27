def sumar(num1: int | float,
          num2: int | float) -> int | float | None:
    try:
        result = num1 + num2
    except ValueError:
        raise (ValueError)
    return result


def restar(num1: int | float,
           num2: int | float) -> int | float | None:
    try:
        result = num1 - num2
    except ValueError:
        raise (ValueError)
    return result


def multiplicar(num1: int | float,
                num2: int | float) -> int | float | None:
    try:
        result = num1 * num2
    except ValueError:
        raise (ValueError)
    return result


def dividir(num1: int | float,
            num2: int | float) -> int | float | None:
    try:
        result = num1 / num2
    except ZeroDivisionError:
        raise (ZeroDivisionError)
    except ValueError:
        raise (ValueError)
    return result
