from tkinter import *

global initial_currency
initial_currency = None
global final_currency
final_currency = None
initial_ratio = [1, 1.20, 0.0094, 1.39, 0.78, 0.79, 1.11, 0.16, 0.13, 0.72, 0.12, 0.00090, 0.75, 0.12, 0.049, 0.014, 0.014, 0.068, 0.14, 0.23]
final_ratio = [1, 0.83, 105.89, 0.72, 1.29, 1.27, 0.90, 6.45, 7.75, 1.39, 8.32, 1106.17, 1.33, 8.50, 20.22, 72.72, 73.73, 14.65, 6.97, 5.41]

#initial currency methods

def usd_in():
    #0
    global initial_currency
    initial_currency = 0
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "USD (US dollar)")

def eur_in():
    #1
    global initial_currency
    initial_currency = 1
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "EUR (euro)")

def jpy_in():
    #2
    global initial_currency
    initial_currency = 2
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "JPY (Japenese yen)")

def gbp_in():
    #3
    global initial_currency
    initial_currency = 3
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "GBP (British pound)")

def aud_in():
    #4
    global initial_currency
    initial_currency = 4
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "AUD (Australian Dollar)")

def cad_in():
    #5
    global initial_currency
    initial_currency = 5
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "CAD (Canadian Dollar)")

def chf_in():
    #6
    global initial_currency
    initial_currency = 6
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "CHF (Swiss franc)")

def cny_in():
    #7
    global initial_currency
    initial_currency = 7
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "CNY (Chinese renminbi)")

def hkd_in():
    #8
    global initial_currency
    initial_currency = 8
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "HKD (Hong Kong dollar)")

def nzd_in():
    #9
    global initial_currency
    initial_currency = 9
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "NZD (New Zealand dollar)")

def sek_in():
    #10
    global initial_currency
    initial_currency = 10
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "SEK (Swedish Krona)")

def krw_in():
    #11
    global initial_currency
    initial_currency = 11
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "KRW (South Korean won)")

def sgd_in():
    #12
    global initial_currency
    initial_currency = 12
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "SGD (Singapore dollar)")

def nok_in():
    #13
    global initial_currency
    initial_currency = 13
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "NOK (Norwegian krone)")

def mxn_in():
    #14
    global initial_currency
    initial_currency = 14
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "MXN (Mexican peso)")

def inr_in():
    #15
    global initial_currency
    initial_currency = 15
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "INR (Indian rupee)")

def rub_in():
    #16
    global initial_currency
    initial_currency = 16
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "RUB (Russian ruble)")

def zar_in():
    #17
    global initial_currency
    initial_currency = 17
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "ZAR (South African rand)")

def try_in():
    #18
    global initial_currency
    initial_currency = 18
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "TRY (Turkish lira)")

def brl_in():
    #19
    global initial_currency
    initial_currency = 19
    initial_currency_text.delete(0.0, END)
    initial_currency_text.insert(INSERT, "BRL (Brazilian real)")

#final_currency methods

def usd_out():
    # 0
    global final_currency
    final_currency = 0
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "USD (US dollar)")

def eur_out():
    # 1
    global final_currency
    final_currency = 1
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "EUR (euro)")

def jpy_out():
    # 2
    global final_currency
    final_currency = 2
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "JPY (Japanese yen)")

def gbp_out():
    # 3
    global final_currency
    final_currency = 3
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "GBP (British dollar)")

def aud_out():
    # 4
    global final_currency
    final_currency = 4
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "AUD (Australian dollar)")

def cad_out():
    # 5
    global final_currency
    final_currency = 5
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "CAD (Canadian dollar)")

def chf_out():
    # 6
    global final_currency
    final_currency = 6
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "CHF (Swiss franc)")

def cny_out():
    # 7
    global final_currency
    final_currency = 7
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "CNY (Chinese Renminbi)")

def hkd_out():
    # 8
    global final_currency
    final_currency = 8
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "HKD (Hong Kong dollar)")

def nzd_out():
    # 9
    global final_currency
    final_currency = 9
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "NZD (New Zealand dollar)")

def sek_out():
    # 10
    global final_currency
    final_currency = 10
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "SEK (Swedish krona)")

def krw_out():
    # 11
    global final_currency
    final_currency = 11
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "KRW (South Korean won)")

def sgd_out():
    # 12
    global final_currency
    final_currency = 12
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "SGD (Singapore dollar)")

