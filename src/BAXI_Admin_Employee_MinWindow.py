import datetime
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QFileDialog
from BAXI_Admin_Employee import Ui_BAXI_Admin_Employee
from db.database import *
from verify import *

from set_info import InsertInfo


class MainWindow:
    info_dict = InsertInfo()

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
        self.ui.pushButt_go_to_employee_panel_authentication_request_employee_panel.clicked.connect(
            self.show_employee_panel_authentication_request)
        # ------------------------------------------------------------------------------------------------------------------------------------------
        # go to employee_sign_in from employee_panel -----------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_employee_sign_in.clicked.connect(self.show_employee_panel)
        # ------------------------------------------------------------------------------------------------
        # go to employee_panel from employee_panel_authentication_request ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel)
        # -------------------------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication from employee_panel_authentication_request --------------------------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1.clicked.connect(
            self.show_employee_panel_authentication_successful)
        # ---------------------------------------------------------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication_request from employee_panel_authentication ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_request_employee_panel_authentication.clicked.connect(
            self.show_employee_panel_authentication_request)
        # ----------------------------------------------------------------------------------------------------------------------------------
        # go to employee_panel_authentication_successful from employee_panel_authentication_1 ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_authentication_successful_employee_panel_authentication.clicked.connect(
            self.show_employee_panel_authentication_successful)
        # -------------------------------------------------------------------------------------------------------------------------------------
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

        # -------------------------------------------------------------------------------------------------------------------------------------
        # go to employee_panel from employee_panel_authentication_successful ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_employee_panel_authentication_successful.clicked.connect(
            self.show_employee_panel)
        # ----------------------------------------------------------------------------------------------------------------------
        # go to employee_panel from employee_panel_authentication_rejected ---------------------------------------------------
        self.ui.pushButt_go_to_employee_panel_employee_panel_authentication_rejected.clicked.connect(
            self.show_employee_panel)
        # --------------------------------------------------------------------------------------------------------------------
        # show_first_name -----------------------------------------------------------------
        ###self.ui.pushButt_show_first_name_employee_panel_authentication_1.clicked.connect()###
        # --------------------------------------------------------------------------------
        # show_last_name -----------------------------------------------------------------
        ###self.ui.pushButt_show_last_name_employee_panel_authentication_1.clicked.connect()###
        # --------------------------------------------------------------------------------
        # show_code_meli -----------------------------------------------------------------
        ###self.ui.pushButt_show_code_meli_employee_panel_authentication.clicked.connect()###
        # --------------------------------------------------------------------------------
        # show_birthdate -----------------------------------------------------------------
        ###self.ui.pushButt_show_birthdate_employee_panel_authentication_1.clicked.connect()###
        # --------------------------------------------------------------------------------
        # show_sex -----------------------------------------------------------------
        ###self.ui.pushButt_show_sex_employee_panel_authentication_1.clicked.connect()###
        # --------------------------------------------------------------------------------
        # show_phone_number -----------------------------------------------------------------
        ###self.ui.pushButt_show_phone_number_employee_panel_authentication_1.clicked.connect()###
        # --------------------------------------------------------------------------------
        # show_shaba_number -----------------------------------------------------------------
        ###self.ui.pushButt_show_shaba_number_employee_panel_authentication_1.clicked.connect()###
        # --------------------------------------------------------------------------------
        self.ui.pushButt_text_1_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel_authentication_1)

        self.ui.pushButt_text_2_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel_authentication_2)
        self.ui.pushButt_text_3_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel_authentication_3)
        self.ui.pushButt_text_4_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel_authentication_4)
        self.ui.pushButt_text_5_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel_authentication_5)
        self.ui.pushButt_text_6_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel_authentication_6)
        self.ui.pushButt_text_7_employee_panel_authentication_request.clicked.connect(
            self.show_employee_panel_authentication_7)

    def show(self):
        self.main_win.show()

    def show_loading(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading)

    def show_sign_in_admin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_sign_in)

    def show_employee_sign_in(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_sign_in)

    def show_admin_panel(self):
        if IS_MANAGER(self.ui.get_id_admin_sign_in.toPlainText(), self.ui.get_password_admin_sign_in.toPlainText()):
            self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel)

    def exit_app(self):
        sys.exit()

    def show_admin_panel_recruitment_successful(self):
        self.info_dict.set_first_name_insert_employee_dict(self.ui.get_first_name_admin_panel_recruitment.toPlainText())
        self.info_dict.set_last_name_insert_employee_dict(self.ui.get_last_name_admin_panel_recruitment.toPlainText())
        print('1', self.ui.get_code_meli_admin_panel_recruitment.toPlainText())
        self.info_dict.set_birth_date_insert_employee_dict(
            datetime(int(self.ui.get_birthyear_admin_panel_recruitment.text()),
                     int(self.ui.get_birthmonth_admin_panel_recruitment.text()),
                     int(self.ui.get_birthday_admin_panel_recruitment.text())))
        print("2", self.ui.get_sex_admin_panel_recruitment.currentText())
        self.info_dict.set_personnel_code_insert_employee_dict(
            self.ui.get_code_personnel_admin_panel_recruitment.toPlainText())
        self.info_dict.set_department_insert_employee_dict(self.ui.get_department_admin_panel_recruitment.currentText())
        self.info_dict.set_position_code_insert_employee_dict(self.ui.get_semat_admin_panel_recruitment.currentText())
        self.info_dict.set_proficiency_insert_employee_dict(self.ui.get_skill_admin_panel_recruitment.currentText())
        self.info_dict.set_shaba_number_insert_employee_dict(
            self.ui.get_shaba_number_admin_panel_recruitment.toPlainText())
        self.info_dict.set_signup_time_insert_employee_dict()
        self.info_dict.set_salary_insert_employee_dict(self.ui.get_salary_admin_panel_recruitment.toPlainText())
        self.info_dict.set_password_insert_employee_dict(self.ui.get_code_meli_admin_panel_recruitment.toPlainText())

        try:
            insert_employee(self.info_dict.insert_employee_dict)
            print("employee add successfully to db")
        except Exception as err:
            print(err)

        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel_recruitment_successful)

    def show_admin_panel_query(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel_query)

    def show_admin_panel_recruitment(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.admin_panel_recruitment)

    def show_employee_panel_authentication_request(self):
        res = get_unverified_drivers()
        print(res)
        flag = 1
        for driver in res:
            flname = driver[7] + " " + driver[8]
            print(flname)
            if flag == 1:
                self.ui.pushButt_text_1_employee_panel_authentication_request.setText(flname)
            elif flag == 2:
                self.ui.pushButt_text_2_employee_panel_authentication_request.setText(flname)
            elif flag == 3:
                self.ui.pushButt_text_3_employee_panel_authentication_request.setText(flname)
            elif flag == 4:
                self.ui.pushButt_text_4_employee_panel_authentication_request.setText(flname)
            elif flag == 5:
                self.ui.pushButt_text_5_employee_panel_authentication_request.setText(flname)
            elif flag == 6:
                self.ui.pushButt_text_6_employee_panel_authentication_request.setText(flname)
            elif flag == 7:
                self.ui.pushButt_text_7_employee_panel_authentication_request.setText(flname)
            flag += 1

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication_request)

    def show_employee_panel(self):
        if flname := IS_EMPLOYEE(self.ui.get_id_employee_sign_in.toPlainText(),
                                 self.ui.get_password_employee_sign_in.toPlainText()):
            self.ui.box_fname_employee_panel.setPlainText(flname[0][0])
            self.ui.box_lname_employee_panel.setPlainText(flname[0][1])
            self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel)

    def show_employee_panel_authentication_1(self):
        res = get_unverified_drivers()
        print('driver', res[0])
        driver = res[0]
        self.ui.pushButt_show_first_name_employee_panel_authentication.setText(driver[7])
        self.ui.pushButt_show_last_name_employee_panel_authentication.setText(driver[8])
        self.ui.pushButt_show_code_meli_employee_panel_authentication.setText(driver[3])
        self.ui.pushButt_show_birthdate_employee_panel_authentication.setText(str(driver[9]))
        self.ui.pushButt_show_sex_employee_panel_authentication.setText(driver[13])
        self.ui.pushButt_show_phone_number_employee_panel_authentication.setText(driver[1])
        self.ui.pushButt_show_shaba_number_employee_panel_authentication.setText(driver[2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)

    def show_employee_panel_authentication_2(self):
        res = get_unverified_drivers()
        print('driver', res[1])
        driver = res[1]
        self.ui.pushButt_show_first_name_employee_panel_authentication.setText(driver[7])
        self.ui.pushButt_show_last_name_employee_panel_authentication.setText(driver[8])
        self.ui.pushButt_show_code_meli_employee_panel_authentication.setText(driver[3])
        self.ui.pushButt_show_birthdate_employee_panel_authentication.setText(str(driver[9]))
        self.ui.pushButt_show_sex_employee_panel_authentication.setText(driver[13])
        self.ui.pushButt_show_phone_number_employee_panel_authentication.setText(driver[1])
        self.ui.pushButt_show_shaba_number_employee_panel_authentication.setText(driver[2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)


    def show_employee_panel_authentication_3(self):
        res = get_unverified_drivers()
        print('driver', res[2])
        driver = res[2]
        self.ui.pushButt_show_first_name_employee_panel_authentication.setText(driver[7])
        self.ui.pushButt_show_last_name_employee_panel_authentication.setText(driver[8])
        self.ui.pushButt_show_code_meli_employee_panel_authentication.setText(driver[3])
        self.ui.pushButt_show_birthdate_employee_panel_authentication.setText(str(driver[9]))
        self.ui.pushButt_show_sex_employee_panel_authentication.setText(driver[13])
        self.ui.pushButt_show_phone_number_employee_panel_authentication.setText(driver[1])
        self.ui.pushButt_show_shaba_number_employee_panel_authentication.setText(driver[2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)

    def show_employee_panel_authentication_4(self):
        res = get_unverified_drivers()
        print('driver', res[3])
        driver = res[3]
        self.ui.pushButt_show_first_name_employee_panel_authentication.setText(driver[7])
        self.ui.pushButt_show_last_name_employee_panel_authentication.setText(driver[8])
        self.ui.pushButt_show_code_meli_employee_panel_authentication.setText(driver[3])
        self.ui.pushButt_show_birthdate_employee_panel_authentication.setText(str(driver[9]))
        self.ui.pushButt_show_sex_employee_panel_authentication.setText(driver[13])
        self.ui.pushButt_show_phone_number_employee_panel_authentication.setText(driver[1])
        self.ui.pushButt_show_shaba_number_employee_panel_authentication.setText(driver[2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)

    def show_employee_panel_authentication_5(self):
        res = get_unverified_drivers()
        print('driver', res[4])
        driver = res[4]
        self.ui.pushButt_show_first_name_employee_panel_authentication.setText(driver[7])
        self.ui.pushButt_show_last_name_employee_panel_authentication.setText(driver[8])
        self.ui.pushButt_show_code_meli_employee_panel_authentication.setText(driver[3])
        self.ui.pushButt_show_birthdate_employee_panel_authentication.setText(str(driver[9]))
        self.ui.pushButt_show_sex_employee_panel_authentication.setText(driver[13])
        self.ui.pushButt_show_phone_number_employee_panel_authentication.setText(driver[1])
        self.ui.pushButt_show_shaba_number_employee_panel_authentication.setText(driver[2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)

    def show_employee_panel_authentication_6(self):
        res = get_unverified_drivers()
        print('driver', res[5])
        driver = res[5]
        self.ui.pushButt_show_first_name_employee_panel_authentication.setText(driver[7])
        self.ui.pushButt_show_last_name_employee_panel_authentication.setText(driver[8])
        self.ui.pushButt_show_code_meli_employee_panel_authentication.setText(driver[3])
        self.ui.pushButt_show_birthdate_employee_panel_authentication.setText(str(driver[9]))
        self.ui.pushButt_show_sex_employee_panel_authentication.setText(driver[13])
        self.ui.pushButt_show_phone_number_employee_panel_authentication.setText(driver[1])
        self.ui.pushButt_show_shaba_number_employee_panel_authentication.setText(driver[2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)

    def show_employee_panel_authentication_7(self):
        res = get_unverified_drivers()
        print('driver', res[6])
        driver = res[6]
        self.ui.pushButt_show_first_name_employee_panel_authentication.setText(driver[7])
        self.ui.pushButt_show_last_name_employee_panel_authentication.setText(driver[8])
        self.ui.pushButt_show_code_meli_employee_panel_authentication.setText(driver[3])
        self.ui.pushButt_show_birthdate_employee_panel_authentication.setText(str(driver[9]))
        self.ui.pushButt_show_sex_employee_panel_authentication.setText(driver[13])
        self.ui.pushButt_show_phone_number_employee_panel_authentication.setText(driver[1])
        self.ui.pushButt_show_shaba_number_employee_panel_authentication.setText(driver[2])

        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication)

    def show_employee_panel_authentication_successful(self):
        res = IS_DRIVER(self.ui.pushButt_show_phone_number_employee_panel_authentication.text())
        try:
            print("1")
            set_license_verification_date(res[0][0], datetime.now())
            print("1")
            set_judicial_letter_verification_date(res[0][0], datetime.now())
            print("1")
            set_final_verification_date(res[0][0], datetime.now())
            print("1")
            set_verifier_personnel_code(res[0][0], self.ui.get_id_employee_sign_in.toPlainText())
            print("driver authentication successfully add to db ")
        except Exception as err:
            print(err)
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication_successful)

    def show_employee_panel_authentication_rejected(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employee_panel_authentication_rejected)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = Ui_BAXI_Admin_Employee()
    main_win.show()
    sys.exit(app.exec())
