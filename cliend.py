# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 572)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)
        self.lineEdit_Nome = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Nome.setObjectName("lineEdit_Nome")
        self.gridLayout_3.addWidget(self.lineEdit_Nome, 1, 0, 1, 1)
        self.lineEdit_Medico = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Medico.setObjectName("lineEdit_Medico")
        self.gridLayout_3.addWidget(self.lineEdit_Medico, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 1, 1, 1)
        self.lineEdit_Posto = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Posto.setObjectName("lineEdit_Posto")
        self.gridLayout_3.addWidget(self.lineEdit_Posto, 3, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_3.addWidget(self.dateTimeEdit, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        self.label_Hemacias = QtWidgets.QLabel(self.centralWidget)
        self.label_Hemacias.setObjectName("label_Hemacias")
        self.gridLayout_2.addWidget(self.label_Hemacias, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        self.label_Hemoglobina = QtWidgets.QLabel(self.centralWidget)
        self.label_Hemoglobina.setObjectName("label_Hemoglobina")
        self.gridLayout_2.addWidget(self.label_Hemoglobina, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 3, 1, 1)
        self.label_Hematocrito = QtWidgets.QLabel(self.centralWidget)
        self.label_Hematocrito.setObjectName("label_Hematocrito")
        self.gridLayout_2.addWidget(self.label_Hematocrito, 2, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 3, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 3, 1, 1)
        self.label_VCM = QtWidgets.QLabel(self.centralWidget)
        self.label_VCM.setObjectName("label_VCM")
        self.gridLayout_2.addWidget(self.label_VCM, 3, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 4, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 4, 3, 1, 1)
        self.label_HCM = QtWidgets.QLabel(self.centralWidget)
        self.label_HCM.setObjectName("label_HCM")
        self.gridLayout_2.addWidget(self.label_HCM, 4, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 5, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 5, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 5, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 5, 3, 1, 1)
        self.label_CHCM = QtWidgets.QLabel(self.centralWidget)
        self.label_CHCM.setObjectName("label_CHCM")
        self.gridLayout_2.addWidget(self.label_CHCM, 5, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 2, 1, 1)
        self.pushButton_Hemograma = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Hemograma.setObjectName("pushButton_Hemograma")
        self.gridLayout_2.addWidget(self.pushButton_Hemograma, 6, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)
        self.lineEdit_Leucocitos = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Leucocitos.setObjectName("lineEdit_Leucocitos")
        self.gridLayout.addWidget(self.lineEdit_Leucocitos, 0, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.centralWidget)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 1, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.centralWidget)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)
        self.lineEdit_Basofilos = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Basofilos.setObjectName("lineEdit_Basofilos")
        self.gridLayout.addWidget(self.lineEdit_Basofilos, 2, 1, 1, 1)
        self.label_Basofilos = QtWidgets.QLabel(self.centralWidget)
        self.label_Basofilos.setObjectName("label_Basofilos")
        self.gridLayout.addWidget(self.label_Basofilos, 2, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.lineEdit_Eosinofilos = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Eosinofilos.setObjectName("lineEdit_Eosinofilos")
        self.gridLayout.addWidget(self.lineEdit_Eosinofilos, 3, 1, 1, 1)
        self.label_Eosinofilos = QtWidgets.QLabel(self.centralWidget)
        self.label_Eosinofilos.setObjectName("label_Eosinofilos")
        self.gridLayout.addWidget(self.label_Eosinofilos, 3, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 0, 1, 1)
        self.lineEdit_Mielocitos = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Mielocitos.setObjectName("lineEdit_Mielocitos")
        self.gridLayout.addWidget(self.lineEdit_Mielocitos, 4, 1, 1, 1)
        self.label_Mielocitos = QtWidgets.QLabel(self.centralWidget)
        self.label_Mielocitos.setObjectName("label_Mielocitos")
        self.gridLayout.addWidget(self.label_Mielocitos, 4, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 5, 0, 1, 1)
        self.lineEdit_Metamielocitos = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Metamielocitos.setObjectName("lineEdit_Metamielocitos")
        self.gridLayout.addWidget(self.lineEdit_Metamielocitos, 5, 1, 1, 1)
        self.label_Metamielocitos = QtWidgets.QLabel(self.centralWidget)
        self.label_Metamielocitos.setObjectName("label_Metamielocitos")
        self.gridLayout.addWidget(self.label_Metamielocitos, 5, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 6, 0, 1, 1)
        self.lineEdit_Bastoes = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Bastoes.setObjectName("lineEdit_Bastoes")
        self.gridLayout.addWidget(self.lineEdit_Bastoes, 6, 1, 1, 1)
        self.label_Bastoes = QtWidgets.QLabel(self.centralWidget)
        self.label_Bastoes.setObjectName("label_Bastoes")
        self.gridLayout.addWidget(self.label_Bastoes, 6, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 7, 0, 1, 1)
        self.lineEdit_Segmentados = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Segmentados.setObjectName("lineEdit_Segmentados")
        self.gridLayout.addWidget(self.lineEdit_Segmentados, 7, 1, 1, 1)
        self.label_Segmentados = QtWidgets.QLabel(self.centralWidget)
        self.label_Segmentados.setObjectName("label_Segmentados")
        self.gridLayout.addWidget(self.label_Segmentados, 7, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralWidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 8, 0, 1, 1)
        self.lineEdit_Linfocitos = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Linfocitos.setObjectName("lineEdit_Linfocitos")
        self.gridLayout.addWidget(self.lineEdit_Linfocitos, 8, 1, 1, 1)
        self.label_Linfocitos = QtWidgets.QLabel(self.centralWidget)
        self.label_Linfocitos.setObjectName("label_Linfocitos")
        self.gridLayout.addWidget(self.label_Linfocitos, 8, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 9, 0, 1, 1)
        self.lineEdit_Monocitos = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Monocitos.setObjectName("lineEdit_Monocitos")
        self.gridLayout.addWidget(self.lineEdit_Monocitos, 9, 1, 1, 1)
        self.label_Monocitos = QtWidgets.QLabel(self.centralWidget)
        self.label_Monocitos.setObjectName("label_Monocitos")
        self.gridLayout.addWidget(self.label_Monocitos, 9, 2, 1, 1)
        self.pushButton_Leucocitos = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Leucocitos.setObjectName("pushButton_Leucocitos")
        self.gridLayout.addWidget(self.pushButton_Leucocitos, 10, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_Plaquetas = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Plaquetas.setObjectName("lineEdit_Plaquetas")
        self.horizontalLayout.addWidget(self.lineEdit_Plaquetas)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.pushButton_Imprimir = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Imprimir.setObjectName("pushButton_Imprimir")
        self.horizontalLayout.addWidget(self.pushButton_Imprimir)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.horizontalLayout.setStretch(2, 10)
        self.horizontalLayout.setStretch(4, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 805, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton_Hemograma.clicked.connect(self.GerarEsquerda)
        self.pushButton_Leucocitos.clicked.connect(self.GerarDireita)
        self.pushButton_Imprimir.clicked.connect(self.main)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cliend"))
        self.label_10.setText(_translate("MainWindow", "Nome"))
        self.label_12.setText(_translate("MainWindow", "Médico"))
        self.label_11.setText(_translate("MainWindow", "Posto de Coleta"))
        self.label_13.setText(_translate("MainWindow", "Data"))
        self.label_8.setText(_translate("MainWindow", "Hemacias"))
        self.label_Hemacias.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Hemoglobina"))
        self.label_Hemoglobina.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Hematocrito"))
        self.label_Hematocrito.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "V.C.M"))
        self.label_VCM.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "H.C.M"))
        self.label_HCM.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "C.H.C.M"))
        self.label_CHCM.setText(_translate("MainWindow", "0"))
        self.pushButton_Hemograma.setText(_translate("MainWindow", "Gerar"))
        self.label_16.setText(_translate("MainWindow", "Leucocitos"))
        self.label_41.setText(_translate("MainWindow", "Relativos"))
        self.label_40.setText(_translate("MainWindow", "Absolutos"))
        self.label_17.setText(_translate("MainWindow", "Basofilos"))
        self.label_Basofilos.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Eosinofilos"))
        self.label_Eosinofilos.setText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "Mielocitos"))
        self.label_Mielocitos.setText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "Metamielocitos"))
        self.label_Metamielocitos.setText(_translate("MainWindow", "0"))
        self.label_25.setText(_translate("MainWindow", "Bastoes"))
        self.label_Bastoes.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "Segmentados"))
        self.label_Segmentados.setText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "Linfocitos"))
        self.label_Linfocitos.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "Monocitos"))
        self.label_Monocitos.setText(_translate("MainWindow", "0"))
        self.pushButton_Leucocitos.setText(_translate("MainWindow", "Gerar"))
        self.label.setText(_translate("MainWindow", "Plaquetas"))
        self.pushButton_Imprimir.setText(_translate("MainWindow", "Imprimir"))

    def GerarEsquerda(self):
        hematocrito = int(self.lineEdit.text())
        hemoglobina = hematocrito/3
        hemacias = (hematocrito+4)*100000
        vcm = (hematocrito/hemacias)*10**7
        hcm = (hemoglobina/hemacias)*10**7
        chcm = (hemoglobina/hematocrito)*100
        self.label_Hemacias.setText(str(hemacias))
        self.label_Hematocrito.setText(str(round(hematocrito, 2)))
        self.label_Hemoglobina.setText((str(round(hemoglobina, 2))))
        self.label_VCM.setText(str(round(vcm,0)))
        self.label_HCM.setText(str(round(hcm,0)))
        self.label_CHCM.setText(str(round(chcm,0)))


    def GerarDireita(self):

        leucocitos = int(self.lineEdit_Leucocitos.text())
        basofilos = (leucocitos/100)*int(self.lineEdit_Basofilos.text())
        eosinofilos = (leucocitos / 100) * int(self.lineEdit_Eosinofilos.text())
        mielocitos = (leucocitos / 100) * int(self.lineEdit_Mielocitos.text())
        metamielocitos = (leucocitos / 100) * int(self.lineEdit_Metamielocitos.text())
        bastoes = (leucocitos / 100) * int(self.lineEdit_Bastoes.text())
        segmentados = (leucocitos / 100) * int(self.lineEdit_Segmentados.text())
        linfocitos = (leucocitos / 100) * int(self.lineEdit_Linfocitos.text())
        monocitos = (leucocitos / 100) * int(self.lineEdit_Monocitos.text())

        soma = int(self.lineEdit_Basofilos.text()) + int(self.lineEdit_Eosinofilos.text()) + int(self.lineEdit_Mielocitos.text()) + int(self.lineEdit_Metamielocitos.text())
        soma = soma + int(self.lineEdit_Bastoes.text()) + int(self.lineEdit_Segmentados.text()) + int(self.lineEdit_Linfocitos.text()) + int(self.lineEdit_Monocitos.text())

        if  soma == 100:
            self.label_Basofilos.setText(str(int(basofilos)))
            self.label_Eosinofilos.setText(str(int(eosinofilos)))
            self.label_Mielocitos.setText(str(int(mielocitos)))
            self.label_Metamielocitos.setText(str(int(metamielocitos)))
            self.label_Bastoes.setText(str(int(bastoes)))
            self.label_Segmentados.setText(str(int(segmentados)))
            self.label_Linfocitos.setText(str(int(linfocitos)))
            self.label_Monocitos.setText(str(int(monocitos)))

    def main(self):
        data = self.dateTimeEdit.text().split()
        auxdata = data[0][0]+data[0][1]+"." + data[0][3]+ data[0][4] + "."+ data[0][8] + data [0][9] + "_" + self.lineEdit_Nome.text()
        cnv = canvas.Canvas("Exames/"+ auxdata + ".pdf")
        cnv.setLineWidth(.3)
        width, height = A4
        print("Largura= ", width, "  Altura= ", height)
        cnv.setFont("Helvetica-Bold", 25)
        cnv.drawString(40,790, "CLIEND")
        cnv.setFont("Helvetica", 10)
        cnv.drawString(41, 779, "Clinica e Laboratório Médico")
        cnv.drawString(41, 768, "Matriz: Rua Nascimento Fernandes 1753, Lagoa Nova")
        cnv.drawString(41, 757, "Natal-RN CEP: 59056-280  Tel:(84) 32110772")
        cnv.drawString(350, 757, "Bioquimico de Teste - CRF 0000")
        cnv.line(25, 750, 575, 750)
        cnv.setFont("Helvetica", 12)
        cnv.drawString(41, 710, "Cliente...............:  " + self.lineEdit_Nome.text())
        cnv.drawString(400, 710, "Data: " + self.dateTimeEdit.text())
        cnv.drawString(41, 695, "Posto de Coleta.:  " + self.lineEdit_Posto.text())
        cnv.drawString(41, 680, "Medico...............:  " + self.lineEdit_Medico.text())
        cnv.setFont("Helvetica-Bold", 18)
        cnv.drawString(227, 645, "HEMOGRAMA")
        cnv.setFont("Helvetica", 15)
        cnv.drawString(41, 623, "ERITOGRAMA")
        cnv.line(25, 620, 575, 620)
        cnv.setFont("Helvetica-Oblique", 10)
        cnv.drawString(41, 590, "SÉRIE VERMELHA")
        cnv.drawString(200, 590, "RESULTADOS")
        cnv.drawString(350, 590, "VALORES DE REFERÊNCIA - ADULTO")
        cnv.drawString(350, 572, "HOMEM                              MULHER")
        cnv.setFont("Helvetica", 10)
        cnv.drawString(41, 560, "HEMACIAS..............................")
        cnv.drawString(41, 545, "HEMOGLOBINA......................")
        cnv.drawString(41, 530, "HEMATOCRITO......................")
        cnv.drawString(41, 515, "VCM.........................................")
        cnv.drawString(41, 500, "HCM.........................................")
        cnv.drawString(41, 485, "CHCM......................................")

        cnv.drawString(200, 560, self.label_Hemacias.text())
        cnv.drawString(200, 545, self.label_Hemoglobina.text())
        cnv.drawString(200, 530, self.label_Hematocrito.text())
        cnv.drawString(200, 515, self.label_VCM.text())
        cnv.drawString(200, 500, self.label_HCM.text())
        cnv.drawString(200, 485, self.label_CHCM.text())

        cnv.drawString(260, 560, "/mm3")
        cnv.drawString(260, 545, "g%")
        cnv.drawString(260, 530, "%")
        cnv.drawString(260, 515, "u3")
        cnv.drawString(260, 500, "pg")
        cnv.drawString(260, 485, "%")

        cnv.drawString(350, 560, "4,5 a 6,0 milhões/mm3       4,0 a 5,0 milhões/mm3")
        cnv.drawString(350, 545, "12.8 a 17.5 g%                   12.0 a 16.3 g%")
        cnv.drawString(350, 530, "40 a 50 %                           37 a 45%")
        cnv.drawString(350, 515, "80 a 98 u3                          80 a 98 u3")
        cnv.drawString(350, 500, "25 a 35 pg                          25 a 35 pg")
        cnv.drawString(350, 485, "31 a 36 %                           31 a 36%")

        cnv.setFont("Helvetica", 15)
        cnv.drawString(41, 438, "LEUCOGRAMA")
        cnv.line(25, 435, 575, 435)
        cnv.setFont("Helvetica", 10)
        cnv.drawString(41, 405, "SÉRIE BRANCA")
        cnv.drawString(200, 405, "RESULTADO")
        cnv.drawString(350, 405, "VALOR DE REFERÊNCIA - ADULTO")
        cnv.drawString(41, 385, "LEUCOCITOS..........................")
        cnv.drawString(200, 385, self.lineEdit_Leucocitos.text())
        cnv.drawString(260, 385, "/mm3")
        cnv.drawString(350, 385, "4000 a 10000 /mm3")

        cnv.drawString(41, 335, "BASOFILOS.............................")
        cnv.drawString(41, 320, "EOSINOFILOS.........................")
        cnv.drawString(41, 305, "MIELOCITOS...........................")
        cnv.drawString(41, 290, "METAMIELOCITOS.................")
        cnv.drawString(41, 275, "BASTOES................................")
        cnv.drawString(41, 260, "SEGMENTADOS.....................")
        cnv.drawString(41, 245, "LINFOCITOS............................")
        cnv.drawString(41, 230, "MONOCITOS...........................")

        cnv.drawString(200, 353, "RELATIVOS")
        cnv.drawString(280, 353, "NORMAL")
        cnv.drawString(370, 353, "ABSOLUTOS")
        cnv.drawString(450, 353, "NORMAL")


        cnv.drawString(200, 335, self.lineEdit_Basofilos.text())
        cnv.drawString(200, 320, self.lineEdit_Eosinofilos.text())
        cnv.drawString(200, 305, self.lineEdit_Mielocitos.text())
        cnv.drawString(200, 290, self.lineEdit_Metamielocitos.text())
        cnv.drawString(200, 275, self.lineEdit_Bastoes.text())
        cnv.drawString(200, 260, self.lineEdit_Segmentados.text())
        cnv.drawString(200, 245, self.lineEdit_Linfocitos.text())
        cnv.drawString(200, 230, self.lineEdit_Monocitos.text())

        cnv.drawString(280, 335, "( 0 a 1% )")
        cnv.drawString(280, 320, "( 2 a 4% )")
        cnv.drawString(280, 305, "( 0 a 0% )")
        cnv.drawString(280, 290, "( 0 a 1% )")
        cnv.drawString(280, 275, "( 3 a 5% )")
        cnv.drawString(280, 260, "(50 a 66%)")
        cnv.drawString(280, 245, "(20 a 38%)")
        cnv.drawString(280, 230, "( 4 a 8% )")

        cnv.drawString(370, 335, self.label_Basofilos.text())
        cnv.drawString(370, 320, self.label_Eosinofilos.text())
        cnv.drawString(370, 305, self.label_Mielocitos.text())
        cnv.drawString(370, 290, self.label_Metamielocitos.text())
        cnv.drawString(370, 275, self.label_Bastoes.text())
        cnv.drawString(370, 260, self.label_Segmentados.text())
        cnv.drawString(370, 245, self.label_Linfocitos.text())
        cnv.drawString(370, 230, self.label_Monocitos.text())

        cnv.drawString(450, 335, "( 0 a 80 )")
        cnv.drawString(450, 320, "( 60 a 320 )")
        cnv.drawString(450, 305, "( 0 a 0 )")
        cnv.drawString(450, 290, "( 0 a 80 )")
        cnv.drawString(450, 275, "(120 a 320)")
        cnv.drawString(450, 260, "(3300 a 5200)")
        cnv.drawString(450, 245, "(1200 a 2400)")
        cnv.drawString(450, 230, "(240 a 620)")

        cnv.setFont("Helvetica", 15)
        cnv.drawString(41, 183, "CONTAGEM DE PLAQUETAS")
        cnv.line(25, 180, 575, 180)
        cnv.setFont("Helvetica", 10)

        cnv.drawString(41, 155, "SÉRIE PLAQUETÁRIA")
        cnv.drawString(200, 155, "RESULTADO")
        cnv.drawString(350, 155, "VALOR DE REFERÊNCIA - ADULTO")
        cnv.drawString(41, 135, "PLAQUETAS............................")
        cnv.drawString(200, 135, self.lineEdit_Plaquetas.text())
        cnv.drawString(260, 135, "mm3")
        cnv.drawString(350, 135, "150000 a 400000 mm3")
        cnv.drawString(41, 125, "Obs:")



        cnv.drawString(41, 70, "DATA:____/____/_______ ")

        cnv.line(300, 70, 530, 70)
        cnv.drawString(350, 60, "BIOQUÍMICO RESPONSÁVEL")
        cnv.drawString(332, 50, "Bioquimico de Teste - CRF RN 0000")


        cnv.save()
        return 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

