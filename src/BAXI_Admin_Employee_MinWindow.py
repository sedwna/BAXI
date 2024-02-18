import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QFileDialog
from BAXI_Admin_Employee import Ui_BAXI_Admin_Employee


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_BAXI_Admin_Employee()
        self.ui.setupUi(self.main_win)
        # loading page -------------------------------------------------------------------
        self.show_loading()
        # --------------------------------------------------------------------------------
        # go to sign in page--------------------------------------------------------------
        self.ui.pushButt_loading.clicked.connect(self.show_sign_in_admin)
        # --------------------------------------------------------------------------------
        # switch between login and signin page--------------------------------------------
        self.ui.pushButt_admin.clicked.connect(self.show_sign_in_admin)
        self.ui.pushButt_employee.clicked.connect(self.show_sign_in_employee)
        # --------------------------------------------------------------------------------
        # go to sign in page from admin_panel page -----------------------------------------
        self.ui.pushButt_go_to_sign_in_admin_panel.clicked.connect(self.show_sign_in_admin)
        # --------------------------------------------------------------------------------
        # go to show_admin_panel page -----------------------------------------
        self.ui.pushBut_admin_sign_in.clicked.connect(self.show_admin_panel)
        # --------------------------------------------------------------------------------
        # exit from show_admin_panel page -----------------------------------------
        self.ui.pushButt_exit_admin_panel.clicked.connect(self.exit_app)
        # --------------------------------------------------------------------------------

    def show(self):
        self.main_win.show()

    def show_loading(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading)

    def show_sign_in_admin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_sign_in)

    def show_sign_in_employee(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_sign_in)

    def show_admin_panel(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel)

    def exit_app(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = Ui_BAXI_Admin_Employee()
    main_win.show()
    sys.exit(app.exec())
