import math

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


def to_radians(value, angle_mode):
    """
    function description: converts a value to radians when in degree mode
    :param value: the angle to convert
    :type value: float
    :param angle_mode: either "DEG" or "RAD"
    :type angle_mode: str
    :return: the angle in radians
    :rtype: float
    """
    if angle_mode == "DEG":
        return math.radians(value)
    return value


def to_display_angle(value, angle_mode):
    """
    function description: converts a value from radians back to degrees when in degree mode
    :param value: the angle in radians
    :type value: float
    :param angle_mode: either "DEG" or "RAD"
    :type angle_mode: str
    :return: the angle in the current display mode
    :rtype: float
    """
    if angle_mode == "DEG":
        return math.degrees(value)
    return value


def fact(value):
    """
    function description: calculates the factorial of a number
    :param value: the number to calculate factorial for
    :type value: float
    :raise ValueError: if value is negative or not a whole number
    :return: the factorial of value
    :rtype: int
    """
    if value == 0:
            return 1
    if value == 1:
            return 1
    if value < 0 or value != int(value):
        raise ValueError("must be positive number")
    return math.factorial(int(value))


def recip(value):
    """
    function description: calculates the reciprocal (1/x) of a number
    :param value: the number to invert
    :type value: float
    :raise ValueError: if value is zero.
    :return: the reciprocal of value
    :rtype: float
    """
    if value == 0:
        raise ValueError("can't divide by zero")
    return 1 / value


def sq(value):
    """
    function description: calculates the square of a number
    :param value: the number to square
    :type value: float
    :return: value squared
    :rtype: float
    """
    return value ** 2


def cube(value):
    """
    function description: calculates the cube of a number
    :param value: the number to cube
    :type value: float
    :return: value cubed
    :rtype: float
    """
    return value ** 3


def log10(value):
    """
    function description: calculates the base-10 logarithm of a number.
    :param value: the number to take the logarithm of
    :type value: float
    :raise ValueError: if value is not positive.
    :return: log base 10 of value
    :rtype: float
    """
    if value <= 0:
        raise ValueError("must be positive number")
    return math.log10(value)


def ln(value):
    """
    function description: calculates the natural logarithm of a number
    :param value: the number to take the natural logarithm of
    :type value: float
    :raise ValueError: if value is not positive.
    :return: the natural logarithm of value
    :rtype: float
    """
    if value <= 0:
        raise ValueError("must be positive number")
    return math.log(value)


def sqrt(value):
    """
    function description: calculates the square root of a number
    :param value: the number to take the square root of
    :type value: float
    :raise ValueError: if value is negative.
    :return: the square root of value
    :rtype: float
    """
    if value < 0:
        raise ValueError("must be positive number")
    return math.sqrt(value)


def get_functions(angle_mode):
    """
    function description: builds the table of function names available inside an expression, wrapping trig functions so they respect the current angle mode
    :param angle_mode: either "DEG" or "RAD"
    :type angle_mode: str
    :return: mapping of function name to callable
    :rtype: dict
    """
    return {
        "sin": lambda x: math.sin(to_radians(x, angle_mode)),
        "cos": lambda x: math.cos(to_radians(x, angle_mode)),
        "tan": lambda x: math.tan(to_radians(x, angle_mode)),
        "asin": lambda x: to_display_angle(math.asin(x), angle_mode),
        "acos": lambda x: to_display_angle(math.acos(x), angle_mode),
        "atan": lambda x: to_display_angle(math.atan(x), angle_mode),
        "sqrt": sqrt,
        "log": log10,
        "ln": ln,
        "exp": math.exp,
        "abs": abs,
        "fact": fact,
        "factorial": fact,
        "sq": sq,
        "cube": cube,
        "recip": recip,
    }