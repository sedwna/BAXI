# Form implementation generated from reading ui file 'BAXI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BAXI(object):
    def setupUi(self, BAXI):
        BAXI.setObjectName("BAXI")
        BAXI.resize(360, 640)
        BAXI.setMinimumSize(QtCore.QSize(360, 640))
        BAXI.setMaximumSize(QtCore.QSize(360, 640))
        self.centralwidget = QtWidgets.QWidget(parent=BAXI)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.stackedWidget.setMinimumSize(QtCore.QSize(360, 640))
        self.stackedWidget.setMaximumSize(QtCore.QSize(360, 640))
        self.stackedWidget.setObjectName("stackedWidget")
        self.loading = QtWidgets.QWidget()
        self.loading.setObjectName("loading")
        self.label = QtWidgets.QLabel(parent=self.loading)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../image/loading/Android Small - 1.png"))
        self.label.setObjectName("label")
        self.pushButt_logo = QtWidgets.QPushButton(parent=self.loading)
        self.pushButt_logo.setEnabled(True)
        self.pushButt_logo.setGeometry(QtCore.QRect(120, 170, 120, 120))
        self.pushButt_logo.setMinimumSize(QtCore.QSize(120, 120))
        self.pushButt_logo.setMaximumSize(QtCore.QSize(120, 120))
        self.pushButt_logo.setText("")
        self.pushButt_logo.setIconSize(QtCore.QSize(120, 120))
        self.pushButt_logo.setCheckable(False)
        self.pushButt_logo.setChecked(False)
        self.pushButt_logo.setAutoRepeat(False)
        self.pushButt_logo.setAutoExclusive(False)
        self.pushButt_logo.setAutoDefault(False)
        self.pushButt_logo.setDefault(False)
        self.pushButt_logo.setFlat(True)
        self.pushButt_logo.setObjectName("pushButt_logo")
        self.stackedWidget.addWidget(self.loading)
        self.get_sex_birth_meli = QtWidgets.QWidget()
        self.get_sex_birth_meli.setObjectName("get_sex_birth_meli")
        self.label_8 = QtWidgets.QLabel(parent=self.get_sex_birth_meli)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../image/get_sex_birth_meli/get_sex_birth_meli.png"))
        self.label_8.setObjectName("label_8")
        self.pushButt_next_get_sex_birth_meli = QtWidgets.QPushButton(parent=self.get_sex_birth_meli)
        self.pushButt_next_get_sex_birth_meli.setGeometry(QtCore.QRect(40, 440, 281, 29))
        self.pushButt_next_get_sex_birth_meli.setText("")
        self.pushButt_next_get_sex_birth_meli.setFlat(True)
        self.pushButt_next_get_sex_birth_meli.setObjectName("pushButt_next_get_sex_birth_meli")
        self.pushButt_back_get_sex_birth_meli = QtWidgets.QPushButton(parent=self.get_sex_birth_meli)
        self.pushButt_back_get_sex_birth_meli.setGeometry(QtCore.QRect(40, 510, 281, 29))
        self.pushButt_back_get_sex_birth_meli.setText("")
        self.pushButt_back_get_sex_birth_meli.setFlat(True)
        self.pushButt_back_get_sex_birth_meli.setObjectName("pushButt_back_get_sex_birth_meli")
        self.meli_get_sex_birth_meli = QtWidgets.QTextEdit(parent=self.get_sex_birth_meli)
        self.meli_get_sex_birth_meli.setGeometry(QtCore.QRect(140, 360, 171, 31))
        self.meli_get_sex_birth_meli.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.meli_get_sex_birth_meli.setObjectName("meli_get_sex_birth_meli")
        self.day_get_sex_birth_meli = QtWidgets.QSpinBox(parent=self.get_sex_birth_meli)
        self.day_get_sex_birth_meli.setGeometry(QtCore.QRect(270, 230, 48, 29))
        self.day_get_sex_birth_meli.setWrapping(False)
        self.day_get_sex_birth_meli.setFrame(True)
        self.day_get_sex_birth_meli.setReadOnly(False)
        self.day_get_sex_birth_meli.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.day_get_sex_birth_meli.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.day_get_sex_birth_meli.setKeyboardTracking(True)
        self.day_get_sex_birth_meli.setMinimum(1)
        self.day_get_sex_birth_meli.setMaximum(31)
        self.day_get_sex_birth_meli.setProperty("value", 10)
        self.day_get_sex_birth_meli.setObjectName("day_get_sex_birth_meli")
        self.month_get_sex_birth_meli = QtWidgets.QSpinBox(parent=self.get_sex_birth_meli)
        self.month_get_sex_birth_meli.setGeometry(QtCore.QRect(210, 230, 48, 29))
        self.month_get_sex_birth_meli.setWrapping(False)
        self.month_get_sex_birth_meli.setFrame(True)
        self.month_get_sex_birth_meli.setReadOnly(False)
        self.month_get_sex_birth_meli.setKeyboardTracking(True)
        self.month_get_sex_birth_meli.setMinimum(1)
        self.month_get_sex_birth_meli.setMaximum(12)
        self.month_get_sex_birth_meli.setProperty("value", 6)
        self.month_get_sex_birth_meli.setObjectName("month_get_sex_birth_meli")
        self.year__get_sex_birth_meli = QtWidgets.QSpinBox(parent=self.get_sex_birth_meli)
        self.year__get_sex_birth_meli.setGeometry(QtCore.QRect(130, 230, 71, 29))
        self.year__get_sex_birth_meli.setWrapping(False)
        self.year__get_sex_birth_meli.setFrame(True)
        self.year__get_sex_birth_meli.setReadOnly(False)
        self.year__get_sex_birth_meli.setKeyboardTracking(True)
        self.year__get_sex_birth_meli.setSuffix("")
        self.year__get_sex_birth_meli.setMinimum(1300)
        self.year__get_sex_birth_meli.setMaximum(1384)
        self.year__get_sex_birth_meli.setProperty("value", 1370)
        self.year__get_sex_birth_meli.setObjectName("year__get_sex_birth_meli")
        self.sex_get_sex_birth_meli = QtWidgets.QComboBox(parent=self.get_sex_birth_meli)
        self.sex_get_sex_birth_meli.setGeometry(QtCore.QRect(240, 290, 82, 28))
        self.sex_get_sex_birth_meli.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.sex_get_sex_birth_meli.setFrame(True)
        self.sex_get_sex_birth_meli.setObjectName("sex_get_sex_birth_meli")
        self.sex_get_sex_birth_meli.addItem("")
        self.sex_get_sex_birth_meli.addItem("")
        self.stackedWidget.addWidget(self.get_sex_birth_meli)
        self.sign_in = QtWidgets.QWidget()
        self.sign_in.setObjectName("sign_in")
        self.label_4 = QtWidgets.QLabel(parent=self.sign_in)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../image/sign_in/Android Small - 11.png"))
        self.label_4.setObjectName("label_4")
        self.pushButt_enter_sign_in = QtWidgets.QPushButton(parent=self.sign_in)
        self.pushButt_enter_sign_in.setGeometry(QtCore.QRect(42, 350, 281, 29))
        self.pushButt_enter_sign_in.setText("")
        self.pushButt_enter_sign_in.setFlat(True)
        self.pushButt_enter_sign_in.setObjectName("pushButt_enter_sign_in")
        self.enter_number_sign_in = QtWidgets.QTextEdit(parent=self.sign_in)
        self.enter_number_sign_in.setGeometry(QtCore.QRect(140, 260, 171, 31))
        self.enter_number_sign_in.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.enter_number_sign_in.setObjectName("enter_number_sign_in")
        self.pushButt_sign_up = QtWidgets.QPushButton(parent=self.sign_in)
        self.pushButt_sign_up.setGeometry(QtCore.QRect(50, 140, 83, 29))
        self.pushButt_sign_up.setText("")
        self.pushButt_sign_up.setFlat(True)
        self.pushButt_sign_up.setObjectName("pushButt_sign_up")
        self.stackedWidget.addWidget(self.sign_in)
        self.get_flname_driver = QtWidgets.QWidget()
        self.get_flname_driver.setObjectName("get_flname_driver")
        self.fname = QtWidgets.QTextEdit(parent=self.get_flname_driver)
        self.fname.setGeometry(QtCore.QRect(70, 230, 221, 31))
        self.fname.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QTextEdit(parent=self.get_flname_driver)
        self.lname.setGeometry(QtCore.QRect(70, 290, 221, 31))
        self.lname.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lname.setObjectName("lname")
        self.pushButt_next_get_flname_driver = QtWidgets.QPushButton(parent=self.get_flname_driver)
        self.pushButt_next_get_flname_driver.setGeometry(QtCore.QRect(30, 360, 281, 29))
        self.pushButt_next_get_flname_driver.setText("")
        self.pushButt_next_get_flname_driver.setFlat(True)
        self.pushButt_next_get_flname_driver.setObjectName("pushButt_next_get_flname_driver")
        self.label_5 = QtWidgets.QLabel(parent=self.get_flname_driver)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../image/flname_driver/Android Small -.png"))
        self.label_5.setObjectName("label_5")
        self.pushButt_back_get_flname_driver = QtWidgets.QPushButton(parent=self.get_flname_driver)
        self.pushButt_back_get_flname_driver.setGeometry(QtCore.QRect(30, 430, 281, 29))
        self.pushButt_back_get_flname_driver.setText("")
        self.pushButt_back_get_flname_driver.setFlat(True)
        self.pushButt_back_get_flname_driver.setObjectName("pushButt_back_get_flname_driver")
        self.label_5.raise_()
        self.fname.raise_()
        self.lname.raise_()
        self.pushButt_next_get_flname_driver.raise_()
        self.pushButt_back_get_flname_driver.raise_()
        self.stackedWidget.addWidget(self.get_flname_driver)
        self.select_driver_user = QtWidgets.QWidget()
        self.select_driver_user.setObjectName("select_driver_user")
        self.label_6 = QtWidgets.QLabel(parent=self.select_driver_user)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../image/select_driver_user/Android Small - 7.png"))
        self.label_6.setObjectName("label_6")
        self.pushButt_select_user = QtWidgets.QPushButton(parent=self.select_driver_user)
        self.pushButt_select_user.setGeometry(QtCore.QRect(40, 270, 281, 61))
        self.pushButt_select_user.setText("")
        self.pushButt_select_user.setFlat(True)
        self.pushButt_select_user.setObjectName("pushButt_select_user")
        self.pushButt_select_driver = QtWidgets.QPushButton(parent=self.select_driver_user)
        self.pushButt_select_driver.setGeometry(QtCore.QRect(40, 370, 281, 61))
        self.pushButt_select_driver.setText("")
        self.pushButt_select_driver.setFlat(True)
        self.pushButt_select_driver.setObjectName("pushButt_select_driver")
        self.pushButt_back_select_driver_user = QtWidgets.QPushButton(parent=self.select_driver_user)
        self.pushButt_back_select_driver_user.setGeometry(QtCore.QRect(40, 480, 281, 31))
        self.pushButt_back_select_driver_user.setText("")
        self.pushButt_back_select_driver_user.setFlat(True)
        self.pushButt_back_select_driver_user.setObjectName("pushButt_back_select_driver_user")
        self.stackedWidget.addWidget(self.select_driver_user)
        self.select_service = QtWidgets.QWidget()
        self.select_service.setObjectName("select_service")
        self.label_11 = QtWidgets.QLabel(parent=self.select_service)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../image/select_service/select_service.png"))
        self.label_11.setObjectName("label_11")
        self.pushButt_baxi_select_service = QtWidgets.QPushButton(parent=self.select_service)
        self.pushButt_baxi_select_service.setGeometry(QtCore.QRect(40, 240, 281, 29))
        self.pushButt_baxi_select_service.setText("")
        self.pushButt_baxi_select_service.setFlat(True)
        self.pushButt_baxi_select_service.setObjectName("pushButt_baxi_select_service")
        self.pushButt_baxi_box_select_service = QtWidgets.QPushButton(parent=self.select_service)
        self.pushButt_baxi_box_select_service.setGeometry(QtCore.QRect(40, 290, 281, 29))
        self.pushButt_baxi_box_select_service.setText("")
        self.pushButt_baxi_box_select_service.setFlat(True)
        self.pushButt_baxi_box_select_service.setObjectName("pushButt_baxi_box_select_service")
        self.pushButt_baxi_bar_select_service = QtWidgets.QPushButton(parent=self.select_service)
        self.pushButt_baxi_bar_select_service.setGeometry(QtCore.QRect(40, 335, 281, 29))
        self.pushButt_baxi_bar_select_service.setText("")
        self.pushButt_baxi_bar_select_service.setFlat(True)
        self.pushButt_baxi_bar_select_service.setObjectName("pushButt_baxi_bar_select_service")
        self.pushButt_baxi_woman_select_service = QtWidgets.QPushButton(parent=self.select_service)
        self.pushButt_baxi_woman_select_service.setGeometry(QtCore.QRect(40, 380, 281, 29))
        self.pushButt_baxi_woman_select_service.setText("")
        self.pushButt_baxi_woman_select_service.setFlat(True)
        self.pushButt_baxi_woman_select_service.setObjectName("pushButt_baxi_woman_select_service")
        self.pushButt_back_select_service = QtWidgets.QPushButton(parent=self.select_service)
        self.pushButt_back_select_service.setGeometry(QtCore.QRect(40, 450, 281, 29))
        self.pushButt_back_select_service.setText("")
        self.pushButt_back_select_service.setFlat(True)
        self.pushButt_back_select_service.setObjectName("pushButt_back_select_service")
        self.stackedWidget.addWidget(self.select_service)
        self.accept_code_sign_up = QtWidgets.QWidget()
        self.accept_code_sign_up.setObjectName("accept_code_sign_up")
        self.label_7 = QtWidgets.QLabel(parent=self.accept_code_sign_up)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../image/send_code/Android Small - 5.png"))
        self.label_7.setObjectName("label_7")
        self.pushButt_accept_sign_up_code = QtWidgets.QPushButton(parent=self.accept_code_sign_up)
        self.pushButt_accept_sign_up_code.setGeometry(QtCore.QRect(30, 300, 291, 41))
        self.pushButt_accept_sign_up_code.setText("")
        self.pushButt_accept_sign_up_code.setFlat(True)
        self.pushButt_accept_sign_up_code.setObjectName("pushButt_accept_sign_up_code")
        self.pushButt_edit_number_sign_up = QtWidgets.QPushButton(parent=self.accept_code_sign_up)
        self.pushButt_edit_number_sign_up.setGeometry(QtCore.QRect(30, 360, 291, 41))
        self.pushButt_edit_number_sign_up.setText("")
        self.pushButt_edit_number_sign_up.setFlat(True)
        self.pushButt_edit_number_sign_up.setObjectName("pushButt_edit_number_sign_up")
        self.stackedWidget.addWidget(self.accept_code_sign_up)
        self.accept_code_sign_in = QtWidgets.QWidget()
        self.accept_code_sign_in.setObjectName("accept_code_sign_in")
        self.label_3 = QtWidgets.QLabel(parent=self.accept_code_sign_in)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../image/send_code/Android Small - 5.png"))
        self.label_3.setObjectName("label_3")
        self.pushButt_accept_sign_in_code = QtWidgets.QPushButton(parent=self.accept_code_sign_in)
        self.pushButt_accept_sign_in_code.setGeometry(QtCore.QRect(30, 300, 291, 41))
        self.pushButt_accept_sign_in_code.setText("")
        self.pushButt_accept_sign_in_code.setFlat(True)
        self.pushButt_accept_sign_in_code.setObjectName("pushButt_accept_sign_in_code")
        self.pushButt_edit_number_sign_in = QtWidgets.QPushButton(parent=self.accept_code_sign_in)
        self.pushButt_edit_number_sign_in.setGeometry(QtCore.QRect(30, 360, 291, 41))
        self.pushButt_edit_number_sign_in.setText("")
        self.pushButt_edit_number_sign_in.setFlat(True)
        self.pushButt_edit_number_sign_in.setObjectName("pushButt_edit_number_sign_in")
        self.stackedWidget.addWidget(self.accept_code_sign_in)
        self.get_photo_meli_certificate_obviously = QtWidgets.QWidget()
        self.get_photo_meli_certificate_obviously.setObjectName("get_photo_meli_certificate_obviously")
        self.label_9 = QtWidgets.QLabel(parent=self.get_photo_meli_certificate_obviously)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../image/get_photo_meli_pcertificate_obviously/get_photo_meli_certificate_obviously.png"))
        self.label_9.setObjectName("label_9")
        self.obviously_get_photo_meli_pcertificate_obviously = QtWidgets.QComboBox(parent=self.get_photo_meli_certificate_obviously)
        self.obviously_get_photo_meli_pcertificate_obviously.setGeometry(QtCore.QRect(130, 390, 191, 28))
        self.obviously_get_photo_meli_pcertificate_obviously.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.obviously_get_photo_meli_pcertificate_obviously.setObjectName("obviously_get_photo_meli_pcertificate_obviously")
        self.obviously_get_photo_meli_pcertificate_obviously.addItem("")
        self.obviously_get_photo_meli_pcertificate_obviously.addItem("")
        self.obviously_get_photo_meli_pcertificate_obviously.addItem("")
        self.obviously_get_photo_meli_pcertificate_obviously.addItem("")
        self.meli_get_photo_meli_certificate_obviously = QtWidgets.QPushButton(parent=self.get_photo_meli_certificate_obviously)
        self.meli_get_photo_meli_certificate_obviously.setGeometry(QtCore.QRect(230, 240, 83, 29))
        self.meli_get_photo_meli_certificate_obviously.setText("")
        self.meli_get_photo_meli_certificate_obviously.setFlat(True)
        self.meli_get_photo_meli_certificate_obviously.setObjectName("meli_get_photo_meli_certificate_obviously")
        self.certificate_get_photo_meli_certificate_obviously = QtWidgets.QPushButton(parent=self.get_photo_meli_certificate_obviously)
        self.certificate_get_photo_meli_certificate_obviously.setGeometry(QtCore.QRect(230, 320, 83, 29))
        self.certificate_get_photo_meli_certificate_obviously.setText("")
        self.certificate_get_photo_meli_certificate_obviously.setFlat(True)
        self.certificate_get_photo_meli_certificate_obviously.setObjectName("certificate_get_photo_meli_certificate_obviously")
        self.pushButt_next_get_photo_meli_certificate_obviously = QtWidgets.QPushButton(parent=self.get_photo_meli_certificate_obviously)
        self.pushButt_next_get_photo_meli_certificate_obviously.setGeometry(QtCore.QRect(40, 440, 271, 29))
        self.pushButt_next_get_photo_meli_certificate_obviously.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButt_next_get_photo_meli_certificate_obviously.setText("")
        self.pushButt_next_get_photo_meli_certificate_obviously.setFlat(True)
        self.pushButt_next_get_photo_meli_certificate_obviously.setObjectName("pushButt_next_get_photo_meli_certificate_obviously")
        self.pushButt_back_get_photo_meli_certificate_obviously = QtWidgets.QPushButton(parent=self.get_photo_meli_certificate_obviously)
        self.pushButt_back_get_photo_meli_certificate_obviously.setGeometry(QtCore.QRect(40, 510, 271, 29))
        self.pushButt_back_get_photo_meli_certificate_obviously.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButt_back_get_photo_meli_certificate_obviously.setText("")
        self.pushButt_back_get_photo_meli_certificate_obviously.setFlat(True)
        self.pushButt_back_get_photo_meli_certificate_obviously.setObjectName("pushButt_back_get_photo_meli_certificate_obviously")
        self.stackedWidget.addWidget(self.get_photo_meli_certificate_obviously)
        self.get_shaba = QtWidgets.QWidget()
        self.get_shaba.setObjectName("get_shaba")
        self.label_10 = QtWidgets.QLabel(parent=self.get_shaba)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_10.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../image/get_shaba/get_shaba.png"))
        self.label_10.setObjectName("label_10")
        self.enter_shaba_number = QtWidgets.QTextEdit(parent=self.get_shaba)
        self.enter_shaba_number.setGeometry(QtCore.QRect(65, 275, 251, 31))
        self.enter_shaba_number.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.enter_shaba_number.setObjectName("enter_shaba_number")
        self.pushButt_next_get_shaba = QtWidgets.QPushButton(parent=self.get_shaba)
        self.pushButt_next_get_shaba.setGeometry(QtCore.QRect(38, 353, 281, 29))
        self.pushButt_next_get_shaba.setText("")
        self.pushButt_next_get_shaba.setFlat(True)
        self.pushButt_next_get_shaba.setObjectName("pushButt_next_get_shaba")
        self.pushButt_back_get_shaba = QtWidgets.QPushButton(parent=self.get_shaba)
        self.pushButt_back_get_shaba.setGeometry(QtCore.QRect(40, 410, 281, 29))
        self.pushButt_back_get_shaba.setText("")
        self.pushButt_back_get_shaba.setFlat(True)
        self.pushButt_back_get_shaba.setObjectName("pushButt_back_get_shaba")
        self.stackedWidget.addWidget(self.get_shaba)
        self.sign_up = QtWidgets.QWidget()
        self.sign_up.setObjectName("sign_up")
        self.label_2 = QtWidgets.QLabel(parent=self.sign_up)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../image/sign_up/Android Small - 8.png"))
        self.label_2.setObjectName("label_2")
        self.pushButt_enter_sign_up = QtWidgets.QPushButton(parent=self.sign_up)
        self.pushButt_enter_sign_up.setGeometry(QtCore.QRect(40, 350, 281, 29))
        self.pushButt_enter_sign_up.setText("")
        self.pushButt_enter_sign_up.setFlat(True)
        self.pushButt_enter_sign_up.setObjectName("pushButt_enter_sign_up")
        self.pushButt_sign_in = QtWidgets.QPushButton(parent=self.sign_up)
        self.pushButt_sign_in.setGeometry(QtCore.QRect(220, 140, 83, 29))
        self.pushButt_sign_in.setText("")
        self.pushButt_sign_in.setFlat(True)
        self.pushButt_sign_in.setObjectName("pushButt_sign_in")
        self.enter_number_sign_up = QtWidgets.QTextEdit(parent=self.sign_up)
        self.enter_number_sign_up.setGeometry(QtCore.QRect(140, 260, 171, 31))
        self.enter_number_sign_up.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.enter_number_sign_up.setObjectName("enter_number_sign_up")
        self.stackedWidget.addWidget(self.sign_up)
        BAXI.setCentralWidget(self.centralwidget)

        self.retranslateUi(BAXI)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(BAXI)

    def retranslateUi(self, BAXI):
        _translate = QtCore.QCoreApplication.translate
        BAXI.setWindowTitle(_translate("BAXI", "MainWindow"))
        self.sex_get_sex_birth_meli.setItemText(0, _translate("BAXI", "آقا"))
        self.sex_get_sex_birth_meli.setItemText(1, _translate("BAXI", "خانم"))
        self.obviously_get_photo_meli_pcertificate_obviously.setItemText(0, _translate("BAXI", "بدون محدودیت"))
        self.obviously_get_photo_meli_pcertificate_obviously.setItemText(1, _translate("BAXI", "ناشنوا"))
        self.obviously_get_photo_meli_pcertificate_obviously.setItemText(2, _translate("BAXI", "ناتوان حرکتی"))
        self.obviously_get_photo_meli_pcertificate_obviously.setItemText(3, _translate("BAXI", "هردو"))
