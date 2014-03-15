# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearmijuego-dvy.ui'
#
# Created: Fri Mar 14 17:46:08 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pafy import Pafy
import threading
import subprocess
import os
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1028, 611)
        MainWindow.setMinimumSize(QtCore.QSize(1028, 611))
        MainWindow.setMaximumSize(QtCore.QSize(1028, 611))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #00569F"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///home/cesar/documentos/youtube/index.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(675, 220, 81, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.Label_Video_Duracion = QtGui.QLabel(self.centralwidget)
        self.Label_Video_Duracion.setGeometry(QtCore.QRect(650, 240, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Video_Duracion.setFont(font)
        self.Label_Video_Duracion.setStyleSheet(_fromUtf8("Color:rgb(255, 255, 255)"))
        self.Label_Video_Duracion.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Video_Duracion.setObjectName(_fromUtf8("Label_Video_Duracion"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(685, 180, 41, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_Descargar = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Descargar.setGeometry(QtCore.QRect(660, 470, 101, 23))
        self.pushButton_Descargar.setStyleSheet(_fromUtf8("background-color: #00B1EB"))
        self.pushButton_Descargar.setObjectName(_fromUtf8("pushButton_Descargar"))
        self.Lista_Formato_Calidad = QtGui.QListWidget(self.centralwidget)
        self.Lista_Formato_Calidad.setGeometry(QtCore.QRect(650, 280, 118, 151))
        self.Lista_Formato_Calidad.setStyleSheet(_fromUtf8("background-color: white"))
        self.Lista_Formato_Calidad.setObjectName(_fromUtf8("Lista_Formato_Calidad"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(690, 140, 41, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.Label_Video_Autor = QtGui.QLabel(self.centralwidget)
        self.Label_Video_Autor.setGeometry(QtCore.QRect(650, 160, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Video_Autor.setFont(font)
        self.Label_Video_Autor.setStyleSheet(_fromUtf8("Color:rgb(255, 255, 255)"))
        self.Label_Video_Autor.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Video_Autor.setObjectName(_fromUtf8("Label_Video_Autor"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(660, 440, 100, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.Label_Video_Reproducciones = QtGui.QLabel(self.centralwidget)
        self.Label_Video_Reproducciones.setGeometry(QtCore.QRect(650, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Video_Reproducciones.setFont(font)
        self.Label_Video_Reproducciones.setStyleSheet(_fromUtf8("Color:rgb(255, 255, 255)"))
        self.Label_Video_Reproducciones.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Video_Reproducciones.setObjectName(_fromUtf8("Label_Video_Reproducciones"))
        self.pushButton_Descargar_Cancelar = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Descargar_Cancelar.setGeometry(QtCore.QRect(660, 500, 101, 26))
        self.pushButton_Descargar_Cancelar.setStyleSheet(_fromUtf8("background-color: #00B1EB"))
        self.pushButton_Descargar_Cancelar.setObjectName(_fromUtf8("pushButton_Descargar_Cancelar"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(650, 260, 111, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_11.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.widget_fondo_detalle_descarga = QtGui.QWidget(self.centralwidget)
        self.widget_fondo_detalle_descarga.setGeometry(QtCore.QRect(0, 570, 1031, 21))
        self.widget_fondo_detalle_descarga.setStyleSheet(_fromUtf8("background-color: #00B1EB"))
        self.widget_fondo_detalle_descarga.setObjectName(_fromUtf8("widget_fondo_detalle_descarga"))
        self.Label_Descargando_info_estado = QtGui.QLabel(self.widget_fondo_detalle_descarga)
        self.Label_Descargando_info_estado.setGeometry(QtCore.QRect(10, 0, 1011, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 177, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Label_Descargando_info_estado.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_Descargando_info_estado.setFont(font)
        self.Label_Descargando_info_estado.setStyleSheet(_fromUtf8("Color:rgb(255, 255, 255)"))
        self.Label_Descargando_info_estado.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Descargando_info_estado.setObjectName(_fromUtf8("Label_Descargando_info_estado"))
        self.widget_2_fondo_ruta_descarga = QtGui.QWidget(self.centralwidget)
        self.widget_2_fondo_ruta_descarga.setGeometry(QtCore.QRect(0, 550, 1031, 21))
        self.widget_2_fondo_ruta_descarga.setStyleSheet(_fromUtf8("background-color: #0090D7"))
        self.widget_2_fondo_ruta_descarga.setObjectName(_fromUtf8("widget_2_fondo_ruta_descarga"))
        self.Label_Video_Ruta_Descarga = QtGui.QLabel(self.widget_2_fondo_ruta_descarga)
        self.Label_Video_Ruta_Descarga.setGeometry(QtCore.QRect(10, 0, 1011, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_Video_Ruta_Descarga.setFont(font)
        self.Label_Video_Ruta_Descarga.setStyleSheet(_fromUtf8("Color:rgb(255, 255, 255)"))
        self.Label_Video_Ruta_Descarga.setObjectName(_fromUtf8("Label_Video_Ruta_Descarga"))
        self.widget_fondo_detalle_descarga_3 = QtGui.QWidget(self.centralwidget)
        self.widget_fondo_detalle_descarga_3.setGeometry(QtCore.QRect(770, 0, 4, 551))
        self.widget_fondo_detalle_descarga_3.setStyleSheet(_fromUtf8("background-color: #0090D7"))
        self.widget_fondo_detalle_descarga_3.setObjectName(_fromUtf8("widget_fondo_detalle_descarga_3"))
        self.widget_2_fondo_ruta_descarga_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2_fondo_ruta_descarga_2.setGeometry(QtCore.QRect(0, 530, 1031, 21))
        self.widget_2_fondo_ruta_descarga_2.setStyleSheet(_fromUtf8("background-color: #0090D7"))
        self.widget_2_fondo_ruta_descarga_2.setObjectName(_fromUtf8("widget_2_fondo_ruta_descarga_2"))
        self.Label_Descargando_info_total = QtGui.QLabel(self.widget_2_fondo_ruta_descarga_2)
        self.Label_Descargando_info_total.setGeometry(QtCore.QRect(10, 0, 1011, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_Descargando_info_total.setFont(font)
        self.Label_Descargando_info_total.setStyleSheet(_fromUtf8("Color:rgb(255, 255, 255)"))
        self.Label_Descargando_info_total.setObjectName(_fromUtf8("Label_Descargando_info_total"))
        self.widget_fondo_detalle_descarga_4 = QtGui.QWidget(self.widget_2_fondo_ruta_descarga_2)
        self.widget_fondo_detalle_descarga_4.setGeometry(QtCore.QRect(0, 20, 1031, 2))
        self.widget_fondo_detalle_descarga_4.setStyleSheet(_fromUtf8("background-color: #00B1EB"))
        self.widget_fondo_detalle_descarga_4.setObjectName(_fromUtf8("widget_fondo_detalle_descarga_4"))
        self.pushButton_reproducir_video = QtGui.QPushButton(self.centralwidget)
        self.pushButton_reproducir_video.setGeometry(QtCore.QRect(660, 25, 101, 23))
        self.pushButton_reproducir_video.setStyleSheet(_fromUtf8("background-color: #00B1EB"))
        self.pushButton_reproducir_video.setObjectName(_fromUtf8("pushButton_reproducir_video"))
        self.Label_Video_Audio = QtGui.QLabel(self.centralwidget)
        self.Label_Video_Audio.setGeometry(QtCore.QRect(10, 390, 641, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Video_Audio.setFont(font)
        self.Label_Video_Audio.setStyleSheet(_fromUtf8("Color:rgb(255, 255, 255)"))
        self.Label_Video_Audio.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Video_Audio.setObjectName(_fromUtf8("Label_Video_Audio"))
        self.widget_2_fondo_ruta_descarga_3 = QtGui.QWidget(self.centralwidget)
        self.widget_2_fondo_ruta_descarga_3.setGeometry(QtCore.QRect(3, 28, 645, 365))
        self.widget_2_fondo_ruta_descarga_3.setStyleSheet(_fromUtf8("background-color: #0090D7"))
        self.widget_2_fondo_ruta_descarga_3.setObjectName(_fromUtf8("widget_2_fondo_ruta_descarga_3"))
        self.web_cargarlink = QtWebKit.QWebView(self.widget_2_fondo_ruta_descarga_3)
        self.web_cargarlink.setGeometry(QtCore.QRect(2, 2, 640, 360))
        self.web_cargarlink.setUrl(QtCore.QUrl(_fromUtf8("https://dl.dropboxusercontent.com/u/70131928/index.html")))
        self.web_cargarlink.setObjectName(_fromUtf8("web_cargarlink"))
        self.Lista_Reproducir = QtGui.QListWidget(self.centralwidget)
        self.Lista_Reproducir.setGeometry(QtCore.QRect(650, 50, 118, 91))
        self.Lista_Reproducir.setStyleSheet(_fromUtf8("background-color: white"))
        self.Lista_Reproducir.setObjectName(_fromUtf8("Lista_Reproducir"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 23))
        self.menubar.setStyleSheet(_fromUtf8("background-color: #0090D7"))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuIncio = QtGui.QMenu(self.menubar)
        self.menuIncio.setStyleSheet(_fromUtf8(""))
        self.menuIncio.setObjectName(_fromUtf8("menuIncio"))
        self.menuAutor = QtGui.QMenu(self.menubar)
        self.menuAutor.setStyleSheet(_fromUtf8(""))
        self.menuAutor.setObjectName(_fromUtf8("menuAutor"))
        MainWindow.setMenuBar(self.menubar)
        self.actionRuta_de_Descarga = QtGui.QAction(MainWindow)
        self.actionRuta_de_Descarga.setObjectName(_fromUtf8("actionRuta_de_Descarga"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionHecho_Por = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionHecho_Por.setFont(font)
        self.actionHecho_Por.setObjectName(_fromUtf8("actionHecho_Por"))
        self.actionAyuda = QtGui.QAction(MainWindow)
        self.actionAyuda.setObjectName(_fromUtf8("actionAyuda"))
        self.menuIncio.addAction(self.actionRuta_de_Descarga)
        self.menuIncio.addSeparator()
        self.menuIncio.addAction(self.actionSalir)
        self.menuAutor.addAction(self.actionHecho_Por)
        self.menuAutor.addSeparator()
        self.menuAutor.addAction(self.actionAyuda)
        self.menubar.addAction(self.menuIncio.menuAction())
        self.menubar.addAction(self.menuAutor.menuAction())


        def ingresar_url(url,poster,op_video_audio):
            f = open("link.html","w")
            f.write("<!DOCTYPE html>\n")
            f.write("<html lang='es'>\n")
            f.write(" <head>\n")
            f.write("        <title></title>\n")
            f.write("  <link href='video-js.css' rel='stylesheet' type='text/css'>\n")
            f.write("  <script src='video.js'></script>\n")
            f.write("  <script>\n")
            f.write("    videojs.options.flash.swf = 'video-js.swf';\n")
            f.write("  </script>\n")
            f.write(" </head>\n")

            f.write("<body>\n")
            f.write("  <"+op_video_audio+" id='example_video_1' class='video-js vjs-default-skin' autoplay controls preload='none' width='640' height='360'\n")
            f.write("      poster='"+poster+"'\n")
            if op_video_audio=='audio':
                f.write("      data-setup='{}' style='top:160px; left:160px;'>\n")
            else:
                f.write("      data-setup='{}'>\n")
            f.write(" <source src='")
            f.write(url)
            f.write("' type='"+op_video_audio+"/webm'></"+op_video_audio+">\n")
            f.write("    </body>\n")
            f.write("</html>\n")
            f.close()



        def reproducir_video():
            self.Lista_Reproducir.clear()
            self.Lista_Formato_Calidad.clear()
            lista_reproduccion_get.clear()
            lista_titulos_get.clear()

            hola = self.webView.page().mainFrame().documentElement()
            usuario = hola.findFirst("#linkyoutube")
            url = usuario.attribute('value')
            self.Label_Descargando_info_estado.setText('Cargando Lista...')
            t2 = threading.Thread(target=sacarvideo,args=(url,'mp4','video'))
            t2.start()
            #sacarvideo(url,'mp4','video')

         # SACA LA RUTA DE LINK,  INICIO
        def rutaget():
            if 'win32' in sistema() or 'win64' in sistema():
                print("windows no implementado, por el momento")
                return ''
            if 'linux' in sistema():
                ruta_pwd = subprocess.Popen('pwd',stdout=subprocess.PIPE)
                salida = ruta_pwd.communicate()[0]
                salida_cadena = ''+str(salida)
                ruta = salida_cadena[2:-3]
                return ruta
        # SACA LA RUTA DE LINK,   FIN

        # lista para almacenar las urls de la reproduccion INICIO
        lista_reproduccion_get = {}
        lista_titulos_get = {}
        # lista para almacenar las urls de la reproduccion FIN
        def lista_reproduccion(index):
            # opcion -> thumb - url
            if index=='Audio':
                lista_almacenar = lista_reproduccion_get[index]

                sacar_url_poster = (str(lista_almacenar)).split()
                poster= sacar_url_poster[0]
                url_video=sacar_url_poster[1]
                titulo = str(lista_titulos_get[index])
                ingresar_url(url_video,poster,'audio')
                self.web_cargarlink.setUrl(QtCore.QUrl(("file://"+rutaget()+"/link.html")))
                self.Label_Video_Audio.setText('Reproduciendo en Audio : '+titulo)
            else:
                lista_reproduccion_get[index]
                lista_almacenar = lista_reproduccion_get[index]

                sacar_url_poster = (str(lista_almacenar)).split()
                poster= sacar_url_poster[0]
                url_video=sacar_url_poster[1]
                titulo = str(lista_titulos_get[index])
                ingresar_url(url_video,poster,'video')
                self.web_cargarlink.setUrl(QtCore.QUrl(("file://"+rutaget()+"/link.html")))
                self.Label_Video_Audio.setText('[''] Reproduciendo en Video : '+titulo)
        #almacenar stream
        def sacarvideo(url,opc,op_video_audio):
            self.video = Pafy(url)
            streams = self.video.allstreams
            for s in streams:

                #cargar a la lista de reproduccion
                if (s.extension=='m4a' and s.quality=='128k') or (s.extension=='mp4' and s.resolution=='1280x720') or (s.extension=='mp4' and s.resolution=='640x360') or (s.extension=='flv' and s.resolution=='320x240') or (s.extension=='3gp' and s.resolution=='176x144'):
                    RR= s.resolution
                    EE = s.extension
                    miniimagen = self.video.thumb

                    if EE=='m4a':
                        lista_reproduccion_get['Audio']=(miniimagen)+' '+(s.url)
                        lista_titulos_get['Audio']=str(self.video.title)
                        self.Lista_Reproducir.addItem(str('Audio'))
                    else:
                        lista_reproduccion_get[RR]=(miniimagen)+' '+(s.url)
                        lista_titulos_get[RR]=str(self.video.title)
                        self.Lista_Reproducir.addItem(str(RR))

                # cargar a la lista el formato y calidad
                if s.extension=='mp4' or s.extension=='flv' or s.extension=='webm' or s.extension=='3gp' or s.extension=='m4a' or s.resolution=='1920x1080':
                    RR= s.resolution
                    EE = s.extension
                    if EE=='m4a':
                        self.Lista_Formato_Calidad.addItem(str('Audio' +' '+ 'mp3'))
                    else:
                        if RR=='1920x1080':
                            self.Lista_Formato_Calidad.addItem(str('1920x1080' +' '+ 'mp4'))
                        else:
                            self.Lista_Formato_Calidad.addItem(str(RR +' '+ EE))

            self.Label_Video_Autor.setText(str(self.video.author))
            self.Label_Video_Duracion.setText(str(self.video.duration))
            self.Label_Video_Reproducciones.setText(str(self.video.viewcount))
            self.Label_Descargando_info_estado.setText('Lista Cargada de '+self.video.title)

#========================================= PARA DESCARGAR INICIO===============================================

        def mostrar():

            tama=(self.Lista_Formato_Calidad.currentItem().text())
            posfinal=tama.split(' ')
            reso=posfinal[0]
            exten=posfinal[1]
            # mensaje para Label " Estado de la descarga"
            self.Label_Descargando_info_total.setText("Preparando Descarga...")
            descargar('',reso,exten)

        def descargar(url,reso,exten):

            streams = self.video.allstreams

            if reso=='Audio':
                reso='0x0'
                exten='m4a'
                resolucion_mostrar = reso
            else:
                resolucion_mostrar=''


            for s in streams:
                if s.resolution==reso and s.extension==exten:
                    best=s

            def des(total, recvd, ratio, rate, eta):
                velocidad_descarga=rate
                cantidad_descargado=recvd
                tiempo_faltante=eta
                tota_peso=total
                porcentaje=ratio
                tiempo_faltante_s=abs(int(tiempo_faltante%60))
                tiempo_faltante_m=abs(int( (tiempo_faltante/60)%60 ))
                tiempo_faltante_h=abs(int(tiempo_faltante/3600))

                tiempo=str(tiempo_faltante_h)+'H '+str(tiempo_faltante_m)+'M '+str(tiempo_faltante_s)+'S'
                tamano_total_MB = round(((tota_peso/1024)/1024),2)
                cant_descargada_MB = round(((cantidad_descargado/1024)/1024),2)
                if resolucion_mostrar=='0x0':
                    self.Label_Descargando_info_total.setText(str('P: '+str(tamano_total_MB)+'MB - T : '+str(tiempo)+' - R : '+str(cant_descargada_MB)+' MB - V : '+str( round(velocidad_descarga,2) )+' Kbps'+' Descag.. [Audio mp3] '+ titulo))
                else:
                    self.Label_Descargando_info_total.setText(str('P: '+str(tamano_total_MB)+'MB - T : '+str(tiempo)+' - R : '+str(cant_descargada_MB)+' MB - V : '+str( round(velocidad_descarga,2) )+' Kbps'+' Descag.. ['+reso+']['+exten+'] '+ titulo))

            titulo = best.title
            titulo = str(titulo).replace('.','')
            titulo = str(titulo).replace('"','')
            titulo = str(titulo).replace(':','')
            titulo = str(titulo).replace('_','')
            titulo = str(titulo).replace('-','')
            titulo = str(titulo).replace(';','')
            titulo = str(titulo).replace('|','')
            titulo = str(titulo).replace("'",'')
            titulo = str(titulo).replace("+",'')
            titulo = str(titulo).replace("!",'')
            titulo = str(titulo).replace("/",'')
            titulo = str(titulo).replace("\\",'')
            titulo = str(titulo).replace("*",'')
            titulo = str(titulo).replace("#",'')
            titulo = str(titulo).replace("%",'')
            titulo = str(titulo).replace("&",'')
            titulo = str(titulo).replace("(",'')
            titulo = str(titulo).replace(")",'')
            titulo = str(titulo).replace("?",'')
            titulo = str(titulo).replace("多",'')
            titulo = str(titulo).replace("臓",'')
            titulo = str(titulo).replace("[",'')
            titulo = str(titulo).replace("]",'')
            titulo = str(titulo).replace("{",'')
            titulo = str(titulo).replace("}",'')
            titulo = str(titulo).replace("=",'')
            titulo = str(titulo).replace("~",'')
            titulo = str(titulo).replace("<",'')
            titulo = str(titulo).replace(">",'')
            if 'win32' in sistema() or 'win64' in sistema():
                print("windows no implementado, por el momento")
            if 'linux' in sistema():
                filename = rutaget() + '/descargas/' + titulo +"."+ best.extension

            best.download(quiet=False, filepath=filename,callback=des)
            self.Label_Descargando_info_total.setText("Descarganda completa....")

        def descargarenlace():
            t2 = threading.Thread(target=mostrar)
            t2.start()
        def descargarcancelar():
            borrar = 'borrar borrando'
#========================================= PARA DESCARGAR FIN===============================================


#========================================= PARA SABER QUE PLATAFORMA ES INICIO===============================================
        def sistema():
            return sys.platform
#========================================= PARA SABER QUE PLATAFORMA ES FIN===============================================
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.actionHecho_Por, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.show)
        QtCore.QObject.connect(self.actionAyuda, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.show)
        QtCore.QObject.connect(self.actionRuta_de_Descarga, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.show)
        QtCore.QObject.connect(self.web_cargarlink, QtCore.SIGNAL(_fromUtf8("loadProgress(int)")), self.progressBar.setValue)
        QtCore.QObject.connect(self.pushButton_Descargar, QtCore.SIGNAL(_fromUtf8("clicked()")), descargarenlace)
        QtCore.QObject.connect(self.pushButton_Descargar_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), descargarcancelar)
        QtCore.QObject.connect(self.pushButton_reproducir_video, QtCore.SIGNAL(_fromUtf8("clicked()")), reproducir_video)
        QtCore.QObject.connect(self.Lista_Reproducir, QtCore.SIGNAL(_fromUtf8("currentTextChanged(QString)")),lista_reproduccion)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CrearMiJuego DVY", None))
        self.label_9.setText(_translate("MainWindow", "Duración", None))
        self.Label_Video_Duracion.setText(_translate("MainWindow", "", None))
        self.label_8.setText(_translate("MainWindow", "Visto", None))
        self.pushButton_Descargar.setText(_translate("MainWindow", "Descargar", None))
        self.Lista_Formato_Calidad.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "Autor", None))
        self.Label_Video_Autor.setText(_translate("MainWindow", "", None))
        self.Label_Video_Reproducciones.setText(_translate("MainWindow", "", None))
        self.pushButton_Descargar_Cancelar.setText(_translate("MainWindow", "Cancelar", None))
        self.label_11.setText(_translate("MainWindow", "Formato y Calidad", None))
        self.Label_Descargando_info_estado.setText(_translate("MainWindow", "Detalle", None))
        self.Label_Video_Ruta_Descarga.setText(_translate("MainWindow", "Sí, no elije la ruta. Por defecto se descargara, en donde se encuentra CrearMiJuegoDVY", None))
        self.Label_Descargando_info_total.setText(_translate("MainWindow", "Informacion Descarga", None))
        self.pushButton_reproducir_video.setText(_translate("MainWindow", "Cargar", None))
        self.Label_Video_Audio.setText(_translate("MainWindow", "Reproduciendo", None))
        self.Lista_Reproducir.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.menuIncio.setTitle(_translate("MainWindow", "Incio", None))
        self.menuAutor.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionRuta_de_Descarga.setText(_translate("MainWindow", "Ruta de Descarga", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionHecho_Por.setText(_translate("MainWindow", "Hecho Por", None))
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda", None))

from PyQt4 import QtWebKit
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.webView.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
    ui.web_cargarlink.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
    MainWindow.show()
    sys.exit(app.exec_())