from tkinter import *
import pandas as pd
from pandastable import Table
import numpy_financial as npf
from datetime import date

HEIGHT = 600
WIDTH = 900

root = Tk()
root.title("Loan Calculator by MartinP")
root.iconbitmap('')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

"""Draw and Display top and middle frames"""
top_frame = Frame(root, bd=2, bg='black')
top_frame.place(relx=0.5, rely=0.0, relwidth=1, relheight=0.1, anchor='n')
top_frame_label = Label(top_frame, anchor='nw', bd=2)
top_frame_label.place(relwidth=1, relheight=1)

middle_frame = Frame(root, bd=2, bg='black')
middle_frame.place(relx=0.5, rely=0.09, relwidth=1, relheight=1, anchor='n')
bottom_frame_label = Label(middle_frame, bg='white', anchor='nw', bd=2)
bottom_frame_label.place(relwidth=1, relheight=1)

"""Draw and display calculator frame, labels, entry and button inside the frame"""
calculator_frame = Frame(root, bd=2, bg='black')
calculator_frame.place(relx=0.21, rely=0.12, relwidth=0.4, relheight=0.4, anchor='n')
calculator_frame_label = Label(calculator_frame, bg='white', font=('Courier', 12), anchor='nw', justify='left', bd=4)
calculator_frame_label.place(relwidth=1, relheight=1)

label1 = Label(calculator_frame, bg='white', text="Loan Amount", font=('Courier', 14), anchor='nw', justify='left')
label1.place(relx=0.03, rely=0.08, relwidth=0.5, relheight=0.1)
entry1 = Entry(calculator_frame, bg='white', bd=2, font=('Courier', 12))
entry1.place(relx=0.55, rely=0.08, relwidth=0.4, relheight=0.1)

label2 = Label(calculator_frame, bg='white', text="Term (Months)", font=('Courier', 14), anchor='nw', justify='left')
label2.place(relx=0.03, rely=0.28, relwidth=0.5, relheight=0.1)
entry2 = Entry(calculator_frame, bg='white', bd=2, font=('Courier', 12))
entry2.place(relx=0.55, rely=0.28, relwidth=0.4, relheight=0.1)

label3 = Label(calculator_frame, bg='white', text="Interest Rate %", font=('Courier', 14), anchor='nw', justify='left')
label3.place(relx=0.03, rely=0.48, relwidth=0.5, relheight=0.1)
entry3 = Entry(calculator_frame, bg='white', bd=2, font=('Courier', 12))
entry3.place(relx=0.55, rely=0.48, relwidth=0.4, relheight=0.1)

label4 = Label(calculator_frame, bg='white', text="Start Date Y-M-D", font=('Courier', 14), anchor='nw', justify='left')
label4.place(relx=0.03, rely=0.68, relwidth=0.5, relheight=0.1)
entry4 = Entry(calculator_frame, bg='white', bd=2, font=('Courier', 12))
entry4.place(relx=0.55, rely=0.68, relwidth=0.4, relheight=0.1)

"""Draw and display the result frame and labels inside the frame"""
result_frame = Frame(root, bd=2, bg='red')
result_frame.place(relx=0.7, rely=0.12, relwidth=0.55, relheight=0.4, anchor='n')
label = Label(result_frame, bg='white', font=('Courier', 12), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

label_monthly_payment = Label(result_frame, bg='white', text="Your Monthly Payments", font=('Courier', 20), anchor='n', justify='center')
label_monthly_payment.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)

label_total_principal = Label(result_frame, bg='white', text="Total Principal", font=('Courier', 14), anchor='nw', justify='left')
label_total_principal.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.15)

label_total_interest = Label(result_frame, bg='white', text="Total Interest", font=('Courier', 14), anchor='nw', justify='left')
label_total_interest.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.15)

label_total_cost = Label(result_frame, bg='white', text="Total Cost", font=('Courier', 14), anchor='nw', justify='left')
label_total_cost.place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.15)

"""Draw and display the table frame"""
table_frame = Frame(root, bd=2, bg='black')
table_frame.place(relx=0.495, rely=0.54, relwidth=0.965, relheight=0.44, anchor='n')
label = Label(table_frame, font=('Courier', 12), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


def calculate_loan():
    amount = float(entry1.get())
    months = float(entry2.get())
    interest = float(entry3.get())
    start_date = (entry4.get())

    interest = interest/100
    interest_monthly = interest/12
    numerator = interest_monthly*((1 + interest_monthly)**months)
    denominator = (1 + interest_monthly)**months - 1
    payment = amount*numerator/denominator
    total_cost = months * payment
    total_interest = total_cost - amount

    label_calc_loan_result_result = Label(result_frame, bg='white', text="{0:.2f}".format(payment), font=('Courier', 20), anchor='n', justify='center')
    label_calc_loan_result_result.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.15)

    label_total_principal_result = Label(result_frame, bg='white', text="{0:.2f}".format(amount), font=('Courier', 14), anchor='nw', justify='left')
    label_total_principal_result.place(relx=0.7, rely=0.6, relwidth=0.3, relheight=0.1)

    label_total_interest_result = Label(result_frame, bg='white', text="{0:.2f}".format(total_interest), font=('Courier', 14), anchor='nw', justify='left')
    label_total_interest_result.place(relx=0.7, rely=0.7, relwidth=0.3, relheight=0.1)

    label_total_cost_result = Label(result_frame, bg='white', text="{0:.2f}".format(total_cost), font=('Courier', 14), anchor='nw', justify='left')
    label_total_cost_result.place(relx=0.7, rely=0.8, relwidth=0.3, relheight=0.1)

    """dataframe"""
    pmt = -1 * npf.pmt(interest_monthly, months, amount)
    ipmt = -1 * npf.ipmt(interest_monthly, 1, months, amount)
    ppmt = -1 * npf.ppmt(interest_monthly, 1, months, amount)

    rng = pd.date_range(start_date, periods=months, freq='MS')
    rng.name = "Payment Date"
    df = pd.DataFrame(index=rng, columns=['Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance'],
                      dtype='float')
    df.reset_index(inplace=True)
    df.index += 1
    df.index.name = "Period"

    df["Payment"] = -1 * npf.pmt(interest_monthly, months, amount)
    df["Principal Paid"] = -1 * npf.ipmt(interest_monthly, 1, months, amount)
    df["Interest Paid"] = -1 * npf.ppmt(interest_monthly, 1, months, amount)
    df = df.round(2)

    df["Ending Balance"] = 0
    df.loc[1, "Ending Balance"] = amount - df.loc[1, "Principal Paid"]

    for period in range(2, len(df) + 1):
        previous_balance = df.loc[period - 1, "Ending Balance"]
        principal_paid = df.loc[period, "Principal Paid"]

        if previous_balance == 0:
            df.loc[period, ['Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance']] == 0
            continue
        elif principal_paid <= previous_balance:
            df.loc[period, 'Ending Balance'] = previous_balance - principal_paid

    pt = Table(table_frame, dataframe=df)
    pt.show()


button_calc = Button(calculator_frame, text="Calculate", bd=2, font=('Courier', 14), command=lambda: calculate_loan())
button_calc.place(relx=0.55, rely=0.85, relwidth=0.4, relheight=0.1)

root.mainloop()

# pyinstaller.exe --onefile --icon=myicon.ico main.py
