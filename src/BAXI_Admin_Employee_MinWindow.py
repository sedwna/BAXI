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
        self.ui.pushButt_employee.clicked.connect(self.show_employee_sign_in)
        # --------------------------------------------------------------------------------
        # go to sign in page from admin_panel page ----------------------------------------
        self.ui.pushButt_go_to_sign_in_admin_panel.clicked.connect(self.show_sign_in_admin)
        # ---------------------------------------------------------------------------------
        # go to admin_panel_recruitment page from admin_panel page ----------------------------------------
        self.ui.pushButt_add_new_employee_admin_panel.clicked.connect(self.show_admin_panel_recruitment)
        # ---------------------------------------------------------------------------------
        # go to show_admin_panel page --------------------------------------
        self.ui.pushBut_admin_sign_in.clicked.connect(self.show_admin_panel)
        # ------------------------------------------------------------------
        # go to admin_panel_query page --------------------------------------
        self.ui.pushButt_query_admin_panel.clicked.connect(self.show_admin_panel_query)
        # ------------------------------------------------------------------
        # exit from show_admin_panel page ------------------------------
        self.ui.pushButt_exit_admin_panel.clicked.connect(self.exit_app)
        # --------------------------------------------------------------
        # go to admin_panel_recruitment_successful page ----------------------------------------------------------------
        self.ui.pushButt_estekhdam_admin_panel_recruitment.clicked.connect(self.show_admin_panel_recruitment_successful)
        # --------------------------------------------------------------------------------------------------------------
        # go to admin_panel page -----------------------------------------------------------
        self.ui.pushButt_back_admin_panel_recruitment.clicked.connect(self.show_admin_panel)
        # ----------------------------------------------------------------------------------
        # upload degree of education ----------------------------------------------
        ###self.ui.pushButt_upload_education_admin_panel_recruitment.clicked.connect()###
        # -------------------------------------------------------------------------
        # upload Profile photo -------------------------------------------------------
        ###self.ui.pushButt_upload_profilePhoto_admin_panel_recruitment.clicked.connect()###
        # ----------------------------------------------------------------------------
        # go to admin_panel page ------------------------------------------------------------------
        self.ui.pushButt_go_to_admin_panel_admin_panel_query.clicked.connect(self.show_admin_panel)
        # -----------------------------------------------------------------------------------------
        # queris ----------------------------------------------------
        ###self.ui.pushButt_query_1_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_2_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_3_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_4_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_5_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_6_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_7_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_8_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_9_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_10_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_11_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_12_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_13_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_14_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_15_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_16_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_17_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_18_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_19_admin_panel_query.clicked.connect()###
        ###self.ui.pushButt_query_20_admin_panel_query.clicked.connect()###
        # -----------------------------------------------------------
        # go to admin_panel page -----------------------------------------------------------------------------------
        self.ui.pushButt_go_to_admin_panel_admin_panel_recruitment_successful.clicked.connect(self.show_admin_panel)
        # ----------------------------------------------------------------------------------------------------------
        # exit from employee panel page -----------------------------------------
        self.ui.pushButt_go_to_exit_employee_panel.clicked.connect(self.exit_app)
        # -----------------------------------------------------------------------
        # go to employee_sign_in from employee_panel -----------------------------------------------------
        self.ui.pushButt_go_to_employee_sign_in_employee_panel.clicked.connect(self.show_employee_sign_in)
        # ------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication_request from employee_panel --------------------------------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_request_employee_panel.clicked.connect(self.show_employee_panel_authentication_request)
        # ------------------------------------------------------------------------------------------------------------------------------------------
        # go to employee_sign_in from employee_panel -----------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_employee_sign_in.clicked.connect(self.show_employee_panel)
        # ------------------------------------------------------------------------------------------------
        # go to employee_panel from employee_panel_authentication_request ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_employee_panel_authentication_request.clicked.connect(self.show_employee_panel)
        # -------------------------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication from employee_panel_authentication_request --------------------------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1.clicked.connect(self.show_employee_panel_authentication_1)
        self.ui.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_2.clicked.connect(self.show_employee_panel_authentication_1)
        self.ui.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_3.clicked.connect(self.show_employee_panel_authentication_1)
        # ---------------------------------------------------------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication_request from employee_panel_authentication ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_request_employee_panel_authentication.clicked.connect(self.show_employee_panel_authentication_request)
        # ----------------------------------------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication_successful from employee_panel_authentication ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_successful_employee_panel_authentication.clicked.connect(self.show_employee_panel_authentication_successful)
        # -------------------------------------------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication_successful from employee_panel_authentication ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_employee_panel_authentication.clicked.connect(self.show_employee_panel_authentication_2)
        # -------------------------------------------------------------------------------------------------------------------------------------
            # show_licence -----------------------------------------------------------------
        ###self.ui.pushButt_show_licence_employee_panel_authentication.clicked.connect()###
        # ------------------------------------------------------------------------------
        # show_cart_meli -----------------------------------------------------------------
        ###self.ui.pushButt_show_cart_meli_employee_panel_authentication.clicked.connect()###
        # ------------------------------------------------------------------------------
        # show_sopishine -----------------------------------------------------------------
        ###self.ui.pushButt_show_sopishine_employee_panel_authentication.clicked.connect()###
        # ------------------------------------------------------------------------------





    def show(self):
        self.main_win.show()

    def show_loading(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading)

    def show_sign_in_admin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_sign_in)

    def show_employee_sign_in(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_sign_in)

    def show_admin_panel(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel)

    def exit_app(self):
        sys.exit()

    def show_admin_panel_recruitment_successful(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel_recruitment_successful)

    def show_admin_panel_query(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel_query)

    def show_admin_panel_recruitment(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel_recruitment)
    def show_employee_panel_authentication_request(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication_request)

    def show_employee_panel(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel)
    def show_employee_panel_authentication_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)

    def show_employee_panel_authentication_request(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication_request)

    def show_employee_panel_authentication_successful(self):
        #dest page not ready yet
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication_request)#(self.ui.employee_panel_authentication_successful)
    def show_employee_panel_authentication_2(self):
        #dest page not ready yet
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication_request)#(self.ui.employee_panel_authentication)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = Ui_BAXI_Admin_Employee()
    main_win.show()
    sys.exit(app.exec())
