import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QFileDialog

from BAXI import Ui_BAXI
from show_map import MapWindow
from db.database import *
import datetime

from set_info import InsertInfo
from generate_random_number import GenerateRandom4Digit


class MainWindow():
    driver_info = InsertInfo()
    gen_rand_number = GenerateRandom4Digit()

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
        self.ui.pushButt_back_baxi_woman_baxi_woman_user_choose_vehicle_type.clicked.connect(self.show_user_home)
        # -------------------------------------------------------------------------------------------------
        # go to baxi_user_choose_vehicle_type page --------------------------------------------------------
        self.ui.pushButt_accept_user_home.clicked.connect(self.show_baxi_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_baxi_bar_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_baxi_woman_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_user_choose_vehicle_type)
        # -------------------------------------------------------------------------------------------------
        # go to baxi_box_user_choose_vehicle_type page
        self.ui.pushButt_go_to_baxi_box_baxi_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_box_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_box_baxi_bar_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_box_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_box_baxi_woman_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_box_user_choose_vehicle_type)
        # -------------------------------------------------------------------------------------------------
        # go to baxi_bar_choose_vehicle_type page
        self.ui.pushButt_go_to_baxi_bar_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_bar_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_bar_baxi_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_bar_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_bar_baxi_woman_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_bar_user_choose_vehicle_type)
        # -------------------------------------------------------------------------------------------------
        # go to show_baxi_woman_user_choose_vehicle_type page
        self.ui.pushButt_go_to_baxi_woman_baxi_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_woman_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_woman_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_woman_user_choose_vehicle_type)
        self.ui.pushButt_go_to_baxi_woman_baxi_bar_user_choose_vehicle_type.clicked.connect(
            self.show_baxi_woman_user_choose_vehicle_type)
        # -------------------------------------------------------------------------------------------------
        # set popup success hide-------------------------------------------------------------------------
        self.ui.pushButt_request_baxi_user_choose_vehicle_type.clicked.connect(
            self.popup_success_baxi_user_choose_vehicle_type_setHidden)

        self.ui.pushButt_request_baxi_woman_baxi_woman_user_choose_vehicle_type.clicked.connect(
            self.popup_success_baxi_woman_user_choose_vehicle_type_setHidden)

        self.ui.pushButt_request_baxi_box_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.popup_success_baxi_box_user_choose_vehicle_type_setHidden)

        self.ui.pushButt_request_baxi_bar_baxi_bar_user_choose_vehicle_type.clicked.connect(
            self.popup_success_baxi_bar_user_choose_vehicle_type_setHidden)
        # -------------------------------------------------------------------------------------------------
        # set menu bar in user home -----------------------------------------------------------------------
        self.ui.pushButt_profile_user_home.clicked.connect(self.show_menu_bar_user_home)
        self.ui.pushButt_menu_off_user_home.clicked.connect(self.off_menu_bar_user_home)
        self.ui.pushButt_logout_user_home.clicked.connect(self.show_sign_in)
        # self.ui.pushButt_history_user_home.clicked.connect()
        # go to setting in user home page --------------------------------------------------------------------
        self.ui.pushButt_settings_user_home.clicked.connect(self.show_user_setting)
        # ----------------------------------------------------------------------------------------------------
        # go to user_my_account------------------------------------------------------------------------------
        self.ui.pushButt_go_to_my_account.clicked.connect(self.show_user_my_account)
        # ----------------------------------------------------------------------------------------------------
        # go back from user_my_account page-------------------------------------------------------------------
        self.ui.pushButt_back_user_my_account.clicked.connect(self.show_user_setting)
        # ----------------------------------------------------------------------------------------------------
        # go back from user_setting page-----------------------------------------------------------------------
        self.ui.pushButt_back_user_setting.clicked.connect(self.show_user_home)
        # ----------------------------------------------------------------------------------------------------
        # go to user_my_wallet--------------------------------------------------------------------------------
        self.ui.pushButt_my_wallet_user_home.clicked.connect(self.show_user_my_wallet)
        # ----------------------------------------------------------------------------------------------------
        # go back from user_my_wallet page--------------------------------------------------------------------
        self.ui.pushButt_back_user_my_wallet.clicked.connect(self.show_user_home)
        # ----------------------------------------------------------------------------------------------------
        # go to user_payment_method----------------------------------------------------------------------------
        self.ui.pushButt_go_to_payment_methods_user_my_wallet.clicked.connect(self.show_user_payment_method)
        # ----------------------------------------------------------------------------------------------------
        # go back from user_payment_method page---------------------------------------------------------------
        self.ui.pushButt_back_user_payment_method.clicked.connect(self.show_user_my_wallet)
        # ----------------------------------------------------------------------------------------------------
        # go to user_history page-----------------------------------------------------------------------------
        self.ui.pushButt_history_user_home.clicked.connect(self.show_pushButt_history_user_home)
        # go back user_history page--------------------------------------------------------------------------------
        self.ui.pushButt_back_user_history.clicked.connect(self.show_user_home)
        # ----------------------------------------------------------------------------------------------------
        # go to user_driver_request_accepts_info page--------------------------------------------------------
        self.ui.pushButt_done_baxi_user_choose_vehicle_type.clicked.connect(self.show_user_driver_request_accepts_info)
        self.ui.pushButt_done_baxi_woman_user_choose_vehicle_type.clicked.connect(
            self.show_user_driver_request_accepts_info)
        self.ui.pushButt_done_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_user_driver_request_accepts_info)
        self.ui.pushButt_done_baxi_bar_user_choose_vehicle_type.clicked.connect(
            self.show_user_driver_request_accepts_info)
        # ------------------------------------------------------------------------------------------------------
        # go back from user_driver_request_accepts_info page------------------------------------------------------
        self.ui.pushButt_cancel_request_user_driver_request_accepts_info.clicked.connect(self.show_user_home)
        # -----------------------------------------------------------------------------------------------------------
        # select_go_to_user_or_driver_home---------------------------------------------------------------------------
        self.ui.pushButt_accept_sign_in_code.clicked.connect(self.select_go_to_user_or_driver_home)
        # -----------------------------------------------------------------------------------------------------------
        # go to driver_accept_request page ---------------------------------------------------------------------------
        self.ui.pushButt_accept_request_driver_home.clicked.connect(self.show_driver_accept_request)
        # -----------------------------------------------------------------------------------------------------------
        # go to driver_passenger_boarded page -----------------------------------------------------------------------
        self.ui.pushButt_reached_the_origin_driver_accept_request.clicked.connect(self.show_driver_passenger_boarded)
        # -----------------------------------------------------------------------------------------------------------
        # go to driver_reached_the_destination page-----------------------------------------------------------------
        self.ui.pushButt_passanger_boarded_driver_passenger_boarded.clicked.connect(
            self.show_driver_reached_the_destination)
        # -----------------------------------------------------------------------------------------------------------
        # go back from driver_reached_the_destination page-----------------------------------------------------------
        self.ui.pushButt_reached_destination_driver_reached_the_destination.clicked.connect(self.show_driver_home)
        # -----------------------------------------------------------------------------------------------------------
        self.ui.meli_get_photo_meli_certificate_obviously.clicked.connect(self.brows_select_meli_card)

    def show(self):
        self.main_win.show()

    def show_loading(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading)

    def show_sign_up(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up)

    def show_sign_in(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_in)

    def show_accept_code_sign_in(self):
        # try:
        #     if not phone_number_exists(self.ui.enter_number_sign_up.toPlainText()):
        #         self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_in)
        #     else:
        #         print("this phone number already exist")
        # except Exception as err:
        #     print(err)
        self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_in)

    def show_accept_code_sign_up(self):
        print(self.ui.enter_number_sign_up.toPlainText())
        try:
            if phone_number_exists(self.ui.enter_number_sign_up.toPlainText()):
                self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_up)
            else:
                print("this phone number already exist")
        except Exception as err:
            print(err)
        # self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_up)

        self.driver_info.set_phone_number_insert_driver_dict(self.ui.enter_number_sign_up.toPlainText())
        self.gen_rand_number.gen_password_code_rand()


    def show_select_driver_user(self):
        input_password = self.ui.pass_digit1_accept_code_sign_up.toPlainText() + self.ui.pass_digit2_accept_code_sign_up.toPlainText() + self.ui.pass_digit3_accept_code_sign_up.toPlainText() + self.ui.pass_digit4_accept_code_sign_up.toPlainText()
        try:
            if int(input_password) == int(self.password.rand_number):
                self.ui.stackedWidget.setCurrentWidget(self.ui.select_driver_user)
            else:
                print("incorrect password")

        except:
            print("err1")
        self.ui.stackedWidget.setCurrentWidget(self.ui.select_driver_user)

    def show_get_flname_driver(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_flname_driver)

    def show_get_sex_birth_meli(self):
        self.driver_info.set_first_name_insert_driver_dict(self.ui.fname_get_flname_driver.toPlainText())
        self.driver_info.set_last_name_insert_driver_dict(self.ui.lname_get_flname_driver.toPlainText())
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_sex_birth_meli)

    def show_get_photo_meli_pcertificate_obviously(self):

        self.driver_info.set_sex_insert_driver_dict(self.ui.sex_get_sex_birth_meli.currentText())
        self.driver_info.set_birth_date_insert_driver_dict(datetime.datetime(int(self.ui.year_get_sex_birth_meli.text()),
                                                          int(self.ui.month_get_sex_birth_meli.text()),
                                                          int(self.ui.day_get_sex_birth_meli.text())))
        self.driver_info.set_national_code_insert_driver_dict(self.ui.meli_get_sex_birth_meli.toPlainText())

        self.ui.stackedWidget.setCurrentWidget(self.ui.get_photo_meli_certificate_obviously)

    def brows_select_meli_card(self):
        dialog = QFileDialog(filter="Images *.png ", caption="select a file")
        print(dialog.getOpenFileName())

    def show_get_shaba(self):
        self.driver_info.set_national_card_photo_path_insert_driver_dict("../c:desktop/national id card")
        self.driver_info.set_license_photo_path_insert_driver_dict("../c:desktop/license card")
        self.driver_info.set_disability_insert_driver_dict(self.ui.obviously_get_photo_meli_pcertificate_obviously.currentText())

        self.ui.stackedWidget.setCurrentWidget(self.ui.get_shaba)

    def show_select_service(self):
        self.driver_info.set_shaba_number_insert_driver_dict(self.ui.enter_shaba_number.toPlainText())
        self.send_driver_info_to_db()

        self.ui.stackedWidget.setCurrentWidget(self.ui.select_service)

    def show_get_machine_baxi_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_info)

    def show_get_machine_baxi_woman_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_woman_info)

    def show_registration_successful(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.registration_successful)

    def exit_app(self):
        sys.exit()

    def show_get_flname_user(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_flname_user)

    def show_user_home(self):
        self.off_menu_bar_user_home()
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_home)
        self.ui.stackedWidget.setCurrentWidget(self.mp.show())

    def popup_success_baxi_user_choose_vehicle_type_setHidden(self):
        self.ui.popup_success_baxi_user_choose_vehicle_type.setHidden(False)
        self.ui.pushButt_done_baxi_user_choose_vehicle_type.setHidden(False)

    def popup_success_baxi_woman_user_choose_vehicle_type_setHidden(self):
        self.ui.popup_success_baxi_woman_user_choose_vehicle_type.setHidden(False)
        self.ui.pushButt_done_baxi_woman_user_choose_vehicle_type.setHidden(False)

    def popup_success_baxi_bar_user_choose_vehicle_type_setHidden(self):
        self.ui.popup_success_baxi_bar_user_choose_vehicle_type.setHidden(False)
        self.ui.pushButt_done_baxi_bar_user_choose_vehicle_type.setHidden(False)

    def popup_success_baxi_box_user_choose_vehicle_type_setHidden(self):
        self.ui.popup_success_baxi_box_user_choose_vehicle_type.setHidden(False)
        self.ui.pushButt_done_baxi_box_user_choose_vehicle_type.setHidden(False)

    def send_driver_info_to_db(self):
        self.gen_rand_number.gen_referral_code_rand()
        self.driver_info.set_referral_code_insert_driver_dict(self.gen_rand_number.referral_code)
        self.driver_info.set_signup_time_insert_driver_dict()
        print(self.driver_info.insert_driver_dict)
        try:
            insert_driver(self.driver_info.insert_driver_dict)
        except Exception as err:
            print(err)
        finally:
            print("finish")

    def show_get_machine_baxi_bar_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_bar_info)

    def show_get_motor_baxi_box_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_motor_baxi_box_info)

    def show_baxi_user_choose_vehicle_type(self):
        self.ui.popup_success_baxi_user_choose_vehicle_type.setHidden(True)
        self.ui.pushButt_done_baxi_user_choose_vehicle_type.setHidden(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_user_choose_vehicle_type)

    def show_baxi_box_user_choose_vehicle_type(self):
        self.ui.popup_success_baxi_box_user_choose_vehicle_type.setHidden(True)
        self.ui.pushButt_done_baxi_box_user_choose_vehicle_type.setHidden(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_box_user_choose_vehicle_type)

    def show_baxi_bar_user_choose_vehicle_type(self):
        self.ui.popup_success_baxi_bar_user_choose_vehicle_type.setHidden(True)
        self.ui.pushButt_done_baxi_bar_user_choose_vehicle_type.setHidden(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_bar_user_choose_vehicle_type)

    def show_baxi_woman_user_choose_vehicle_type(self):
        self.ui.popup_success_baxi_woman_user_choose_vehicle_type.setHidden(True)
        self.ui.pushButt_done_baxi_woman_user_choose_vehicle_type.setHidden(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_woman_user_choose_vehicle_type)

    def show_menu_bar_user_home(self):
        self.ui.pushButt_my_wallet_user_home.setHidden(False)
        self.ui.pushButt_history_user_home.setHidden(False)
        self.ui.pushButt_settings_user_home.setHidden(False)
        self.ui.pushButt_logout_user_home.setHidden(False)
        self.ui.pushButt_menu_off_user_home.setHidden(False)
        self.ui.menu_bar_user_home.setHidden(False)

    def off_menu_bar_user_home(self):
        self.ui.pushButt_my_wallet_user_home.setHidden(True)
        self.ui.pushButt_history_user_home.setHidden(True)
        self.ui.pushButt_settings_user_home.setHidden(True)
        self.ui.pushButt_logout_user_home.setHidden(True)
        self.ui.pushButt_menu_off_user_home.setHidden(True)
        self.ui.menu_bar_user_home.setHidden(True)

    def show_user_setting(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_setting)

    def show_user_my_account(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_my_account)

    def show_user_my_wallet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_my_wallet)

    def show_user_payment_method(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_payment_method)

    def show_pushButt_history_user_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_history)

    def show_user_driver_request_accepts_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_driver_request_accepts_info)

    def select_go_to_user_or_driver_home(self):
        if True:
            self.ui.stackedWidget.setCurrentWidget(self.ui.driver_home)
        if False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.user_home)

    def show_driver_accept_request(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_accept_request)

    def show_driver_passenger_boarded(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_passenger_boarded)

    def show_driver_reached_the_destination(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_reached_the_destination)

    def show_driver_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_home)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = Ui_BAXI()
    mp = MapWindow()
    main_win.show()
    sys.exit(app.exec())
