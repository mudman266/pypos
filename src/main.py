# Josh Williams
# PyPOS

# Import all the windows
from FIRST import Ui_MainWindow
from begin import Ui_BeginWindow
from password_entry import Ui_Dialog
from make_sale import Ui_SaleWindow
from settle import Ui_settle_window
from customer_lookup import Ui_customer_lookup_dialog
from new_customer import Ui_new_customer_dialog
from account_search_results import Ui_select_account_dialog
from manage_account import Ui_manage_account_dialog
from select_employee import Ui_time_clock_dialog
from manager import Ui_manager_dialog
from stock import Ui_stock_dialog
from groups import Ui_groups_dialog
from vendors import Ui_vendors_dialog
from inventory_count import Ui_count_dialog
from payroll import Ui_payroll_dialog
from manufacturing import Ui_manufacturing_dialog
from open_orders import Ui_open_orders_dialog
from assign_work import Ui_assign_work_dialog
from check_materials import Ui_check_materials_dialog
from receipt import Ui_receipt
from enter_amount import Ui_payment_amount_dialog
from employee_check import Ui_payroll_check_display
from timecard import Ui_timecard_dialog
from commission import Ui_commission_dialog

from PyQt6 import QtWidgets as qtw
from PyQt6.QtCore import pyqtSignal
import mysql.connector as mc
from datetime import datetime
import num2words as n2w


debugging = True

db = mc.connect(
                host="10.0.0.126",
                user="sqluser",
                password="essqueel",
                charset="utf8mb4"
            )
cursor = db.cursor()

# Set the current session number
cursor.execute("SELECT ID FROM dbs1709505.sessions")
session = cursor.fetchall()
for ses in session:
    cur_session = ses
if debugging:
    print("Session: {}".format(cur_session[0]))


# Each window needs its own class
class PyPOS(qtw.QMainWindow):
    # Custom initializer to build the window
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Define the windows that can be reached from here
        self.begin_window = Begin()
        self.time_clock_window = selectEmployee()

        # Connect the buttons to methods
        self.ui.btn_begin.clicked.connect(self.show_password_entry)
        self.ui.btn_quit.clicked.connect(self.exit)
        self.ui.btn_timeclock.clicked.connect(self.time_clock)

    # Methods to show each window
    def show_password_entry(self):
        self.pass_window = PasswordEntry()
        self.pass_window.show()

    def exit(self):
        exit(0)

    def time_clock(self):
        self.time_clock_window.show()


