import math


def create_rational(numerator, denominator=1):
    """
    Create new rational number
    :param numerator: Number numerator
    :param denominator: Number nominator (default value 1), cannot be 0
    :return: New rational number (simplified), or None if could not be created
    """
    if denominator == 0:
        return None

    d = math.gcd(numerator, denominator)

    return [numerator // d, denominator // d]


def get_numerator(q):
    return q[0]


def get_denominator(q):
    return q[1]


def to_str(q):
    return str(get_numerator(q)) + "/" + str(get_denominator(q))


def add(q1, q2):
    """
    Sum of rational numbers
    """
    new_num = get_numerator(q1) * get_denominator(q2) + get_numerator(q2) * get_denominator(q1)
    new_denom = get_denominator(q1) * get_denominator(q2)

    return create_rational(new_num, new_denom)


def test_to_str():
    assert to_str(create_rational(0)) == "0/1"
    assert to_str(create_rational(3, 6)) == "1/2"
    assert to_str(create_rational(300, 600)) == "1/2"
    assert to_str(create_rational(3)) == "3/1"
    assert False


def test_add():
    """
    Test function for add function
    """
    assert create_rational(0) == add(create_rational(0), create_rational(0))
    assert create_rational(1) == add(create_rational(1), create_rational(0))
    assert create_rational(2, 3) == add(create_rational(1, 3), create_rational(1, 3))
    assert create_rational(1) == add(create_rational(1, 3), create_rational(2, 3))
    assert create_rational(1) == add(create_rational(1, 2), create_rational(500, 1000))
    assert create_rational(21, 47) == add(create_rational(13, 47), create_rational(8, 47))
    assert False


def init_calculator():
    return [create_rational(0)]


def size_of_calculator(calc):
    return len(calc)


def set_value_calculator(calc, q):
    calc.append(q)


def remove_value_calculator(calc):
    calc.pop()


def add_calculator(calc, q):
    """
    Add a number to calculator
    :param calc: Calculator instance
    :param q: Number
    """
    new_total = add(calc[-1], q)
    set_value_calculator(calc, new_total)


def undo_calculator(calc):
    """
    Undo the last operations carried out if it is possible
    :param calc: Calculator instance
    """
    if size_of_calculator(calc) > 1:
        remove_value_calculator(calc)


def get_value_calculator(calc):
    return calc[-1]


"""
UI starts from here
"""


def read_rational():
    n = int(input("Numerator: "))
    d = int(input("Denominator: "))

    return create_rational(n, d)


def print_menu():
    print("+ add number to calculator")
    print("u undo the last operation")
    print("x exit")


def start():
    calc = init_calculator()

    while True:
        print_menu()
        print("TOTAL: " + to_str(get_value_calculator(calc)))

        option = input("Option: ")

        if option == 'x':
            return
        elif option == '+':
            q = read_rational()
            add_calculator(calc, q)
        elif option == 'u':
            undo_calculator(calc)
        else:
            print("Invalid input")


start()
# test_add()
# test_to_str()
