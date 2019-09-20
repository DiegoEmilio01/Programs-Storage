import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class MiVentana(QWidget):
    def __init__(self, nombre, *args):
        super().__init__(*args)
        self.setWindowTitle(nombre)
        self.init_gui()

    def init_gui(self):
        """
        Este método configura la interfaz y todos sus widgets,
        posterior a __init__().
        """
        self.setGeometry(200, 100, 500, 300)

        self.labels = {}
        self.labels['label1'] = QLabel('Texto:', self)
        self.labels['label1'].move(10, 15)
        self.labels['label2'] = QLabel('Aquí se escribe la respuesta', self)
        self.labels['label2'].move(10, 50)

        self.edit1 = QLineEdit('', self)
        self.edit1.setGeometry(70, 15, 100, 20)

        # Agregamos cuadros de texto mediante QLineEdit(texto_inicial, padre)
        self.boton1 = QPushButton('&Procesar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(5, 70)

        self.show()


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana_1 = MiVentana("ventana_cuadro_label")
    sys.exit(app.exec_())