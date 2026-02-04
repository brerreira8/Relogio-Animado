from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QColor
import sys

app = QApplication(sys.argv)

# Criar label
label = QLabel()
label.setAlignment(Qt.AlignCenter)
label.resize(400, 150)

# Fonte futurista
label.setFont(QFont("Consolas", 48, QFont.Bold))

# Estilo inicial
label.setStyleSheet("""
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364
    );
    color: #00FFCC;
    border: 2px solid #00FFCC;
    border-radius: 20px;
    padding: 20px;
""")

# Efeito de sombra neon
sombra = QGraphicsDropShadowEffect()
sombra.setBlurRadius(30)
sombra.setColor(QColor("#00FFCC"))
sombra.setOffset(0, 0)
label.setGraphicsEffect(sombra)

# Função para atualizar hora
def atualizar():
    hora = QTime.currentTime().toString("hh:mm:ss")
    label.setText(hora)

    # Animação simples: mudar cor dos segundos
    segundos = QTime.currentTime().second()
    if segundos % 2 == 0:
        label.setStyleSheet("""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364
            );
            color: #00FFCC;
            border: 2px solid #00FFCC;
            border-radius: 20px;
            padding: 20px;
        """)
    else:
        label.setStyleSheet("""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #1a1a1a, stop:1 #333333
            );
            color: #FF00FF;
            border: 2px solid #FF00FF;
            border-radius: 20px;
            padding: 20px;
        """)

# Timer para atualizar a cada segundo
timer = QTimer()
timer.timeout.connect(atualizar)
timer.start(1000)

atualizar()
label.show()
sys.exit(app.exec_())
