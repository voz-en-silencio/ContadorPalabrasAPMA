import sys
from PyQt5 import QtWidgets,uic

class ContadorPalabras (QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #Carga de nuestra ventana
        uic.loadUi("untitled.ui",self)
        self.btContar.clicked.connect(self.ContarPalabras)
        
    def ContarPalabras (self):
        #Recuperar el texto
        texto = self.edtCaracteres.text()
        print(texto)
        
        textoSeparado = texto.split()
        print(textoSeparado)
        #contar palabras
        cantidadpalabras=len(textoSeparado)
        self.tvPalabras.setText(f"Palabras:{cantidadpalabras}")
        
        #contar caracteres
        totalcaracteres=0
        for palabra in textoSeparado:
            totalcaracteres+=len(palabra)
            totalcaracteres
            self.tvCaracteres.setText(f"caracteres: {totalcaracteres}")
        
        print("Se ha presionado el boton")
        
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras ()
ventana.show()
sys.exit(app.exec())