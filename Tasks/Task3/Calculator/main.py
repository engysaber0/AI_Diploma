from calculator import Calculator
from constants import COMMANDS, GOODBYE, HELP_TEXT, WELCOME
from parser import ParserError
from utils import is_empty
def show_status(calc):
    """
    function description: prints the calculator's current mode, memory,and last answer
    :param calc: the active Calculator instance
    :type calc: Calculator
    """
    status = calc.status()
    print(f"Mode   : {status['mode']}")
    print(f"Memory : {status['memory']}")
    print(f"Ans    : {status['ans']}")


def run_command(command, calc):
    """
    function description: handles a recognized command such as help,history, clear,mode, deg, rad, or a memory key
    :param command: the lowercase command word
    :type command: str
    :param calc: the active Calculator instance
    :type calc: Calculator
    :return: False when the app should quit, True otherwise
    :rtype: bool
    """
    if command in ("exit", "quit"):
        print(GOODBYE)
        return False

    if command == "help":
        print(HELP_TEXT)

    elif command == "history":
        if calc.history.is_empty():
            print("empty history")
        else:
            print("History:")
            for line in calc.history.as_lines():
                print(line)

    elif command == "clear":
        calc.history.clear()
        print("History cleared")

    elif command == "mode":
        print(f"current angle mode: {calc.angle_mode}")

    elif command == "deg":
        calc.set_angle_mode("DEG")
        print("Angle mode set to DEG")

    elif command == "rad":
        calc.set_angle_mode("RAD")
        print("Angle mode set to RAD")

    elif command == "mc":
        calc.memory_clear()
        print("Memory cleared")

    elif command == "mr":
        print(f"Memory recall: {calc.memory_recall()}")

    elif command == "ms":
        print(f"Stored Ans into memory. Memory = {calc.memory_store()}")

    elif command == "m+":
        print(f"Added Ans to memory. Memory = {calc.memory_add()}")

    elif command == "m-":
        print(f"Subtracted Ans from memory. Memory = {calc.memory_subtract()}")

    return True

def main():
    """
    function description: main program loop. Shows the status bar,reads a line of input, and either runs it as a command or evaluates it as a math expression
    :return: None
    :rtype: None
    """
    calc = Calculator()
    print(WELCOME)

    running = True
    while running:
        print()
        show_status(calc)
        text = input("> ")

        if is_empty(text):
            continue

        command = text.strip().lower()

        if command in COMMANDS:
            running = run_command(command, calc)
            continue

        try:
            result = calc.run(text)
            print(f"{text} = {result}")
        except ParserError as exc:
            print(f"Error: {exc}")
        except ZeroDivisionError:
            print("can't divide by zero")
        except OverflowError:
            print("out is so large")


if __name__ == "__main__":
    main()