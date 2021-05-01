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
from enter_amount import Ui_payment_amount_dialog
from manage_account import Ui_manage_account_dialog
from select_employee import Ui_time_clock_dialog
from manager import Ui_manager_dialog
from stock import Ui_stock_dialog
from groups import Ui_groups_dialog
from vendors import Ui_vendors_dialog
from add_item import Ui_add_item_dialog
from edit_employee import Ui_edit_employee_dialog
from edit_item import Ui_edit_item_dialog
from inventory_count import Ui_count_dialog
from payroll import Ui_payroll_dialog
from manufacturing import Ui_manufacturing_dialog
from open_orders import Ui_open_orders_dialog
from assign_work import Ui_assign_work_dialog
from check_materials import Ui_check_materials_dialog
from PyQt6 import QtWidgets as qtw
from PyQt6.QtCore import pyqtSignal
import mysql.connector as mc
from datetime import datetime


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
        self.pass_window = PasswordEntry()
        self.begin_window = Begin()
        self.time_clock_window = selectEmployee()
        self.manager_window = manager()

        # Connect the buttons to methods
        self.ui.btn_begin.clicked.connect(self.show_password_entry)
        self.ui.btn_quit.clicked.connect(self.exit)
        self.ui.btn_timeclock.clicked.connect(self.time_clock)
        self.ui.btn_manager.clicked.connect(self.show_manager)

    # Methods to show each window
    def show_password_entry(self):
        self.pass_window.show()

    def show_manager(self):
        self.manager_window.show()

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

        # Create a new ticket in the sales database for the emp_id passed in
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
        if debugging:
            print("Datetime: {}".format(timestampStr))
            print("Attempting to create new sale....")

        cursor.execute(f"INSERT INTO dbs1709505.sales (sessions_id, employee_id, sales_date, sales_tax, subtotal) VALUES ({cur_session[0]}, {int(emp_id)}, {timestampStr!r}, 0.0, 0.0)")
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
        self.populate_grid("tops")

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
            cursor.execute(f"SELECT ID, name, price FROM dbs1709505.stock WHERE stock_group=1 or stock_group=4 or stock_group=5 or stock_group=6 or stock_group=8")
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
            # new_item = qtw.QTableWidgetItem("Test 1")
            # self.ui.tableWidget_chit.setItem(1, 1, new_item)
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
        cursor.execute(f"INSERT INTO dbs1709505.sales_detail (sales_id, stock_id, qty, needs_mfg) VALUES ({args[1][0][0]}, {args[0]}, 1, 0)")
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

        if 'paid_amt' not in locals():
            self.paid_amt = 0.0

        # Update the sale database with the tax and subtotal
        cursor.execute(f"UPDATE dbs1709505.sales SET sales_tax = {tax}, subtotal = {subtotal} WHERE id = {sales_id[0][0]}")
        db.commit()

        # Setup the UI
        self.ui = Ui_settle_window()
        self.ui.setupUi(self)
        self.ui.lbl_total_amt.setText("{:.2f}".format(subtotal + tax))
        self.ui.lbl_paid_amt.setText("{:.2f}".format(self.paid_amt))
        self.ui.lbl_balance_amt.setText("{:.2f}".format((subtotal + tax) - self.paid_amt))

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_finalize.clicked.connect(self.finalize)
        self.ui.btn_cash.clicked.connect(self.cash)

    def exit(self):
        self.close()

    def cash(self):
        self.add_payment = makePayment()
        self.add_payment.show()

    def finalize(self):
        self.close()
        # Close the sale window
        # TODO: Fix this to close the sale window instead of the entire program
        # makeSale.exit(self.makeSale)