class PasswordEntry(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.password = ""

        # Connect the buttons to methods
        self.ui.btn_ok.clicked.connect(self.try_login)
        self.ui.btn_1.clicked.connect(self.btn_1)
        self.ui.btn_2.clicked.connect(self.btn_2)
        self.ui.btn_3.clicked.connect(self.btn_3)
        self.ui.btn_4.clicked.connect(self.btn_4)
        self.ui.btn_5.clicked.connect(self.btn_5)
        self.ui.btn_6.clicked.connect(self.btn_6)
        self.ui.btn_7.clicked.connect(self.btn_7)
        self.ui.btn_8.clicked.connect(self.btn_8)
        self.ui.btn_9.clicked.connect(self.btn_9)
        self.ui.btn_0.clicked.connect(self.btn_0)
        self.ui.btn_backspace.clicked.connect(self.btn_backspace)

    def exit(self):
        self.close()

    def try_login(self):
        cursor.execute("SELECT ID, first_name FROM dbs1709505.employee WHERE passcode='{}'".format(self.password))
        r = cursor.fetchall()
        # Debugging - print the password entered and the employee ID it links to.
        if debugging:
            print("password is: {}".format(self.password))
            for row in r:
                print("Employee ID: {}".format(row[0]))

        # Verify password is good
        if cursor.rowcount < 1:
            print("Login Failure")
            self.ui.lbl_pass_input.setText("Invalid Password")
            self.password = ""
        else:
            # Set the ID of the user that logged in, to pass to the sale window.
            for row in r:
                empid = row[0]
                print("Set empid to {}".format(empid))
            print("Login Success")
            self.load_sale_window(empid)

    def load_sale_window(self, emp_id):
        self.sale_window = makeSale(str(emp_id))
        self.close()
        self.sale_window.show()

    def btn_1(self):
        self.button_press("1")

    def btn_2(self):
        self.button_press("2")

    def btn_3(self):
        self.button_press("3")

    def btn_4(self):
        self.button_press("4")

    def btn_5(self):
        self.button_press("5")

    def btn_6(self):
        self.button_press("6")

    def btn_7(self):
        self.button_press("7")

    def btn_8(self):
        self.button_press("8")

    def btn_9(self):
        self.button_press("9")

    def btn_0(self):
        self.button_press("0")

    def btn_backspace(self):
        l = len(self.password)
        self.password = self.password[:l-1]
        cur_text = self.ui.lbl_pass_input.text()
        l2 = len(cur_text)
        cur_text = ""
        for i in range(l2 - 1):
            cur_text += "*"
        self.ui.lbl_pass_input.setText(cur_text)

    def button_press(self, pressed):
        self.password = self.password + pressed
        cur_text = self.ui.lbl_pass_input.text()
        if cur_text == "Enter Password" or cur_text == "Invalid Password":
            self.ui.lbl_pass_input.setText("*")
        else:
            self.ui.lbl_pass_input.setText(cur_text + "*")


class Begin(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_BeginWindow()
        self.ui2.setupUi(self)
        self.ui2.btn_sale_2.clicked.connect(self.exit)

    def exit(self):
        self.close()


class makeSale(qtw.QMainWindow):
    def __init__(self, emp_id):
        super().__init__()

        self.emp_id = emp_id
        self.subtotal = 0.0
        self.tax = 0.0
        self.total = 0.0

        # Setup the UI
        self.ui = Ui_SaleWindow()
        self.ui.setupUi(self)

        # Link the buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_settle.clicked.connect(self.settle_window)
        self.ui.btn_cust_lookup.clicked.connect(self.customer_lookup)
        self.ui.btn_manage_acct.clicked.connect(self.manage_account)
        self.ui.btn_tops.clicked.connect(self.pop_tops)
        self.ui.btn_bottoms.clicked.connect(self.pop_bottoms)
        self.ui.btn_ties.clicked.connect(self.pop_ties)
        self.ui.btn_manager.clicked.connect(self.show_manager)

        # Create a new ticket in the sales database for the emp_id passed in
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
        if debugging:
            print("Datetime: {}".format(timestampStr))
            print("Attempting to create new sale....")

        cursor.execute(f"INSERT INTO dbs1709505.sales (sessions_id, employee_id, sales_date, sales_tax, subtotal)\
         VALUES ({cur_session[0]}, {int(emp_id)}, {timestampStr!r}, 0.0, 0.0)")
        if debugging:
            print("Cursor executed. Committing....")
        db.commit()

        if debugging:
            print("New sale created. Huzzah!")

        # Get the sale ID so items can be added to sales_detail
        cursor.execute(f"SELECT ID FROM dbs1709505.sales WHERE sales_date = {timestampStr!r}")
        self.sale_id = cursor.fetchall()
        if debugging:
            print(f"Gathered sale id: {self.sale_id[0][0]}")

        # First group is tops
        # Todo: Make this dynamic. Add a spot in setup to choose which window to display.
        self.populate_grid("tops")

    def show_manager(self):
        self.manager_window = manager(self.emp_id)
        self.manager_window.show()

    def pop_tops(self):
        self.populate_grid("tops")

    def pop_bottoms(self):
        self.populate_grid("bottoms")

    def pop_ties(self):
        self.populate_grid("ties")

    # Populate the grid layout with stock items matching desired group
    def populate_grid(self, major_group):
        if major_group.lower() == "tops":
            # tops are groups 1,4,5,6, and 8
            if debugging:
                print("Asked for tops. Gathering tops...")
            cursor.execute(f"SELECT ID, name, price FROM dbs1709505.stock WHERE stock_group=1 or stock_group=4 or \
                stock_group=5 or stock_group=6 or stock_group=8")
            self.items = []
            for item in cursor:
                if debugging:
                    print("Item found. Array: {}".format(item))
                self.items.append(item)
            if debugging:
                print("All items in group: {}".format(self.items))
        elif major_group.lower() == "bottoms":
            # bottoms are groups 2
            if debugging:
                print("Asked for bottoms. Gathering bottoms...")
            cursor.execute(f"SELECT ID, name, price FROM dbs1709505.stock WHERE stock_group=2")
            self.items = []
            for item in cursor:
                if debugging:
                    print("Item found. Array: {}".format(item))
                self.items.append(item)
            if debugging:
                print("All items in group: {}".format(self.items))
        else:
            # remaining groups for display are ties and hats - 10 and 3 respectively
            if debugging:
                print("Asked for ties. Gathering ties...")
            cursor.execute(f"SELECT ID, name, price FROM dbs1709505.stock WHERE stock_group=3 or stock_group=10")
            self.items = []
            for item in cursor:
                if debugging:
                    print("Item found. Array: {}".format(item))
                self.items.append(item)
            if debugging:
                print("All items in group: {}".format(self.items))

        # Populate the grid with the items
        if debugging:
            print("Populating grid...")
        self.fill_items_in_grid(self.items)

        # Update the chit view if a new check
        if self.ui.tableWidget_chit.rowCount() == 0:
            if debugging:
                print("Updating the chit...")
            # Set the rows and columns. Set the column headers.
            self.ui.tableWidget_chit.setRowCount(0)
            self.ui.tableWidget_chit.setColumnCount(2)
            self.ui.tableWidget_chit.setHorizontalHeaderLabels(["Item", "Price", "Subtotal"])

        # TODO - Add Subtotal, tax, and total to the bottom of the chit.

    def fill_items_in_grid(self, items_passed):
        # Clear any items that may already be present
        self.clear_layout(self.ui.gridLayout)

        # Create the buttons from the items passed in
        row = 1
        col = 1
        for stock_item in items_passed:
            button = qtw.QPushButton(stock_item[1], self)
            button.setGeometry(200, 150, 100, 40)
            button.clicked.connect(lambda state, x=stock_item[0], y=self.sale_id: self.add_item(x, y))
            self.ui.gridLayout.addWidget(button, row, col)
            row += 1
            if row > 5:
                col += 1
                row = 1

    def add_item(self, *args):
        # Adds a selected item to the chit
        if debugging:
            print(f"Adding Item id: {args[0]} to Sale id: {args[1][0][0]}")
        cursor.execute(f"INSERT INTO dbs1709505.sales_detail (sales_id, stock_id, qty, needs_mfg) VALUES \
            ({args[1][0][0]}, {args[0]}, 1, 0)")
        db.commit()
        if debugging:
            print("Item added to sales_detail.")

        # Update the chit
        # Increase the row count by 1
        row_count = self.ui.tableWidget_chit.rowCount()
        if debugging:
            print(f"Row count is: {row_count}")
        self.ui.tableWidget_chit.setRowCount(row_count + 1)
        # Populate the row with the added item
        cursor.execute(f"SELECT name, price FROM dbs1709505.stock WHERE id = {args[0]}")
        for item in cursor:
            item_name = item[0]
            item_price = item[1]
            if debugging:
                print(f"Item stats adding to chit: Name: {item[0]} Price: {item[1]} at row: {row_count + 1}")
            self.ui.tableWidget_chit.setItem(row_count, 0, qtw.QTableWidgetItem(item_name))
            self.ui.tableWidget_chit.setItem(row_count, 1, qtw.QTableWidgetItem(str(item_price)))

        # Adjust subtotal, tax, and total.
        self.subtotal = self.subtotal + item_price
        self.tax = self.subtotal * .08
        self.total = self.subtotal + self.tax

        # Update total labels
        self.ui.lbl_subtotal_amt.setText("{:.2f}".format(self.subtotal))
        self.ui.lbl_tax_amt.setText("{:.2f}".format(self.tax))
        self.ui.lbl_total_amt.setText("{:.2f}".format(self.total))

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_layout(child.layout())

    def exit(self):
        self.close()

    def settle_window(self):
        self.settle_window = settle(self.sale_id, self.subtotal, self.tax)
        self.hide()
        self.settle_window.show()

    def customer_lookup(self):
        self.customer_lookup_window = customerLookup()
        self.customer_lookup_window.show()

    def manage_account(self):
        self.manage_account_window = manageAccount()
        self.manage_account_window.show()


class settle(qtw.QMainWindow):
    def __init__(self, sales_id, subtotal, tax):
        super().__init__()

        self.sales_id = sales_id
        self.subtotal = subtotal
        self.tax = tax
        self.payment_type = 0

        if 'paid_amt' not in locals():
            self.paid_amt = 0.0

        # Update the sale database with the tax and subtotal
        cursor.execute(f"UPDATE dbs1709505.sales SET sales_tax = {tax}, subtotal = {subtotal} WHERE id = \
            {sales_id[0][0]}")
        db.commit()

        # Setup the UI
        self.ui = Ui_settle_window()
        self.ui.setupUi(self)
        self.ui.lbl_total_amt.setText("{:.2f}".format(subtotal + tax))

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_finalize.clicked.connect(self.finalize)
        self.ui.btn_cash.clicked.connect(self.cash)
        self.ui.btn_credit.clicked.connect(self.credit)
        self.ui.btn_check.clicked.connect(self.check)
        self.ui.btn_on_acct.clicked.connect(self.on_acct)
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_0.clicked.connect(self.btn_0)
        self.ui.btn_1.clicked.connect(self.btn_1)
        self.ui.btn_2.clicked.connect(self.btn_2)
        self.ui.btn_3.clicked.connect(self.btn_3)
        self.ui.btn_4.clicked.connect(self.btn_4)
        self.ui.btn_5.clicked.connect(self.btn_5)
        self.ui.btn_6.clicked.connect(self.btn_6)
        self.ui.btn_7.clicked.connect(self.btn_7)
        self.ui.btn_8.clicked.connect(self.btn_8)
        self.ui.btn_9.clicked.connect(self.btn_9)
        self.ui.btn_decimal.clicked.connect(self.btn_decimal)
        self.ui.btn_backspace.clicked.connect(self.btn_backspace)

    def btn_1(self):
        self.button_press("1")

    def btn_2(self):
        self.button_press("2")

    def btn_3(self):
        self.button_press("3")

    def btn_4(self):
        self.button_press("4")

    def btn_5(self):
        self.button_press("5")

    def btn_6(self):
        self.button_press("6")

    def btn_7(self):
        self.button_press("7")

    def btn_8(self):
        self.button_press("8")

    def btn_9(self):
        self.button_press("9")

    def btn_0(self):
        self.button_press("0")

    def btn_decimal(self):
        self.button_press(".")

    def btn_backspace(self):
        # Take the last char off the string
        l = len(str(self.paid_amt))
        if l > 0:
            if debugging:
                print(f"Current amount: {self.paid_amt}\nAdjusting amount...")
            self.paid_amt = self.paid_amt[:l - 1]
            if debugging:
                print(f"Amount now: {self.paid_amt}")
            self.ui.lbl_amt.setText(self.paid_amt)

    def button_press(self, pressed):
        if self.paid_amt == 0:
            self.paid_amt = pressed
        else:
            self.paid_amt = str(self.paid_amt) + pressed
        cur_text = self.ui.lbl_amt.text()
        if cur_text == "0.00" or cur_text == "0.0" or cur_text == "0." or cur_text == "0" or cur_text == "":
            self.ui.lbl_amt.setText(pressed)
        else:
            self.ui.lbl_amt.setText(cur_text + pressed)

    def exit(self):
        self.close()
        makeSale.show(self)

    def cash(self):
        self.payment_type = 1
        self.paid_amt = float(self.ui.lbl_amt.text())
        self.ui.lbl_change_due_amt.setText("{:.2f}".format((self.subtotal + self.tax) - self.paid_amt))

    def credit(self):
        self.payment_type = 2

    def check(self):
        self.payment_type = 3

    def on_acct(self):
        self.payment_type = 4

    def finalize(self, payment_type=None):
        # Check that the order total has been handled.
        if float(self.paid_amt) < self.subtotal + self.tax or self.payment_type is None:
            self.warning_window = qtw.QDialog(self)
            self.warning_window.setWindowTitle("Balance not settled.")
            warning_label = qtw.QLabel("The balance has not been settled or no payment type has been chosen.")
            self.warning_window.layout = qtw.QVBoxLayout()
            self.warning_window.layout.addWidget(warning_label)
            self.warning_window.setLayout(self.warning_window.layout)
            self.warning_window.show()
            return

        # Update the DB with the payment type
        cursor.execute(
            f"UPDATE dbs1709505.sales SET payment_types_id = {self.payment_type} WHERE id = {self.sales_id[0][0]}")
        db.commit()
        if debugging:
            print("Updated sales DB with payment type.")
        self.window = receipt(self.sales_id[0][0])
        self.window.show()
        self.close()


class receipt(qtw.QDialog):
    def __init__(self, sale_id):
        super().__init__()

        self.sale_id = sale_id
        # Setup the UI
        self.ui = Ui_receipt()
        self.ui.setupUi(self)

        if debugging:
            print("Generating chit...")
        # Set the column headers
        self.ui.items_table.setRowCount(0)
        self.ui.items_table.setColumnCount(2)
        self.ui.items_table.setHorizontalHeaderLabels(["Item", "Amount"])

        # TODO: Update the Date label

        # Get all items from the sale
        sold_items = []
        cursor.execute(f"SELECT stock_id FROM dbs1709505.sales_detail WHERE sales_id = {self.sale_id}")
        # Add every sold item's id to an array
        for item in cursor:
            sold_items.append(item[0])
            if debugging:
                print(f"Appended {item[0]} to sold_items: {sold_items}")

        # For every sold item id in the array, get the name and price and insert into the table
        for items in sold_items:
            cursor.execute(f"SELECT name, price FROM dbs1709505.stock WHERE id = {items}")
            for name, price in cursor:
                cur_rows = self.ui.items_table.rowCount()
                self.ui.items_table.setRowCount(cur_rows + 1)
                self.ui.items_table.setItem(cur_rows, 0, qtw.QTableWidgetItem(name))
                self.ui.items_table.setItem(cur_rows, 1, qtw.QTableWidgetItem(str(price)))

        # Update the subtotal, tax, and total
        cursor.execute(f"SELECT subtotal, sales_tax FROM dbs1709505.sales WHERE id = {self.sale_id}")
        for subtotal, tax in cursor:
            self.ui.lbl_subtotal_amt.setText(str(subtotal))
            self.ui.lbl_tax_amt.setText(str(tax))
            self.ui.lbl_total_amt.setText(str(subtotal + tax))

        # Link buttons to methods
        self.ui.btn_done.clicked.connect(self.exit)

    def exit(self):
        self.close()


class customerLookup(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_customer_lookup_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_new_customer.clicked.connect(self.new_customer)
        self.ui.btn_search.clicked.connect(self.search_customer)

    def exit(self):
        self.close()

    def search_customer(self):
        # Find the customer based on input data
        if debugging:
            print("Beginning search routine.")

        # Check last name
        if self.ui.line_lname.text().strip():
            if debugging:
                print(f"Last name detected: {self.ui.line_lname.text()}. Searching...")
            cursor.execute(f"SELECT * FROM dbs1709505.customer WHERE last_name LIKE '%{self.ui.line_lname.text()}%'")
            # Check for 0 results

        # Check first name
        elif self.ui.line_fname.text().strip():
            if debugging:
                print("Last name empty. Checking first name.")
            if self.ui.line_fname.text().strip():
                if debugging:
                    print(f"First name detected: {self.ui.line_lname.text()}. Searching...")
                cursor.execute(
                    f"SELECT * FROM dbs1709505.customer WHERE first_name LIKE '%{self.ui.line_fname.text()}%'")

        # Check phone number
        elif self.ui.line_phone.text().strip():
            if debugging:
                print("First name empty. Checking phone number.")
            if self.ui.line_phone.text().strip():
                if debugging:
                    print(f"Phone number detected: {self.ui.line_phone.text()}. Searching...")
                cursor.execute(
                    f"SELECT * FROM dbs1709505.customer WHERE phone LIKE '%{self.ui.line_phone.text()}%'")

        # Check address
        elif self.ui.line_address.text().strip():
            if debugging:
                print("Phone number empty. Checking address.")
            if self.ui.line_address.text().strip():
                if debugging:
                    print(f"Address detected: {self.ui.line_address.text()}. Searching...")
                cursor.execute(
                    f"SELECT * FROM dbs1709505.customer WHERE address LIKE '%{self.ui.line_address.text()}%'")
                # Check for 0 results
                records = cursor.fetchall()
                if debugging:
                    print(f"Row count: {cursor.rowcount}")

        # Check for results
        records = cursor.fetchall()
        if debugging:
            print(f"Row count: {cursor.rowcount}")
        if cursor.rowcount < 1:
            error_window = qtw.QDialog(self)
            error_window.setWindowTitle("No Results")
            QBtn = qtw.QDialogButtonBox.StandardButtons.Ok
            error_window.buttonBox = qtw.QDialogButtonBox(QBtn)
            error_window.buttonBox.accepted.connect(error_window.close)
            error_window.layout = qtw.QVBoxLayout()
            message = qtw.QLabel("That search returned 0 results. Try again.")
            error_window.layout.addWidget(message)
            error_window.layout.addWidget(error_window.buttonBox)
            error_window.setLayout(error_window.layout)
            error_window.exec()
        else:
            # Record(s) found. Pass them to the customer results window
            self.close()
            self.search_reults = search_customer_results(records)
            self.search_reults.show()

    def new_customer(self):
        self.close()
        self.new_customer_window = newCustomer()
        self.new_customer_window.show()


class search_customer_results(qtw.QDialog):
    def __init__(self, recs):
        super().__init__()

        # Setup the UI
        self.ui = Ui_select_account_dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget_customers.setRowCount(cursor.rowcount)
        self.ui.tableWidget_customers.setColumnCount(7)
        self.ui.tableWidget_customers.setHorizontalHeaderLabels(["ID", "First", "Last", "Phone", "Address", "City", "State",
                                                                 "Zip"])
        # Hide the vertical header (row #)
        self.ui.tableWidget_customers.verticalHeader().setVisible(False)

        # Link buttons to methods
        self.ui.btn_select.clicked.connect(self.select_customer)
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_up.clicked.connect(self.up)
        self.ui.btn_down.clicked.connect(self.down)

        # Populate the table
        i = 0
        if debugging:
            print(f"Row count is now: {cursor.rowcount}")
        for row in recs:
            self.ui.tableWidget_customers.setItem(i, 0, qtw.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_customers.setItem(i, 1, qtw.QTableWidgetItem(row[1]))
            self.ui.tableWidget_customers.setItem(i, 2, qtw.QTableWidgetItem(row[2]))
            self.ui.tableWidget_customers.setItem(i, 3, qtw.QTableWidgetItem(row[3]))
            self.ui.tableWidget_customers.setItem(i, 4, qtw.QTableWidgetItem(row[4]))
            self.ui.tableWidget_customers.setItem(i, 5, qtw.QTableWidgetItem(row[5]))
            self.ui.tableWidget_customers.setItem(i, 6, qtw.QTableWidgetItem(row[6]))
            self.ui.tableWidget_customers.setItem(i, 7, qtw.QTableWidgetItem(row[7]))
            i += 1

    def exit(self):
        self.close()

    def select_customer(self):
        self.close()

    def up(self):
        True
        # TODO: Make it move

    def down(self):
        True
        # TODO: Make it move

        # TODO: Return customer record to the make sale screen


class newCustomer(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_new_customer_dialog()
        self.ui.setupUi(self)

        # Connect buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_add.clicked.connect(self.add_cust)

    def add_cust(self):
        if debugging:
            print("Adding customer to DB.")
        if self.ui.rad_female.isChecked():
            gender = 'F'
        else:
            gender = 'M'
        cursor.execute(f"INSERT INTO dbs1709505.customer (first_name, last_name, address, city, state, zip, gender)\
            VALUES ('{self.ui.line_fname.text()}', '{self.ui.line_lname.text()}', '{self.ui.line_street.text()}',\
            '{self.ui.line_city.text()}', '{self.ui.line_state.text()}', {self.ui.line_zip.text()}, '{gender}')")
        db.commit()
        if debugging:
            print("Customer added.")
        self.close()

    def exit(self):
        self.close()


class manageAccount(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_manage_account_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_payment.clicked.connect(self.make_payment)

    def exit(self):
        self.close()

    def make_payment(self):
        self.close()
        self.make_payment_screen = makePayment()
        self.make_payment_screen.show()


class selectEmployee(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_time_clock_dialog()
        self.ui.setupUi(self)

        # TODO: Make the employee list dynamic

        # Link buttons to methods
        self.ui.btn_emp_1.clicked.connect(self.btn_1)
        self.ui.btn_emp_2.clicked.connect(self.btn_2)
        self.ui.btn_emp_3.clicked.connect(self.btn_3)
        self.ui.btn_emp_4.clicked.connect(self.btn_4)
        self.ui.btn_emp_5.clicked.connect(self.btn_5)
        self.ui.btn_emp_6.clicked.connect(self.btn_6)
        self.ui.btn_emp_7.clicked.connect(self.btn_7)
        self.ui.btn_emp_8.clicked.connect(self.btn_8)
        self.ui.btn_emp_9.clicked.connect(self.btn_9)
        self.ui.btn_emp_10.clicked.connect(self.btn_10)
        self.ui.btn_emp_11.clicked.connect(self.btn_11)

    def exit(self):
        self.close()

    def btn_1(self):
        self.time_clock(1)

    def btn_2(self):
        self.time_clock(2)

    def btn_3(self):
        self.time_clock(3)

    def btn_4(self):
        self.time_clock(12)

    def btn_5(self):
        self.time_clock(5)

    def btn_6(self):
        self.time_clock(6)

    def btn_7(self):
        self.time_clock(7)

    def btn_8(self):
        self.time_clock(8)

    def btn_9(self):
        self.time_clock(9)

    def btn_10(self):
        self.time_clock(10)

    def btn_11(self):
        self.time_clock(11)

    def btn_12(self):
        self.time_clock(12)

    def time_clock(self, emp_id):
        # is the employee already clocked in?
        logins = []
        cur_date = datetime.now()
        cur_date_string = datetime.strftime(cur_date, "%Y-%m-%d")
        cur_date_string = cur_date_string
        # Get all logins from today
        cursor.execute(f"SELECT id, time_in, time_out FROM dbs1709505.labor WHERE employee_id = {emp_id} AND time_in \
            LIKE CONCAT({cur_date_string!r}, '%')")
        for login_id, time_in, time_out in cursor:
            logins.append([login_id, time_in, time_out])
        if debugging:
            print(f"Retrieved logins: {logins}")
        # If zero logins were returned, use the clock in function
        if len(logins) < 1:
            self.login(emp_id)

        # If a time_in exists with no time_out, use the logout function with the record id
        for sets in logins:
            if sets[1] is not None:
                if sets[2] is None:
                    self.logout(sets[0])
        if len(logins) > 0:
            if logins[len(logins) - 1][2] is not None:
                self.login(emp_id)

    def login(self, emp_id):
        if debugging:
            print(f"Running login for emp: {emp_id}")
        cur_date = datetime.now()
        timestampStr = cur_date.strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(f"INSERT INTO dbs1709505.labor (time_in, employee_id) VALUES ({timestampStr!r}, {emp_id})")
        db.commit()
        self.close()
        if debugging:
            print("Logged in.")

    def logout(self, login_record_id):
        if debugging:
            print(f"Running logout on record: {login_record_id}")
        cur_date = datetime.now()
        timestampStr = cur_date.strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(f"UPDATE dbs1709505.labor SET time_out = {timestampStr!r} WHERE id = {login_record_id}")
        db.commit()
        if debugging:
            print("Logged out.")
            self.close()


class manager(qtw.QDialog):
    def __init__(self, emp_id):
        super().__init__()

        self.manager_id = emp_id

        # Setup the UI
        self.ui = Ui_manager_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_stock.clicked.connect(self.stock)
        self.ui.btn_deposit.clicked.connect(self.deposit)
        self.ui.btn_payroll.clicked.connect(self.payroll)
        self.ui.btn_manufacturin.clicked.connect(self.manufacturing)
        self.ui.btn_stock.clicked.connect(self.stock)

    def exit(self):
        self.close()

    def deposit(self):
        self.close()
        self.window = enter_deposit(self.manager_id)
        self.window.show()

    def stock(self):
        True

    def payroll(self):
        self.close()
        self.window = payroll()
        self.window.show()

    def manufacturing(self):
        self.close()
        self.window = manufacturing()
        self.window.show()

    def stock(self):
        self.window = stock()
        self.window.show()

class enter_deposit(qtw.QDialog):
    def __init__(self, emp_id):
        super().__init__()

        self.paid_amt = 0
        self.cash = None
        self.checks = None
        self.emp_id = emp_id

        # Setup the UI
        self.ui = Ui_payment_amount_dialog()
        self.ui.setupUi(self)
        self.ui.label.setText("Enter Cash:")

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_0.clicked.connect(self.btn_0)
        self.ui.btn_1.clicked.connect(self.btn_1)
        self.ui.btn_2.clicked.connect(self.btn_2)
        self.ui.btn_3.clicked.connect(self.btn_3)
        self.ui.btn_4.clicked.connect(self.btn_4)
        self.ui.btn_5.clicked.connect(self.btn_5)
        self.ui.btn_6.clicked.connect(self.btn_6)
        self.ui.btn_7.clicked.connect(self.btn_7)
        self.ui.btn_8.clicked.connect(self.btn_8)
        self.ui.btn_9.clicked.connect(self.btn_9)
        self.ui.btn_decimal.clicked.connect(self.btn_decimal)
        self.ui.btn_backspace.clicked.connect(self.btn_backspace)
        self.ui.btn_ok.clicked.connect(self.ok)

    def btn_1(self):
        self.button_press("1")

    def btn_2(self):
        self.button_press("2")

    def btn_3(self):
        self.button_press("3")

    def btn_4(self):
        self.button_press("4")

    def btn_5(self):
        self.button_press("5")

    def btn_6(self):
        self.button_press("6")

    def btn_7(self):
        self.button_press("7")

    def btn_8(self):
        self.button_press("8")

    def btn_9(self):
        self.button_press("9")

    def btn_0(self):
        self.button_press("0")

    def btn_decimal(self):
        self.button_press(".")

    def btn_backspace(self):
        # Take the last char off the string
        l = len(str(self.paid_amt))
        if l > 0:
            if debugging:
                print(f"Current amount: {self.paid_amt}\nAdjusting amount...")
            self.paid_amt = self.paid_amt[:l - 1]
            if debugging:
                print(f"Amount now: {self.paid_amt}")
            self.ui.lbl_amt.setText(self.paid_amt)

    def button_press(self, pressed):
        if self.paid_amt == 0:
            self.paid_amt = pressed
        else:
            self.paid_amt = str(self.paid_amt) + pressed
        cur_text = self.ui.lbl_amt.text()
        if cur_text == "0.00" or cur_text == "0.0" or cur_text == "0." or cur_text == "0" or cur_text == "":
            self.ui.lbl_amt.setText(pressed)
        else:
            self.ui.lbl_amt.setText(cur_text + pressed)

    def ok(self):
        # Has cash already been entered?
        if self.cash is None:
            self.cash = self.paid_amt
            if debugging:
                print(f"Got cash input of: {self.cash}")
            self.ui.label.setText("Enter Checks:")
            self.ui.lbl_amt.setText("0.00")
            self.paid_amt = 0
        else:
            # Cash already entered, this must be checks
            self.checks = self.paid_amt
            if debugging:
                print(f"Got check input of: {self.checks}")
                print("Making deposit...")
            cur_date = datetime.now()
            cur_date_string = datetime.strftime(cur_date, "%Y-%m-%d %H:%M:%S")
            cursor.execute(f"INSERT INTO dbs1709505.deposits (date_time, employee_id, cash, checks) VALUES ("
                           f"{cur_date_string!r}, {self.emp_id}, {self.cash}, {self.checks})")
            db.commit()
            if debugging:
                print("Deposit made.")
            self.close()

    def exit(self):
        self.close()


class stock(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_stock_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_vendor_functs.clicked.connect(self.edit_vendor)
        self.ui.btn_perform_count.clicked.connect(self.inventory_count)
        self.ui.btn_receive_order.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def edit_vendor(self):
        self.close()
        self.vendor_screen = vendors()
        self.vendor_screen.show()

    def inventory_count(self):
        self.close()
        self.window = inventoryCount()
        self.window.show()


class groups(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_groups_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class vendors(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_vendors_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_add.clicked.connect(self.exit)
        self.ui.btn_generate.clicked.connect(self.exit)

        # Setup the table
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Name", "Vendor ID", "Street", "City", "State", "Zip",
                                                       "Contact", "Phone", "Products"])

        # Populate table
        cursor.execute("SELECT * FROM dbs1709505.vendors")
        for idx, name, vendor_id, contact_name, phone, address, city, state, zipc, products in cursor:
            # Add a row
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, qtw.QTableWidgetItem(name))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, qtw.QTableWidgetItem(str(vendor_id)))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, qtw.QTableWidgetItem(address))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 3, qtw.QTableWidgetItem(city))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 4, qtw.QTableWidgetItem(state))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 5, qtw.QTableWidgetItem(zipc))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 6, qtw.QTableWidgetItem(contact_name))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 7, qtw.QTableWidgetItem(phone))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 8, qtw.QTableWidgetItem(products))

    def exit(self):
        self.close()


