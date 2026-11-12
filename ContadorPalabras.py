import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras (QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #carga de nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.cliked.connect(self.ContarPalabras)
        
    def ContarPalabras(self):
    #recuperar el texto
    texto= self.edtCaracteres.text()
    print(textoseparado)
    #separar las palabras
    textoseparado=texto.split()
    #
    #
    #
    print("se a presioando el boton")
        
app = QtWidgets.QApplication(sys.argv)
ventana=ContadorPalabras()
ventana.show()
sys.exit(app.exec())