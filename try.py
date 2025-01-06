from PyQt5.QtCore import QObject, QMetaObject, Qt
from PyQt5.QtWidgets import QApplication, QLabel
import threading
import time

class Worker(QObject):
    def do_work(self):
        print("Worker thread:", threading.current_thread().name)
        QMetaObject.invokeMethod(self, "update_ui", Qt.QueuedConnection)

    def update_ui(self):
        print("Main thread (UI update):", threading.current_thread().name)
        label.setText("Updated from worker thread!")

app = QApplication([])

label = QLabel("Initial text")
label.show()

worker = Worker()

# 在子线程中触发事件
thread = threading.Thread(target=worker.do_work)
thread.start()

app.exec_()