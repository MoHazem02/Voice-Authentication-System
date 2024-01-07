from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget
from ApplicationManager import *


class Ui_Voice_Recognizer(object):
    def setupUi(self, Voice_Recognizer):
        Voice_Recognizer.setObjectName("Voice_Recognizer")
        Voice_Recognizer.resize(1321, 799)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Fingerprint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Voice_Recognizer.setWindowIcon(icon)
        Voice_Recognizer.setStyleSheet("background-color: #1e1e2f;\n"
"color:white;")
        self.gridLayout_2 = QtWidgets.QGridLayout(Voice_Recognizer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Voice_Recognizer)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Voice_Recognizer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Start_Recording_Button = QtWidgets.QPushButton(self.groupBox, clicked = lambda: MAESTRO.record_voice())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_Recording_Button.sizePolicy().hasHeightForWidth())
        self.Start_Recording_Button.setSizePolicy(sizePolicy)
        self.Start_Recording_Button.setMinimumSize(QtCore.QSize(143, 29))
        self.Start_Recording_Button.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Start_Recording_Button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Start_Recording_Button.setFont(font)
        self.Start_Recording_Button.setStyleSheet("background-color:#3366ff;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Assets/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Recording_Button.setIcon(icon1)
        self.Start_Recording_Button.setIconSize(QtCore.QSize(20, 20))
        self.Start_Recording_Button.setObjectName("Start_Recording_Button")
        self.gridLayout_5.addWidget(self.Start_Recording_Button, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Input_Speech_Label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Input_Speech_Label.setFont(font)
        self.Input_Speech_Label.setObjectName("Input_Speech_Label")
        self.verticalLayout.addWidget(self.Input_Speech_Label)
        self.Input_Speech_Space_Label = QtWidgets.QLabel(self.groupBox)
        self.Input_Speech_Space_Label.setMinimumSize(QtCore.QSize(350, 85))
        self.Input_Speech_Space_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.Input_Speech_Space_Label.setText("")
        self.Input_Speech_Space_Label.setObjectName("Input_Speech_Space_Label")
        self.verticalLayout.addWidget(self.Input_Speech_Space_Label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Access_Label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Access_Label.setFont(font)
        self.Access_Label.setObjectName("Access_Label")
        self.verticalLayout_3.addWidget(self.Access_Label)
        self.Access_Icon_Label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Access_Icon_Label.sizePolicy().hasHeightForWidth())
        self.Access_Icon_Label.setSizePolicy(sizePolicy)
        self.Access_Icon_Label.setMinimumSize(QtCore.QSize(80, 75))
        self.Access_Icon_Label.setText("")
        self.Access_Icon_Label.setObjectName("Access_Icon_Label")
        self.verticalLayout_3.addWidget(self.Access_Icon_Label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.Spectrogram = MplWidget(self.frame_2)
        self.Spectrogram.setObjectName("Spectrogram")
        self.gridLayout_4.addWidget(self.Spectrogram, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Security_Voice_Code_RadioButton = QtWidgets.QRadioButton(self.groupBox_2, clicked= lambda: MAESTRO.switch_modes(False))
        self.Security_Voice_Code_RadioButton.setChecked(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Security_Voice_Code_RadioButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Assets/Unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Security_Voice_Code_RadioButton.setIcon(icon2)
        self.Security_Voice_Code_RadioButton.setIconSize(QtCore.QSize(45, 45))
        self.Security_Voice_Code_RadioButton.setObjectName("Security_Voice_Code_RadioButton")
        self.horizontalLayout_3.addWidget(self.Security_Voice_Code_RadioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.Security_Voice_Fingerprint_RadioButton = QtWidgets.QRadioButton(self.groupBox_2, clicked= lambda: MAESTRO.switch_modes(True))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Security_Voice_Fingerprint_RadioButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Assets/fingerprint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Security_Voice_Fingerprint_RadioButton.setIcon(icon3)
        self.Security_Voice_Fingerprint_RadioButton.setIconSize(QtCore.QSize(45, 45))
        self.Security_Voice_Fingerprint_RadioButton.setObjectName("Security_Voice_Fingerprint_RadioButton")
        self.horizontalLayout_3.addWidget(self.Security_Voice_Fingerprint_RadioButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Hazem_CheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Hazem_CheckBox.setFont(font)
        self.Hazem_CheckBox.setObjectName("Hazem_CheckBox")
        self.horizontalLayout_4.addWidget(self.Hazem_CheckBox)
        self.Omar_CheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Omar_CheckBox.setFont(font)
        self.Omar_CheckBox.setObjectName("Omar_CheckBox")
        self.horizontalLayout_4.addWidget(self.Omar_CheckBox)
        self.Ahmed_CheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Ahmed_CheckBox.setFont(font)
        self.Ahmed_CheckBox.setObjectName("Ahmed_CheckBox")
        self.horizontalLayout_4.addWidget(self.Ahmed_CheckBox)
        self.Youssef_CheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Youssef_CheckBox.setFont(font)
        self.Youssef_CheckBox.setObjectName("Youssef_CheckBox")
        self.horizontalLayout_4.addWidget(self.Youssef_CheckBox)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 2, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.Grant_Me_Access_ProgressBar = QtWidgets.QProgressBar(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Grant_Me_Access_ProgressBar.setFont(font)
        self.Grant_Me_Access_ProgressBar.setProperty("value", 0)
        self.Grant_Me_Access_ProgressBar.setObjectName("Grant_Me_Access_ProgressBar")
        self.verticalLayout_5.addWidget(self.Grant_Me_Access_ProgressBar)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.Open_Middle_Door_ProgressBar = QtWidgets.QProgressBar(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Open_Middle_Door_ProgressBar.setFont(font)
        self.Open_Middle_Door_ProgressBar.setProperty("value", 0)
        self.Open_Middle_Door_ProgressBar.setObjectName("Open_Middle_Door_ProgressBar")
        self.verticalLayout_6.addWidget(self.Open_Middle_Door_ProgressBar)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.Release_Entrance_Key_ProgressBar = QtWidgets.QProgressBar(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Release_Entrance_Key_ProgressBar.setFont(font)
        self.Release_Entrance_Key_ProgressBar.setProperty("value", 0)
        self.Release_Entrance_Key_ProgressBar.setObjectName("Release_Entrance_Key_ProgressBar")
        self.verticalLayout_7.addWidget(self.Release_Entrance_Key_ProgressBar)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.gridLayout_8.addLayout(self.verticalLayout_8, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem6, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.Hazem_ProgressBar = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Hazem_ProgressBar.setFont(font)
        self.Hazem_ProgressBar.setProperty("value", 0)
        self.Hazem_ProgressBar.setObjectName("Hazem_ProgressBar")
        self.verticalLayout_9.addWidget(self.Hazem_ProgressBar)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem7)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.Omar_ProgressBar = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Omar_ProgressBar.setFont(font)
        self.Omar_ProgressBar.setProperty("value", 0)
        self.Omar_ProgressBar.setObjectName("Omar_ProgressBar")
        self.verticalLayout_10.addWidget(self.Omar_ProgressBar)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem8)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.Ahmed_ProgressBar = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Ahmed_ProgressBar.setFont(font)
        self.Ahmed_ProgressBar.setProperty("value", 0)
        self.Ahmed_ProgressBar.setObjectName("Ahmed_ProgressBar")
        self.verticalLayout_11.addWidget(self.Ahmed_ProgressBar)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem9)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setScaledContents(False)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.Youssef_ProgressBar = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Youssef_ProgressBar.setFont(font)
        self.Youssef_ProgressBar.setProperty("value", 0)
        self.Youssef_ProgressBar.setObjectName("Youssef_ProgressBar")
        self.verticalLayout_12.addWidget(self.Youssef_ProgressBar)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setScaledContents(False)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.label_12)
        self.progressBar_8 = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_8.setFont(font)
        self.progressBar_8.setProperty("value", 0)
        self.progressBar_8.setObjectName("progressBar_8")
        self.verticalLayout_14.addWidget(self.progressBar_8)
        self.verticalLayout_18.addLayout(self.verticalLayout_14)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem10)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setScaledContents(False)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_15.addWidget(self.label_14)
        self.progressBar_9 = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_9.setFont(font)
        self.progressBar_9.setProperty("value", 0)
        self.progressBar_9.setObjectName("progressBar_9")
        self.verticalLayout_15.addWidget(self.progressBar_9)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem11)
        self.verticalLayout_18.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(False)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.progressBar_10 = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_10.setFont(font)
        self.progressBar_10.setProperty("value", 0)
        self.progressBar_10.setObjectName("progressBar_10")
        self.verticalLayout_16.addWidget(self.progressBar_10)
        self.verticalLayout_18.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem12)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setScaledContents(False)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_17.addWidget(self.label_15)
        self.progressBar_11 = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_11.setFont(font)
        self.progressBar_11.setProperty("value", 0)
        self.progressBar_11.setObjectName("progressBar_11")
        self.verticalLayout_17.addWidget(self.progressBar_11)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.horizontalLayout_5.addLayout(self.verticalLayout_18)
        self.gridLayout_9.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(Voice_Recognizer)
        QtCore.QMetaObject.connectSlotsByName(Voice_Recognizer)

    def retranslateUi(self, Voice_Recognizer):
        _translate = QtCore.QCoreApplication.translate
        Voice_Recognizer.setWindowTitle(_translate("Voice_Recognizer", "Voice_Recognizer"))
        self.label.setText(_translate("Voice_Recognizer", "Voice Recognition Authentication System"))
        self.groupBox.setTitle(_translate("Voice_Recognizer", "Voice Recording"))
        self.Start_Recording_Button.setText(_translate("Voice_Recognizer", "Start Recording"))
        self.Input_Speech_Label.setText(_translate("Voice_Recognizer", "Input Speech"))
        self.Access_Label.setText(_translate("Voice_Recognizer", "Access"))
        self.label_6.setText(_translate("Voice_Recognizer", "Spectrogram"))
        self.groupBox_2.setTitle(_translate("Voice_Recognizer", "Security Modes"))
        self.Security_Voice_Code_RadioButton.setText(_translate("Voice_Recognizer", "Security Voice Code"))
        self.Security_Voice_Fingerprint_RadioButton.setText(_translate("Voice_Recognizer", "Security Voice Fingerprint"))
        self.Hazem_CheckBox.setText(_translate("Voice_Recognizer", "Hazem"))
        self.Omar_CheckBox.setText(_translate("Voice_Recognizer", "Omar"))
        self.Ahmed_CheckBox.setText(_translate("Voice_Recognizer", "Ahmed"))
        self.Youssef_CheckBox.setText(_translate("Voice_Recognizer", "Youssef"))
        self.groupBox_3.setTitle(_translate("Voice_Recognizer", "Sentences Matching"))
        self.label_2.setText(_translate("Voice_Recognizer", "Grant Me Access"))
        self.label_3.setText(_translate("Voice_Recognizer", "Open Middle Door"))
        self.label_7.setText(_translate("Voice_Recognizer", "Release Entrance Key"))
        self.groupBox_4.setTitle(_translate("Voice_Recognizer", "Persons Matching"))
        self.label_10.setText(_translate("Voice_Recognizer", "Hazem"))
        self.label_9.setText(_translate("Voice_Recognizer", "Omar"))
        self.label_8.setText(_translate("Voice_Recognizer", "Ahmed"))
        self.label_11.setText(_translate("Voice_Recognizer", "Youssef"))
        self.label_12.setText(_translate("Voice_Recognizer", "Person5"))
        self.label_14.setText(_translate("Voice_Recognizer", "Person6"))
        self.label_13.setText(_translate("Voice_Recognizer", "Person7"))
        self.label_15.setText(_translate("Voice_Recognizer", "Person8"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Voice_Recognizer = QtWidgets.QWidget()
    ui = Ui_Voice_Recognizer()
    ui.setupUi(Voice_Recognizer)
    MAESTRO = ApplicationManger(ui)
    # MAESTRO.create_database()
    MAESTRO.switch_modes(False)
    Voice_Recognizer.show()
    sys.exit(app.exec_())
