from tkinter import *
from tkinter.messagebox import showerror
from support import int_list_creator, _gcd
from os import remove
from random import randint


class IntegerValueError(Exception):
    pass


class AmountError(Exception):
    pass


class AmountValueError(Exception):
    pass


def integer_value_error_message(_reason, index=None):
    message = "Incorrect input, you are supposed to enter single integer bigger than 0." \
              f"\nBut you entered -> '{_reason}'"
    if _reason == '0' and index is not None:
        message += f' in position {index + 1}, index -> {index}.'
    else:
        message += '.'
    showerror(title="Error", message=message)


def amount_value_error_message(_reason):
    message = 'Incorrect input, you are supposed to enter single integer bigger than 1.' \
              f'\nBut you entered -> {_reason} in position 2, index -> 1.'
    showerror(title="Error", message=message)


def amount_error_message(amount, _type: str):
    word = example = args = ""
    if _type == "full":
        word = "two"
        example = "120, 2"
        args = "First argument is max possible integer,\nsecond - amount" \
               f"\nBut you entered only {amount}"
    elif _type == "custom":
        word = "multiple"
        example = "12, 6, 24"
        args = f"\nBut you entered only {amount}"
    message = f"Incorrect input, you are supposed to enter {word} integers " \
              f"\n(e.g. {example}). {args}."
    showerror(title="Error", message=message)


class MainAppBody(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("500x250")
        self.title("GCD app")
        self.iconbitmap("icon.ico")
        self.resizable(0, 0)
        container = Frame(self, bg="black")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        frame_collection = (StartPage, GeneratorHome, CustomMainPage, FullControlPage, MaxNumberControlPage,
                            MaxNumberResultsPage, CustomResultsPage, FullControlResultsPage)

        for frame in frame_collection:
            current_frame = frame(container, self)

            self.frames[frame] = current_frame

            current_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="Black")

        text = "This program generates from 2 up to 20 (Generator)\n" \
               "or takes user's (Custom)\n" \
               "integers and finds their greatest common divisor,"

        label = Label(self, text=text, font=("Times New Roman", 16), bg="black", fg="#00ff00")
        label.pack(padx=5, pady=10, fill=BOTH)

        generator_home_button = Button(self, text="Generator", bg="#0a0a0c", fg="#00ff00", font=("Colibri", 30),
                                       activeforeground="green", activebackground="black", bd=0,
                                       command=lambda: controller.show_frame(GeneratorHome))
        generator_home_button.pack(fill=BOTH)

        custom_home_button = Button(self, text="Custom", bg="#0a0c0a", fg="#00ff00", font=("Colibri", 30),
                                    activeforeground="green", activebackground="black", bd=0,
                                    disabledforeground="black",
                                    command=lambda: controller.show_frame(CustomMainPage))
        custom_home_button.pack(side=BOTTOM, fill=BOTH)


class GeneratorHome(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="Black")

        text = "Welcome to generator.\nHere you can pick generator type:"

        label = Label(self, text=text, font=("Times New Roman", 18), bg="black", fg="#00ff00")
        label.pack(padx=5, pady=10, fill=BOTH)

        home_button = Button(self, text="Return home", bg="#0a0a0a", fg="#00ff00", font=("Colibri", 23),
                             activeforeground="green", activebackground="black", bd=0,
                             command=lambda: controller.show_frame(StartPage))
        home_button.pack(fill=BOTH, side=BOTTOM)

        full_ctrl_page = Button(self, text="full control", bg="#0a0c0a", fg="#00ff00", font=("Colibri", 23),
                                activeforeground="green", activebackground="black", bd=0, disabledforeground="black",
                                command=lambda: controller.show_frame(FullControlPage))
        full_ctrl_page.pack(side=BOTTOM, fill=BOTH, pady=1)

        max_num_page = Button(self, text="max number control", bg="#0c0a0a", fg="#00ff00", font=("Colibri", 23),
                              activeforeground="green", activebackground="black", bd=0, disabledforeground="black",
                              command=lambda: controller.show_frame(MaxNumberControlPage))
        max_num_page.pack(fill=BOTH)


class MaxNumberControlPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")
        self.controller = controller

        text = "Enter largest possible integer to continue." \
               "\nAfter pressing 'Confirm' program will check" \
               "\nif input is valid else it will show you an error."

        label = Label(self, text=text, font=("Times New Roman", 16), bg="black", fg="#00ff00")
        label.pack(padx=5, pady=10, fill=BOTH)

        def check_if_valid():
            _input = entry.get()
            try:
                if _input.isdigit() and _input != "0":
                    _input = int(_input)
                else:
                    raise IntegerValueError
                entry.delete(0, END)
                entry.insert(0, '')
                file = open("temporary_storage.txt", 'w')
                file.seek(0)
                file.write(str(_input))
                file.close()
                return True
            except IntegerValueError:
                entry.delete(0, END)
                integer_value_error_message(_input)

        entry = Entry(self, bg="black", fg="#00ff00", font=("Times New Roman", 20),
                      selectbackground="white", selectforeground="#ff00ff",
                      width=250, highlightthickness=1, insertbackground="white")
        entry.config(highlightbackground="green", highlightcolor="light green")
        entry.pack()

        confirm_button = Button(self, bg="#0a0c0a", fg="#00ff00", font=("Colibri", 23),
                                activeforeground="green", activebackground="black", bd=0, text="Confirm",
                                command=lambda: controller.show_frame(MaxNumberResultsPage)
                                if check_if_valid() else None)
        confirm_button.pack(fill=BOTH)

        def clicked_return_button():
            entry.delete(0, END)
            controller.show_frame(GeneratorHome)

        return_button = Button(self, text="Return to previous page", bg="#0a0a0a",
                               fg="#00ff00", font=("Colibri", 23), command=clicked_return_button,
                               activeforeground="green", activebackground="black", bd=0)
        return_button.pack(fill=BOTH, side=BOTTOM)


class MaxNumberResultsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")

        def getting_results():
            file = open('temporary_storage.txt', 'r')
            limit = file.read()
            file.close()
            remove("temporary_storage.txt")
            amount = randint(2, 20)
            text_area.delete("1.0", END)
            results = int_list_creator(amount, int(limit))
            string_results = ', '.join(map(str, results))
            text_area.insert('0.0', f"Generated {amount} numbers in range from 1 to {limit}:\n")
            text_area.insert(END, string_results)
            text_area.insert(END, "\nGreatest common divisor: ")
            text_area.insert(END, str(_gcd(results)) + '\n')
            text_area.config(state=DISABLED)
            home_button.config(state=ACTIVE)
            launch_button.config(state=DISABLED)

        def return_to_home():
            text_area.config(state=NORMAL)
            text_area.delete("1.0", END)
            text_area.insert('0.0', text)
            home_button.config(state=DISABLED)
            launch_button.config(state=ACTIVE)
            controller.show_frame(StartPage)

        text = 'Press "Finish" button to get results, or type here for fun'

        text_area = Text(self, font=("Times New Roman", 13), bg="black", fg="#00ff00",
                         selectbackground="white", selectforeground="#ff00ff",
                         insertbackground="white", width=55, height=6, wrap=WORD)
        text_area.insert("0.0", text)
        text_area.pack(padx=5, pady=10)

        home_button = Button(self, text="Return home", bg="#0a0a0a", fg="#00ff00", font=("Colibri", 23),
                             activeforeground="green", activebackground="black", bd=0, state=DISABLED,
                             command=return_to_home, disabledforeground="black")
        home_button.pack(fill=BOTH, side=BOTTOM)

        launch_button = Button(self, text="Finish", bg="#0c0a0a", fg="#00ff00", font=("Colibri", 23),
                               activeforeground="green", activebackground="black", bd=0,
                               command=getting_results, disabledforeground="black")
        launch_button.pack(fill=BOTH, side=BOTTOM, pady=1)


class FullControlPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")

        text = "Enter largest possible integer and amount to continue." \
               "\n(e.g. 120, 2) After pressing 'Continue' program" \
               "\nwill check if input is valid else it will show you an error."

        label = Label(self, text=text, font=("Times New Roman", 16), bg="black", fg="#00ff00")
        label.pack(padx=5, pady=10, fill=BOTH)

        def check_if_valid():
            _input_str = entry.get()
            try:
                integers = list(map(int, _input_str.split(', ')))
                if len(integers) == 2:
                    if integers[1] < 2:
                        raise AmountValueError(f'{integers[1]}')
                    elif 0 in integers:
                        raise ValueError(f"invalid literal for int() with base 10: '0' '{integers.index(0)}'")
                else:
                    raise AmountError(f"{len(integers)}")
                entry.delete(0, END)
                file = open("temporary_storage.txt", 'w')
                file.seek(0)
                file.write(str(integers)[1:-1])
                file.close()
                return True
            except ValueError as reason:
                entry.delete(0, END)
                if str(reason)[41:42] == "0":
                    integer_value_error_message(str(reason)[41:42], int(str(reason)[45:-1]))
                else:
                    integer_value_error_message(str(reason)[41:42])
            except AmountError as error_message_fragment:
                entry.delete(0, END)
                amount_error_message(error_message_fragment, "full")
            except AmountValueError as error_reason:
                entry.delete(0, END)
                amount_value_error_message(error_reason)

        entry = Entry(self, bg="black", fg="#00ff00", font=("Times New Roman", 20),
                      selectbackground="white", selectforeground="#ff00ff",
                      width=250, highlightthickness=1, insertbackground="white")
        entry.config(highlightbackground="green", highlightcolor="light green")
        entry.pack()

        confirm_button = Button(self, bg="#0a0a0c", fg="#00ff00", font=("Colibri", 23),
                                activeforeground="green", activebackground="black", bd=0, text="Continue",
                                command=lambda: controller.show_frame(FullControlResultsPage)
                                if check_if_valid() else None)
        confirm_button.pack(fill=BOTH)

        def clicked_return_button():
            entry.delete(0, END)
            controller.show_frame(GeneratorHome)

        return_button = Button(self, text="Return to previous page", bg="#0a0a0a",
                               fg="#00ff00", font=("Colibri", 23), command=clicked_return_button,
                               activeforeground="green", activebackground="black", bd=0)
        return_button.pack(fill=BOTH, side=BOTTOM)


class FullControlResultsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        def getting_results():
            file = open('temporary_storage.txt', 'r')
            string_results = file.read()
            arguments = list(map(int, string_results.split(', ')))
            results = int_list_creator(int(arguments[1]), int(arguments[0]))
            file.close()
            remove("temporary_storage.txt")
            text_area.delete("1.0", END)
            text_area.insert('0.0', f"Generated {arguments[1]} numbers in range from 1 to {arguments[0]}:\n")
            text_area.insert(END, ', '.join(map(str, results)))
            text_area.insert(END, "\nGreatest common divisor: ")
            text_area.insert(END, str(_gcd(results)) + '\n')
            text_area.config(state=DISABLED)
            home_button.config(state=ACTIVE)
            launch_button.config(state=DISABLED)

        def return_to_home():
            text_area.config(state=NORMAL)
            text_area.delete("1.0", END)
            text_area.insert('0.0', text)
            home_button.config(state=DISABLED)
            launch_button.config(state=ACTIVE)
            controller.show_frame(StartPage)

        text = 'Press "Finish" button to get results, or type here for fun'

        text_area = Text(self, font=("Times New Roman", 13), bg="black", fg="#00ff00",
                         selectbackground="white", selectforeground="#ff00ff",
                         insertbackground="white", width=55, height=6, wrap=WORD)
        text_area.insert("0.0", text)
        text_area.pack(padx=5, pady=10)

        home_button = Button(self, text="Return home", bg="#0a0a0a", fg="#00ff00", font=("Colibri", 23),
                             activeforeground="green", activebackground="black", bd=0, state=DISABLED,
                             command=return_to_home, disabledforeground="black")
        home_button.pack(fill=BOTH, side=BOTTOM)

        launch_button = Button(self, text="Finish", bg="#0c0a0a", fg="#00ff00", font=("Colibri", 23),
                               activeforeground="green", activebackground="black", bd=0,
                               command=getting_results, disabledforeground="black")
        launch_button.pack(fill=BOTH, side=BOTTOM, pady=1)


class CustomMainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="Black")

        text = "Here you can enter your integers (e.g. 120, 20)"

        label = Label(self, text=text, font=("Times New Roman", 18), bg="black", fg="#00ff00")
        label.pack(padx=5, fill=BOTH)

        text_area = Text(self, font=("Times New Roman", 13), bg="black", fg="#00ff00",
                         selectbackground="white", selectforeground="#ff00ff",
                         insertbackground="white", width=55, height=5, wrap=WORD)
        text_area.pack(padx=5, pady=2)

        home_button = Button(self, text="Return home", bg="#0a0a0a", fg="#00ff00", font=("Colibri", 22),
                             activeforeground="green", activebackground="black", bd=0,
                             command=lambda: controller.show_frame(StartPage))
        home_button.pack(fill=BOTH, side=BOTTOM)

        def check_if_valid():
            _input_str = text_area.get('0.0', END)
            try:
                integers = list(map(int, _input_str.split(', ')))
                if 0 in integers and len(integers) > 1:
                    raise ValueError(f"invalid literal for int() with base 10: '0' '{integers.index(0)}'")
                if len(integers) < 2:
                    raise AmountError(f"{len(integers)}")
                text_area.delete('0.0', END)
                file = open("temporary_storage.txt", 'w')
                file.seek(0)
                file.write(str(integers)[1:-1])
                file.close()
                return True
            except ValueError as reason:
                text_area.delete('0.0', END)
                if str(reason)[41:42] == "0":
                    integer_value_error_message(str(reason)[41:42], int(str(reason)[45:-1]))
                else:
                    integer_value_error_message(str(reason)[41:42])
            except AmountError as error_message_fragment:
                text_area.delete("1.0", END)
                amount_error_message(error_message_fragment, "custom")

        confirm_button = Button(self, text="Confirm", bg="#0a0a0c", fg="#00ff00", font=("Colibri", 22),
                                activeforeground="green", activebackground="black", bd=0,
                                command=lambda: controller.show_frame(CustomResultsPage)
                                if check_if_valid() else None)
        confirm_button.pack(fill=BOTH)


class CustomResultsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="Black")

        def getting_results():
            file = open('temporary_storage.txt', 'r')
            string_results = file.read()
            results = list(map(int, string_results.split(', ')))
            file.close()
            remove("temporary_storage.txt")
            text_area.delete("1.0", END)
            text_area.insert('0.0', f"Entered {len(results)} numbers:\n")
            text_area.insert(END, string_results)
            text_area.insert(END, "\nGreatest common divisor: ")
            text_area.insert(END, str(_gcd(results)) + '\n')
            text_area.config(state=DISABLED)
            home_button.config(state=ACTIVE)
            launch_button.config(state=DISABLED)

        def return_to_home():
            text_area.config(state=NORMAL)
            text_area.delete("1.0", END)
            text_area.insert('0.0', text)
            home_button.config(state=DISABLED)
            launch_button.config(state=ACTIVE)
            controller.show_frame(StartPage)

        text = 'Press "Finish" button to get results, or type here for fun'

        text_area = Text(self, font=("Times New Roman", 13), bg="black", fg="#00ff00",
                         selectbackground="white", selectforeground="#ff00ff",
                         insertbackground="white", width=55, height=6, wrap=WORD)
        text_area.insert("0.0", text)
        text_area.pack(padx=5, pady=10)

        home_button = Button(self, text="Return home", bg="#0a0a0a", fg="#00ff00", font=("Colibri", 23),
                             activeforeground="green", activebackground="black", bd=0, state=DISABLED,
                             command=return_to_home, disabledforeground="black")
        home_button.pack(fill=BOTH, side=BOTTOM)

        launch_button = Button(self, text="Finish", bg="#0a0a0c", fg="#00ff00", font=("Colibri", 23),
                               activeforeground="green", activebackground="black", bd=0,
                               command=getting_results, disabledforeground="black")
        launch_button.pack(fill=BOTH, side=BOTTOM, pady=1)
