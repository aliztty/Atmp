#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from pathlib import Path

script_dir=Path(__file__).parent
project_root=script_dir.parent
data_file_path=project_root / "data" / "data.txt"
data_file_path.parent.mkdir(parents=True, exist_ok=True)

window = Tk()
window.geometry("300x400")

def Card_Registration():
    dct = open(data_file_path, "a+")

    def Save_Info():
        number = entry_1.get()
        name = entry_2.get()
        passcode = entry_3.get()
        phone = entry_4.get()
#           Card_Number : Account_Balance : Account_Pass : Phone_Number : Account_Name 
        lst = [number, ":", "100000", ":", passcode, ":", phone, ":", "0", ":", name]
        for string in lst:
            dct.write(string)
        dct.write("\n")

    def exit_inside():
        new_window.destroy()

    new_window = Toplevel()
    new_window.geometry("250x250")
    new_window.title("Card_Registration")

    label_1 = Label(new_window, text="Enter card number")
    label_2 = Label(new_window, text="Enter card's name")
    label_3 = Label(new_window, text="Enter card's passcode")
    label_4 = Label(new_window, text="Enter phone number")

    entry_1 = Entry(new_window)
    entry_2 = Entry(new_window)
    entry_3 = Entry(new_window)
    entry_4 = Entry(new_window)

    Button(new_window, text="back", bg="black", fg="red", width=3, height=1, command=exit_inside).pack(side=BOTTOM)
    Button(new_window, text="verify", bg="black", fg="red", width=3, height=1, command=Save_Info).pack(side=BOTTOM)

    s = [label_1, entry_1, label_2, entry_2, label_3, entry_3, label_4, entry_4]
    for i in s:
        i.pack()

    new_window.mainloop()


def Account_Balance():
    def account_balance_inside():
        number = entry_1.get()
        passcode = entry_2.get()
        file = open(data_file_path, "r")
        for each in file:
            lst = each.split(" : ")
            if (number in lst) and (passcode in lst):
                window_2 = Tk()
                Label(window_2, text="account balance is : {} Toman".format(lst[-1])).pack()
                window_2.mainloop()
                new_window.destroy()
            else:
                messagebox.showerror("hello", "no information")
                new_window.destroy()

    def exit_inside():
        new_window.destroy()

    new_window = Toplevel()
    new_window.geometry("250x250")
    new_window.title("Account_Balance")

    label_1 = Label(new_window, text="Enter card number")
    label_2 = Label(new_window, text="Enter card passcode")

    entry_1 = Entry(new_window)
    entry_2 = Entry(new_window)

    Button(new_window, text="back", bg="black", fg="red", width=3, height=1, command=exit_inside).pack(side=BOTTOM)
    Button(new_window, text="verify", bg="black", fg="red", width=3, height=1, command=account_balance_inside).pack(side=BOTTOM)

    s = [label_1, entry_1, label_2, entry_2]
    for i in s:
        i.pack()
    new_window.mainloop()


def Buy_Charge():
    def charge_inside():
        with open(data_file_path, "r+") as file:
            data = file.readlines()

        phone_number = entry_1.get()
        charge_value = entry_2.get()
        card_number = entry_3.get()
        card_passcode = entry_4.get()
        #   (card_number) : (card_balance) : (card_passcode) : (phone_number) : (phone_charge) : (name)
        lst_card_number = []
        lst_card_passcode = []
        lst_phone_number = []
        lst_phone_charge = []
        lst_card_balance = []

        for each in data:
            lst = each.split(":")
            lst_card_number.append(lst[0])
            lst_card_balance.append(lst[1])
            lst_card_passcode.append(lst[2])
            lst_phone_number.append(lst[3])
            lst_phone_charge.append(lst[4])

        if card_number in lst_card_number:
            index = lst_card_number.index(card_number)
            if card_passcode == lst_card_passcode[index]:
                if int(charge_value) <= int(lst_card_balance[index]):
                    if phone_number in lst_phone_number:
                        dct = {0: "", 1: "", 2: "", 3: "", 4: "", 5: ""}
                        lst = data[index].split(":")
                        for index_temp in range(6):
                            dct[index_temp] = lst[index_temp]
                        temp_1, temp_2 = int(dct[1]), int(dct[4])
                        temp_1 -= int(charge_value)
                        temp_2 += int(charge_value)
                        dct[1], dct[4] = str(temp_1), str(temp_2)
                        string = ""
                        for string_temp in dct.values():
                            string += string_temp
                            string += ":"
                        data[index] = string[:-1]
                        with open(data_file_path, "a") as file:
                            file.writelines(data)

                    else:
                        with open(data_file_path, "a") as file:
                            string = "_:_:_:%s:%s:_" % (phone_number, charge_value)
                            file.write(string)
                else:
                    messagebox.showerror("Error", "Card balance is not enough")
            else:
                messagebox.showerror("Error", "Card passcode is not valid")
        else:
            messagebox.showerror("Error", "Card number is not valid")

    def exit_inside():
        new_window.destroy()

    new_window = Toplevel()
    new_window.geometry("250x250")

    new_window.title("Buy charge")

    label_1 = Label(new_window, text="Enter phone number")
    label_2 = Label(new_window, text="Enter charge value")
    label_3 = Label(new_window, text="Enter card number")
    label_4 = Label(new_window, text="Enter card passcode")

    entry_1 = Entry(new_window)
    entry_2 = Entry(new_window)
    entry_3 = Entry(new_window)
    entry_4 = Entry(new_window)

    button_1 = Button(new_window, text="varify", bg="black", fg="red", width=3, height=1, command=charge_inside)
    button_2 = Button(new_window, text="back", bg="black", fg="red", width=3, height=1, command=exit_inside)

    s = [label_1, entry_1, label_2, entry_2, label_3, entry_3, label_4, entry_4, button_1, button_2]
    for i in s:
        i.pack()

    new_window.mainloop()


