# App Store 🛒

A small Python electronics store simulator with a login flow, a product catalog, quantity-based discounts, delivery/pick-up shipping, and multi-currency checkout.

The project ships in two forms that share the same underlying logic (`login_system.py`, `product.py`, `store.py`):

| Entry point | Interface | Description |
|---|---|---|
| `main.py` | Command line (terminal) | Text-based prompts, run entirely in the console |
| `Gui.py` *(built from `app.py`)* | Graphical (Tkinter) | Dark-themed desktop window with tables, buttons, and a scrollable catalog/checkout |

---

## Features

- **Login + verification** — username/password check followed by a randomly generated 4-digit verification code
- **Product catalog** — 15 starter electronics with live stock tracking
- **Quantity discounts** — 5% off per 5 units purchased, capped at 25%
- **Shopping cart** — add multiple products before checking out
- **Shipping options** — Delivery ($200) or Pick-up ($50)
- **Multi-currency checkout** — USD, EUR, EGP (converted from a fixed rate table)
- **Order confirmation** — final total shown in the chosen currency
- **GUI version** — modern dark theme, card-style panels, striped tables, and mouse-wheel scrolling on the catalog and checkout screens

---

## Project structure

```
app-store/
├── main.py            # CLI entry point
├── Gui.py              # GUI entry point (Tkinter, styled)
├── login_system.py    # LoginSystem class — username/password/code checks
├── product.py          # Product class — name, price, stock
├── store.py             # Store class — catalog, cart, discounts, checkout, CLI flow
└── README.md
```

> Note: the GUI file only needs to sit in the same folder as `login_system.py`, `product.py`, and `store.py` — it imports the same classes the CLI version uses, so business logic (discounts, currency rates, stock handling) is identical in both.

---

## Requirements

- Python 3.7+
- No third-party packages — everything used (`tkinter`, `random`) is part of the Python standard library

> On some Linux distributions Tkinter isn't installed by default. If `import tkinter` fails, install it with:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## Getting started

1. Clone or download the project files into a single folder.
2. Make sure `login_system.py`, `product.py`, `store.py`, and whichever entry point you want to run (`main.py` or `Gui.py`) are all in that same folder.
3. Run one of the two versions:

```bash
# Command-line version
python main.py

# GUI version
python Gui.py
```

### Default login credentials

| Field | Value |
|---|---|
| Username | `Engy` |
| Password | `engy1234?` |

The verification code is generated randomly each login (shown in the terminal for the CLI version, in a pop-up for the GUI version) — you'll need to type it back in to get past the verify step.

---

## How it works

### 1. Login flow
`LoginSystem` checks the typed username and password against the stored ones, then generates a random 4-digit code (`make_code`) that must be re-entered correctly (`check_code`) before the store unlocks.

### 2. Browsing & adding to cart
The catalog (`Store.products`) lists each `Product`'s name, price, and remaining stock. Picking a product and a quantity runs it through `work_out_discount`, which applies:

```
discount % = (quantity // 5) * 5     # capped at 25%
price_after = price * quantity * (1 - discount / 100)
```

Stock is reduced immediately (`Product.take_from_stock`) once an item is added to the cart.

### 3. Checkout
Once the cart has at least one item, checkout asks for:
- **Shipping**: Delivery ($200) or Pick-up ($50)
- **Currency**: USD, EUR, or EGP (via `Store.CURRENCY_RATES`)

The final total is the discounted subtotal plus shipping, converted into the chosen currency.

### 4. Confirmation
A summary screen (or printed message in the CLI) shows the final total and confirms the order.

---

## Currency rates

Defined in `Store.CURRENCY_RATES` — edit these values to adjust conversion rates:

```python
CURRENCY_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "EGP": 48.0,
}
```

---

## Customizing the catalog

Products are defined as a plain list of `Product(name, price, stock)` objects — in `main.py`'s `make_products()` for the CLI, and inside `AppWindow.__init__` for the GUI. Add, remove, or edit entries there to change what's for sale.

---

## GUI notes

- Built with `tkinter.ttk` and a custom dark color palette (see the constants at the top of `Gui.py` — `BG`, `ACCENT`, `CARD`, etc. — to re-theme it).
- The **Catalog** and **Checkout** screens scroll (mouse wheel or trackpad) if content doesn't fit the window, while headers and action buttons stay pinned in place.
- Icons are plain BMP-safe Unicode symbols (no emoji) to avoid `_tkinter.TclError` crashes on older Tcl/Tk builds (common on some Windows Python installs).

---

## Known limitations

- Data isn't persisted — restarting the app resets stock levels and the cart.
- Only one user account is supported (hardcoded in `main.py` / `Gui.py`).
- No input sanitization beyond basic type/range checks (e.g., no protection against extremely large quantities).

