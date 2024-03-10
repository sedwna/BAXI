import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QFileDialog

from BAXI import Ui_BAXI
from show_map import MapWindow
import datetime
from db.database import *

from set_info import InsertInfo
from generate_random_number import GenerateRandom
from verify import *
from get_lat_lon_info import get_lat_lon_info, trip_cost_baxi, trip_cost_heavy, trip_cost_light
from client import Client
from driver import Driver


class MainWindow:
    info_dict = InsertInfo()
    gen_rand_number = GenerateRandom()
    client_1 = Client()
    driver_1 = Driver()

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
        self.ui.pushButt_back_select_driver_user.clicked.connect(self.show_sign_up)
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
        self.ui.pushButt_next_get_machine_baxi_info.clicked.connect(self.show_registration_successful_baxi)
        self.ui.pushButt_next_get_machine_baxi_woman_info.clicked.connect(
            self.show_registration_successful_baxi_woman)
        self.ui.pushButt_next_get_machine_baxi_bar_info.clicked.connect(self.show_registration_successful_baxi_bar)
        self.ui.pushButt_next_get_motor_baxi_box_info.clicked.connect(self.show_registration_successful_baxi_box)
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
        # go back from get_flname_sex_birth_user page ---------------------------------------------------------------
        self.ui.pushButt_back_get_flname_sex_birth_user.clicked.connect(self.show_select_driver_user)
        # -------------------------------------------------------------------------------------------------

        self.ui.pushButt_select_user_select_driver_user.clicked.connect(self.show_get_flname_sex_birth_user)
        # -------------------------------------------------------------------------------------------------
        # go to show_user_home page ---------------------------------------------------------------------
        self.ui.pushButt_next_get_flname_sex_birth_user.clicked.connect(self.show_user_home_after_sign_up)
        self.ui.pushButt_back_baxi_box_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_user_home_after_sign_in)
        self.ui.pushButt_back_baxi_user_choose_vehicle_type.clicked.connect(self.show_user_home_after_sign_in)
        self.ui.pushButt_back_baxi_bar_baxi_bar_user_choose_vehicle_type.clicked.connect(
            self.show_user_home_after_sign_in)
        self.ui.pushButt_back_baxi_woman_baxi_woman_user_choose_vehicle_type.clicked.connect(
            self.show_user_home_after_sign_in)
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
            self.show_booking_successful_baxi)

        self.ui.pushButt_request_baxi_woman_baxi_woman_user_choose_vehicle_type.clicked.connect(
            self.show_booking_successful_baxi_woman)

        self.ui.pushButt_request_baxi_box_baxi_box_user_choose_vehicle_type.clicked.connect(
            self.show_booking_successful_baxi_box)

        self.ui.pushButt_request_baxi_bar_baxi_bar_user_choose_vehicle_type.clicked.connect(
            self.show_booking_successful_baxi_bar)
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
        self.ui.pushButt_back_user_setting.clicked.connect(self.show_user_home_after_sign_in)
        # ----------------------------------------------------------------------------------------------------
        # go to user_my_wallet--------------------------------------------------------------------------------
        self.ui.pushButt_my_wallet_user_home.clicked.connect(self.show_user_my_wallet)
        # ----------------------------------------------------------------------------------------------------
        # go back from user_my_wallet page--------------------------------------------------------------------
        self.ui.pushButt_back_user_my_wallet.clicked.connect(self.show_user_home_after_sign_in)
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
        self.ui.pushButt_back_user_history.clicked.connect(self.show_user_home_after_sign_in)
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
        self.ui.pushButt_cancel_request_user_driver_request_accepts_info.clicked.connect(
            self.show_user_home_after_sign_in)
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
        self.ui.pushButt_reached_destination_driver_reached_the_destination.clicked.connect(
            self.show_driver_home_on_off_service)
        # -----------------------------------------------------------------------------------------------------------
        self.ui.meli_get_photo_meli_certificate_obviously.clicked.connect(self.brows_select_meli_card)

        self.ui.pushButt_on_service_driver_home_on_off_service.clicked.connect(self.show_driver_home)

        self.ui.pushButt_cancel_booking_successful.clicked.connect(self.cancel_request)

        self.ui.pushButt_apply_changes_user_my_account.clicked.connect(self.set_apply_changes_user_my_account)

        self.ui.pushButt_done_user_payment_method.clicked.connect(self.set_transaction_user)

        self.ui.pushButt_done_booking_successful.clicked.connect(self.show_user_home_after_sign_in)

    def show(self):
        self.main_win.show()

    def show_loading(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loading)

    def show_sign_up(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up)

    def show_sign_in(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_in)

    def show_accept_code_sign_in(self):
        try:

            if IS_DRIVER(self.ui.enter_number_sign_in.toPlainText()) or IS_CLIENT(
                    self.ui.enter_number_sign_in.toPlainText()):
                self.gen_rand_number.gen_password_code_rand()
                self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_in)
            else:
                print("pls enter a valid number")

        except Exception as err:
            print(err)

    def show_accept_code_sign_up(self):
        try:
            if (self.ui.enter_number_sign_up.toPlainText()) and not CHECK_PHONE_EXIST(
                    self.ui.enter_number_sign_up.toPlainText()):
                self.ui.stackedWidget.setCurrentWidget(self.ui.accept_code_sign_up)
                self.gen_rand_number.gen_password_code_rand()
            else:
                print("pls enter a valid number")

        except Exception as err:
            print(err)

    def show_select_driver_user(self):
        input_password = self.ui.pass_digit1_accept_code_sign_up.toPlainText()
        if CHECK_IN_PASS_EQ_GEN_PASS(input_password, self.gen_rand_number.password_code):
            self.ui.stackedWidget.setCurrentWidget(self.ui.select_driver_user)

    def show_get_flname_driver(self):
        self.info_dict.set_phone_number_insert_driver_dict(self.ui.enter_number_sign_up.toPlainText().strip('0'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_flname_driver)

    def show_get_sex_birth_meli(self):
        try:
            self.info_dict.set_first_name_insert_driver_dict(self.ui.fname_get_flname_driver.toPlainText())
            self.info_dict.set_last_name_insert_driver_dict(self.ui.lname_get_flname_driver.toPlainText())
        except Exception as eer:
            print(eer)

        self.ui.stackedWidget.setCurrentWidget(self.ui.get_sex_birth_meli)

    def show_get_photo_meli_pcertificate_obviously(self):
        try:
            self.info_dict.set_sex_insert_driver_dict(self.ui.sex_get_sex_birth_meli.currentText())
            self.info_dict.set_birth_date_insert_driver_dict(int(self.ui.year_get_sex_birth_meli.text()),
                                                             int(self.ui.month_get_sex_birth_meli.text()),
                                                             int(self.ui.day_get_sex_birth_meli.text()))

            self.info_dict.set_national_code_insert_driver_dict(self.ui.meli_get_sex_birth_meli.toPlainText())
        except Exception as err:
            print(err)

        self.ui.stackedWidget.setCurrentWidget(self.ui.get_photo_meli_certificate_obviously)

    def brows_select_meli_card(self):
        dialog = QFileDialog(filter="Images *.png ", caption="select a file")
        print(dialog.getOpenFileName())

    def show_get_shaba(self):
        try:
            self.info_dict.set_national_card_photo_path_insert_driver_dict("../c:desktop/national id card")
            self.info_dict.set_license_photo_path_insert_driver_dict("../c:desktop/license card")
            self.info_dict.set_disability_insert_driver_dict(
                self.ui.obviously_get_photo_meli_pcertificate_obviously.currentText())
        except Exception as err:
            print(err)

        self.ui.stackedWidget.setCurrentWidget(self.ui.get_shaba)

    def show_select_service(self):
        try:
            self.info_dict.set_shaba_number_insert_driver_dict(self.ui.enter_shaba_number.toPlainText())
            self.send_driver_info_to_db()
        except Exception as err:
            print(err)

        self.ui.stackedWidget.setCurrentWidget(self.ui.select_service)

    def show_get_machine_baxi_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_info)

    def show_get_machine_baxi_woman_info(self):

        if CHECK_M_OR_F(self.ui.enter_number_sign_up.toPlainText()):
            self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_woman_info)

    def show_registration_successful_baxi_woman(self):
        try:
            self.info_dict.set_vehicle_production_date_insert_baxi_dict(
                datetime(int(self.ui.machine_generate_year_get_machine_baxi_woman_info.text()), 1, 1))
            self.info_dict.set_vehicle_name_insert_baxi_dict(
                self.ui.machine_name_get_machine_baxi_info.toPlainText())
            self.info_dict.set_vehicle_color_insert_baxi_dict(
                self.ui.machine_color_get_machine_baxi_woman_info.currentText())
            self.info_dict.set_vehicle_license_plate_insert_baxi_dict(
                self.ui.two_digit_left_pelak_get_machine_baxi_woman_info.toPlainText() +
                self.ui.alphabet_get_machine_baxi_woman_info.currentText() +
                self.ui.three_digit_pelak_get_machine_baxi_woman_info.toPlainText() +
                "-" +
                self.ui.two_digit_right_pelak_get_machine_baxi_woman_info.toPlainText())
            self.info_dict.set_vehicle_fuel_type_insert_baxi_dict(
                self.ui.machine_fuel_get_machine_baxi_woman_info.currentText())
            self.info_dict.set_vehicle_capacity_insert_baxi_dict(
                self.ui.machine_capacity_get_machine_baxi_woman_info.currentText())
            i_d = CHECK_ID_DRIVER(self.ui.enter_number_sign_up.toPlainText())

            self.info_dict.set_driver_id_insert_baxi_dict(i_d[0][0])
            print(self.info_dict.insert_baxi_dict)
            insert_baxi(self.info_dict.insert_baxi_dict)

            print("baxi women info successfully ad to db")
        except Exception as err:
            print(err)
        self.ui.stackedWidget.setCurrentWidget(self.ui.registration_successful)

    def show_registration_successful_baxi_bar(self):
        try:
            self.info_dict.set_vehicle_name_insert_baar_dict(
                self.ui.machine_name_get_machine_baxi_bar_info.toPlainText())
            self.info_dict.set_vehicle_production_date_insert_baar_dict(
                datetime(int(self.ui.machine_generate_year_get_machine_baxi_bar_info.text()), 1, 1))

            self.info_dict.set_vehicle_color_insert_baar_dict(
                self.ui.machine_color_get_machine_baxi_bar_info.currentText())
            self.info_dict.set_vehicle_license_plate_insert_baar_dict(
                self.ui.two_digit_left_pelak_get_machine_baxi_bar_info.toPlainText()
                +
                self.ui.alphabet_get_machine_baxi_bar_info.currentText()
                +
                self.ui.three_digit_pelak_get_machine_baxi_bar_info.toPlainText()
                +
                "-" + self.ui.two_digit_right_pelak_get_machine_baxi_bar_info.toPlainText())
            self.info_dict.set_vehicle_fuel_type_insert_baar_dict(
                self.ui.machine_fuel_get_machine_baxi_bar_info.currentText())
            self.info_dict.set_vehicle_capacity_insert_baar_dict(
                self.ui.machine_capacity_get_machine_baxi_bar_info.toPlainText())
            i_d = CHECK_ID_DRIVER(self.ui.enter_number_sign_up.toPlainText())
            self.info_dict.set_driver_id_insert_insert_baar_dict(i_d[0][0])

            insert_baar(self.info_dict.insert_baar_dict)
            print(self.info_dict.insert_baar_dict)
            print("baxi baar info successfully ad to db")
        except Exception as err:
            print(err)
        self.ui.stackedWidget.setCurrentWidget(self.ui.registration_successful)

    def show_registration_successful_baxi_box(self):
        try:

            self.info_dict.set_vehicle_name_insert_box_dict(
                self.ui.motor_name_get_motor_baxi_box_info.toPlainText())

            self.info_dict.set_vehicle_production_date_insert_box_dict(
                datetime(int(self.ui.motor_generate_year_get_motor_baxi_box_info.text()), 1, 1))

            self.info_dict.set_vehicle_license_plate_insert_box_dict(
                self.ui.five_digit_pelak_get_motor_baxi_box_info.toPlainText() +
                "-" +
                self.ui.three_digit_pelak_get_motor_baxi_box_info.toPlainText())

            self.info_dict.set_vehicle_capacity_insert_box_dict(
                self.ui.motor_capacity_get_motor_baxi_box_info.toPlainText())

            i_d = CHECK_ID_DRIVER(self.ui.enter_number_sign_up.toPlainText())
            self.info_dict.set_driver_id_insert_insert_box_dict(i_d[0][0])
            print(self.info_dict.insert_box_dict)
            insert_box(self.info_dict.insert_box_dict)

            print("baxi box info successfully ad to db")
        except Exception as err:
            print(err)
        self.ui.stackedWidget.setCurrentWidget(self.ui.registration_successful)

    def show_registration_successful_baxi(self):
        try:
            self.info_dict.set_vehicle_production_date_insert_baxi_dict(
                datetime(int(self.ui.machine_generate_year_get_machine_baxi_info.text()), 1, 1))
            self.info_dict.set_vehicle_name_insert_baxi_dict(
                self.ui.machine_name_get_machine_baxi_info.toPlainText())
            self.info_dict.set_vehicle_color_insert_baxi_dict(
                self.ui.machine_color_get_machine_baxi_info.currentText())
            self.info_dict.set_vehicle_license_plate_insert_baxi_dict(
                self.ui.two_digit_left_pelak_get_machine_baxi_info.toPlainText() +
                self.ui.alphabet_get_machine_baxi_info.currentText() +
                self.ui.three_digit_pelak_get_machine_baxi_info.toPlainText() +
                "-" + self.ui.two_digit_right_pelak_get_machine_baxi_info.toPlainText())
            self.info_dict.set_vehicle_fuel_type_insert_baxi_dict(
                self.ui.machine_fuel_get_machine_baxi_info.currentText())
            self.info_dict.set_vehicle_capacity_insert_baxi_dict(
                self.ui.machine_capacity_get_machine_baxi_info.currentText())
            i_d = CHECK_ID_DRIVER(self.ui.enter_number_sign_up.toPlainText())
            self.info_dict.set_driver_id_insert_baxi_dict(i_d[0][0])

            print(self.info_dict.insert_baxi_dict)
            insert_baxi(self.info_dict.insert_baxi_dict)

            print("baxi info successfully ad to db")

        except Exception as err:
            print(err)

        self.ui.stackedWidget.setCurrentWidget(self.ui.registration_successful)

    def exit_app(self):
        sys.exit()

    def show_get_flname_sex_birth_user(self):
        self.info_dict.set_phone_number_insert_client_dict(self.ui.enter_number_sign_up.toPlainText().strip('0'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_flname_sex_birth_user)

    def show_user_home_after_sign_in(self):
        self.off_menu_bar_user_home()
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_home)
        self.ui.stackedWidget.setCurrentWidget(self.mp.show())

    def show_user_home_after_sign_up(self):
        self.info_dict.set_sign_up_time_insert_client_dict()
        self.info_dict.set_sex_insert_client_dict(self.ui.sex_get_flname_sex_birth_user.currentText())
        self.info_dict.set_first_name_insert_client_dict(self.ui.fname_get_flname_sex_birth_user.toPlainText())
        self.info_dict.set_last_name_insert_client_dict(self.ui.lname_get_flname_sex_birth_user.toPlainText())
        self.info_dict.set_birth_date_insert_client_dict(datetime(int(self.ui.year_get_flname_sex_birth_user.text()),
                                                                  int(self.ui.day_get_flname_sex_birth_user.text()),
                                                                  int(self.ui.month_get_flname_sex_birth_user.text())))

        try:
            insert_client(self.info_dict.insert_client_dict)
            print(self.info_dict.insert_client_dict)
            print('add client was successful')
        except Exception as err:
            print(err)

        res = IS_CLIENT(self.ui.enter_number_sign_up.toPlainText().strip('0'))
        self.client_1.set_phone_number(self.ui.enter_number_sign_in.toPlainText())
        self.client_1.set_id(res[0][0])
        self.client_1.set_wallet_balance(res[0][1])
        self.client_1.set_first_name(res[0][2])
        self.client_1.set_last_name(res[0][3])
        res = client_panel_info(res[0][0])
        self.client_1.set_email(res[0][0])
        self.client_1.set_sex(res[0][1])
        self.client_1.set_birth_date(str(res[0][2]))

        self.off_menu_bar_user_home()
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_home)
        self.ui.stackedWidget.setCurrentWidget(self.mp.show())

    def send_driver_info_to_db(self):
        self.gen_rand_number.gen_referral_code_rand()
        self.info_dict.set_referral_code_insert_driver_dict(self.gen_rand_number.referral_code)
        self.info_dict.set_signup_time_insert_driver_dict()
        print(self.info_dict.insert_driver_dict)
        try:
            insert_driver(self.info_dict.insert_driver_dict)
            print("insert_driver successfully")
        except Exception as err:
            print(err)

    def show_get_machine_baxi_bar_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_machine_baxi_bar_info)

    def show_get_motor_baxi_box_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.get_motor_baxi_box_info)

    def show_baxi_user_choose_vehicle_type(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_user_choose_vehicle_type)

    def show_baxi_box_user_choose_vehicle_type(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_box_user_choose_vehicle_type)

    def show_baxi_bar_user_choose_vehicle_type(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_bar_user_choose_vehicle_type)

    def show_baxi_woman_user_choose_vehicle_type(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.baxi_woman_user_choose_vehicle_type)

    def show_menu_bar_user_home(self):
        self.ui.pushButt_my_wallet_user_home.setHidden(False)
        self.ui.pushButt_history_user_home.setHidden(False)
        self.ui.pushButt_settings_user_home.setHidden(False)
        self.ui.pushButt_logout_user_home.setHidden(False)
        self.ui.pushButt_menu_off_user_home.setHidden(False)
        self.ui.menu_bar_user_home.setHidden(False)
        self.ui.box_show_flname_user_home.setHidden(False)
        self.ui.box_show_cash_user_home.setHidden(False)
        self.ui.box_show_flname_user_home.setText(self.client_1.get_first_name() + " " + self.client_1.get_last_name())
        self.ui.box_show_cash_user_home.setText(str(get_client_balance(self.client_1.get_client_id())[0][0]))

    def off_menu_bar_user_home(self):
        self.ui.pushButt_my_wallet_user_home.setHidden(True)
        self.ui.pushButt_history_user_home.setHidden(True)
        self.ui.pushButt_settings_user_home.setHidden(True)
        self.ui.pushButt_logout_user_home.setHidden(True)
        self.ui.pushButt_menu_off_user_home.setHidden(True)
        self.ui.menu_bar_user_home.setHidden(True)
        self.ui.box_show_flname_user_home.setHidden(True)
        self.ui.box_show_cash_user_home.setHidden(True)

    def show_user_setting(self):
        self.ui.box_show_flname_user_setting.setText(
            self.client_1.get_first_name() + " " + self.client_1.get_last_name())
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_setting)

    def show_user_my_account(self):
        self.ui.show_box_flname_user_my_account.setText(
            self.client_1.get_first_name() + " " + self.client_1.get_last_name())
        self.ui.box_show_phone_numbe_user_my_account.setText(self.client_1.get_phone_number())
        self.ui.show_box_email_user_my_account.setText(self.client_1.get_email())
        self.ui.show_box_gender_user_my_account.setText(self.client_1.get_sex())
        self.ui.box_show_birthday_user_my_account.setText(str(self.client_1.get_birth_date()))
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_my_account)

    def show_user_my_wallet(self):
        self.ui.box_show_Balance_user_my_wallet.setText(str(get_client_balance(self.client_1.get_client_id())[0][0]))
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_my_wallet)

    def show_user_payment_method(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_payment_method)

    def show_pushButt_history_user_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_history)

    def show_user_driver_request_accepts_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_driver_request_accepts_info)

    def select_go_to_user_or_driver_home(self):
        input_password = self.ui.pass_digit1_accept_code_sign_in.toPlainText()

        print(self.gen_rand_number.password_code)
        if CHECK_IN_PASS_EQ_GEN_PASS(input_password, self.gen_rand_number.password_code):
            if driver_res := IS_DRIVER(self.ui.enter_number_sign_in.toPlainText()):
                self.driver_1.set_id(driver_res[0][0])
                self.driver_1.set_wallet_balance(driver_res[0][1])
                self.driver_1.set_first_name(driver_res[0][2])
                self.driver_1.set_last_name(driver_res[0][3])

                self.show_driver_home_on_off_service()
            if client_res := IS_CLIENT(self.ui.enter_number_sign_in.toPlainText()):
                print("client_res 3 ", client_res)
                self.client_1.set_phone_number(self.ui.enter_number_sign_in.toPlainText())
                self.client_1.set_id(client_res[0][0])
                self.client_1.set_wallet_balance(client_res[0][1])
                self.client_1.set_first_name(client_res[0][2])
                self.client_1.set_last_name(client_res[0][3])
                print(client_res[0][0])
                try:
                    res = client_panel_info(client_res[0][0])
                except Exception as err:
                    print(err)

                self.client_1.set_email(res[0][0])
                self.client_1.set_sex(res[0][1])
                self.client_1.set_birth_date(str(res[0][2]))
                self.show_user_home_after_sign_in()

    def show_driver_accept_request(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_accept_request)

    def show_driver_passenger_boarded(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_passenger_boarded)

    def show_driver_reached_the_destination(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_reached_the_destination)

    def show_driver_home(self):
        x = float(self.ui.get_x_driver_home_on_off_service.toPlainText())
        y = float(self.ui.get_y_driver_home_on_off_service.toPlainText())
        try:
            update_location(self.driver_1.get_driver_id(), x, y)
            print("update_location was successful")
        except Exception as err:
            print(err)

        try:
            res = requests_within_range(x, y)
        except Exception as err:
            print(err)
        print("requests_within_range", res)

        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_home)

    def show_driver_home_on_off_service(self):
        self.ui.stackedWidget.setCurrentWidget(self.mp.show())
        self.ui.box_show_wallet_balance_driver_home_on_off_service.setText(
            str(get_driver_balance(self.driver_1.get_driver_id())[0][0]))
        self.ui.box_show_flname_balance_driver_home_on_off_service.setText(
            self.driver_1.get_first_name() + " " + self.driver_1.get_last_name())
        self.ui.stackedWidget.setCurrentWidget(self.ui.driver_home_on_off_service)

    def set_general_info_trip(self):
        lat_pickup = self.ui.get_pickup_lat_user_home.toPlainText()
        lon_pickup = self.ui.get_pickup_lon_user_home.toPlainText()
        res_pickup = get_lat_lon_info(lat_pickup, lon_pickup)
        self.client_1.set_pickup((lat_pickup, lon_pickup))
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.client_1.set_request_time(date)
        self.info_dict.set_pickup_province_insert_request_dict(res_pickup['state'])
        self.info_dict.set_pickup_city_insert_request_dict(res_pickup['city'])
        self.info_dict.set_pickup_latitude_insert_request_dict(float(lat_pickup))
        self.info_dict.set_pickup_longitude_insert_request_dict(float(lon_pickup))
        self.info_dict.set_request_time_insert_request_dict(self.client_1.get_request_time())
        self.info_dict.set_client_id_insert_request_dict(self.client_1.get_client_id())

        lat_drop_off = self.ui.get_drop_off_lat_user_home.toPlainText()
        lon_drop_off = self.ui.get_deop_off_lon_user_home.toPlainText()
        res_drop_off = get_lat_lon_info(lat_drop_off, lon_drop_off)
        self.client_1.set_dropoff((lat_drop_off, lon_drop_off))

        self.info_dict.set_client_id_insert_destination_dict(self.client_1.get_client_id())
        self.info_dict.set_latitude_insert_destination_dict(float(lat_drop_off))
        self.info_dict.set_longitude_insert_destination_dict(float(lon_drop_off))
        self.info_dict.set_city_insert_destination_dict(res_drop_off['city'])

        self.info_dict.set_request_time_insert_destination_dict(self.client_1.get_request_time())

        try:
            print(self.info_dict.insert_request_dict)
            insert_request(self.info_dict.insert_request_dict)
            print("insert_request successfully")
        except Exception as err:
            print(err)

    def send_baxi_bar_request_to_db(self):
        res = self.client_1.get_dropoff()

        city = get_lat_lon_info(res[0][0], res[0][1])

        self.info_dict.set_dropoff_longitude_insert_heavy_dict(res[0][0])
        self.info_dict.set_dropoff_latitude_insert_heavy_dict(res[0][1])
        self.info_dict.set_cargo_type_insert_heavy_dict(
            self.ui.cargo_type_baxi_bar_user_choose_vehicle_type.currentText())
        self.info_dict.set_client_id_insert_heavy_dict(self.client_1.get_client_id())
        self.info_dict.set_cargo_weight_insert_heavy_dict(
            int(self.ui.cargo_weight_baxi_bar_user_choose_vehicle_type.value()))
        self.info_dict.set_dropoff_city_insert_heavy_dict(city['city'])
        self.info_dict.set_request_time_insert_heavy_dict(self.client_1.get_request_time())
        self.info_dict.set_cargo_value_insert_heavy_dict(
            int(self.ui.cargo_value_baxi_bar_user_choose_vehicle_type.toPlainText()))
        self.info_dict.set_cost_insert_heavy_dict(int(trip_cost_heavy(self.client_1.pickup, self.client_1.dropoff)))
        self.info_dict.set_client_helped_insert_heavy_dict(
            self.ui.client_helped_baxi_bar_user_choose_vehicle_type.currentText())

        try:
            print(self.info_dict.insert_trip_dict)
            insert_heavy(self.info_dict.insert_heavy_dict)
            print("insert_heavy_dict was successful")
        except Exception as err:
            print(err)

    def send_baxi_box_request_to_db(self):
        res = self.client_1.get_dropoff()
        city = get_lat_lon_info(res[0][0], res[0][1])
        print(city)
        self.info_dict.set_dropoff_longitude_insert_light_dict(res[0][0])
        self.info_dict.set_dropoff_latitude_insert_light_dict(res[0][1])
        self.info_dict.set_client_id_insert_light_dict(self.client_1.get_client_id())
        self.info_dict.set_request_time_insert_light_dict(self.client_1.get_request_time())
        self.info_dict.set_cargo_weight_insert_light_dict(
            int(self.ui.cargo_weight_baxi_box_user_choose_vehicle_type.value()))
        self.info_dict.set_dropoff_city_insert_light_dict(city['city'])
        self.info_dict.set_cargo_value_insert_light_dict(
            int(self.ui.cargo_value_baxi_box_user_choose_vehicle_type.value()))
        self.info_dict.set_cost_insert_light_dict(int(trip_cost_light(self.client_1.pickup, self.client_1.dropoff)))
        self.info_dict.set_insurance_cost_insert_light_dict(
            int(self.ui.cargo_value_baxi_box_user_choose_vehicle_type.text()) * 2)
        self.info_dict.set_cargo_type_insert_light_dict(
            self.ui.cargo_type_baxi_box_user_choose_vehicle_type.currentText())
        try:
            print(self.info_dict.insert_light_dict)
            insert_light(self.info_dict.insert_light_dict)
            print("insert_light_dict was successful")
        except Exception as err:
            print(err)

    def send_baxi_request_to_db(self):

        print(trip_cost_baxi(self.client_1.pickup, self.client_1.dropoff))
        self.info_dict.set_cost_insert_trip_dict(int(trip_cost_baxi(self.client_1.pickup, self.client_1.dropoff)))
        self.info_dict.set_client_id_insert_trip_dict(self.client_1.get_client_id())
        self.info_dict.set_round_trip_insert_trip_dict(self.ui.round_trip_baxi_user_choose_vehicle_type.currentText())
        self.info_dict.set_request_time_insert_trip_dict(self.client_1.get_request_time())
        print("date 4", self.client_1.get_request_time())

        try:
            print(self.info_dict.insert_destination_dict)
            insert_destination(self.info_dict.insert_destination_dict)
            print("insert_destination_dict successfully")
        except Exception as err:
            print(err)

        try:
            print(self.info_dict.insert_trip_dict)
            insert_trip(self.info_dict.insert_trip_dict)
            print("insert_trip was successful")
        except Exception as err:
            print(err)

    def send_baxi_woman_request_to_db(self):

        print(trip_cost_baxi(self.client_1.pickup, self.client_1.dropoff))
        self.info_dict.set_cost_insert_trip_dict(int(trip_cost_baxi(self.client_1.pickup, self.client_1.dropoff)))
        self.info_dict.set_client_id_insert_trip_dict(self.client_1.get_client_id())
        self.info_dict.set_round_trip_insert_trip_dict(
            self.ui.round_trip_baxi_woman_user_choose_vehicle_type.currentText())
        self.info_dict.set_request_time_insert_trip_dict(self.client_1.get_request_time())

        try:
            print(self.info_dict.insert_destination_dict)
            insert_destination(self.info_dict.insert_destination_dict)
            print("insert_destination_dict successfully")
        except Exception as err:
            print(err)

        try:
            print(self.info_dict.insert_trip_dict)
            insert_trip(self.info_dict.insert_trip_dict)
            print("insert_trip was successful")
        except Exception as err:
            print(err)

    def show_booking_successful_baxi(self):
        self.set_general_info_trip()
        self.send_baxi_request_to_db()
        self.ui.stackedWidget.setCurrentWidget(self.ui.booking_successful)

    def show_booking_successful_baxi_woman(self):
        self.set_general_info_trip()
        self.send_baxi_woman_request_to_db()
        self.ui.stackedWidget.setCurrentWidget(self.ui.booking_successful)

    def show_booking_successful_baxi_bar(self):
        self.set_general_info_trip()
        self.send_baxi_bar_request_to_db()
        self.ui.stackedWidget.setCurrentWidget(self.ui.booking_successful)

    def show_booking_successful_baxi_box(self):
        print("sllllm")
        self.set_general_info_trip()
        print("sllllm")
        self.send_baxi_box_request_to_db()
        print("sllllm")
        self.ui.stackedWidget.setCurrentWidget(self.ui.booking_successful)

    def cancel_request(self):
        print(self.client_1.get_client_id())
        print(self.client_1.get_request_time())
        close_request(self.client_1.get_client_id(), self.client_1.get_request_time())
        self.show_user_home_after_sign_in()

    def set_apply_changes_user_my_account(self):
        self.client_1.set_email(self.ui.show_box_email_user_my_account.toPlainText())
        try:
            set_email(self.client_1.get_client_id(), self.client_1.get_email())
            print("applying successful")
        except Exception as err:
            print(err)

    def set_transaction_user(self):
        self.gen_rand_number.gen_tracking_code_rand()
        self.info_dict.set_amount_insert_transaction_dict(int(self.ui.card_to_wallet_user_payment_method.toPlainText()))
        self.info_dict.set_tracking_code_insert_transaction_dict(self.gen_rand_number.tracking_code)
        self.info_dict.set_state_insert_transaction_dict('completed')
        self.info_dict.set_time_insert_transaction_dict(datetime.now())
        self.info_dict.set_type_insert_transaction_dict('card-to-wallet')

        print('info_dict.insert_transaction_dict ', self.info_dict.insert_transaction_dict)
        try:
            insert_transaction(self.info_dict.insert_transaction_dict)
        except Exception as err:
            print(err)

        self.info_dict.set_tracking_code_insert_deposit_dict(self.gen_rand_number.tracking_code)
        self.info_dict.set_client_id_insert_deposit_dict(self.client_1.get_client_id())

        print('info_dict.insert_deposit_dict ', self.info_dict.insert_deposit_dict)
        try:
            insert_deposit(self.info_dict.insert_deposit_dict)
        except Exception as err:
            print(err)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = Ui_BAXI()
    mp = MapWindow()
    main_win.show()
    sys.exit(app.exec())
