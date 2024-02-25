import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QFileDialog

from BAXI import Ui_BAXI
from show_map import MapWindow


class MainWindow():
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()

        self.ui = Ui_BAXI()
        self.ui.setupUi(self.main_win)

        self.mp = MapWindow()
        self.mp.setupUi(self.main_win)

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
        # go to select driver user page---------------------------------------------------
        self.ui.pushButt_accept_sign_up_code.clicked.connect(self.show_select_driver_user)
        # ---------------------------------------------------------------------------------
        # sign up as driver -----------------------------------------------------------------
        self.ui.pushButt_select_driver_select_driver_user.clicked.connect(self.show_get_flname_driver)
        # ---------------------------------------------------------------------------------
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
        # go to get_sex_birth_meli page ------------------------------------------------------
        self.ui.pushButt_next_get_flname_driver.clicked.connect(self.show_get_sex_birth_meli)
        # --------------------------------------------------------------------------------------
        # go back page from get_sex_birth_meli  --------------------------------------------
        self.ui.pushButt_back_get_sex_birth_meli.clicked.connect(self.show_get_flname_driver)
        # --------------------------------------------------------------------------------------
        # go to get_photo_meli_pcertificate_obviously page ------------------------------------------------------
        self.ui.pushButt_next_get_sex_birth_meli.clicked.connect(self.show_get_photo_meli_pcertificate_obviously)
        # --------------------------------------------------------------------------------------
        # go back page from get_photo_meli_certificate_obviously  --------------------------------------------
        self.ui.pushButt_back_get_photo_meli_certificate_obviously.clicked.connect(self.show_get_sex_birth_meli)
        # --------------------------------------------------------------------------------------
        # go to brows and select meli card ------------------------------------------------------
        self.ui.meli_get_photo_meli_certificate_obviously.clicked.connect(self.brows_select_meli_card)
        # --------------------------------------------------------------------------------------
        # go to get_shaba page -----------------------------------------------------------------
        self.ui.pushButt_next_get_photo_meli_certificate_obviously.clicked.connect(self.show_get_shaba)
        # --------------------------------------------------------------------------------------
        # go back page from get_shaba ------------------------------------------------------
        self.ui.pushButt_back_get_shaba.clicked.connect(self.show_get_photo_meli_pcertificate_obviously)
        # --------------------------------------------------------------------------------------
        # go to select_service page ------------------------------------------------------------
        self.ui.pushButt_next_get_shaba.clicked.connect(self.show_select_service)
        # --------------------------------------------------------------------------------------
        # go back page select_service -----------------------------------------------------------
        self.ui.pushButt_back_select_service.clicked.connect(self.show_get_shaba)
        # --------------------------------------------------------------------------------------
        # go to get_machine_baxi_info page ------------------------------------------------------------
        self.ui.pushButt_baxi_select_service.clicked.connect(self.show_get_machine_baxi_info)
        # --------------------------------------------------------------------------------------
        # go back page from get_machine_baxi_info page -------------------------------------------
        self.ui.pushButt_back_get_machine_baxi_info.clicked.connect(self.show_select_service)
        # --------------------------------------------------------------------------------------
        # go to get_machine_baxi_woman_info page ------------------------------------------------------------
        self.ui.pushButt_baxi_woman_select_service.clicked.connect(self.show_get_machine_baxi_woman_info)
        # --------------------------------------------------------------------------------------
        # go back page from get_machine_baxi_woman_info page -------------------------------------------
        self.ui.pushButt_back_get_machine_baxi_woman_info.clicked.connect(self.show_select_service)
        # --------------------------------------------------------------------------------------
        # go to registration_successful page ------------------------------------------------------------
        self.ui.pushButt_next_get_machine_baxi_info.clicked.connect(self.show_registration_successful)
        self.ui.pushButt_next_get_machine_baxi_woman_info.clicked.connect(self.show_registration_successful)
        self.ui.pushButt_next_get_machine_baxi_bar_info.clicked.connect(self.show_registration_successful)
        self.ui.pushButt_next_get_motor_baxi_box_info.clicked.connect(self.show_registration_successful)
        # --------------------------------------------------------------------------------------
        # go back to sign in page from registration_successful page -----------------------------------------
        self.ui.pushButt_back_to_sign_in_registration_successful.clicked.connect(self.show_sign_in)
        # --------------------------------------------------------------------------------------
        # exit app from registration_successful page ---------------------------------------------
        self.ui.pushButt_exiet_registration_successful.clicked.connect(self.exit_app)
        # --------------------------------------------------------------------------------------
        # go back page from get_machine_baxi_bar_info page -------------------------------------------
        self.ui.pushButt_back_get_machine_baxi_bar_info.clicked.connect(self.show_select_service)
        # --------------------------------------------------------------------------------------
        # go to get_machine_baxi_bar_info page ------------------------------------------------------------
        self.ui.pushButt_baxi_bar_select_service.clicked.connect(self.show_get_machine_baxi_bar_info)
        # -------------------------------------------------------------------------------------------------
        # go back page from get_motor_baxi_box_info page -------------------------------------------
        self.ui.pushButt_back_get_motor_baxi_box_info.clicked.connect(self.show_select_service)
        # --------------------------------------------------------------------------------------
        # go to get_motor_baxi_bbox_info page ------------------------------------------------------------
        self.ui.pushButt_baxi_box_select_service.clicked.connect(self.show_get_motor_baxi_box_info)
        # -------------------------------------------------------------------------------------------------
        # go back from get_flname_user page ---------------------------------------------------------------
        self.ui.pushButt_back_get_flname_user.clicked.connect(self.show_select_driver_user)
        # -------------------------------------------------------------------------------------------------

        self.ui.pushButt_select_user_select_driver_user.clicked.connect(self.show_get_flname_user)
        # -------------------------------------------------------------------------------------------------
        # go to show_user_home page ---------------------------------------------------------------------
        self.ui.pushButt_next_get_flname_user.clicked.connect(self.show_user_home)
        self.ui.pushButt_back_baxi_box_baxi_box_user_choose_vehicle_type.clicked.connect(self.show_user_home)
        self.ui.pushButt_back_baxi_user_choose_vehicle_type.clicked.connect(self.show_user_home)
        self.ui.pushButt_back_baxi_bar_baxi_bar_user_choose_vehicle_type.clicked.connect(self.show_user_home)
        # -------------------------------------------------------------------------------------------------
        # go to baxi_user_choose_vehicle_type page --------------------------------------------------------
        self.ui.pushButt_accept_user_home.clicked.connect(self.show_baxi_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_baxi_bar_choose_vehicle_type.clicked.connect(
            self.show_baxi_user_choose_vehicle_type)
        # -------------------------------------------------------------------------------------------------
        # go to baxi_box_user_choose_vehicle_type page
        self.ui.pushButt_go_to_baxi_box_baxi_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_box_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_box_baxi_bar_choose_vehicle_type.clicked.connect(
            self.show_baxi_box_user_choose_vehicle_type)
        # -------------------------------------------------------------------------------------------------
        # go to baxi_bar_choose_vehicle_type page
        self.ui.pushButt_go_to_baxi_bar_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_bar_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_bar_baxi_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_bar_user_choose_vehicle_type)
        # -------------------------------------------------------------------------------------------------

    def show(self):
        self.main_win.show()

    def show_loading(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading)

    def show_sign_up(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up)

    def show_sign_in(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_in)

    def show_accept_code_sign_in(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_in)

    def show_accept_code_sign_up(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_up)

    def show_select_driver_user(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.select_driver_user)

    def show_get_flname_driver(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_flname_driver)

    def show_get_sex_birth_meli(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_sex_birth_meli)

    def show_get_photo_meli_pcertificate_obviously(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_photo_meli_certificate_obviously)

    def brows_select_meli_card(self):
        dialog = QFileDialog(filter="Images *.png ", caption="select a file")
        # print(dialog.getOpenFileName())

    def show_get_shaba(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_shaba)

    def show_select_service(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.select_service)

    def show_get_machine_baxi_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_info)

    def show_get_machine_baxi_woman_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_woman_info)

    def show_registration_successful(self):
        self.baxi_driver_ful_info()
        self.ui.stackedWidget.setCurrentWidget(self.ui.registration_successful)

    def exit_app(self):
        sys.exit()

    def show_get_flname_user(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_flname_user)

    def show_user_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_home)
        self.ui.stackedWidget.setCurrentWidget(self.mp.show())
        # self.ui.stackedWidget.createWindowContainer(self.mp.show)

    def baxi_driver_ful_info(self):
        # -----------------------------------------------------
        # get number and show in terminal:
        print("number: ", self.ui.enter_number_sign_up.toPlainText())
        # -----------------------------------------------------
        # get fname, lname driver and show in terminal:
        print("fname: ", self.ui.fname_get_flname_driver.toPlainText())
        print("lname: ", self.ui.lname_get_flname_driver.toPlainText())
        # -----------------------------------------------------
        # get birthday show in terminal:-----------------------
        print("year: ", self.ui.year_get_sex_birth_meli.text())
        print("month: ", self.ui.month_get_sex_birth_meli.text())
        print("day: ", self.ui.day_get_sex_birth_meli.text())
        # -----------------------------------------------------
        # get sex show in terminal:----------------------------
        print("sex: ", self.ui.sex_get_sex_birth_meli.currentText())
        # -----------------------------------------------------
        # get meli card number show in terminal:---------------
        print("meli number: ", self.ui.meli_get_sex_birth_meli.toPlainText())
        # -----------------------------------------------------
        # get obviously show in terminal:---------------
        print("obvioudly: ", self.ui.obviously_get_photo_meli_pcertificate_obviously.currentText())
        # -----------------------------------------------------
        # get shaba number show in terminal:---------------
        print("shaba number: ", self.ui.enter_shaba_number.toPlainText())
        # -----------------------------------------------------
        # get machine baxi info show in terminal:---------------
        print("machine name: ", self.ui.machine_name_get_machine_baxi_info.toPlainText())
        print("machine generate year: ", self.ui.machine_generate_year_get_machine_baxi_info.toPlainText())
        print("machine color: ", self.ui.machine_color_get_machine_baxi_info.currentText())
        print("machine pelak: ", self.ui.two_digit_left_pelak_get_machine_baxi_info.toPlainText())
        print("machine pelak: ", self.ui.alphabet_get_machine_baxi_info.currentText())
        print("machine pelak: ", self.ui.three_digit_pelak_get_machine_baxi_info.toPlainText())
        print("machine pelak: ", self.ui.two_digit_right_pelak_get_machine_baxi_info.toPlainText())
        print("machine fuel: ", self.ui.machine_fuel_get_machine_baxi_info.currentText())
        print("machine capacity: ", self.ui.machine_capacity_get_machine_baxi_info.currentText())
        # -----------------------------------------------------

    def show_get_machine_baxi_bar_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_bar_info)

    def show_get_motor_baxi_box_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_motor_baxi_box_info)

    def show_baxi_user_choose_vehicle_type(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_user_choose_vehicle_type)

    def show_baxi_box_user_choose_vehicle_type(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_box_user_choose_vehicle_type)

    def show_baxi_bar_user_choose_vehicle_type(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_bar_choose_vehicle_type)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = Ui_BAXI()
    mp = MapWindow()
    main_win.show()
    sys.exit(app.exec())
