# Form implementation generated from reading ui file 'BAXI_Admin_Employee.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BAXI_Admin_Employee(object):
    def setupUi(self, BAXI_Admin_Employee):
        BAXI_Admin_Employee.setObjectName("BAXI_Admin_Employee")
        BAXI_Admin_Employee.resize(360, 640)
        BAXI_Admin_Employee.setMinimumSize(QtCore.QSize(360, 640))
        BAXI_Admin_Employee.setMaximumSize(QtCore.QSize(360, 640))
        self.centralwidget = QtWidgets.QWidget(parent=BAXI_Admin_Employee)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.stackedWidget.setObjectName("stackedWidget")
        self.loading = QtWidgets.QWidget()
        self.loading.setObjectName("loading")
        self.label = QtWidgets.QLabel(parent=self.loading)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/loading/loading.png"))
        self.label.setObjectName("label")
        self.pushButt_loading = QtWidgets.QPushButton(parent=self.loading)
        self.pushButt_loading.setGeometry(QtCore.QRect(130, 240, 101, 101))
        self.pushButt_loading.setText("")
        self.pushButt_loading.setFlat(True)
        self.pushButt_loading.setObjectName("pushButt_loading")
        self.stackedWidget.addWidget(self.loading)
        self.admin_panel = QtWidgets.QWidget()
        self.admin_panel.setObjectName("admin_panel")
        self.label_4 = QtWidgets.QLabel(parent=self.admin_panel)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/admin_panel/admin_panel.png"))
        self.label_4.setObjectName("label_4")
        self.pushButt_go_to_sign_in_admin_panel = QtWidgets.QPushButton(parent=self.admin_panel)
        self.pushButt_go_to_sign_in_admin_panel.setGeometry(QtCore.QRect(175, 587, 91, 24))
        self.pushButt_go_to_sign_in_admin_panel.setText("")
        self.pushButt_go_to_sign_in_admin_panel.setFlat(True)
        self.pushButt_go_to_sign_in_admin_panel.setObjectName("pushButt_go_to_sign_in_admin_panel")
        self.pushButt_exit_admin_panel = QtWidgets.QPushButton(parent=self.admin_panel)
        self.pushButt_exit_admin_panel.setGeometry(QtCore.QRect(110, 590, 31, 24))
        self.pushButt_exit_admin_panel.setText("")
        self.pushButt_exit_admin_panel.setFlat(True)
        self.pushButt_exit_admin_panel.setObjectName("pushButt_exit_admin_panel")
        self.pushButt_add_new_employee_admin_panel = QtWidgets.QPushButton(parent=self.admin_panel)
        self.pushButt_add_new_employee_admin_panel.setGeometry(QtCore.QRect(40, 453, 281, 31))
        self.pushButt_add_new_employee_admin_panel.setText("")
        self.pushButt_add_new_employee_admin_panel.setFlat(True)
        self.pushButt_add_new_employee_admin_panel.setObjectName("pushButt_add_new_employee_admin_panel")
        self.pushButt_query_admin_panel = QtWidgets.QPushButton(parent=self.admin_panel)
        self.pushButt_query_admin_panel.setGeometry(QtCore.QRect(40, 530, 281, 31))
        self.pushButt_query_admin_panel.setText("")
        self.pushButt_query_admin_panel.setFlat(True)
        self.pushButt_query_admin_panel.setObjectName("pushButt_query_admin_panel")
        self.stackedWidget.addWidget(self.admin_panel)
        self.admin_panel_recruitment = QtWidgets.QWidget()
        self.admin_panel_recruitment.setObjectName("admin_panel_recruitment")
        self.label_5 = QtWidgets.QLabel(parent=self.admin_panel_recruitment)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/admin_panel_recruitment/admin_panel_recruitment.png"))
        self.label_5.setObjectName("label_5")
        self.pushButt_estekhdam_admin_panel_recruitment = QtWidgets.QPushButton(parent=self.admin_panel_recruitment)
        self.pushButt_estekhdam_admin_panel_recruitment.setGeometry(QtCore.QRect(130, 540, 101, 31))
        self.pushButt_estekhdam_admin_panel_recruitment.setText("")
        self.pushButt_estekhdam_admin_panel_recruitment.setFlat(True)
        self.pushButt_estekhdam_admin_panel_recruitment.setObjectName("pushButt_estekhdam_admin_panel_recruitment")
        self.pushButt_back_admin_panel_recruitment = QtWidgets.QPushButton(parent=self.admin_panel_recruitment)
        self.pushButt_back_admin_panel_recruitment.setGeometry(QtCore.QRect(130, 590, 101, 21))
        self.pushButt_back_admin_panel_recruitment.setText("")
        self.pushButt_back_admin_panel_recruitment.setFlat(True)
        self.pushButt_back_admin_panel_recruitment.setObjectName("pushButt_back_admin_panel_recruitment")
        self.get_last_name_admin_panel_recruitment = QtWidgets.QTextEdit(parent=self.admin_panel_recruitment)
        self.get_last_name_admin_panel_recruitment.setGeometry(QtCore.QRect(40, 140, 131, 41))
        self.get_last_name_admin_panel_recruitment.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_last_name_admin_panel_recruitment.setObjectName("get_last_name_admin_panel_recruitment")
        self.get_sex_admin_panel_recruitment = QtWidgets.QComboBox(parent=self.admin_panel_recruitment)
        self.get_sex_admin_panel_recruitment.setGeometry(QtCore.QRect(230, 285, 81, 31))
        self.get_sex_admin_panel_recruitment.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.get_sex_admin_panel_recruitment.setObjectName("get_sex_admin_panel_recruitment")
        self.get_sex_admin_panel_recruitment.addItem("")
        self.get_sex_admin_panel_recruitment.addItem("")
        self.get_birthday_admin_panel_recruitment = QtWidgets.QSpinBox(parent=self.admin_panel_recruitment)
        self.get_birthday_admin_panel_recruitment.setGeometry(QtCore.QRect(140, 220, 42, 22))
        self.get_birthday_admin_panel_recruitment.setMinimum(1)
        self.get_birthday_admin_panel_recruitment.setMaximum(31)
        self.get_birthday_admin_panel_recruitment.setObjectName("get_birthday_admin_panel_recruitment")
        self.get_department_admin_panel_recruitment = QtWidgets.QComboBox(parent=self.admin_panel_recruitment)
        self.get_department_admin_panel_recruitment.setGeometry(QtCore.QRect(252, 350, 71, 31))
        self.get_department_admin_panel_recruitment.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.get_department_admin_panel_recruitment.setObjectName("get_department_admin_panel_recruitment")
        self.get_department_admin_panel_recruitment.addItem("")
        self.get_department_admin_panel_recruitment.addItem("")
        self.get_department_admin_panel_recruitment.addItem("")
        self.get_semat_admin_panel_recruitment = QtWidgets.QComboBox(parent=self.admin_panel_recruitment)
        self.get_semat_admin_panel_recruitment.setGeometry(QtCore.QRect(143, 350, 71, 31))
        self.get_semat_admin_panel_recruitment.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.get_semat_admin_panel_recruitment.setObjectName("get_semat_admin_panel_recruitment")
        self.get_semat_admin_panel_recruitment.addItem("")
        self.get_semat_admin_panel_recruitment.addItem("")
        self.get_semat_admin_panel_recruitment.addItem("")
        self.get_skill_admin_panel_recruitment = QtWidgets.QComboBox(parent=self.admin_panel_recruitment)
        self.get_skill_admin_panel_recruitment.setGeometry(QtCore.QRect(40, 350, 68, 31))
        self.get_skill_admin_panel_recruitment.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.get_skill_admin_panel_recruitment.setObjectName("get_skill_admin_panel_recruitment")
        self.get_skill_admin_panel_recruitment.addItem("")
        self.get_skill_admin_panel_recruitment.addItem("")
        self.get_skill_admin_panel_recruitment.addItem("")
        self.get_first_name_admin_panel_recruitment = QtWidgets.QTextEdit(parent=self.admin_panel_recruitment)
        self.get_first_name_admin_panel_recruitment.setGeometry(QtCore.QRect(210, 147, 111, 31))
        self.get_first_name_admin_panel_recruitment.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_first_name_admin_panel_recruitment.setObjectName("get_first_name_admin_panel_recruitment")
        self.get_code_meli_admin_panel_recruitment = QtWidgets.QTextEdit(parent=self.admin_panel_recruitment)
        self.get_code_meli_admin_panel_recruitment.setGeometry(QtCore.QRect(210, 217, 111, 31))
        self.get_code_meli_admin_panel_recruitment.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_code_meli_admin_panel_recruitment.setObjectName("get_code_meli_admin_panel_recruitment")
        self.get_code_personnel_admin_panel_recruitment = QtWidgets.QTextEdit(parent=self.admin_panel_recruitment)
        self.get_code_personnel_admin_panel_recruitment.setGeometry(QtCore.QRect(35, 285, 141, 31))
        self.get_code_personnel_admin_panel_recruitment.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_code_personnel_admin_panel_recruitment.setObjectName("get_code_personnel_admin_panel_recruitment")
        self.get_shaba_number_admin_panel_recruitment = QtWidgets.QTextEdit(parent=self.admin_panel_recruitment)
        self.get_shaba_number_admin_panel_recruitment.setGeometry(QtCore.QRect(40, 420, 281, 31))
        self.get_shaba_number_admin_panel_recruitment.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_shaba_number_admin_panel_recruitment.setObjectName("get_shaba_number_admin_panel_recruitment")
        self.get_salary_admin_panel_recruitment = QtWidgets.QTextEdit(parent=self.admin_panel_recruitment)
        self.get_salary_admin_panel_recruitment.setGeometry(QtCore.QRect(50, 489, 81, 31))
        self.get_salary_admin_panel_recruitment.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_salary_admin_panel_recruitment.setObjectName("get_salary_admin_panel_recruitment")
        self.pushButt_upload_education_admin_panel_recruitment = QtWidgets.QPushButton(parent=self.admin_panel_recruitment)
        self.pushButt_upload_education_admin_panel_recruitment.setGeometry(QtCore.QRect(160, 490, 71, 31))
        self.pushButt_upload_education_admin_panel_recruitment.setText("")
        self.pushButt_upload_education_admin_panel_recruitment.setFlat(True)
        self.pushButt_upload_education_admin_panel_recruitment.setObjectName("pushButt_upload_education_admin_panel_recruitment")
        self.pushButt_upload_profilePhoto_admin_panel_recruitment = QtWidgets.QPushButton(parent=self.admin_panel_recruitment)
        self.pushButt_upload_profilePhoto_admin_panel_recruitment.setGeometry(QtCore.QRect(250, 487, 71, 31))
        self.pushButt_upload_profilePhoto_admin_panel_recruitment.setText("")
        self.pushButt_upload_profilePhoto_admin_panel_recruitment.setFlat(True)
        self.pushButt_upload_profilePhoto_admin_panel_recruitment.setObjectName("pushButt_upload_profilePhoto_admin_panel_recruitment")
        self.get_birthmonth_admin_panel_recruitment = QtWidgets.QSpinBox(parent=self.admin_panel_recruitment)
        self.get_birthmonth_admin_panel_recruitment.setGeometry(QtCore.QRect(90, 220, 42, 22))
        self.get_birthmonth_admin_panel_recruitment.setMinimum(1)
        self.get_birthmonth_admin_panel_recruitment.setMaximum(12)
        self.get_birthmonth_admin_panel_recruitment.setObjectName("get_birthmonth_admin_panel_recruitment")
        self.get_birthyear_admin_panel_recruitment = QtWidgets.QSpinBox(parent=self.admin_panel_recruitment)
        self.get_birthyear_admin_panel_recruitment.setGeometry(QtCore.QRect(34, 220, 51, 22))
        self.get_birthyear_admin_panel_recruitment.setMinimum(1350)
        self.get_birthyear_admin_panel_recruitment.setMaximum(1600)
        self.get_birthyear_admin_panel_recruitment.setObjectName("get_birthyear_admin_panel_recruitment")
        self.stackedWidget.addWidget(self.admin_panel_recruitment)
        self.admin_panel_query = QtWidgets.QWidget()
        self.admin_panel_query.setObjectName("admin_panel_query")
        self.label_6 = QtWidgets.QLabel(parent=self.admin_panel_query)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/admin_panel_query/admin_panel_query.png"))
        self.label_6.setObjectName("label_6")
        self.pushButt_go_to_admin_panel_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_go_to_admin_panel_admin_panel_query.setGeometry(QtCore.QRect(134, 585, 91, 24))
        self.pushButt_go_to_admin_panel_admin_panel_query.setText("")
        self.pushButt_go_to_admin_panel_admin_panel_query.setFlat(True)
        self.pushButt_go_to_admin_panel_admin_panel_query.setObjectName("pushButt_go_to_admin_panel_admin_panel_query")
        self.pushButt_query_1_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_1_admin_panel_query.setGeometry(QtCore.QRect(220, 180, 81, 21))
        self.pushButt_query_1_admin_panel_query.setText("")
        self.pushButt_query_1_admin_panel_query.setFlat(True)
        self.pushButt_query_1_admin_panel_query.setObjectName("pushButt_query_1_admin_panel_query")
        self.pushButt_query_2_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_2_admin_panel_query.setGeometry(QtCore.QRect(220, 218, 81, 21))
        self.pushButt_query_2_admin_panel_query.setText("")
        self.pushButt_query_2_admin_panel_query.setFlat(True)
        self.pushButt_query_2_admin_panel_query.setObjectName("pushButt_query_2_admin_panel_query")
        self.pushButt_query_3_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_3_admin_panel_query.setGeometry(QtCore.QRect(220, 255, 81, 21))
        self.pushButt_query_3_admin_panel_query.setText("")
        self.pushButt_query_3_admin_panel_query.setFlat(True)
        self.pushButt_query_3_admin_panel_query.setObjectName("pushButt_query_3_admin_panel_query")
        self.pushButt_query_4_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_4_admin_panel_query.setGeometry(QtCore.QRect(220, 295, 81, 21))
        self.pushButt_query_4_admin_panel_query.setText("")
        self.pushButt_query_4_admin_panel_query.setFlat(True)
        self.pushButt_query_4_admin_panel_query.setObjectName("pushButt_query_4_admin_panel_query")
        self.pushButt_query_5_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_5_admin_panel_query.setGeometry(QtCore.QRect(220, 330, 81, 21))
        self.pushButt_query_5_admin_panel_query.setText("")
        self.pushButt_query_5_admin_panel_query.setFlat(True)
        self.pushButt_query_5_admin_panel_query.setObjectName("pushButt_query_5_admin_panel_query")
        self.pushButt_query_6_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_6_admin_panel_query.setGeometry(QtCore.QRect(220, 370, 81, 21))
        self.pushButt_query_6_admin_panel_query.setText("")
        self.pushButt_query_6_admin_panel_query.setFlat(True)
        self.pushButt_query_6_admin_panel_query.setObjectName("pushButt_query_6_admin_panel_query")
        self.pushButt_query_7_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_7_admin_panel_query.setGeometry(QtCore.QRect(220, 405, 81, 21))
        self.pushButt_query_7_admin_panel_query.setText("")
        self.pushButt_query_7_admin_panel_query.setFlat(True)
        self.pushButt_query_7_admin_panel_query.setObjectName("pushButt_query_7_admin_panel_query")
        self.pushButt_query_9_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_9_admin_panel_query.setGeometry(QtCore.QRect(220, 483, 81, 21))
        self.pushButt_query_9_admin_panel_query.setText("")
        self.pushButt_query_9_admin_panel_query.setFlat(True)
        self.pushButt_query_9_admin_panel_query.setObjectName("pushButt_query_9_admin_panel_query")
        self.pushButt_query_10_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_10_admin_panel_query.setGeometry(QtCore.QRect(220, 520, 81, 21))
        self.pushButt_query_10_admin_panel_query.setText("")
        self.pushButt_query_10_admin_panel_query.setFlat(True)
        self.pushButt_query_10_admin_panel_query.setObjectName("pushButt_query_10_admin_panel_query")
        self.pushButt_query_8_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_8_admin_panel_query.setGeometry(QtCore.QRect(220, 445, 81, 21))
        self.pushButt_query_8_admin_panel_query.setText("")
        self.pushButt_query_8_admin_panel_query.setFlat(True)
        self.pushButt_query_8_admin_panel_query.setObjectName("pushButt_query_8_admin_panel_query")
        self.pushButt_query_15_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_15_admin_panel_query.setGeometry(QtCore.QRect(66, 330, 81, 21))
        self.pushButt_query_15_admin_panel_query.setText("")
        self.pushButt_query_15_admin_panel_query.setFlat(True)
        self.pushButt_query_15_admin_panel_query.setObjectName("pushButt_query_15_admin_panel_query")
        self.pushButt_query_14_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_14_admin_panel_query.setGeometry(QtCore.QRect(66, 293, 81, 21))
        self.pushButt_query_14_admin_panel_query.setText("")
        self.pushButt_query_14_admin_panel_query.setFlat(True)
        self.pushButt_query_14_admin_panel_query.setObjectName("pushButt_query_14_admin_panel_query")
        self.pushButt_query_13_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_13_admin_panel_query.setGeometry(QtCore.QRect(66, 255, 81, 21))
        self.pushButt_query_13_admin_panel_query.setText("")
        self.pushButt_query_13_admin_panel_query.setFlat(True)
        self.pushButt_query_13_admin_panel_query.setObjectName("pushButt_query_13_admin_panel_query")
        self.pushButt_query_12_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_12_admin_panel_query.setGeometry(QtCore.QRect(66, 217, 81, 21))
        self.pushButt_query_12_admin_panel_query.setText("")
        self.pushButt_query_12_admin_panel_query.setFlat(True)
        self.pushButt_query_12_admin_panel_query.setObjectName("pushButt_query_12_admin_panel_query")
        self.pushButt_query_11_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_11_admin_panel_query.setGeometry(QtCore.QRect(66, 180, 81, 21))
        self.pushButt_query_11_admin_panel_query.setText("")
        self.pushButt_query_11_admin_panel_query.setFlat(True)
        self.pushButt_query_11_admin_panel_query.setObjectName("pushButt_query_11_admin_panel_query")
        self.pushButt_query_16_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_16_admin_panel_query.setGeometry(QtCore.QRect(66, 370, 81, 21))
        self.pushButt_query_16_admin_panel_query.setText("")
        self.pushButt_query_16_admin_panel_query.setFlat(True)
        self.pushButt_query_16_admin_panel_query.setObjectName("pushButt_query_16_admin_panel_query")
        self.pushButt_query_17_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_17_admin_panel_query.setGeometry(QtCore.QRect(66, 406, 81, 21))
        self.pushButt_query_17_admin_panel_query.setText("")
        self.pushButt_query_17_admin_panel_query.setFlat(True)
        self.pushButt_query_17_admin_panel_query.setObjectName("pushButt_query_17_admin_panel_query")
        self.pushButt_query_18_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_18_admin_panel_query.setGeometry(QtCore.QRect(66, 445, 81, 21))
        self.pushButt_query_18_admin_panel_query.setText("")
        self.pushButt_query_18_admin_panel_query.setFlat(True)
        self.pushButt_query_18_admin_panel_query.setObjectName("pushButt_query_18_admin_panel_query")
        self.pushButt_query_19_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_19_admin_panel_query.setGeometry(QtCore.QRect(66, 483, 81, 21))
        self.pushButt_query_19_admin_panel_query.setText("")
        self.pushButt_query_19_admin_panel_query.setFlat(True)
        self.pushButt_query_19_admin_panel_query.setObjectName("pushButt_query_19_admin_panel_query")
        self.pushButt_query_20_admin_panel_query = QtWidgets.QPushButton(parent=self.admin_panel_query)
        self.pushButt_query_20_admin_panel_query.setGeometry(QtCore.QRect(66, 520, 81, 21))
        self.pushButt_query_20_admin_panel_query.setText("")
        self.pushButt_query_20_admin_panel_query.setFlat(True)
        self.pushButt_query_20_admin_panel_query.setObjectName("pushButt_query_20_admin_panel_query")
        self.stackedWidget.addWidget(self.admin_panel_query)
        self.admin_panel_recruitment_successful = QtWidgets.QWidget()
        self.admin_panel_recruitment_successful.setObjectName("admin_panel_recruitment_successful")
        self.label_7 = QtWidgets.QLabel(parent=self.admin_panel_recruitment_successful)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/admin_panel_recruitment_successful/admin_panel_recruitment_successful.png"))
        self.label_7.setObjectName("label_7")
        self.pushButt_go_to_admin_panel_admin_panel_recruitment_successful = QtWidgets.QPushButton(parent=self.admin_panel_recruitment_successful)
        self.pushButt_go_to_admin_panel_admin_panel_recruitment_successful.setGeometry(QtCore.QRect(140, 585, 81, 24))
        self.pushButt_go_to_admin_panel_admin_panel_recruitment_successful.setText("")
        self.pushButt_go_to_admin_panel_admin_panel_recruitment_successful.setFlat(True)
        self.pushButt_go_to_admin_panel_admin_panel_recruitment_successful.setObjectName("pushButt_go_to_admin_panel_admin_panel_recruitment_successful")
        self.stackedWidget.addWidget(self.admin_panel_recruitment_successful)
        self.employee_panel_authentication_request = QtWidgets.QWidget()
        self.employee_panel_authentication_request.setObjectName("employee_panel_authentication_request")
        self.label_9 = QtWidgets.QLabel(parent=self.employee_panel_authentication_request)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/employee_panel_authentication_request/employee_panel_authentication_request.png"))
        self.label_9.setObjectName("label_9")
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1 = QtWidgets.QPushButton(parent=self.employee_panel_authentication_request)
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1.setGeometry(QtCore.QRect(24, 143, 311, 41))
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1.setText("")
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1.setFlat(True)
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1.setObjectName("pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_1")
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_2 = QtWidgets.QPushButton(parent=self.employee_panel_authentication_request)
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_2.setGeometry(QtCore.QRect(24, 270, 311, 41))
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_2.setText("")
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_2.setFlat(True)
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_2.setObjectName("pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_2")
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_3 = QtWidgets.QPushButton(parent=self.employee_panel_authentication_request)
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_3.setGeometry(QtCore.QRect(24, 210, 311, 41))
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_3.setText("")
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_3.setFlat(True)
        self.pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_3.setObjectName("pushButt_go_to_employee_panel_authentication_employee_panel_authentication_request_3")
        self.pushButt_go_to_employee_panel_employee_panel_authentication_request = QtWidgets.QPushButton(parent=self.employee_panel_authentication_request)
        self.pushButt_go_to_employee_panel_employee_panel_authentication_request.setGeometry(QtCore.QRect(130, 580, 101, 31))
        self.pushButt_go_to_employee_panel_employee_panel_authentication_request.setText("")
        self.pushButt_go_to_employee_panel_employee_panel_authentication_request.setFlat(True)
        self.pushButt_go_to_employee_panel_employee_panel_authentication_request.setObjectName("pushButt_go_to_employee_panel_employee_panel_authentication_request")
        self.stackedWidget.addWidget(self.employee_panel_authentication_request)
        self.employee_sign_in = QtWidgets.QWidget()
        self.employee_sign_in.setObjectName("employee_sign_in")
        self.label_3 = QtWidgets.QLabel(parent=self.employee_sign_in)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/employee_sign_in/employee_sign_in.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.pushButt_admin = QtWidgets.QPushButton(parent=self.employee_sign_in)
        self.pushButt_admin.setGeometry(QtCore.QRect(55, 150, 41, 41))
        self.pushButt_admin.setText("")
        self.pushButt_admin.setFlat(True)
        self.pushButt_admin.setObjectName("pushButt_admin")
        self.pushButt_go_to_employee_panel_employee_sign_in = QtWidgets.QPushButton(parent=self.employee_sign_in)
        self.pushButt_go_to_employee_panel_employee_sign_in.setGeometry(QtCore.QRect(210, 425, 91, 31))
        self.pushButt_go_to_employee_panel_employee_sign_in.setText("")
        self.pushButt_go_to_employee_panel_employee_sign_in.setFlat(True)
        self.pushButt_go_to_employee_panel_employee_sign_in.setObjectName("pushButt_go_to_employee_panel_employee_sign_in")
        self.get_id_employee_sign_in = QtWidgets.QTextEdit(parent=self.employee_sign_in)
        self.get_id_employee_sign_in.setGeometry(QtCore.QRect(93, 219, 211, 31))
        self.get_id_employee_sign_in.setAutoFillBackground(True)
        self.get_id_employee_sign_in.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_id_employee_sign_in.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.get_id_employee_sign_in.setObjectName("get_id_employee_sign_in")
        self.get_password_employee_sign_in = QtWidgets.QTextEdit(parent=self.employee_sign_in)
        self.get_password_employee_sign_in.setGeometry(QtCore.QRect(90, 279, 211, 31))
        self.get_password_employee_sign_in.setAutoFillBackground(True)
        self.get_password_employee_sign_in.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_password_employee_sign_in.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.get_password_employee_sign_in.setObjectName("get_password_employee_sign_in")
        self.stackedWidget.addWidget(self.employee_sign_in)
        self.employee_panel = QtWidgets.QWidget()
        self.employee_panel.setObjectName("employee_panel")
        self.label_8 = QtWidgets.QLabel(parent=self.employee_panel)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/employee_panel/employee_panel.png"))
        self.label_8.setObjectName("label_8")
        self.pushButt_go_to_employee_panel_authentication_request_employee_panel = QtWidgets.QPushButton(parent=self.employee_panel)
        self.pushButt_go_to_employee_panel_authentication_request_employee_panel.setGeometry(QtCore.QRect(30, 480, 301, 41))
        self.pushButt_go_to_employee_panel_authentication_request_employee_panel.setText("")
        self.pushButt_go_to_employee_panel_authentication_request_employee_panel.setFlat(True)
        self.pushButt_go_to_employee_panel_authentication_request_employee_panel.setObjectName("pushButt_go_to_employee_panel_authentication_request_employee_panel")
        self.pushButt_go_to_employee_sign_in_employee_panel = QtWidgets.QPushButton(parent=self.employee_panel)
        self.pushButt_go_to_employee_sign_in_employee_panel.setGeometry(QtCore.QRect(170, 590, 101, 21))
        self.pushButt_go_to_employee_sign_in_employee_panel.setText("")
        self.pushButt_go_to_employee_sign_in_employee_panel.setFlat(True)
        self.pushButt_go_to_employee_sign_in_employee_panel.setObjectName("pushButt_go_to_employee_sign_in_employee_panel")
        self.pushButt_go_to_exit_employee_panel = QtWidgets.QPushButton(parent=self.employee_panel)
        self.pushButt_go_to_exit_employee_panel.setGeometry(QtCore.QRect(108, 590, 41, 21))
        self.pushButt_go_to_exit_employee_panel.setText("")
        self.pushButt_go_to_exit_employee_panel.setFlat(True)
        self.pushButt_go_to_exit_employee_panel.setObjectName("pushButt_go_to_exit_employee_panel")
        self.stackedWidget.addWidget(self.employee_panel)
        self.admin_sign_in = QtWidgets.QWidget()
        self.admin_sign_in.setObjectName("admin_sign_in")
        self.label_2 = QtWidgets.QLabel(parent=self.admin_sign_in)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../image/admin_eployee_panel/admin_sign_in/admin_sign_in.png"))
        self.label_2.setObjectName("label_2")
        self.pushButt_employee = QtWidgets.QPushButton(parent=self.admin_sign_in)
        self.pushButt_employee.setGeometry(QtCore.QRect(270, 150, 41, 41))
        self.pushButt_employee.setText("")
        self.pushButt_employee.setFlat(True)
        self.pushButt_employee.setObjectName("pushButt_employee")
        self.pushBut_admin_sign_in = QtWidgets.QPushButton(parent=self.admin_sign_in)
        self.pushBut_admin_sign_in.setGeometry(QtCore.QRect(210, 425, 91, 31))
        self.pushBut_admin_sign_in.setText("")
        self.pushBut_admin_sign_in.setFlat(True)
        self.pushBut_admin_sign_in.setObjectName("pushBut_admin_sign_in")
        self.get_id_admin_sign_in = QtWidgets.QTextEdit(parent=self.admin_sign_in)
        self.get_id_admin_sign_in.setGeometry(QtCore.QRect(90, 219, 211, 31))
        self.get_id_admin_sign_in.setAutoFillBackground(True)
        self.get_id_admin_sign_in.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_id_admin_sign_in.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.get_id_admin_sign_in.setObjectName("get_id_admin_sign_in")
        self.get_password_admin_sign_in = QtWidgets.QTextEdit(parent=self.admin_sign_in)
        self.get_password_admin_sign_in.setGeometry(QtCore.QRect(90, 279, 211, 31))
        self.get_password_admin_sign_in.setAutoFillBackground(True)
        self.get_password_admin_sign_in.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.get_password_admin_sign_in.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.get_password_admin_sign_in.setObjectName("get_password_admin_sign_in")
        self.stackedWidget.addWidget(self.admin_sign_in)
        BAXI_Admin_Employee.setCentralWidget(self.centralwidget)

        self.retranslateUi(BAXI_Admin_Employee)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(BAXI_Admin_Employee)

    def retranslateUi(self, BAXI_Admin_Employee):
        _translate = QtCore.QCoreApplication.translate
        BAXI_Admin_Employee.setWindowTitle(_translate("BAXI_Admin_Employee", "MainWindow"))
        self.get_sex_admin_panel_recruitment.setItemText(0, _translate("BAXI_Admin_Employee", "آقا"))
        self.get_sex_admin_panel_recruitment.setItemText(1, _translate("BAXI_Admin_Employee", "خانم"))
        self.get_department_admin_panel_recruitment.setItemText(0, _translate("BAXI_Admin_Employee", "الف"))
        self.get_department_admin_panel_recruitment.setItemText(1, _translate("BAXI_Admin_Employee", "ب"))
        self.get_department_admin_panel_recruitment.setItemText(2, _translate("BAXI_Admin_Employee", "پ"))
        self.get_semat_admin_panel_recruitment.setItemText(0, _translate("BAXI_Admin_Employee", "مدیر"))
        self.get_semat_admin_panel_recruitment.setItemText(1, _translate("BAXI_Admin_Employee", "برنامه نویس"))
        self.get_semat_admin_panel_recruitment.setItemText(2, _translate("BAXI_Admin_Employee", "کارمند"))
        self.get_skill_admin_panel_recruitment.setItemText(0, _translate("BAXI_Admin_Employee", "الف "))
        self.get_skill_admin_panel_recruitment.setItemText(1, _translate("BAXI_Admin_Employee", "ب"))
        self.get_skill_admin_panel_recruitment.setItemText(2, _translate("BAXI_Admin_Employee", "پ"))
