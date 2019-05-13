import csv
from tkinter import messagebox
from pandas import read_csv,DataFrame
from os import path
from datetime import datetime
current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
import tkinter as tk
from tkinter.ttk import Progressbar
import time
from tkinter import HORIZONTAL,filedialog
from PyQt5.QtGui import QStandardItemModel,QStandardItem,QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QAbstractItemView,QFileDialog,QLineEdit,QLabel,QProgressBar,QListWidget,QListView
import sys
import list11
from tkinter import *
from tkinter import ttk
from tkinter.font import Font


class App(QWidget):


    def __init__(self):
        super().__init__()

        self.title = 'Trimmer'
        self.left = x
        self.top = y
        self.width = 620
        self.height = 400
        self.initUI()


    def initUI(self):
        global button1
        global button2
        global button3
        global button4
        global button5

        self.setWindowTitle(self.title)
        self.setMaximumSize(620,400)
        self.setMinimumSize(620,700)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon("images.ico"))

        button1 = QPushButton('Select Files', self)
        button1.setToolTip('This is an example button')
        button1.move(70, 60)
        button1.resize(100,30)
        button1.clicked.connect(self.openFileNamesDialog)

        button2 = QPushButton('Run for All', self)
        button2.setToolTip('This is an example button')
        button2.move(70, 480)
        button2.resize(240,30)
        button2.clicked.connect(self.trim)
        button2.setEnabled(False)


        button3 = QPushButton('Run for Affacted', self)
        button3.setToolTip('This is an example button')
        button3.move(310, 450)
        button3.resize(240,30)
        button3.clicked.connect(self.trim_affacted)
        button3.setEnabled(False)

        button4 = QPushButton('Check Affacted Files', self)
        button4.setToolTip('This is an example button')
        button4.move(70, 450)
        button4.resize(240,30)
        button4.clicked.connect(self.check_Extra_spaces,)
        button4.setEnabled(False)


        button5 = QPushButton('Reset', self)
        button5.setToolTip('This is an example button')
        button5.move(310, 480)
        button5.resize(240, 30)
        button5.clicked.connect(self.reset)
        button5.setEnabled(False)


        button6 = QPushButton('Close', self)
        button6.setToolTip('This is an example button')
        button6.move(450, 630)
        button6.resize(100, 30)
        button6.clicked.connect(self.close_window)


        # button7 = QPushButton('See logs', self)
        # button7.setToolTip('This is an example button')
        # button7.move(250, 630)
        # button7.resize(100, 30)
        # button7.clicked.connect(self.openpop_up)

        label2 = QLabel('Set Output Path :', self)
        label2.move(70, 155)

        global textbox1
        global textbox2
        global textbox3
        global model,list1

        textbox1 = QLineEdit(self)
        textbox1.move(170,60)
        textbox1.resize(380, 30)
        textbox1.setReadOnly(True)

        textbox2 = QLineEdit(desktop,self)
        textbox2.move(170, 150)
        textbox2.resize(380, 30)

        list1 = QListView(self)
        list1.setWindowTitle('Affected File List')
        list1.setMinimumSize(100, 200)
        list1.move(70, 240)
        list1.resize(480, 26)
        list1.setEditTriggers(QAbstractItemView.NoEditTriggers)

        global progress
        progress = QProgressBar(self)
        progress.move(70,530)
        progress.resize(500, 26)
        progress.setValue(0)

        self.show()

    def openFileNamesDialog(self):


        global files
        options = QFileDialog.Options()


        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select Files", "",
                                                " CSV files (*.csv)", options=options)


        if files:
            print(files)
        g = ""
        for i in files:
            c = i.split("/")[-1]
            print(c)
            g = g + c + ";"
        print(g)
        textbox1.setText(g)
        if len(files) !=0:
            button4.setEnabled(True)
            button2.setEnabled(True)
            button5.setEnabled(True)



        # self.textbox1.setText() = 'John'
        # textbox1.move(175, 70)
        # textbox1.resize(320, 26)

    def reset(self):
        textbox1.setText("")
        textbox2.setText(desktop)
        model = QStandardItemModel(list1)
        list1.setModel(model)
        global files
        global file_names
        global file_name_list
        files = []
        file_names = []
        file_name_list = []
        print(textbox2.text())
        button2.setEnabled(False)
        button3.setEnabled(False)
        button4.setEnabled(False)
        progress.setValue(0)

        print("reset")

    def check_Extra_spaces(self):
        root1 = textbox2.text()
        if len(files) !=0:
            button3.setEnabled(True)
            model = QStandardItemModel(list1)
            global file_names
            file_names = []
            for name in files:
                file = open(name)
                reader = csv.reader(file)
                affacted = 0
                for a in reader:
                    if affacted == 0:
                        for i in a:
                            if i.startswith(" ") or i.endswith(" "):
                                print(i)
                                affacted = 1
                                file_names.append(name)
            print(name + "str")
            file_name_list = []
            for file in file_names:
                print(file)
                c = file.split("/")[-1]
                print(c)
                file_name_list.append(c)
            print(file_name_list)
            for file in file_name_list:
                # create an item with a caption
                item = QStandardItem(file)
                # add a checkbox to it

                # item.setCheckable(True)
                # Add the item to the model
                model.appendRow(item)
                # Apply the model to the list view
            list1.setModel(model)
            list1.show()
            if len(file_names) ==0:
                file = "No Affected File found"
                item = QStandardItem(file)
                # add a checkbox to it

                # item.setCheckable(True)
                # Add the item to the model
                model.appendRow(item)
            if file =="No Affected File found":
                button3.setEnabled(False)
            affacted_list = []
            for file in files:
                try:

                    df = read_csv(file)
                    for index, row in df.iterrows():

                            #     print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                            #     print(type(row))
                            current_code = row.iloc[0]
                            for i, v in row.iteritems():
                                if str(v).startswith(" ") or str(v).endswith(" "):
                                    #             print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    row = file.split("/")[-1],current_code, i, v
                                    print("_____________________________")
                                    print(row)
                                    print("_____________________________")
                                    affacted_list.append(row)
                except:
                        pass
            f_df= DataFrame(affacted_list)
            f_df.to_csv(root1+"//Issue_log_"+str(current_datetime)+".csv",index=False)
            return file_names
        else:

            root.withdraw()
            messagebox.showerror("Error", "Please Select Files !")

    def trim(self):
        if path.isdir(textbox2.text()):
            progress.setValue(10)
            time.sleep(3)
            progress.setValue(20)
            time.sleep(2)
            progress.setValue(40)
            time.sleep(2)
            progress.setValue(80)
            time.sleep(2)

            def trimAllColumns(df):
                trimStrings = lambda x: x.strip() if type(x) is str else x
                return df.applymap(trimStrings)
            if path.isdir(str(textbox2.text())):
             root1 = textbox2.text()
            print(str(root1)+"******************")
            print(files)
            for file in files:
                file1 = file.split("/")[-1]
                temp_df = read_csv(file)
                df = trimAllColumns(temp_df)
                print(file1+"gggg")
                df.to_csv(root1+"//Trimed_file_"+str(current_datetime)+"_"+ file1,index=False)
            time.sleep(1)
            progress.setValue(100)
            root.withdraw()
            messagebox.showinfo("Success", "Successfully Removed Leading and trailing spaces.")
        else:
            root.withdraw()
            messagebox.showerror("Error", "Error found in Set Output Path field! \n"
                                          "Given path doesn't exist, Please Enter Correct path.")

    def trim_affacted(self):
        if path.isdir(textbox2.text()):

                progress.setValue(10)
                time.sleep(3)
                progress.setValue(20)
                time.sleep(2)
                progress.setValue(40)
                time.sleep(2)
                progress.setValue(80)
                time.sleep(2)

                def trimAllColumns(df):
                    trimStrings = lambda x: x.strip() if type(x) is str else x
                    return df.applymap(trimStrings)

                if path.isdir(str(textbox2.text())):
                    root1 = textbox2.text()
                print(str(root1) + "******************")
                print(files)
                for file in file_names:
                    try:
                        file1 = file.split("/")[-1]
                        temp_df = read_csv(file)
                        df = trimAllColumns(temp_df)
                        print(file1 + "gggg")
                        df.to_csv(root1 + "//Trimed_file_" + str(current_datetime) + "_" + file1,index=False)
                    except:print(str(file)+" #error")
                time.sleep(1)
                progress.setValue(100)
                root.withdraw()
                messagebox.showinfo("Success", "Successfully Removed Leading and trailing spaces.")
        else:
            root.withdraw()
            messagebox.showerror("Error", "Error found in Set Output Path field! \n"
                                          "Given path doesn't exist, Please Enter Correct path.")

    def openoutput_folder(self):
        root.filename = filedialog.textbox2(initialdir=textbox2.text(), title="Select file",
                                                   filetypes=(("jpeg files", "*.csv"), ("all files", "*.*")))

    def close_window(root):
        root.destroy()

    # def openpop_up(self):
    #     m1 = MCListDemo()
    #     m1._create_demo_panel()






if __name__ == '__main__':
    root = tk.Tk()
    # root.iconbitmap(r'C:\Users\anupam.soni\Pictures\walls\417647.jpg')
    progress = Progressbar(root, orient=HORIZONTAL, length=100, mode="indeterminate")

    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)


    desktop = path.expanduser("~/Desktop")
    desktop = desktop.replace("/", "//")


    # desktop.replace(r"\",")

    global files
    files = ""
    app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())