class customerLookup(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_customer_lookup_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_new_customer.clicked.connect(self.new_customer)

    def exit(self):
        self.close()

    def search_customer(self):
        self.close()
        self.search_reults = search_customer_results()
        self.search_reults.show()

    def new_customer(self):
        self.close()
        self.new_customer_window = newCustomer()
        self.new_customer_window.show()


class search_customer_results(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_select_account_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_select.clicked.connect(self.select_customer)
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def select_customer(self):
        self.close()
        # TODO: Return customer record to the make sale screen


class newCustomer(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_new_customer_dialog()
        self.ui.setupUi(self)

        # Connect buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

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


class makePayment(qtw.QDialog):
    def __init__(self):
        super().__init__()

        self.amount = 0

        # Setup the UI
        self.ui = Ui_payment_amount_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_ok.clicked.connect(self.exit)
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
        l = len(str(self.amount))
        if l > 0:
            if debugging:
                print(f"Current amount: {self.amount}\nAdjusting amount...")
            self.amount = self.amount[:l - 1]
            if debugging:
                print(f"Amount now: {self.amount}")
            self.ui.lbl_amt.setText(self.amount)

    def button_press(self, pressed):
        if self.amount == 0:
            self.amount = pressed
        else:
            self.amount = str(self.amount) + pressed
        cur_text = self.ui.lbl_amt.text()
        if cur_text == "0.00" or cur_text == "0.0" or cur_text == "0." or cur_text == "0" or cur_text == "":
            self.ui.lbl_amt.setText(pressed)
        else:
            self.ui.lbl_amt.setText(cur_text + pressed)

    def exit(self):
        self.close()


class selectEmployee(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI

        # Each name needs to go on a button
        #
        # cursor.execute("SELECT first_name FROM dbs1709505.employee")
        # for row in cursor:
        #     print(row[0])

        self.ui = Ui_time_clock_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_emp_1.clicked.connect(self.exit)
        self.ui.btn_emp_2.clicked.connect(self.exit)
        self.ui.btn_emp_3.clicked.connect(self.exit)
        self.ui.btn_emp_4.clicked.connect(self.exit)
        self.ui.btn_emp_5.clicked.connect(self.exit)
        self.ui.btn_emp_6.clicked.connect(self.exit)
        self.ui.btn_emp_7.clicked.connect(self.exit)
        self.ui.btn_emp_8.clicked.connect(self.exit)
        self.ui.btn_emp_9.clicked.connect(self.exit)
        self.ui.btn_emp_10.clicked.connect(self.exit)
        self.ui.btn_emp_11.clicked.connect(self.exit)

    def exit(self):
        self.close()
    # TODO: Create method to login/logout emp


class manager(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_manager_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_stock.clicked.connect(self.stock)
        self.ui.btn_edit_groups.clicked.connect(self.groups)
        self.ui.btn_deposit.clicked.connect(self.deposit)
        self.ui.btn_payroll.clicked.connect(self.payroll)
        self.ui.btn_manufacturin.clicked.connect(self.manufacturing)

    def exit(self):
        self.close()

    def stock(self):
        self.close()
        self.stock_window = stock()
        self.stock_window.show()

    def groups(self):
        self.close()
        self.groups_window = groups()
        self.groups_window.show()

    def deposit(self):
        self.close()
        self.window = makePayment()
        self.window.show()

    def payroll(self):
        self.close()
        self.window = payroll()
        self.window.show()

    def manufacturing(self):
        self.close()
        self.window = manufacturing()
        self.window.show()


class stock(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_stock_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_add_edit_vendo.clicked.connect(self.edit_vendor)
        # self.ui.btn_edit_item.clicked.connect(self.edit_item)
        self.ui.btn_add_item.clicked.connect(self.add_item)
        self.ui.btn_edit_item.clicked.connect(self.edit_item)
        self.ui.btn_perform_count.clicked.connect(self.inventory_count)

    def exit(self):
        self.close()

    def edit_vendor(self):
        self.close()
        self.vendor_screen = vendors()
        self.vendor_screen.show()

    def add_item(self):
        self.close()
        self.item_window = addItem()
        self.item_window.show()

    def edit_item(self):
        self.close()
        self.edit_item_window = editItem()
        self.edit_item_window.show()

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

    def exit(self):
        self.close()


class addItem(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_add_item_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class edit_employee(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_edit_employee_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class editItem(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_edit_item_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

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