def Sending_Money():
    def Sending_Money_Inside():
        with open(data_file_path, "r") as file:
            data = file.readlines()

        card_number = entry_1.get()
        amount = entry_2.get()
        card_passcode = entry_3.get()
        destination_card = entry_4.get()
        #   (card_number) : (card_balance) : (card_passcode) : (phone_number) : (phone_charge) : (name)
        lst_card_number = []
        lst_card_passcode = []
        lst_card_balance = []
        lst_name = []

        for each in data:
            lst = each.split(":")
            lst_card_number.append(lst[0])
            lst_card_balance.append(lst[1])
            lst_card_passcode.append(lst[2])
            lst_name.append(lst[5])

        if card_number in lst_card_number:
            index = lst_card_number.index(card_number)
            index_destination = lst_card_number.index(destination_card)
            if card_passcode == lst_card_passcode[index]:
                if amount <= lst_card_balance[index]:
                    answer = messagebox.askyesno("Final verify", "You are sending money to %s continue?" % lst_name[index_destination])
                    if answer:
                        dct_1 = {0: "", 1: "", 2: "", 3: "", 4: "", 5: ""}
                        dct_2 = {0: "", 1: "", 2: "", 3: "", 4: "", 5: ""}
                        lst_1 = data[index].split(":")
                        lst_2 = data[index_destination].split(":")
                        for index_temp in range(6):
                            dct_1[index_temp] = lst_1[index_temp]
                            dct_2[index_temp] = lst_2[index_temp]
                        temp_1, temp_2 = int(dct_1[1]), int(dct_2[1])
                        temp_1 -= int(amount)
                        temp_2 += int(amount)
                        dct_1[1], dct_2[1] = str(temp_1), str(temp_2)
                        string_1, string_2 = "", ""
                        for one in dct_1.values():
                            string_1 += one
                            string_1 += ":"
                        for two in dct_2.values():
                            string_2 += two
                            string_2 += ":"
                        data[index] = string_1[:-1]
                        data[index_destination] = string_2[:-1]
                        with open(data_file_path, "a") as file:
                            file.writelines(data)

                    else:
                        new_window.destroy()
                else:
                    messagebox.showerror("Error", "card balance is not enough")
            else:
                messagebox.showerror("Error", "card passcode is not valid")
        else:
            messagebox.showerror("Error", "Card is not valid")

    def exit_inside():
        new_window.destroy()

    new_window = Toplevel()
    new_window.title("Money_Transmission")
    new_window.geometry("250x250")

    label_1 = Label(new_window, text="Enter your card number")
    label_2 = Label(new_window, text="Enter the amount")
    label_3 = Label(new_window, text="Enter card's passcode")
    label_4 = Label(new_window, text="Enter destination card number")

    entry_1 = Entry(new_window)
    entry_2 = Entry(new_window)
    entry_3 = Entry(new_window)
    entry_4 = Entry(new_window)

    button_1 = Button(new_window, text="verify", bg="black", fg="red", width=3, height=1, command=Sending_Money_Inside)
    button_2 = Button(new_window, text="back", bg="black", fg="red", width=3, height=1, command=exit_inside)
    s = [label_1, entry_1, label_2, entry_2, label_3, entry_3, label_4, entry_4, button_1, button_2]
    for i in s:
        i.pack()

    new_window.mainloop()


window.title("Application")
Button(window, text="Money Transmission", bg="black", fg="red", width=40, height=5, command=Sending_Money).pack(side=BOTTOM)
Button(window, text="Buy Charge", bg="black", fg="red", width=40, height=5, command=Buy_Charge).pack(sid=BOTTOM)
Button(window, text="Account Balance", bg="black", fg="red", width=40, height=5, command=Account_Balance).pack(side=BOTTOM)
Button(window, text="Card Registration", bg="black", fg="red", width=40, height=5, command=Card_Registration).pack(side=BOTTOM)


window.mainloop()
