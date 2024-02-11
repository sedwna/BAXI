import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow

from BAXI import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # waiting page -------------------------------------------------------------------
        self.show_loading()
        # --------------------------------------------------------------------------------
        # go to sign in page--------------------------------------------------------------
        self.ui.pushButt_logo.clicked.connect(self.show_sign_up)
        # --------------------------------------------------------------------------------
        # switch between login and signin page--------------------------------------------
        self.ui.pushButt_sign_in.clicked.connect(self.show_sign_in)
        self.ui.pushButt_sign_up.clicked.connect(self.show_sign_up)
        # --------------------------------------------------------------------------------
        # go to code certified page ------------------------------------------------------
        self.ui.pushButt_enter_sign_up.clicked.connect(self.show_accept_code_sign_up)
        self.ui.pushButt_enter_sign_in.clicked.connect(self.show_accept_code_sign_in)
        # --------------------------------------------------------------------------------
        # self.ui.pushButt_accept_login_code.clicked.connect()
        # go to select driver user page---------------------------------------------------
        self.ui.pushButt_accept_sign_up_code.clicked.connect(self.show_select_driver_user)
        # ---------------------------------------------------------------------------------
        # log in as user-------------------------------------------------------------------
        # self.ui.pushButt_select_user.clicked.connect()
        # ----------------------------------------------------------------------------------
        # log in as driver -----------------------------------------------------------------
        self.ui.pushButt_select_driver.clicked.connect(self.show_get_flname_driver)
        # ---------------------------------------------------------------------------------
        # go to    ----------------------------------------------------
        # self.ui.pushButt_next_get_flname_driver.clicked.connect()
        # --------------------------------------------------------------------------------
        # go back page from fl name driver page -----------------------------------------------
        self.ui.pushButt_back_get_flname_driver.clicked.connect(self.show_select_driver_user)
        # --------------------------------------------------------------------------------------
        # go back page from select_driver_user page --------------------------------------------
        self.ui.pushButt_back_select_driver_user.clicked.connect(self.show_accept_code_sign_up)
        # --------------------------------------------------------------------------------------
        # go back page from accept code to edit number --------------------------------------------
        self.ui.pushButt_edit_number_sign_up.clicked.connect(self.show_sign_up)
        self.ui.pushButt_edit_number_sign_in.clicked.connect(self.show_sign_in)
        # --------------------------------------------------------------------------------------
    def show(self):
        self.main_win.show()

    def show_loading(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading)

    def show_sign_up(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up)

    def show_sign_in(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_in)

    def show_accept_code_sign_in(self):
        # get number and show in terminal:
        print(self.ui.enter_number_sign_in.toPlainText())
        # -----------------------------------------------------
        self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_in)

    def show_accept_code_sign_up(self):
        # get number and show in terminal:
        print(self.ui.enter_number_sign_up.toPlainText())
        # -----------------------------------------------------
        self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_up)

    def show_select_driver_user(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.select_driver_user)

    def show_get_flname_driver(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_flname_driver)
        # get fname, lname driver and show in terminal:
        print(self.ui.fname.toPlainText())
        print(self.ui.lname.toPlainText())
        # -----------------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = Ui_MainWindow()
    main_win.show()
    sys.exit(app.exec())