def nok_out():
    # 13
    global final_currency
    final_currency = 13
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "NOK (Norweigian dollar)")

def mxn_out():
    # 14
    global final_currency
    final_currency = 14
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "MXN (Mexican peso)")

def inr_out():
    # 15
    global final_currency
    final_currency = 15
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "INR (Indian rupee)")

def rub_out():
    # 16
    global final_currency
    final_currency = 16
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "RUB (Russian Ruble)")

def zar_out():
    # 17
    global final_currency
    final_currency = 17
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "ZAR (South African rand")

def try_out():
    # 18
    global final_currency
    final_currency = 18
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "TRY (Turkish lira)")

def brl_out():
    # 19
    global final_currency
    final_currency = 19
    final_currency_text.delete(0.0, END)
    final_currency_text.insert(INSERT, "BRL (Brazilian real)")

#convert method
def convert():
    try:
        str_amount = money_amount.get()
        flt_amount = float(str_amount.replace(" ", ""))
    except:
        popupmsg("Invalid: Please only include numbers", "Invalid Input for Money")
    try:
        convert_to_usd = flt_amount*initial_ratio[initial_currency]
        convert_to_final = convert_to_usd*final_ratio[final_currency]
        output_amount = int(convert_to_final*100)/100
        output_text.delete(0.0, END)
        output_text.insert(INSERT, output_amount)
    except:
        popupmsg("Invalid: PLease select the initial and final currency before converting", "Currency Not Selected")

#currency guide
def currency_guide():
    popupmsg("""
    USD - US dollar\tEUR - euro\nJPY - Japanese yen\tGBP - British pound\n
    AUD - Austrailian dollar\tCAD - Canadian dollar\nCHF - Swiss franc\tCNY - Chinese renminbi\n
    HKD - Hong Kong dollar\tNZD - New Zealand dollar\nSEK - Swedish krona\tKRW - South Korean won\n
    SGD - Singapore dollar\tNOK - Norwegian krone\nMXN - Mexican peso\tINR - Indian rupee\n
    RUB - Russian ruble\tZAR - South African rand\nTRY - Turkish lira\tBRL - Brazilian real         
    """ ,"Currency Guide")

#popup message
def popupmsg(msg, title):
    popup = Tk()
    popup.wm_title(title)
    label = Label(popup, text=msg, font="none 12")
    label.pack(side="top", fill="x", pady=10)
    button = Button(popup, text="OK...", pady=3, command=popup.destroy)
    button.pack()
    popup.mainloop()

#clear method
def clear():
    initial_currency_text.delete(0.0, END)
    final_currency_text.delete(0.0, END)
    money_amount.delete(0, END)
    output_text.delete(0.0, END)

#exit function
def close_window():
    window.destroy()
    exit

#main
window = Tk()
window.title("Currency Converter")
window.configure(background="light blue")

#-> initial currency
Button(window, text="USD", width=10, command=usd_in).grid(row=3, column=2, sticky=W)
Button(window, text="EUR", width=10, command=eur_in).grid(row=3, column=3, sticky=W)
Button(window, text="JPY", width=10, command=jpy_in).grid(row=3, column=4, sticky=W)
Button(window, text="GBP", width=10, command=gbp_in).grid(row=3, column=5, sticky=W)
Button(window, text="AUD", width=10, command=aud_in).grid(row=3, column=6, sticky=W)
Button(window, text="CAD", width=10, command=cad_in).grid(row=3, column=7, sticky=W)
Button(window, text="CHF", width=10, command=chf_in).grid(row=3, column=8, sticky=W)
Button(window, text="CNY", width=10, command=cny_in).grid(row=3, column=9, sticky=W)
Button(window, text="HKD", width=10, command=hkd_in).grid(row=3, column=10, sticky=W)
Button(window, text="NZD", width=10, command=nzd_in).grid(row=3, column=11, sticky=W)
Button(window, text="SEK", width=10, command=sek_in).grid(row=4, column=2, sticky=W)
Button(window, text="KRW", width=10, command=krw_in).grid(row=4, column=3, sticky=W)
Button(window, text="SGD", width=10, command=sgd_in).grid(row=4, column=4, sticky=W)
Button(window, text="NOK", width=10, command=nok_in).grid(row=4, column=5, sticky=W)
Button(window, text="MXN", width=10, command=mxn_in).grid(row=4, column=6, sticky=W)
Button(window, text="INR", width=10, command=inr_in).grid(row=4, column=7, sticky=W)
Button(window, text="RUB", width=10, command=rub_in).grid(row=4, column=8, sticky=W)
Button(window, text="ZAR", width=10, command=zar_in).grid(row=4, column=9, sticky=W)
Button(window, text="TRY", width=10, command=try_in).grid(row=4, column=10, sticky=W)
Button(window, text="BRL", width=10, command=brl_in).grid(row=4, column=11, sticky=W)

