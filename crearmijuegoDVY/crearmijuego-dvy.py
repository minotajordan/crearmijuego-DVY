# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearmijuego-dvy.ui'
#
# Created: Sat Mar  1 11:59:34 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from urllib.request import urlretrieve
import sys
from pafy import Pafy
import threading
import subprocess
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(566, 347)
        #self.Lista_Formato_Calidad = QtGui.QListView(Form)
        #self.Lista_Formato_Calidad.setGeometry(QtCore.QRect(390, 50, 161, 201))
        #self.Lista_Formato_Calidad.setObjectName(_fromUtf8("Lista_Formato_Calidad"))
        self.Lista_Formato_Calidad = QtGui.QListWidget(Form)
        self.Lista_Formato_Calidad.setGeometry(QtCore.QRect(390, 50, 161, 201))
        self.Lista_Formato_Calidad.setObjectName(_fromUtf8("Lista_Formato_Calidad"))
        self.Label_Descargando_info = QtGui.QLabel(Form)
        self.Label_Descargando_info.setGeometry(QtCore.QRect(10, 260, 371, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_Descargando_info.setFont(font)
        self.Label_Descargando_info.setText(_fromUtf8(""))
        self.Label_Descargando_info.setObjectName(_fromUtf8("Label_Descargando_info"))
        self.LineText_Video_Ruta = QtGui.QLineEdit(Form)
        self.LineText_Video_Ruta.setGeometry(QtCore.QRect(140, 10, 411, 20))
        self.LineText_Video_Ruta.setText(_fromUtf8(""))
        self.LineText_Video_Ruta.setObjectName(_fromUtf8("LineText_Video_Ruta"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(390, 260, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 371, 211))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 46, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(210, 150, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(210, 70, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(210, 110, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Label_Video_Titulo = QtGui.QLabel(self.groupBox)
        self.Label_Video_Titulo.setGeometry(QtCore.QRect(20, 40, 341, 20))
        self.Label_Video_Titulo.setText(_fromUtf8(""))
        self.Label_Video_Titulo.setObjectName(_fromUtf8("Label_Video_Titulo"))
        self.Label_Video_Autor = QtGui.QLabel(self.groupBox)
        self.Label_Video_Autor.setGeometry(QtCore.QRect(220, 90, 141, 20))
        self.Label_Video_Autor.setText(_fromUtf8(""))
        self.Label_Video_Autor.setObjectName(_fromUtf8("Label_Video_Autor"))
        self.Label_Video_Reproducciones = QtGui.QLabel(self.groupBox)
        self.Label_Video_Reproducciones.setGeometry(QtCore.QRect(220, 130, 141, 16))
        self.Label_Video_Reproducciones.setText(_fromUtf8(""))
        self.Label_Video_Reproducciones.setObjectName(_fromUtf8("Label_Video_Reproducciones"))
        self.Label_Video_Duracion = QtGui.QLabel(self.groupBox)
        self.Label_Video_Duracion.setGeometry(QtCore.QRect(220, 170, 141, 20))
        self.Label_Video_Duracion.setText(_fromUtf8(""))
        self.Label_Video_Duracion.setObjectName(_fromUtf8("Label_Video_Duracion"))
        self.webView = QtWebKit.QWebView(self.groupBox)
        self.webView.setGeometry(QtCore.QRect(10, 70, 191, 131))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("https://dl.dropboxusercontent.com/u/70131928/index.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 260, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 280, 491, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Label_Video_Ruta_Descarga = QtGui.QLabel(self.groupBox_3)
        self.Label_Video_Ruta_Descarga.setGeometry(QtCore.QRect(10, 15, 461, 21))
        self.Label_Video_Ruta_Descarga.setText(_fromUtf8(""))
        self.Label_Video_Ruta_Descarga.setObjectName(_fromUtf8("Label_Video_Ruta_Descarga"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 290, 51, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 330, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        rutaruta=''

        def verformatos():
            self.Lista_Formato_Calidad.clear()
            self.Label_Descargando_info.setText(str("Cargando..."))
            video = Pafy(str(self.LineText_Video_Ruta.text()))
            streams = video.allstreams
            for s in streams:
                if s.extension=='mp4' or s.extension=='flv' or s.extension=='webm' or s.extension=='3gp' or s.extension=='m4a' or s.resolution=='1920x1080':
                    RR= s.resolution
                    EE = s.extension
                    if EE=='m4a':
                        print(RR, EE, s.url)
                        self.Lista_Formato_Calidad.addItem(str('Audio' +' '+ 'mp3'))
                    else:
                        if RR=='1920x1080':
                            self.Lista_Formato_Calidad.addItem(str('1920x1080' +' '+ 'mp4'))
                        else:
                            print(RR, EE, s.url)
                            self.Lista_Formato_Calidad.addItem(str(RR +' '+ EE))

            self.Label_Video_Titulo.setText(str(video.title))
            self.Label_Video_Autor.setText(str(video.author))
            self.Label_Video_Duracion.setText(str(video.duration))
            self.Label_Video_Reproducciones.setText(str(video.viewcount))
            self.Label_Descargando_info.setText(str(""))
        def hiloverformatos():
            t = threading.Thread(target=verformatos)
            t.start()
        def abrir():
            ventana = Secundaria().exec_()
        def mostrar():
            tama=str(self.Lista_Formato_Calidad.currentItem().text())
            posfinal=tama.split(' ')
            reso=posfinal[0]
            exten=posfinal[1]
            url=str(self.LineText_Video_Ruta.text())
            descargar(url,reso,exten)
            #ruta = subprocess.Popen(['python','des.py',reso,forma,url],shell=True)
            #proc = subprocess.Popen(['python','urldes.py',reso,forma,url], shell=True,stdout=subprocess.PIPE)
            #salida = proc.communicate()[0]
            #print(salida)
            #self.Label_Video_Ruta_Descarga.setText(str(salida))
               #self.Label_Video_Ruta_Descarga.setText(str(line))


        def descargar(url,reso,exten):
        # create a video instance
        # get certain attributes
            videoD = Pafy(url)
            streams = videoD.allstreams
            for s in streams:
                if s.resolution==reso and s.extension==exten:
                    archi=s.url
                    nombre=s.title
                    e=s.mediatype
            #def mycb(total, recvd, raio, rate, eta):
            #   etados = "%.2f" % round(eta,2)
            #  recvddos = "%.2f" % round(((recvd/1024)/1024),2)
            # print ('recibido:'+(str(recvddos))+'Mb','velocidad:'+(str(int(rate)))+'/kbps','tiempo restante:'+(str(etados))+'s')

            def funcionprogreso(bloque, tamano_bloque, tamano_total):
                cant_descargada = bloque * tamano_bloque
                self.Label_Video_Ruta_Descarga.setText(str('\rCantidad descargada: %s bytes / %s bytes totales' % (cant_descargada, tamano_total)))
            resultado=nombre+'.'+e # nombre del archivo y la rutqa tambien
            archivo = urlretrieve(archi, resultado,reporthook=funcionprogreso) # el archi es la ruta del video




        def mostrarhil():
            t2 = threading.Thread(target=mostrar)
            t2.start()

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), mostrarhil)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), abrir)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LineText_Video_Ruta.clear)
        QtCore.QObject.connect(self.LineText_Video_Ruta, QtCore.SIGNAL(_fromUtf8("returnPressed()")), hiloverformatos)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "crearmijuego DVY", None))
        self.label_2.setText(_translate("Form", "Url del video youtube", None))
        self.pushButton.setText(_translate("Form", "Descargar", None))
        self.groupBox.setTitle(_translate("Form", "Información del video", None))
        self.label_5.setText(_translate("Form", "Titulo :", None))
        self.label_6.setText(_translate("Form", "Duracion :", None))
        self.label_3.setText(_translate("Form", "Autor :", None))
        self.label_4.setText(_translate("Form", "Reproducciones :", None))
        self.pushButton_2.setText(_translate("Form", "Salir", None))
        self.groupBox_3.setTitle(_translate("Form", "Ruta de descarga", None))
        self.pushButton_3.setText(_translate("Form", "Ruta", None))
        self.label.setText(_translate("Form", "Hecho por : Luis Francisco ,  www.crearmijuego.com", None))
class Secundaria(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)

    def salir(self):
        exit()

from PyQt4 import QtWebKit
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())