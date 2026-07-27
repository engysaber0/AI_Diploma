# Casio Console Calculator

A command-line scientific calculator built with Python that supports basic arithmetic, scientific functions, memory operations, calculation history, and degree/radian angle modes. The calculator evaluates mathematical expressions through a custom expression parser without relying on Python's `eval()`.

## Features

### Basic Operations
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)
- Floor Division (`//`)
- Power (`^`)
- Parentheses support

### Scientific Functions
- `sqrt()` – Square Root
- `sq()` – Square
- `cube()` – Cube
- `sin()`
- `cos()`
- `tan()`
- `asin()`
- `acos()`
- `atan()`
- `log()` – Base 10 Logarithm
- `ln()` – Natural Logarithm
- `exp()` – Exponential
- `abs()` – Absolute Value
- `fact()` / `factorial()`
- `!` (Postfix Factorial)

### Constants
- `pi`
- `e`
- `Ans` (Previous Answer)
- `M` (Stored Memory Value)

### Memory Operations
- `MS` – Store current result
- `MR` – Recall memory
- `MC` – Clear memory
- `M+` – Add current result to memory
- `M-` – Subtract current result from memory

### Other Features
- Interactive console interface
- Calculation history
- Degree and Radian modes
- Input validation
- Error handling
- Help menu

---

## Project Structure

```
Calculator/
├── main.py             # Program entry point
├── calculator.py       # Calculator controller
├── parser.py           # Expression parser and evaluator
├── scientific.py       # Scientific functions
├── memory.py           # Memory operations
├── history.py          # Calculation history
├── constants.py        # Commands and help text
├── utils.py            # Utility functions
└── README.md
```


---

## Run the Project

```bash
python main.py
```

---

## Available Commands

| Command | Description |
|---------|-------------|
| `help` | Display the help menu |
| `history` | Show previous calculations |
| `clear` | Clear calculation history |
| `mode` | Display the current angle mode |
| `deg` | Switch to Degree mode |
| `rad` | Switch to Radian mode |
| `ms` | Store the current result in memory |
| `mr` | Recall the stored value |
| `mc` | Clear memory |
| `m+` | Add the current result to memory |
| `m-` | Subtract the current result from memory |
| `exit` / `quit` | Exit the calculator |

---

## Supported Expressions

```text
2 + 3 * 4

(2 + 3)^2

sqrt(144)

sin(30)

log(100)

ln(e)

factorial(5)

5!

Ans * 2

M + 10

pi * 2
```

---

## Example Session

```text
Welcome to the calculator. Type 'help' if u need assistance

Mode   : DEG
Memory : 0
Ans    : 0

> ((25+15)*4-30)/5
26

> sqrt(144)+log(1000)+factorial(5)
135

> sin(30)+cos(60)+tan(45)+pi
5.141592654

> Ans * 2
10.28318531

> ms
Stored Ans into memory.

> mr
10.28318531

> history

1. ((25+15)*4-30)/5 = 26
2. sqrt(144)+log(1000)+factorial(5) = 135
3. sin(30)+cos(60)+tan(45)+pi = 5.141592654

> exit

Good to see U
```

---

## Error Handling

The calculator checks for common errors such as:

- Division by zero
- Invalid mathematical expressions
- Unknown functions
- Unknown constants
- Invalid arguments
- Invalid factorial values
- Empty input

Examples:

```text
> 10 / 0
Error: Division by zero
```

```text
> factorial(-5)
Error: must be positive number
```

```text
> sqrt(-4)
Error: must be positive number
```

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Custom Recursive Descent Parser
- Python Standard Library
  - `math`
  - `re`

---

## Future Improvements

- Hyperbolic functions
- Unit conversion
- Binary, octal, and hexadecimal modes
- Save history to a file
- Colorized terminal interface
- Keyboard shortcuts
- Complex number support

---

<img width="826" height="558" alt="image" src="https://github.com/user-attachments/assets/fd1f00cd-b7ab-49bf-8d73-ed1955bf4e2a" />
<img width="823" height="599" alt="image" src="https://github.com/user-attachments/assets/d61fe780-9faa-45a0-bf12-d58a086a35e5" />
<img width="559" height="85" alt="image" src="https://github.com/user-attachments/assets/73a3a38e-3f6c-4885-9cd7-3a3c9979e0a9" />
