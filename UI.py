import sys
import os
import json
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import playsound
import wave
import time


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


form = resource_path("design.ui")
form_class = uic.loadUiType(form)[0]


class Worker(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.audiotime = 0
        self.totaltime = 0

    def run(self):
        begin = time.time()
        os.system(
            f'python {os.path.join(os.getcwd(), "TTS", "bin", "synthesize.py")} --text "{self.parent.text}" --model_path {self.parent.model_path} --config_path {os.path.join(self.parent.path, self.parent.config_name)} --out_path {os.path.join(self.parent.path, self.parent.outfile_name)} --speaker_idx {self.parent.speaker} --language_idx {self.parent.language} '
        )
        end = time.time()
        self.parent.label.setText(
            '<html><head/><body><p align="center"><span style=" font-size:28pt; font-weight:600;">DONE!</span></p></body></html>'
        )

        audio = wave.open(
            os.path.join(self.parent.path, self.parent.outfile_name),
            "rb",
        )
        self.audiotime = audio.getnframes() / audio.getframerate()
        self.totaltime = end - begin
        self.totaltime = round(self.totaltime, 3)
        self.audiotime = round(self.audiotime, 3)

        self.parent.total_t.setText(
            f'<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">total time : {self.totaltime}</span></p></body></html>'
        )
        self.parent.audio_t.setText(
            f'<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">audio time : {self.audiotime}</span></p></body></html>'
        )

        if self.parent.voice_output.isChecked():
            playsound.playsound(
                os.path.join(self.parent.path, self.parent.outfile_name), block=True
            )

        else:
            pass


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.outfile_name = "output"
        self.language_list = []
        self.speaker = ""
        self.language = ""
        self.text = ""
        self.path = ""
        self.config_name = "config.json"
        self.lang_id_name = "language_ids_json"
        self.speak_id_name = "speakers.pth"

        self.setWindowTitle("Coqui TTS Gui For Vits")
        self.button.clicked.connect(self.button_event)
        self.path_button.clicked.connect(self.path_event)

    def button_event(self):
        self.text = self.input_text.text()
        if self.outfiletext.text():
            self.outfile_name = self.outfiletext.text()
        else:
            self.outfile_name = "output"
        if self.outfile_name.split(".")[-1] != "wav":
            self.outfile_name = self.outfile_name + ".wav"
        self.speaker = self.speaker_box.currentText()
        self.language = self.language_box.currentText()
        self.label.setText(
            '<html><head/><body><p align="center"><span style=" font-size:28pt; font-weight:600;">Running...</span></p></body></html>'
        )
        self.total_t.setText(
            f'<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">total time : Running...</span></p></body></html>'
        )
        self.audio_t.setText(
            f'<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">audio time : Running...</span></p></body></html>'
        )

        # synthesis
        work = Worker(self)
        work.start()

    def path_event(self):
        fname = QFileDialog.getOpenFileName(
            self,
            filter="pth file(*.pth)",
            directory=os.getcwd(),
        )
        # if cancle
        if fname == ("", ""):
            return

        self.model_path = fname[0]
        self.path = os.path.dirname(self.model_path)
        if os.path.isfile(self.model_path):
            self.model_name = os.path.basename(self.model_path)

        self.path_label.setText(self.model_path)

        self.speaker_list = []
        self.language_list = []
        self.speaker_box.clear()
        self.language_box.clear()

        with open(
            os.path.join(self.path, self.config_name),
            "r",
            encoding="utf-8",
        ) as f:
            dic = json.load(f)
            for i in dic["datasets"]:
                self.speaker_list.append(i["name"])
                self.language_list.append(i["language"])

        self.speaker_box.addItems(list(set(self.speaker_list)))
        self.language_box.addItems(list(set(self.language_list)))
        self.path_label.setText(self.model_path)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
