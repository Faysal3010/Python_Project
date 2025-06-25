import tkinter as tk
from tkinter import ttk, messagebox
import math
import json
import os


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator - ক্যালকুলেটর")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')

        # Set icon (optional)
        try:
            self.root.iconbitmap("calculator.ico")
        except:
            pass

        # Variables
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.current_input = ""
        self.previous_input = ""
        self.operator = ""
        self.should_reset = False
        self.history = []

        # Load history
        self.load_history()

        # Create UI
        self.create_widgets()

        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()

        # Save history on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Title
        title_label = tk.Label(main_frame, text="🧮 Calculator - ক্যালকুলেটর",
                               font=('Arial', 16, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title_label.pack(pady=(0, 10))

        # Display
        display_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        display_frame.pack(fill=tk.X, pady=(0, 10))

        self.display = tk.Entry(display_frame, textvariable=self.display_var,
                                font=('Courier New', 24, 'bold'), justify=tk.RIGHT,
                                bg='#34495e', fg='black', bd=0, relief=tk.FLAT,
                                state='readonly')
        self.display.pack(fill=tk.X, padx=10, pady=10)

        # Memory display
        self.memory_label = tk.Label(main_frame, text="", font=('Arial', 10),
                                     bg='#2c3e50', fg='#95a5a6')
        self.memory_label.pack()

        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='#2c3e50')
        buttons_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        # Button configurations
        buttons = [
            # Row 1
            [('C', self.clear_all, '#e74c3c', 'white'), ('CE', self.clear_entry, '#e67e22', 'white'),
             ('⌫', self.backspace, '#f39c12', 'white'), ('÷', lambda: self.set_operator('/'), '#3498db', 'white')],

            # Row 2
            [('7', lambda: self.append_number('7'), '#34495e', 'white'),
             ('8', lambda: self.append_number('8'), '#34495e', 'white'),
             ('9', lambda: self.append_number('9'), '#34495e', 'white'),
             ('×', lambda: self.set_operator('*'), '#3498db', 'white')],

            # Row 3
            [('4', lambda: self.append_number('4'), '#34495e', 'white'),
             ('5', lambda: self.append_number('5'), '#34495e', 'white'),
             ('6', lambda: self.append_number('6'), '#34495e', 'white'),
             ('−', lambda: self.set_operator('-'), '#3498db', 'white')],

            # Row 4
            [('1', lambda: self.append_number('1'), '#34495e', 'white'),
             ('2', lambda: self.append_number('2'), '#34495e', 'white'),
             ('3', lambda: self.append_number('3'), '#34495e', 'white'),
             ('+', lambda: self.set_operator('+'), '#3498db', 'white')],

            # Row 5
            [('±', self.toggle_sign, '#95a5a6', 'white'), ('0', lambda: self.append_number('0'), '#34495e', 'white'),
             ('.', lambda: self.append_number('.'), '#34495e', 'white'), ('=', self.calculate, '#27ae60', 'white')],

            # Row 6 - Scientific functions
            [('√', self.square_root, '#9b59b6', 'white'), ('x²', self.square, '#9b59b6', 'white'),
             ('%', lambda: self.set_operator('%'), '#9b59b6', 'white'),
             ('History', self.show_history, '#16a085', 'white')]
        ]

        # Create buttons
        for row_index, row in enumerate(buttons):
            for col_index, (text, command, bg_color, fg_color) in enumerate(row):
                btn = tk.Button(buttons_frame, text=text, command=command,
                                font=('Arial', 12, 'bold'), bg=bg_color, fg=fg_color,
                                relief=tk.RAISED, bd=2, cursor='hand2')
                btn.grid(row=row_index, column=col_index, sticky='nsew', padx=2, pady=2)

                # Hover effects
                btn.bind('<Enter>', lambda e, b=btn, bg=bg_color: self.on_hover(b, bg))
                btn.bind('<Leave>', lambda e, b=btn, bg=bg_color: self.on_leave(b, bg))

        # Configure grid weights
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def on_hover(self, button, original_color):
        # Lighten color on hover
        button.configure(bg=self.lighten_color(original_color))

    def on_leave(self, button, original_color):
        button.configure(bg=original_color)

    def lighten_color(self, color):
        # Simple color lightening
        color_map = {
            '#e74c3c': '#ec7063',
            '#e67e22': '#f1c40f',
            '#f39c12': '#f4d03f',
            '#3498db': '#5dade2',
            '#34495e': '#566573',
            '#27ae60': '#58d68d',
            '#9b59b6': '#bb8fce',
            '#16a085': '#48c9b0',
            '#95a5a6': '#aeb6bf'
        }
        return color_map.get(color, color)

    def append_number(self, number):
        if self.should_reset:
            self.display_var.set("0")
            self.should_reset = False

        current = self.display_var.get()
        if current == "0" and number != ".":
            self.display_var.set(number)
        elif number == "." and "." in current:
            return
        else:
            self.display_var.set(current + number)

    def set_operator(self, op):
        if not self.should_reset and self.operator and self.previous_input:
            self.calculate()

        self.previous_input = self.display_var.get()
        self.operator = op
        self.should_reset = True
        self.update_memory_display()

    def calculate(self):
        if not self.operator or not self.previous_input:
            return

        try:
            prev = float(self.previous_input)
            current = float(self.display_var.get())

            if self.operator == '+':
                result = prev + current
            elif self.operator == '-':
                result = prev - current
            elif self.operator == '*':
                result = prev * current
            elif self.operator == '/':
                if current == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = prev / current
            elif self.operator == '%':
                result = prev % current
            else:
                return

            # Add to history
            operation = f"{prev} {self.get_operator_symbol()} {current} = {result}"
            self.add_to_history(operation)

            # Format result
            if result == int(result):
                result = int(result)

            self.display_var.set(str(result))
            self.reset_calculator()
            self.should_reset = True

        except ValueError:
            messagebox.showerror("Error", "Invalid input!")
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")

    def get_operator_symbol(self):
        symbols = {'+': '+', '-': '−', '*': '×', '/': '÷', '%': '%'}
        return symbols.get(self.operator, self.operator)

    def clear_all(self):
        self.display_var.set("0")
        self.reset_calculator()

    def clear_entry(self):
        self.display_var.set("0")

    def backspace(self):
        current = self.display_var.get()
        if len(current) > 1:
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")

    def toggle_sign(self):
        current = self.display_var.get()
        if current != "0":
            if current.startswith('-'):
                self.display_var.set(current[1:])
            else:
                self.display_var.set('-' + current)

    def square_root(self):
        try:
            current = float(self.display_var.get())
            if current < 0:
                messagebox.showerror("Error", "Cannot calculate square root of negative number!")
                return
            result = math.sqrt(current)
            self.add_to_history(f"√{current} = {result}")
            self.display_var.set(str(result))
            self.should_reset = True
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    def square(self):
        try:
            current = float(self.display_var.get())
            result = current ** 2
            self.add_to_history(f"{current}² = {result}")
            self.display_var.set(str(result))
            self.should_reset = True
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    def reset_calculator(self):
        self.previous_input = ""
        self.operator = ""
        self.update_memory_display()

    def update_memory_display(self):
        if self.operator and self.previous_input:
            self.memory_label.configure(text=f"{self.previous_input} {self.get_operator_symbol()}")
        else:
            self.memory_label.configure(text="")

    def add_to_history(self, operation):
        self.history.insert(0, operation)
        if len(self.history) > 50:
            self.history.pop()

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No calculations in history!")
            return

        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("400x300")
        history_window.configure(bg='#2c3e50')

        # History listbox
        listbox_frame = tk.Frame(history_window, bg='#2c3e50')
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set,
                             font=('Courier New', 10), bg='#34495e', fg='#ecf0f1')
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)

        for item in self.history:
            listbox.insert(tk.END, item)

        # Buttons
        btn_frame = tk.Frame(history_window, bg='#2c3e50')
        btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        clear_btn = tk.Button(btn_frame, text="Clear History",
                              command=lambda: self.clear_history(listbox),
                              bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'))
        clear_btn.pack(side=tk.LEFT, padx=(0, 5))

        close_btn = tk.Button(btn_frame, text="Close",
                              command=history_window.destroy,
                              bg='#95a5a6', fg='white', font=('Arial', 10, 'bold'))
        close_btn.pack(side=tk.RIGHT)

    def clear_history(self, listbox):
        self.history.clear()
        listbox.delete(0, tk.END)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit():
            self.append_number(key)
        elif key in '+-*/':
            self.set_operator(key)
        elif key == '.' or key == ',':
            self.append_number('.')
        elif key == '\r' or key == '=':  # Enter key
            self.calculate()
        elif event.keysym == 'Escape':
            self.clear_all()
        elif event.keysym == 'BackSpace':
            self.backspace()

    def load_history(self):
        try:
            if os.path.exists('calculator_history.json'):
                with open('calculator_history.json', 'r') as f:
                    self.history = json.load(f)
        except:
            self.history = []

    def save_history(self):
        try:
            with open('calculator_history.json', 'w') as f:
                json.dump(self.history, f)
        except:
            pass

    def on_closing(self):
        self.save_history()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


# Create and run the calculator
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()