class inventoryCount(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_count_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class payroll(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_payroll_dialog()
        self.ui.setupUi(self)


        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_cut_check.clicked.connect(self.cut_check)
        self.ui.btn_time_card.clicked.connect(self.time_card)
        self.ui.btn_commission.clicked.connect(self.commission)

    def exit(self):
        self.close()

    def cut_check(self):
        if self.ui.radioButton_1.isChecked():
            emp = 1
        elif self.ui.radioButton_2.isChecked():
            emp = 2
        elif self.ui.radioButton_3.isChecked():
            emp = 3
        elif self.ui.radioButton_4.isChecked():
            emp = 12
        elif self.ui.radioButton_5.isChecked():
            emp = 5
        elif self.ui.radioButton_6.isChecked():
            emp = 6
        elif self.ui.radioButton_7.isChecked():
            emp = 7
        elif self.ui.radioButton_8.isChecked():
            emp = 8
        elif self.ui.radioButton_9.isChecked():
            emp = 9
        elif self.ui.radioButton_10.isChecked():
            emp = 10
        elif self.ui.radioButton_11.isChecked():
            emp = 11
        else:
            return
        start_date = self.ui.dateEdit_start.date()
        end_date = self.ui.dateEdit_end.date()
        self.window = employee_check(emp, start_date, end_date)
        self.window.show()

    def time_card(self):
        if self.ui.radioButton_1.isChecked():
            emp = 1
        elif self.ui.radioButton_2.isChecked():
            emp = 2
        elif self.ui.radioButton_3.isChecked():
            emp = 3
        elif self.ui.radioButton_4.isChecked():
            emp = 12
        elif self.ui.radioButton_5.isChecked():
            emp = 5
        elif self.ui.radioButton_6.isChecked():
            emp = 6
        elif self.ui.radioButton_7.isChecked():
            emp = 7
        elif self.ui.radioButton_8.isChecked():
            emp = 8
        elif self.ui.radioButton_9.isChecked():
            emp = 9
        elif self.ui.radioButton_10.isChecked():
            emp = 10
        elif self.ui.radioButton_11.isChecked():
            emp = 11
        else:
            return
        start_date = self.ui.dateEdit_start.date()
        end_date = self.ui.dateEdit_end.date()
        self.window = timecard(emp, start_date, end_date)
        self.window.show()

    def commission(self):
        if self.ui.radioButton_1.isChecked():
            emp = 1
        elif self.ui.radioButton_2.isChecked():
            emp = 2
        elif self.ui.radioButton_3.isChecked():
            emp = 3
        elif self.ui.radioButton_4.isChecked():
            emp = 12
        elif self.ui.radioButton_5.isChecked():
            emp = 5
        elif self.ui.radioButton_6.isChecked():
            emp = 6
        elif self.ui.radioButton_7.isChecked():
            emp = 7
        elif self.ui.radioButton_8.isChecked():
            emp = 8
        elif self.ui.radioButton_9.isChecked():
            emp = 9
        elif self.ui.radioButton_10.isChecked():
            emp = 10
        elif self.ui.radioButton_11.isChecked():
            emp = 11
        else:
            return
        start_date = self.ui.dateEdit_start.date()
        end_date = self.ui.dateEdit_end.date()
        self.window = commission(emp, start_date, end_date)
        self.window.show()


class commission(qtw.QDialog):
    def __init__(self, emp_id, start, end):
        super().__init__()

        # Setup the UI
        self.ui = Ui_commission_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

        # Setup the table
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Sales Date", "Invoice", "Retail Total", "Commission"])

        # Convert Pyqt dates to datetime dates
        self.start_date = datetime.strptime(str(start.toPyDate()), "%Y-%m-%d")
        self.end_date = datetime.strptime(str(end.toPyDate()), "%Y-%m-%d")
        self.start_date_str = datetime.strftime(self.start_date, "%Y-%m-%d %H:%M:%S")
        self.end_date_str = datetime.strftime(self.end_date, "%Y-%m-%d")
        self.end_date_str = self.end_date_str + " 23:59:59"

        # Gather sales by employee during period
        cursor.execute(f"SELECT id, sales_date, subtotal FROM dbs1709505.sales WHERE sales_date >= \
            {self.start_date_str!r} AND sales_date <= {self.end_date_str!r} AND employee_id = {emp_id} \
            AND refunded = 0 AND voided = 0 AND subtotal > 0.0")
        total_sales = 0.0
        total_commish = 0.0
        for inv, dt, sub in cursor:
            # Add a row
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0,
                                        qtw.QTableWidgetItem(datetime.strftime(dt, "%m-%d-%Y")))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, qtw.QTableWidgetItem(str(inv)))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, qtw.QTableWidgetItem(str(sub)))
            total_sales += float(sub)
            commish = round((float(sub) * .1), 2)
            total_commish += commish
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 3,
                                        qtw.QTableWidgetItem(str(f"{commish:.2f}")))

        # Update totals
        self.ui.lbl_total_retail.setText(f"Total Retail: {total_sales:.2f}")
        self.ui.lbl_total_commission.setText(f"Total Commission: {total_commish:.2f}")

        # Update name and date
        cursor.execute(f"SELECT first_name from dbs1709505.employee WHERE id = {emp_id}")
        for name in cursor:
            self.ui.lbl_salesperson.setText(f"Salesperson: {name[0]}")

        cur_date = datetime.now()
        cur_date = datetime.strftime(cur_date, "%m-%d-%Y")
        self.ui.lbl_report_date.setText(f"Report Date: {cur_date}")

    def exit(self):
        self.close()


