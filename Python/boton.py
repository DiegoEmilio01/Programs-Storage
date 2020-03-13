import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)


class MiBoton(QPushButton):

    def __init__(self, nombre, pos, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador = 0
        self.nombre = nombre
        self.move(*pos)
        self.clicked.connect(self.contar)
        
    def contar(self):
        self.contador += 1
        self.setText(str(self.contador))
        print(f'{self.nombre} apretado {self.contador} veces.')


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        # Fija la geometría de la ventana principal
        self.setGeometry(200, 200, 100, 100)
        self.setMaximumHeight(100)
        self.setMaximumWidth(100)
        
        # Instancia dos botones de nuestra clase, con atributos extra
        # de los que QPushButton está acostumbrado: nombre y posición
        self.boton_1 = MiBoton('Botón 1', (10, 20), '0', self)
        self.boton_2 = MiBoton('Botón 2', (10, 60), '0', self)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())