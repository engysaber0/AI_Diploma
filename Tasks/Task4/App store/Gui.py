import tkinter as tk
from tkinter import ttk, messagebox

from login_system import LoginSystem
from product import Product
from store import Store
BG = "#12121c"
CARD = "#1b1b2b"
CARD_ALT = "#20223a"
BORDER = "#2c2f4a"
ACCENT = "#7c9dff"    
ACCENT_HOVER = "#93b0ff"
ACCENT_DARK = "#5a78e0"
DANGER = "#ff6b81"
SUCCESS = "#5ee6b0"
TEXT = "#eef0fb"
TEXT_MUTED = "#9a9dc2"

FONT_FAMILY = "Segoe UI"
F_TITLE = (FONT_FAMILY, 20, "bold")
F_SUBTITLE = (FONT_FAMILY, 11)
F_SECTION = (FONT_FAMILY, 13, "bold")
F_BODY = (FONT_FAMILY, 10)
F_BODY_BOLD = (FONT_FAMILY, 10, "bold")
F_BUTTON = (FONT_FAMILY, 10, "bold")


class AppWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("Nova Store")
        self.root.geometry("640x640")
        self.root.minsize(560, 560)
        self.root.configure(bg=BG)

        self._build_style()

        self.login_system = LoginSystem("Engy", "engy1234?")

        products = [
            Product("MacBook Air M3", 1299, 10),
            Product("iPhone 16", 999, 15),
            Product("Samsung Galaxy S25", 899, 12),
            Product("iPad Air", 599, 8),
            Product("Apple Watch Series 10", 399, 10),
            Product("Sony WH-1000XM5 Headphones", 349, 20),
            Product("Logitech MX Master 3S Mouse", 99, 18),
            Product("Keychron K2 Keyboard", 89, 14),
            Product("Dell UltraSharp U2723QE Monitor", 549, 6),
            Product("Samsung T9 Portable SSD 1TB", 149, 16),
            Product("Anker 737 Power Bank", 129, 25),
            Product("GoPro HERO13 Black", 399, 7),
            Product("Canon EOS R50 Camera", 679, 5),
            Product("PlayStation 5 Slim", 499, 9),
            Product("Nintendo Switch OLED", 349, 11),
        ]
        self.store = Store(products)
        self.order_list = []

        self.current_frame = None
        self.show_login_screen()

    def _build_style(self):
        style = ttk.Style(self.root)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(".", background=BG, foreground=TEXT, font=F_BODY)

        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=CARD)

        style.configure("TLabel", background=BG, foreground=TEXT, font=F_BODY)
        style.configure("Title.TLabel", background=BG, foreground=TEXT, font=F_TITLE)
        style.configure("Subtitle.TLabel", background=BG, foreground=TEXT_MUTED, font=F_SUBTITLE)
        style.configure("Section.TLabel", background=BG, foreground=TEXT, font=F_SECTION)
        style.configure("Muted.TLabel", background=BG, foreground=TEXT_MUTED, font=F_BODY)
        style.configure("Card.TLabel", background=CARD, foreground=TEXT, font=F_BODY)
        style.configure("Price.TLabel", background=BG, foreground=SUCCESS, font=(FONT_FAMILY, 18, "bold"))

        style.configure(
            "TEntry",
            fieldbackground=CARD_ALT,
            background=CARD_ALT,
            foreground=TEXT,
            insertcolor=TEXT,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            borderwidth=1,
            relief="flat",
            padding=8,
        )
        style.map("TEntry", bordercolor=[("focus", ACCENT)])

        style.configure(
            "TCombobox",
            fieldbackground=CARD_ALT,
            background=CARD_ALT,
            foreground=TEXT,
            arrowcolor=TEXT,
            bordercolor=BORDER,
            padding=6,
        )
        self.root.option_add("*TCombobox*Listbox.background", CARD_ALT)
        self.root.option_add("*TCombobox*Listbox.foreground", TEXT)
        self.root.option_add("*TCombobox*Listbox.selectBackground", ACCENT)

        style.configure(
            "Accent.TButton",
            background=ACCENT,
            foreground="#0d0d17",
            font=F_BUTTON,
            padding=(14, 10),
            borderwidth=0,
            relief="flat",
        )
        style.map(
            "Accent.TButton",
            background=[("active", ACCENT_HOVER), ("pressed", ACCENT_DARK)],
        )

        style.configure(
            "Ghost.TButton",
            background=CARD_ALT,
            foreground=TEXT,
            font=F_BUTTON,
            padding=(14, 10),
            borderwidth=1,
            bordercolor=BORDER,
            relief="flat",
        )
        style.map(
            "Ghost.TButton",
            background=[("active", "#282a48")],
            bordercolor=[("active", ACCENT)],
        )

        style.configure(
            "Danger.TButton",
            background=CARD_ALT,
            foreground=DANGER,
            font=F_BUTTON,
            padding=(14, 10),
            borderwidth=1,
            bordercolor=BORDER,
            relief="flat",
        )
        style.map("Danger.TButton", background=[("active", "#2a1c24")], bordercolor=[("active", DANGER)])

        style.configure("TRadiobutton", background=BG, foreground=TEXT, font=F_BODY)
        style.map("TRadiobutton", foreground=[("active", ACCENT)])

        style.configure(
            "Treeview",
            background=CARD,
            fieldbackground=CARD,
            foreground=TEXT,
            rowheight=30,
            borderwidth=0,
            font=F_BODY,
        )
        style.configure(
            "Treeview.Heading",
            background=CARD_ALT,
            foreground=TEXT_MUTED,
            font=F_BODY_BOLD,
            borderwidth=0,
            relief="flat",
        )
        style.map(
            "Treeview",
            background=[("selected", ACCENT)],
            foreground=[("selected", "#0d0d17")],
        )
        style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])

        style.configure(
            "Vertical.TScrollbar",
            background=CARD_ALT,
            troughcolor=BG,
            bordercolor=BG,
            arrowcolor=TEXT_MUTED,
            relief="flat",
        )

    def _style_tree_stripes(self, tree):
        tree.tag_configure("odd", background=CARD)
        tree.tag_configure("even", background=CARD_ALT)

    def _insert_striped(self, tree, iid, text, values):
        tag = "even" if len(tree.get_children()) % 2 == 0 else "odd"
        tree.insert("", "end", iid=iid, text=text, values=values, tags=(tag,))

    def _card(self, parent, **pack_kwargs):
        outer = tk.Frame(parent, bg=BORDER)
        inner = ttk.Frame(outer, style="Card.TFrame", padding=16)
        inner.pack(fill="both", expand=True, padx=1, pady=1)
        outer.pack(**pack_kwargs)
        return inner

    def _header(self, parent, title, subtitle=None, icon=""):
        wrap = ttk.Frame(parent)
        wrap.pack(fill="x", pady=(0, 18))
        title_text = (icon + "  " + title).strip()
        ttk.Label(wrap, text=title_text, style="Title.TLabel").pack(anchor="w")
        if subtitle:
            ttk.Label(wrap, text=subtitle, style="Subtitle.TLabel").pack(anchor="w", pady=(4, 0))

    def _make_scrollable(self, parent):
        container = ttk.Frame(parent)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        inner = ttk.Frame(canvas)
        inner_window = canvas.create_window((0, 0), window=inner, anchor="nw")

        def on_inner_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_canvas_configure(event):
            canvas.itemconfig(inner_window, width=event.width)

        inner.bind("<Configure>", on_inner_configure)
        canvas.bind("<Configure>", on_canvas_configure)

        def on_mousewheel(event):
            if event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")
            else:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def bind_wheel(_event):
            canvas.bind_all("<MouseWheel>", on_mousewheel)
            canvas.bind_all("<Button-4>", on_mousewheel)
            canvas.bind_all("<Button-5>", on_mousewheel)

        def unbind_wheel(_event):
            canvas.unbind_all("<MouseWheel>")
            canvas.unbind_all("<Button-4>")
            canvas.unbind_all("<Button-5>")

        canvas.bind("<Enter>", bind_wheel)
        canvas.bind("<Leave>", unbind_wheel)

        return inner

    def clear_screen(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    def _new_screen(self):
        frame = ttk.Frame(self.root, padding=28)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame
        return frame

    def show_login_screen(self):
        self.clear_screen()
        frame = self._new_screen()
        frame.pack_configure(fill="both", expand=True)

        center = ttk.Frame(frame)
        center.place(relx=0.5, rely=0.42, anchor="center")

        self._header(center, "Pulse Electronics Store", "Sign in to continue")

        card = self._card(center, fill="x")
        card.configure(padding=22)

        ttk.Label(card, text="Username", style="Card.TLabel", font=F_BODY_BOLD).pack(anchor="w")
        username_box = ttk.Entry(card, width=32)
        username_box.pack(fill="x", pady=(6, 14))
        username_box.focus_set()

        ttk.Label(card, text="Password", style="Card.TLabel", font=F_BODY_BOLD).pack(anchor="w")
        password_box = ttk.Entry(card, show="•", width=32)
        password_box.pack(fill="x", pady=(6, 18))

        def handle_login():
            typed_username = username_box.get()
            typed_password = password_box.get()

            if not self.login_system.check_username(typed_username):
                messagebox.showerror("Login", "Username incorrect")
                return
            if not self.login_system.check_password(typed_password):
                messagebox.showerror("Login", "Password incorrect")
                return

            code = self.login_system.make_code()
            messagebox.showinfo("Verification code", "Your verification code is " + str(code))
            self.show_verify_screen()

        password_box.bind("<Return>", lambda e: handle_login())
        ttk.Button(card, text="Log In", style="Accent.TButton", command=handle_login).pack(fill="x")

    def show_verify_screen(self):
        self.clear_screen()
        frame = self._new_screen()

        center = ttk.Frame(frame)
        center.place(relx=0.5, rely=0.42, anchor="center")

        self._header(center, "Verify It's You", "Enter the code we just showed you")

        card = self._card(center, fill="x")
        card.configure(padding=22)

        ttk.Label(card, text="Verification code", style="Card.TLabel", font=F_BODY_BOLD).pack(anchor="w")
        code_box = ttk.Entry(card, width=32)
        code_box.pack(fill="x", pady=(6, 18))
        code_box.focus_set()

        def handle_verify():
            typed_code = code_box.get()
            try:
                typed_code = int(typed_code)
            except ValueError:
                messagebox.showerror("Verify", "Code has to be a number")
                return

            if not self.login_system.check_code(typed_code):
                messagebox.showerror("Verify", "Verification code incorrect")
                return

            self.order_list = []
            messagebox.showinfo("Login", "Welcome!")
            self.show_catalog_screen()

        code_box.bind("<Return>", lambda e: handle_verify())
        ttk.Button(card, text="Verify", style="Accent.TButton", command=handle_verify).pack(fill="x")

    def show_catalog_screen(self):
        self.clear_screen()
        frame = self._new_screen()

        top = ttk.Frame(frame)
        top.pack(fill="x", pady=(0, 14))
        ttk.Label(top, text="Store Catalog", style="Title.TLabel").pack(side="left")
        ttk.Button(top, text="Log Out", style="Danger.TButton", command=self.show_login_screen).pack(side="right")

        button_row = ttk.Frame(frame)
        button_row.pack(fill="x", side="bottom", pady=(14, 0))

        body = self._make_scrollable(frame)

        table_card = self._card(body, fill="x")
        product_table = ttk.Treeview(table_card, columns=("price", "stock"), show="headings", height=6)
        product_table.heading("price", text="Price ($)")
        product_table.heading("stock", text="In Stock")
        product_table.column("price", anchor="center", width=100)
        product_table.column("stock", anchor="center", width=100)
        product_table["show"] = "tree headings"
        product_table.heading("#0", text="Product")
        product_table.column("#0", width=260)
        self._style_tree_stripes(product_table)
        product_table.pack(fill="x")

        def refresh_product_table():
            for row in product_table.get_children():
                product_table.delete(row)
            for product_item in self.store.products:
                self._insert_striped(
                    product_table, product_item.name, product_item.name,
                    (product_item.price, product_item.stock),
                )

        refresh_product_table()

        pick_card = self._card(body, fill="x", pady=(14, 0))
        pick_frame = pick_card

        ttk.Label(pick_frame, text="Product name", style="Card.TLabel", font=F_BODY_BOLD).grid(row=0, column=0, sticky="w")
        name_box = ttk.Entry(pick_frame)
        name_box.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(6, 0))

        ttk.Label(pick_frame, text="Quantity", style="Card.TLabel", font=F_BODY_BOLD).grid(row=0, column=1, sticky="w")
        quantity_box = ttk.Entry(pick_frame, width=10)
        quantity_box.grid(row=1, column=1, sticky="ew", pady=(6, 0))

        pick_frame.columnconfigure(0, weight=1)

        cart_section = ttk.Frame(body)
        cart_section.pack(fill="x", pady=(16, 0))
        ttk.Label(cart_section, text="Your Cart", style="Section.TLabel").pack(anchor="w", pady=(0, 8))

        cart_card = self._card(cart_section, fill="x")
        cart_table = ttk.Treeview(cart_card, columns=("amount", "discount", "price"), show="headings", height=5)
        cart_table.heading("amount", text="Qty")
        cart_table.heading("discount", text="Discount")
        cart_table.heading("price", text="Price ($)")
        cart_table.column("amount", anchor="center", width=70)
        cart_table.column("discount", anchor="center", width=90)
        cart_table.column("price", anchor="center", width=100)
        cart_table["show"] = "tree headings"
        cart_table.heading("#0", text="Product")
        cart_table.column("#0", width=240)
        self._style_tree_stripes(cart_table)
        cart_table.pack(fill="x")

        def refresh_cart_table():
            for row in cart_table.get_children():
                cart_table.delete(row)
            for order_item in self.order_list:
                self._insert_striped(
                    cart_table, order_item["name"] + str(id(order_item)), order_item["name"],
                    (order_item["amount"], str(order_item["discount"]) + "%", order_item["price"]),
                )

        refresh_cart_table()

        def handle_add_to_cart():
            name = name_box.get()
            item = self.store.find_product(name)
            if item is None:
                messagebox.showerror("Add to cart", "Product not found")
                return

            try:
                amount = int(quantity_box.get())
            except ValueError:
                messagebox.showerror("Add to cart", "Quantity has to be a number")
                return

            if amount <= 0 or amount > item.stock:
                messagebox.showerror("Add to cart", "Quantity not available")
                return

            discount, price_after = self.store.work_out_discount(amount, item.price)
            item.take_from_stock(amount)

            self.order_list.append({
                "name": item.name,
                "amount": amount,
                "discount": discount,
                "price": round(price_after, 2),
            })

            refresh_product_table()
            refresh_cart_table()
            name_box.delete(0, "end")
            quantity_box.delete(0, "end")
            messagebox.showinfo("Add to cart", item.name + " added, discount " + str(discount) + "%")

        ttk.Button(
            pick_frame, text="＋ Add to Cart", style="Accent.TButton", command=handle_add_to_cart
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(14, 0))

        def go_to_checkout():
            if not self.order_list:
                messagebox.showerror("Checkout", "Cart is empty")
                return
            self.show_checkout_screen()

        ttk.Button(button_row, text="Checkout →", style="Accent.TButton", command=go_to_checkout).pack(
            side="right"
        )

    def show_checkout_screen(self):
        self.clear_screen()
        frame = self._new_screen()

        self._header(frame, "Checkout", "Review your order and confirm")

        button_row = ttk.Frame(frame)
        button_row.pack(fill="x", side="bottom", pady=(20, 0))

        body = self._make_scrollable(frame)

        cart_card = self._card(body, fill="x")
        cart_table = ttk.Treeview(cart_card, columns=("amount", "discount", "price"), show="headings", height=5)
        cart_table.heading("amount", text="Qty")
        cart_table.heading("discount", text="Discount")
        cart_table.heading("price", text="Price ($)")
        cart_table.column("amount", anchor="center", width=70)
        cart_table.column("discount", anchor="center", width=90)
        cart_table.column("price", anchor="center", width=100)
        cart_table["show"] = "tree headings"
        cart_table.heading("#0", text="Product")
        cart_table.column("#0", width=240)
        self._style_tree_stripes(cart_table)
        cart_table.pack(fill="x")

        for order_item in self.order_list:
            self._insert_striped(
                cart_table, order_item["name"] + str(id(order_item)), order_item["name"],
                (order_item["amount"], str(order_item["discount"]) + "%", order_item["price"]),
            )

        options_card = self._card(body, fill="x", pady=(16, 0))

        ttk.Label(options_card, text="Delivery or Pick-up", style="Card.TLabel", font=F_BODY_BOLD).pack(anchor="w")
        delivery_choice = tk.StringVar(value="pick-up")
        ttk.Radiobutton(options_card, text="Delivery ($200)", variable=delivery_choice, value="delivery").pack(
            anchor="w", pady=(8, 0)
        )
        ttk.Radiobutton(options_card, text="Pick-up ($50)", variable=delivery_choice, value="pick-up").pack(
            anchor="w", pady=(4, 0)
        )

        ttk.Label(options_card, text="Currency", style="Card.TLabel", font=F_BODY_BOLD).pack(anchor="w", pady=(16, 0))
        currency_choice = ttk.Combobox(
            options_card, values=list(self.store.CURRENCY_RATES.keys()), state="readonly"
        )
        currency_choice.set("USD")
        currency_choice.pack(fill="x", pady=(6, 0))

        def handle_confirm_order():
            shipping_cost = 200 if delivery_choice.get() == "delivery" else 50
            currency = currency_choice.get()
            if currency not in self.store.CURRENCY_RATES:
                currency = "USD"

            subtotal = sum(order_item["price"] for order_item in self.order_list)
            total_usd = subtotal + shipping_cost
            total = total_usd * self.store.CURRENCY_RATES[currency]

            self.order_list = []
            self.show_confirm_screen(round(total, 2), currency)

        ttk.Button(button_row, text="← Back to Catalog", style="Ghost.TButton", command=self.show_catalog_screen).pack(
            side="left"
        )
        ttk.Button(button_row, text="Confirm Order", style="Accent.TButton", command=handle_confirm_order).pack(
            side="right"
        )

    def show_confirm_screen(self, total, currency):
        self.clear_screen()
        frame = self._new_screen()

        center = ttk.Frame(frame)
        center.place(relx=0.5, rely=0.45, anchor="center")

        ttk.Label(center, text="✓", foreground=SUCCESS, font=(FONT_FAMILY, 36, "bold")).pack(pady=(0, 6))
        ttk.Label(center, text="Order Confirmed", style="Title.TLabel").pack()
        ttk.Label(
            center, text="Your order is on its way, thank you for your purchase",
            style="Subtitle.TLabel",
        ).pack(pady=(6, 20))

        total_card = self._card(center, pady=(0, 22))
        total_card.configure(padding=(30, 18))
        ttk.Label(total_card, text="Total Charged", style="Card.TLabel").pack()
        ttk.Label(total_card, text=str(total) + " " + currency, style="Price.TLabel").pack(pady=(4, 0))

        ttk.Button(center, text="Back to Store", style="Accent.TButton", command=self.show_catalog_screen).pack(
            fill="x"
        )


def main():
    root = tk.Tk()
    AppWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()