class timecard(qtw.QDialog):
    def __init__(self, emp_id, start, end):
        super().__init__()

        self.total_hours = 0.0

        # Setup the UI
        self.ui = Ui_timecard_dialog()
        self.ui.setupUi(self)

        # Convert Pyqt dates to datetime dates
        self.start_date = datetime.strptime(str(start.toPyDate()), "%Y-%m-%d")
        self.end_date = datetime.strptime(str(end.toPyDate()), "%Y-%m-%d")
        self.start_date_str = datetime.strftime(self.start_date, "%Y-%m-%d %H:%M:%S")
        self.end_date_str = datetime.strftime(self.end_date, "%Y-%m-%d")
        self.end_date_str = self.end_date_str + " 23:59:59"

        # Find logins in time range
        if debugging:
            print(f"Gathering hours for timecard.\nInfo - Emp: {emp_id}\nStart Date: {self.start_date_str!r}\n"
                  f"End Date: {self.end_date_str!r}")
        cursor.execute(f"SELECT time_in, time_out FROM dbs1709505.labor WHERE employee_id = {emp_id} AND time_in "
                       f">= {self.start_date_str!r} and time_out <= {self.end_date_str!r}")

        # Setup the timecard table
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Date", "Time In", "Time Out", "Hours"])

        # For each login, gather the hours worked
        for login_time, logout_time in cursor:
            # Add a row
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)

            # Date from this login
            date = datetime.strftime(login_time, "%m-%d-%Y")
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, qtw.QTableWidgetItem(date))

            # Time in
            time_in = datetime.strftime(login_time, "%H:%M:%S")
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, qtw.QTableWidgetItem(time_in))

            # Time out
            time_out = datetime.strftime(logout_time, "%H:%M:%S")
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, qtw.QTableWidgetItem(time_out))

            delta = logout_time - login_time
            if debugging:
                print(f"Found time delta of: {delta}")

            # Convert the delta to hours
            worked = str(delta).split(":")
            self.total_hours += int(worked[0])
            self.total_hours += int(worked[1]) / 60
            hours_worked = 0
            hours_worked += int(worked[0])
            hours_worked += int(worked[1]) / 60

            # Update hours worked for the row
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 3,
                                        qtw.QTableWidgetItem(str(f"{hours_worked:.2f}")))
        if debugging:
            print(f"Total hours worked: {self.total_hours:.2f}")

        # Update total hours
        self.ui.lbl_total_hours.setText(f"Total Hours: {self.total_hours:.2f}")

        # Set name and ID
        self.ui.lbl_id.setText(f"ID: {emp_id}")
        cursor.execute(f"SELECT first_name FROM dbs1709505.employee WHERE id = {emp_id}")
        for result in cursor:
            self.ui.lbl_name.setText(f"Name: {result[0]}")

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    def exit(self):
        self.close()


