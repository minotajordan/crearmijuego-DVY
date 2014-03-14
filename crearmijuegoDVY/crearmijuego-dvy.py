# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearmijuego-dvy.ui'
#
# Created: Wed Mar 12 14:16:43 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(757, 392)
        MainWindow.setMinimumSize(QtCore.QSize(757, 392))
        MainWindow.setMaximumSize(QtCore.QSize(757, 392))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #-----------------cargandor barra de progreso
        self.Frame_procentaje_fondo = QtGui.QFrame(self.centralwidget)
        self.Frame_procentaje_fondo.setGeometry(QtCore.QRect(590, 220, 161, 21))
        self.Frame_procentaje_fondo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Frame_procentaje_fondo.setFrameShadow(QtGui.QFrame.Raised)
        self.Frame_procentaje_fondo.setObjectName(_fromUtf8("Frame_procentaje_fondo"))
        self.graphicsView_Frame_procentaje_cargar = QtGui.QGraphicsView(self.Frame_procentaje_fondo)
        self.graphicsView_Frame_procentaje_cargar.setGeometry(QtCore.QRect(0, 0, 0, 21))
        self.graphicsView_Frame_procentaje_cargar.setAutoFillBackground(False)
        self.graphicsView_Frame_procentaje_cargar.setObjectName(_fromUtf8("graphicsView_Frame_procentaje_cargar"))
        self.Label_Frame_procentaje = QtGui.QLabel(self.Frame_procentaje_fondo)
        self.Label_Frame_procentaje.setGeometry(QtCore.QRect(0, 1, 161, 20))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.Label_Frame_procentaje.setFont(font)
        self.Label_Frame_procentaje.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Frame_procentaje.setObjectName(_fromUtf8("Label_Frame_procentaje"))
        #-----------------fin

        self.Lista_Formato_Calidad = QtGui.QListWidget(self.centralwidget)
        self.Lista_Formato_Calidad.setGeometry(QtCore.QRect(590, 30, 161, 181))
        self.Lista_Formato_Calidad.setObjectName(_fromUtf8("Lista_Formato_Calidad"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 240, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 171, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.LineText_Video_Ruta = QtGui.QLineEdit(self.centralwidget)
        self.LineText_Video_Ruta.setGeometry(QtCore.QRect(170, 10, 411, 20))
        self.LineText_Video_Ruta.setText(_fromUtf8(""))
        self.LineText_Video_Ruta.setObjectName(_fromUtf8("LineText_Video_Ruta"))
        self.Label_Descargando_info_total = QtGui.QLabel(self.centralwidget)
        self.Label_Descargando_info_total.setGeometry(QtCore.QRect(10, 270, 741, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_Descargando_info_total.setFont(font)
        self.Label_Descargando_info_total.setObjectName(_fromUtf8("Label_Descargando_info_total"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 300, 741, 41))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.Label_Video_Ruta_Descarga = QtGui.QLabel(self.frame)
        self.Label_Video_Ruta_Descarga.setGeometry(QtCore.QRect(10, 10, 721, 21))
        self.Label_Video_Ruta_Descarga.setObjectName(_fromUtf8("Label_Video_Ruta_Descarga"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 46, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(10, 80, 320, 180))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("https://dl.dropboxusercontent.com/u/70131928/index.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.Label_Video_Titulo = QtGui.QLabel(self.centralwidget)
        self.Label_Video_Titulo.setGeometry(QtCore.QRect(20, 50, 551, 21))
        self.Label_Video_Titulo.setText(_fromUtf8(""))
        self.Label_Video_Titulo.setObjectName(_fromUtf8("Label_Video_Titulo"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(340, 80, 241, 181))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.Label_Video_Autor = QtGui.QLabel(self.frame_2)
        self.Label_Video_Autor.setGeometry(QtCore.QRect(20, 30, 211, 20))
        self.Label_Video_Autor.setText(_fromUtf8(""))
        self.Label_Video_Autor.setObjectName(_fromUtf8("Label_Video_Autor"))
        self.Label_Video_Reproducciones = QtGui.QLabel(self.frame_2)
        self.Label_Video_Reproducciones.setGeometry(QtCore.QRect(20, 80, 211, 16))
        self.Label_Video_Reproducciones.setText(_fromUtf8(""))
        self.Label_Video_Reproducciones.setObjectName(_fromUtf8("Label_Video_Reproducciones"))
        self.Label_Video_Duracion = QtGui.QLabel(self.frame_2)
        self.Label_Video_Duracion.setGeometry(QtCore.QRect(20, 130, 201, 20))
        self.Label_Video_Duracion.setText(_fromUtf8(""))
        self.Label_Video_Duracion.setObjectName(_fromUtf8("Label_Video_Duracion"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 46, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_estado_youtube_link = QtGui.QLabel(self.centralwidget)
        self.Label_estado_youtube_link.setGeometry(QtCore.QRect(600, 0, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_estado_youtube_link.setFont(font)
        self.Label_estado_youtube_link.setObjectName(_fromUtf8("Label_estado_youtube_link"))
        self.Label_Descargando_info_estado = QtGui.QLabel(self.centralwidget)
        self.Label_Descargando_info_estado.setGeometry(QtCore.QRect(560, 350, 191, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label_Descargando_info_estado.setFont(font)
        self.Label_Descargando_info_estado.setObjectName(_fromUtf8("Label_Descargando_info_estado"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuIncio = QtGui.QMenu(self.menubar)
        self.menuIncio.setObjectName(_fromUtf8("menuIncio"))
        self.menuAutor = QtGui.QMenu(self.menubar)
        self.menuAutor.setObjectName(_fromUtf8("menuAutor"))
        MainWindow.setMenuBar(self.menubar)
        self.actionRuta_de_Descarga = QtGui.QAction(MainWindow)
        self.actionRuta_de_Descarga.setObjectName(_fromUtf8("actionRuta_de_Descarga"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionHecho_Por = QtGui.QAction(MainWindow)
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

      #-------------------------------------------------------metodos ---------------------------------------------------------

        def verformatos():
            self.Lista_Formato_Calidad.clear()
            self.Label_estado_youtube_link.setText(str("Cargando..."))
            video = Pafy(str(self.LineText_Video_Ruta.text()))
            streams = video.allstreams
            for s in streams:
                if s.extension=='mp4' or s.extension=='flv' or s.extension=='webm' or s.extension=='3gp' or s.extension=='m4a' or s.resolution=='1920x1080':
                    RR= s.resolution
                    EE = s.extension
                    if EE=='m4a':
                        #print(RR, EE, s.url)
                        self.Lista_Formato_Calidad.addItem(str('Audio' +' '+ 'mp3'))
                    else:
                        if RR=='1920x1080':
                            self.Lista_Formato_Calidad.addItem(str('1920x1080' +' '+ 'mp4'))
                        else:
                            #print(RR, EE, s.url)
                            self.Lista_Formato_Calidad.addItem(str(RR +' '+ EE))

            self.Label_Video_Titulo.setText(str(video.title))
            self.Label_Video_Autor.setText(str(video.author))
            self.Label_Video_Duracion.setText(str(video.duration))
            self.Label_Video_Reproducciones.setText(str(video.viewcount))
            self.Label_estado_youtube_link.setText(str("Formato y Calidad"))
        def cargarenlaceyoutube():
            t = threading.Thread(target=verformatos)
            t.start()

        def mostrar():

            tama=(self.Lista_Formato_Calidad.currentItem().text())
            posfinal=tama.split(' ')
            reso=posfinal[0]
            exten=posfinal[1]
            url=str(self.LineText_Video_Ruta.text())
            # mensaje para Label " Estado de la descarga"
            self.Label_Descargando_info_estado.setText("Preparando Descarga...")
            descargar(url,reso,exten)

        def descargar(url,reso,exten):
        # create a video instance
        # get certain attributes
            videoD = Pafy(url)
            streams = videoD.allstreams
            if reso=='Audio':
                reso='0x0'
                exten='m4a'
            else:
                print()


            for s in streams:
                if s.resolution==reso and s.extension==exten:
                    #archi=s.url
                    #nombre=s.title
                    #e=s.extension
                    best=s
            self.Label_Descargando_info_estado.setText("Descargando...")
            def des(total, recvd, ratio, rate, eta):
                #print(recvd, ratio, eta)
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
                self.Label_Descargando_info_total.setText(str('Peso Total : '+str(tamano_total_MB)+'MB '+' Tiempo : '+str(tiempo)+' Recibido : '+str(cant_descargada_MB)+' MB Velocidad : '+str( round(velocidad_descarga,2) )+' Kbps'))
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
            filename = "" + titulo +"."+ best.extension
            best.download(quiet=False, filepath=filename,callback=des)

            self.Label_Descargando_info_estado.setText("Descarganda completa")

        def descargarenlace():
            t2 = threading.Thread(target=mostrar)
            t2.start()
        def convertirmp3():
            archivomp3 = ["ffmpeg", "-i", "audio.m4a", "-y", "audioconvetido.mp3"]   #convierte a mp3
            subprocess.call(archivomp3)
      # --------------------------------------fin de metodos--------------------------------------------


        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), descargarenlace)
        QtCore.QObject.connect(self.LineText_Video_Ruta, QtCore.SIGNAL(_fromUtf8("returnPressed()")), cargarenlaceyoutube)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.actionHecho_Por, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.show)
        QtCore.QObject.connect(self.actionAyuda, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.show)
        QtCore.QObject.connect(self.actionRuta_de_Descarga, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CrearMiJuego DVY", None))
        self.pushButton.setText(_translate("MainWindow", "Descargar", None))
        self.label_2.setText(_translate("MainWindow", "Url del video youtube", None))
        self.Label_Descargando_info_total.setText(_translate("MainWindow", "Tiempo : ", None))
        self.Label_Video_Ruta_Descarga.setText(_translate("MainWindow", "Sí, no elije la ruta. Por defecto se descargara, en donde se encuentra CrearMiJuegoDVY", None))
        self.label_5.setText(_translate("MainWindow", "Titulo :", None))
        self.label_4.setText(_translate("MainWindow", "Reproducciones :", None))
        self.label_3.setText(_translate("MainWindow", "Autor :", None))
        self.label_6.setText(_translate("MainWindow", "Duracion :", None))
        self.Label_estado_youtube_link.setText(_translate("MainWindow", "Formato y Calidad", None))
        self.Label_Descargando_info_estado.setText(_translate("MainWindow", "Estado de la descarga", None))
        self.Label_Frame_procentaje.setText(_translate("MainWindow", "0%", None))
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
    MainWindow.show()
    sys.exit(app.exec_())