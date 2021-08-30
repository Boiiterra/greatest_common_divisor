from tkinter import *
from tkinter.messagebox import showerror
from support import _gcd


class AmountError(Exception):
    pass


def integer_value_error_message(_reason, index=None):
    message = "Incorrect input, you are supposed to enter single integer bigger than 0." \
              f"\nBut you entered -> '{_reason}'"
    if _reason == '0' and index is not None:
        message += f' in position {index + 1}, index -> {index}.'
    else:
        message += '.'
    showerror(title="Error", message=message)


def amount_error_message(amount):
    message = "Incorrect input, you are supposed to enter multiple integers " \
              f"\n(e.g. 12, 6, 24). \nBut you entered only {amount}."
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

        frame_collection = (StartPage, MainPage)

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

        text = "This program takes user's\n" \
               "integers and finds their greatest common divisor"

        label = Label(self, text=text, font=("Times New Roman", 18), bg="black", fg="#00ff00")
        label.pack(padx=5, pady=11, fill=BOTH)

        main_page_button = Button(self, text="\nStart\n", bg="#0a0c0a", fg="#00ff00", font=("Arial", 30),
                                  activeforeground="green", activebackground="black", bd=0,
                                  disabledforeground="black",
                                  command=lambda: controller.show_frame(MainPage))
        main_page_button.pack(fill=BOTH)


class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="Black")

        def reset():
            text_area.config(state=NORMAL)
            text_area.delete("0.0", END)
            confirm_button.config(state=ACTIVE, bg="#0a0a0c", text="Confirm")
            info_plus_reset.config(text=text, state=DISABLED, bg="black")

        def return_to_home():
            text_area.config(state=NORMAL)
            text_area.delete("0.0", END)
            confirm_button.config(state=ACTIVE, bg="#0a0a0c", text="Confirm")
            controller.show_frame(StartPage)

        def check_and_show():
            _input_str = text_area.get('0.0', END)
            try:
                integers = list(map(int, _input_str.split(', ')))
                if 0 in integers and len(integers) > 1:
                    raise ValueError(f"invalid literal for int() with base 10: '0' '{integers.index(0)}'")
                if len(integers) < 2:
                    raise AmountError(f"{len(integers)}")
                text_area.delete('0.0', END)
                show_results(_input_str)
                return True
            except ValueError as reason:
                text_area.delete('0.0', END)
                if str(reason)[41:42] == "0":
                    integer_value_error_message(str(reason)[41:42], int(str(reason)[45:-1]))
                else:
                    integer_value_error_message(str(reason)[41:-1])
            except AmountError as error_message_fragment:
                print(error_message_fragment)
                text_area.delete("1.0", END)
                amount_error_message(error_message_fragment)

        def show_results(string_numbers: str):
            integers = list(map(int, string_numbers.split(', ')))
            text_area.insert('0.0', f"Entered {len(integers)} numbers:\n")
            text_area.insert(END, string_numbers)
            text_area.insert(END, "\nGreatest common divisor: ")
            text_area.insert(END, _gcd(integers))
            text_area.config(state=DISABLED)
            confirm_button.config(state=DISABLED, bg="Black", text="Now you can return home or reset field")
            info_plus_reset.config(text="Reset", state=ACTIVE, bg="#0c0a0a")

        text = "Here you can enter your integers (e.g. 120, 20)"

        info_plus_reset = Button(self, text=text, font=("Times New Roman", 17), bg="black", fg="#00ff00",
                                 activeforeground="green", activebackground="black",
                                 disabledforeground="#00ff00", bd=0, state=DISABLED,
                                 command=reset)
        info_plus_reset.pack(fill=BOTH)

        text_area = Text(self, font=("Times New Roman", 13), bg="black", fg="#00ff00",
                         selectbackground="white", selectforeground="#ff00ff",
                         insertbackground="white", width=55, height=5, wrap=WORD)
        text_area.pack(padx=5, pady=2)

        home_button = Button(self, text="Return home", bg="#0a0a0a", fg="#00ff00", font=("Arial", 21),
                             activeforeground="green", activebackground="black", bd=0,
                             command=return_to_home)
        home_button.pack(fill=BOTH, side=BOTTOM)

        confirm_button = Button(self, text="Confirm", bg="#0a0a0c", fg="#00ff00", font=("Arial", 21),
                                activeforeground="green", activebackground="black", bd=0,
                                command=check_and_show, disabledforeground="#00ff00")
        confirm_button.pack(fill=BOTH)