#-> final currency
Button(window, text="USD", width=10, command=usd_out).grid(row=6, column=2, sticky=W)
Button(window, text="EUR", width=10, command=eur_out).grid(row=6, column=3, sticky=W)
Button(window, text="JPY", width=10, command=jpy_out).grid(row=6, column=4, sticky=W)
Button(window, text="GBP", width=10, command=gbp_out).grid(row=6, column=5, sticky=W)
Button(window, text="AUD", width=10, command=aud_out).grid(row=6, column=6, sticky=W)
Button(window, text="CAD", width=10, command=cad_out).grid(row=6, column=7, sticky=W)
Button(window, text="CHF", width=10, command=chf_out).grid(row=6, column=8, sticky=W)
Button(window, text="CNY", width=10, command=cny_out).grid(row=6, column=9, sticky=W)
Button(window, text="HKD", width=10, command=hkd_out).grid(row=6, column=10, sticky=W)
Button(window, text="NZD", width=10, command=nzd_out).grid(row=6, column=11, sticky=W)
Button(window, text="SEK", width=10, command=sek_out).grid(row=7, column=2, sticky=W)
Button(window, text="KRW", width=10, command=krw_out).grid(row=7, column=3, sticky=W)
Button(window, text="SGD", width=10, command=sgd_out).grid(row=7, column=4, sticky=W)
Button(window, text="NOK", width=10, command=nok_out).grid(row=7, column=5, sticky=W)
Button(window, text="MXN", width=10, command=mxn_out).grid(row=7, column=6, sticky=W)
Button(window, text="INR", width=10, command=inr_out).grid(row=7, column=7, sticky=W)
Button(window, text="RUB", width=10, command=rub_out).grid(row=7, column=8, sticky=W)
Button(window, text="ZAR", width=10, command=zar_out).grid(row=7, column=9, sticky=W)
Button(window, text="TRY", width=10, command=try_out).grid(row=7, column=10, sticky=W)
Button(window, text="BRL", width=10, command=brl_out).grid(row=7, column=11, sticky=W)

#Currency Guide
Button(window, text="Currency Guide", width=20, command=currency_guide).grid(row=1, column=0, sticky=W)

#Labels
Label(window, text="Press the Initial Currency:", bg="light blue", fg="black", font="arial 12 bold").grid(row=3, column=0, sticky=W)
Label(window, text="Press the Final Currency:", bg="light blue", fg="black", font="arial 12 bold").grid(row=6, column=0, sticky=W)
Label(window, text="Enter the Amount of Money (to be converted):", bg="light blue", fg="black", font="arial 12 bold").grid(row=13, column=0, sticky=W)
Label(window, text="Amount of Money (in Final Currency):", bg="light blue", fg="black", font="arial 12 bold").grid(row=9, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=2, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=5, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=7, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=8, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=10, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=12, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=14, column=0, sticky=W)
Label(window, text="", bg="light blue", fg="black", font="arial 12 bold").grid(row=16, column=0, sticky=W)

#money amount method

money_amount = Entry(window, width=30, bg="white")
money_amount.grid(row=9, column=1, sticky=W)

#-> convert
Button(window, text="CONVERT", width=30, command=convert).grid(row=11, column=0, sticky=W)

#initial currency text
initial_currency_text = Text(window, width=30, height=1, wrap=WORD, background="white")
initial_currency_text.grid(row=5, column=0, columnspan=2, sticky=W)

#final currency text
final_currency_text = Text(window, width=30, height=1, wrap=WORD, background="white")
final_currency_text.grid(row=8, column=0, columnspan=2, sticky=W)

#output text
output_text = Text(window, width=30, height=1, wrap=WORD, background="white")
output_text.grid(row=13, column=1, columnspan=2, sticky=W)

#-> clear button
Button(window, text="CLEAR", width=20, command=clear).grid(row=15, column=0, sticky=W)

#-> exit function
Button(window, text="EXIT", width=20, command=close_window).grid(row=17, column=0, sticky=W)

#runs the main loop
window.mainloop()
