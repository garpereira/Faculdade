import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        screen_geo = QDesktopWidget().availableGeometry()
        x = (screen_geo.width() - self.width()) / 2
        y = (screen_geo.height() - self.height()) / 2

        self.setGeometry(x, y, 400, 600) #posicao x, y, largura, altura
        self.setWindowTitle('CHATZAO DOS CRIA')

        self.text_IP = QTextEdit(self)
        self.text_IP.setPlaceholderText('Digite o IP Destino')
        self.text_IP.setGeometry(10, 10, 280, 30)

        self.btn_Conectar = QPushButton('Conectar', self)
        self.btn_Conectar.setGeometry(290, 10, 100, 30)
        
        self.text_KEY = QTextEdit(self)
        self.text_KEY.setPlaceholderText('Digite a Chave Cripto')
        self.text_KEY.setGeometry(10, 70, 280, 30)

        self.checkbox_RC4 = QCheckBox('RC4', self)
        self.checkbox_RC4.setGeometry(320, 50, 100, 30)

        self.checkbox_SDES = QCheckBox('SDES', self)
        self.checkbox_SDES.setGeometry(320, 80, 100, 30)

        self.text_MSGCHAT = QTextEdit(self)
        self.text_MSGCHAT.setGeometry(10, 200, 380, 300)

        scrollbar = QScrollBar(self)
        scrollbar.setGeometry(380, 200, 20, 300)
        self.text_MSGCHAT.setVerticalScrollBar(scrollbar)

        self.text_MSG = QTextEdit(self)
        self.text_MSG.setPlaceholderText('Escreva sua mensagem')
        self.text_MSG.setGeometry(10, 540, 280, 30)
        self.text_MSG.installEventFilter(self)

        self.btn_Enviar = QPushButton('Enviar', self)
        self.btn_Enviar.setGeometry(290, 540, 100, 30)
        self.btn_Enviar.clicked.connect(lambda: self.enviar_mensagem())

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and obj is self.text_MSG:
            if event.key() == Qt.Key_Return:
                self.enviar_mensagem()
                return True
            return False
        return False

    def enviar_mensagem(self):
        mensagem = self.text_MSG.toPlainText()
        self.text_MSGCHAT.append(mensagem)
        self.text_MSG.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = mainWindow()
    janela.show()
    sys.exit(app.exec_())