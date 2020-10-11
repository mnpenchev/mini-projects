from tkinter import *
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox


class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1440x670+0+0")
        self.root.configure(bg='blue')

        MType = StringVar()
        Ref = StringVar()
        Title = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        PostCode = StringVar()
        MobileNo = StringVar()
        BookID = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        SellingPrice = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def iReset():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            PostCode.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            self.txtFrameDetail.delete("1.0", END)
            self.txtDisplayR.delete("1.0", END)

        def iDelete():
            iReset()
            self.txtDisplayR.delete("1.0", END)

        def iDisplayData():
            self.txtFrameDetail.insert(END, "\t" + MType.get() + "\t\t" + Ref.get() + "\t" + Title.get() + "\t" + Firstname.get() + "\t" + Surname.get() + "\t\t" + Address1.get() + "\t" + Address2.get() + "\t" + PostCode.get() + "\t" + BookTitle.get() + "\t\t" + DateBorrowed.get() + "\t\t" + DaysOnLoan.get() + "\n")

        def iReceipt():
            self.txtDisplayR.insert(END, 'Member Type: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Ref No: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Title: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'First name: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Surname: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Address1: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Address2: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Mobile No: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Book ID: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Book Title: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Author: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END, 'Date Borrowed: \t\t' + MType.get() + "\n")

        #==========================Frame===========================================|
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame, width=39, font=('arial', 40, 'bold'), text="\tLibrary Management System\t", padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=('arial', 12, 'bold'), text="Library Membership Info:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=('arial', 12, 'bold'), text="Book Details:")
        DataFrameRIGHT.pack(side=LEFT)

        #==========================Widgets===========================================|
        self.lblMemberType = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, textvariable=MType, font=('arial', 12, 'bold'), state='readonly', width=23, )
        self.cboMemberType['value'] = ('', 'Student', 'Lecturer', 'Admin')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblBookID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Book ID:", padx=2, pady=2)
        self.lblBookID.grid(row=0, column=2, sticky=W)
        self.lblBookID = Entry(DataFrameLEFT, textvariable=BookID, font=('arial', 12, 'bold'), width=25)
        self.lblBookID.grid(row=0, column=3)

        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No:", padx=2, pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, textvariable=Ref, font=('arial', 12, 'bold'), width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="BookTitle:", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtBookTitle = Entry(DataFrameLEFT, textvariable=BookTitle, font=('arial', 12, 'bold'), width=25)
        self.txtBookTitle.grid(row=1, column=3)

        self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)

        self.cboTitle = ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'), state='readonly', width=23, )
        self.cboTitle['value'] = ('', 'Mr', 'Ms', 'Miss', 'Mrs', 'Dr', 'Capt')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(DataFrameLEFT, textvariable=Author, font=('arial', 12, 'bold'), width=25)
        self.txtAuthor.grid(row=2, column=3)

        self.lblFirstname = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="First name:", padx=2, pady=2)
        self.lblFirstname.grid(row=3, column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLEFT, textvariable=Firstname, font=('arial', 12, 'bold'), width=25)
        self.txtFirstname.grid(row=3, column=1)

        self.lblDateBorrowed = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date Borrowed:", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)
        self.txtDateBorrowed = Entry(DataFrameLEFT, textvariable=DateBorrowed, font=('arial', 12, 'bold'), width=25)
        self.txtDateBorrowed.grid(row=3, column=3)

        self.lblSurname = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Surname:", padx=2, pady=2)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, textvariable=Surname, font=('arial', 12, 'bold'), width=25)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date Due:", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.txtDateDue = Entry(DataFrameLEFT, textvariable=DateDue, font=('arial', 12, 'bold'), width=25)
        self.txtDateDue.grid(row=4, column=3)

        self.lblAddress1 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address 1:", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        self.txtAddress1 = Entry(DataFrameLEFT, textvariable=Address1, font=('arial', 12, 'bold'), width=25)
        self.txtAddress1.grid(row=5, column=1)

        self.lblDaysOnLoan = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Days On Loan:", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)
        self.txtDaysOnLoan = Entry(DataFrameLEFT, textvariable=DaysOnLoan, font=('arial', 12, 'bold'), width=25)
        self.txtDaysOnLoan.grid(row=5, column=3)

        self.lblAddress2 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address 2:", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        self.txtAddress2 = Entry(DataFrameLEFT, textvariable=Address2, font=('arial', 12, 'bold'), width=25)
        self.txtAddress2.grid(row=6, column=1)

        self.lblLateReturnFine = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Late Return Fine:", padx=2, pady=2)
        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)
        self.txtLateReturnFine = Entry(DataFrameLEFT, textvariable=LateReturnFine, font=('arial', 12, 'bold'), width=25)
        self.txtLateReturnFine.grid(row=6, column=3)

        self.lblPostCode = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Post Code:", padx=2, pady=2)
        self.lblPostCode.grid(row=7, column=0, sticky=W)
        self.txtPostCode = Entry(DataFrameLEFT, textvariable=PostCode, font=('arial', 12, 'bold'), width=25)
        self.txtPostCode.grid(row=7, column=1)

        self.lblDateOverDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date Over Due:", padx=2, pady=2)
        self.lblDateOverDue.grid(row=7, column=2, sticky=W)
        self.txtDateOverDue = Entry(DataFrameLEFT, textvariable=DateOverDue, font=('arial', 12, 'bold'), width=25)
        self.txtDateOverDue.grid(row=7, column=3)

        self.lblMobileNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Mobile No:", padx=2, pady=2)
        self.lblMobileNo.grid(row=8, column=0, sticky=W)
        self.txtMobileNo = Entry(DataFrameLEFT, textvariable=MobileNo, font=('arial', 12, 'bold'), width=25)
        self.txtMobileNo.grid(row=8, column=1)

        self.lblSellingPrice = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Selling Price:", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        self.txtSellingPrice = Entry(DataFrameLEFT, textvariable=SellingPrice, font=('arial', 12, 'bold'), width=25)
        self.txtSellingPrice.grid(row=8, column=3)

        # ==========================Widget Right===========================================|
        self.txtDisplayR = Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=32, height=13, padx=8, pady=2)
        self.txtDisplayR.grid(row=0, column=2)

        # ==========================Listbox===========================================|
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        ListOfBooks = ['Cinderella', 'Frankenstein', 'Ancient Rome', 'The Count of Monte Cristo', 'Sleeping Beauty', 'Anna Karenina', 'Snow White', 'To Kill a Mockingbird', 'The Great Gatsby', 'One Hundred Years of Solitude', 'Invisible Man', 'Robinson Crusoe', 'A Passage to India', 'Invisible Man', 'Beloved', 'Don Quixote', 'Gulliver\'s Travels', 'Moby-Dick']

        def SelectedBook(evt):
            value = str(booklist.get(booklist.curselection()))
            w = value
            if w == "Cinderella":
                BookID.set("ISBN 9874651548")
                BookTitle.set("The Great")
                Author.set("Paul Parker")
                LateReturnFine.set("$2.99")
                SellingPrice.set("$19.99")
                DaysOnLoan.set(14)
                iReceipt()
                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif w == "Frankenstein":
                BookID.set("ISBN 54735737653")
                BookTitle.set("The Great")
                Author.set("John Lewis")
                LateReturnFine.set("$2.99")
                SellingPrice.set("$19.99")
                DaysOnLoan.set(14)
                iReceipt()
                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

        booklist = Listbox(DataFrameRIGHT, width=20, height=12, font=('arial', 12, 'bold'))
        booklist.bind('<<ListboxSelect>>', SelectedBook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        for items in ListOfBooks:
            booklist.insert(END, items)

        # ==========================Label===========================================|
        self.lblLabel = Label(FrameDetail, font=('arial', 10, 'bold'), pady=8, text="Member Type\t Reference No.\t Title\t First Name\t Surname\t Address 1\t Address 2\t Post Code\t Book Title\t Date borrowed\t Days on loan")
        self.lblLabel.grid(row=0, column=0)

        self.txtDisplayR = Text(FrameDetail, font=('arial', 12, 'bold'), width=121, height=4, padx=2, pady=4)
        self.txtDisplayR.grid(row=1, column=0)

        # ==========================Buttons===========================================|
        self.btnDisplayData = Button(ButtonFrame, text='Display Data', font=('arial', 12, 'bold'), width=30, bd=4, comman=iDisplayData)
        self.btnDisplayData.grid(row=0, column=0)

        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=30, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=1)

        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=30, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=30, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=3)


if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
