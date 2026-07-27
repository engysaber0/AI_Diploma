HELP_TEXT = """
Commands:
  help to show this help message
  history to show past calculations
  clear to clear history
  mode to show current angle mode
  deg to switch to degree mode
  rad to switch to radian mode
  mc to clear memory
  mr to recall memory
  ms to store in memory
  m+ to add to memory
  m- to subtract from memory
  exit / quit to quit

  expressions:
  2 + 3 * 4
  sin(30) + sqrt(16)
  (2 + 3) ^ 2
  log(100) + ln(e)
  5!
  Ans * 2

 functions:
  sin, cos, tan, asin, acos, atan,
  sqrt, log, ln, exp, abs, fact,
  sq (x^2), cube (x^3)

 constants:
  pi, e, Ans
"""

WELCOME = "Welcome to the calculator. Type 'help' if u need assistance"

GOODBYE = "Good to see U"

COMMANDS = {
    "help", "history", "clear",
    "mode", "deg", "rad",
    "mc", "mr", "ms", "m+", "m-",
    "exit", "quit",
}