class employee_check(qtw.QDialog):
    def __init__(self, emp_id, start_date, end_date):
        super().__init__()

        self.total_hours = 0.0

        # Setup the ui
        self.ui = Ui_payroll_check_display()
        self.ui.setupUi(self)

        # Convert Pyqt dates to datetime dates
        self.start_date = datetime.strptime(str(start_date.toPyDate()), "%Y-%m-%d")
        self.end_date = datetime.strptime(str(end_date.toPyDate()), "%Y-%m-%d")
        self.start_date_str = datetime.strftime(self.start_date, "%Y-%m-%d %H:%M:%S")
        self.end_date_str = datetime.strftime(self.end_date, "%Y-%m-%d")
        self.end_date_str = self.end_date_str + " 23:59:59"

        # Find logins in time range
        if debugging:
            print(f"Generating an employee check.\nInfo - Emp: {emp_id}\nStart Date: "
                  f"{self.start_date_str!r}\nEnd Date: {self.end_date_str!r}")
        cursor.execute(f"SELECT time_in, time_out FROM dbs1709505.labor WHERE employee_id = {emp_id} AND time_in "
                       f">= {self.start_date_str!r} and time_out <= {self.end_date_str!r}")

        # For each login, gather the hours worked
        for login_time, logout_time in cursor:
            delta = logout_time - login_time
            if debugging:
                print(f"Found time delta of: {delta}")

            # Convert the delta to hours
            worked = str(delta).split(":")
            self.total_hours += int(worked[0])
            self.total_hours += int(worked[1])/60
        if debugging:
            print(f"Total hours worked: {self.total_hours:.2f}")

        # Build the entry for the payroll_history DB

        # Gross pay
        cursor.execute(f"SELECT salaried, pay_rate, ssn, first_name FROM dbs1709505.employee WHERE id = {emp_id}")
        if debugging:
            print(f"Calculating gross pay for emp: {emp_id}")
        for record in cursor:
            self.salaried = record[0]
            self.pay_rate = record[1]
            self.ssn = record[2]
            self.first_name = record[3]

        if self.salaried == 0:
            self.gross_pay = float(self.pay_rate) * self.total_hours
            self.fica_tax = self.gross_pay * .062
            self.fita_tax = self.gross_pay * .06
            self.medicare_tax = self.gross_pay * .0145
            self.state_tax = self.gross_pay * .0525
            self.total_pay = self.gross_pay - round(self.fica_tax, 2) - round(self.fita_tax, 2)\
                             - round(self.medicare_tax, 2) - round(self.state_tax, 2)
        else:
            # Salaried - pay_rate * number days worked
            cursor.execute(f"SELECT time_in, time_out FROM dbs1709505.labor WHERE employee_id = {emp_id}\
                AND time_in >= {self.start_date_str!r} AND time_out <= {self.end_date_str!r}")
            days_worked = 0
            paying_for_date = None

            # Check each login to see if it occurs on the same day as the previous
            for tin, tout in cursor:
                # First run
                if paying_for_date is None:
                    # Set the paying date
                    paying_for_date_str = datetime.strftime(tin, "%Y-%m-%d")
                    paying_for_date = datetime.strptime(paying_for_date_str, "%Y-%m-%d")
                    days_worked += 1
                else:
                    # Not first run
                    tin_str = datetime.strftime(tin, "%Y-%m-%d")
                    tin_date = datetime.strptime(tin_str, "%Y-%m-%d")
                    if debugging:
                        print(f"Comparing {tin_date} to {paying_for_date}")
                    # Compare login date to the paying date
                    if tin_date > paying_for_date:
                        if debugging:
                            print("Newer date. Adding day worked.")
                        paying_for_date = tin_date
                        days_worked += 1
            if debugging:
                print(f"Day count: {days_worked}")

            self.gross_pay = float(days_worked) * float(self.pay_rate)
            self.fica_tax = self.gross_pay * .062
            self.fita_tax = self.gross_pay * .06
            self.medicare_tax = self.gross_pay * .0145
            self.state_tax = self.gross_pay * .0525
            self.total_pay = self.gross_pay - round(self.fica_tax, 2) - round(self.fita_tax, 2) \
                             - round(self.medicare_tax, 2) - round(self.state_tax, 2)

        # Insert the entry into payroll_history DB
        cur_date = datetime.now()
        cur_date_str = datetime.strftime(cur_date, "%Y-%m-%d %H:%M:%S")
        cursor.execute(f"INSERT INTO dbs1709505.paycheck_history (employee_id, date_time, gross_pay, fica_tax, "
                       f"fita_tax, medicare_tax, state_tax) VALUES ({emp_id}, {cur_date_str!r}, {self.gross_pay}, "
                       f"{self.fica_tax}, {self.fita_tax}, {self.medicare_tax}, {self.state_tax})")
        db.commit()
        if debugging:
            print("Paycheck added to paycheck_history.")

        # Use the record number for the check number
        cursor.execute("SELECT MAX(id) FROM dbs1709505.paycheck_history")
        for rec in cursor:
            self.check_number = rec[0]

        # Update the UI
        cur_date_only = datetime.strftime(cur_date, "%m-%d-%Y")
        self.ui.lbl_name.setText(f"Name: {self.first_name}")
        self.ui.lbl_pay_to.setText(f"Pay to the order of: {self.first_name}")
        self.ui.lbl_date.setText(f"Date: {cur_date_only}")
        self.ui.lbl_chk_no.setText(f"Check Number: {self.check_number}")
        self.ui.lbl_numeric_amt.setText(f"${self.total_pay:.2f}")
        amounts = f"{self.total_pay:.2f}".split(".")
        written_dollar_amt = n2w.num2words(amounts[0])
        written_change_amt = n2w.num2words(amounts[1])
        self.ui.lbl_written_amt.setText(f"Amount: {written_dollar_amt} Dollars and {written_change_amt} Cents.")

        # Update tables
        self.ui.tableWidget_2.setRowCount(6)
        self.ui.tableWidget_2.setColumnCount(2)
        self.ui.tableWidget_2.setVerticalHeaderLabels(["Gross Pay", "FICA", "FITA", "Med", "State", "Net Pay"])
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Current", "Year to Date"])

        # Top info table
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setHorizontalHeaderLabels(["SSN"])
        self.ui.tableWidget.setItem(0, 0, qtw.QTableWidgetItem(f"{self.ssn}"))

        # Current paycheck table
        self.ui.tableWidget_2.setItem(0, 0, qtw.QTableWidgetItem(f"{self.gross_pay:.2f}"))
        self.ui.tableWidget_2.setItem(1, 0, qtw.QTableWidgetItem(f"{self.fica_tax:.2f}"))
        self.ui.tableWidget_2.setItem(2, 0, qtw.QTableWidgetItem(f"{self.fita_tax:.2f}"))
        self.ui.tableWidget_2.setItem(3, 0, qtw.QTableWidgetItem(f"{self.medicare_tax:.2f}"))
        self.ui.tableWidget_2.setItem(4, 0, qtw.QTableWidgetItem(f"{self.state_tax:.2f}"))
        self.ui.tableWidget_2.setItem(5, 0, qtw.QTableWidgetItem(f"{self.total_pay:.2f}"))

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    def exit(self):
        self.close()


class manufacturing(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_manufacturing_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_view_orders.clicked.connect(self.open_orders)
        self.ui.btn_assign_work.clicked.connect(self.assign_work)
        self.ui.btn_check_materials.clicked.connect(self.check_materials)

    def exit(self):
        self.close()

    def open_orders(self):
        self.close()
        self.window = openOrders()
        self.window.show()

    def assign_work(self):
        self.close()
        self.window = assignWork()
        self.window.show()

    def check_materials(self):
        self.close()
        self.window = checkMaterials()
        self.window.show()


class openOrders(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_open_orders_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    def exit(self):
        self.close()


class assignWork(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_assign_work_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class checkMaterials(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_check_materials_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
