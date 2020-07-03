from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyPDF2 import PdfFileReader, PdfFileWriter
import difflib
import os
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(527, 501)
        self.list = QListWidget(Form)
        self.list.setObjectName(u"list")
        self.list.setGeometry(QRect(240, 70, 256, 341))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 241, 41))
        self.label.setStyleSheet(u"font-size: 28px;\n"
                                 "font: 75 22pt \"Consolas\";\n"
                                 "align: center;")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 150, 171, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt Consolas")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt Consolas;")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.start = QSpinBox(self.gridLayoutWidget)
        self.start.setObjectName(u"start")

        self.gridLayout.addWidget(self.start, 0, 1, 1, 1)

        self.end = QSpinBox(self.gridLayoutWidget)
        self.end.setObjectName(u"end")

        self.gridLayout.addWidget(self.end, 1, 1, 1, 1)

        self.select = QPushButton(Form)
        self.select.setObjectName(u"select")
        self.select.setGeometry(QRect(50, 70, 171, 71))
        self.select.setStyleSheet(u"font: 75 15pt \"Consolas\";")
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 250, 171, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add = QPushButton(self.verticalLayoutWidget)
        self.add.setObjectName(u"add")
        self.add.setStyleSheet(u"font: 12px Arial; ")

        self.verticalLayout.addWidget(self.add)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.delete_one = QPushButton(self.verticalLayoutWidget)
        self.delete_one.setObjectName(u"delete_one")
        self.delete_one.setStyleSheet(u"font: 12px Arial;")

        self.verticalLayout.addWidget(self.delete_one)

        self.delete_all = QPushButton(self.verticalLayoutWidget)
        self.delete_all.setObjectName(u"delete_all")
        self.delete_all.setStyleSheet(u"font: 12px Arial;\n"
                                      "")

        self.verticalLayout.addWidget(self.delete_all)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 430, 441, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.out_filename = QLineEdit(self.horizontalLayoutWidget)
        self.out_filename.setObjectName(u"out_filename")
        self.out_filename.setStyleSheet(u"height: 30px;")
        self.out_filename.setMaxLength(30)
        self.out_filename.setReadOnly(False)
        self.out_filename.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.out_filename)

        self.extract = QPushButton(self.horizontalLayoutWidget)
        self.extract.setObjectName(u"extract")
        self.extract.setStyleSheet(u"font: 11pt Consolas;\n"
                                   "height: 30px;")

        self.horizontalLayout.addWidget(self.extract)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate(
            "Form", u"Pdf \u62bd\u53d6 - v2.0", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"PDF extraction", None))
        self.label_3.setText(
            QCoreApplication.translate("Form", u"End page", None))
        self.label_2.setText(QCoreApplication.translate(
            "Form", u"Start page", None))
        self.select.setText(QCoreApplication.translate(
            "Form", u"Select file", None))
        self.add.setText(QCoreApplication.translate(
            "Form", u"Add Record", None))
        self.delete_one.setText(QCoreApplication.translate(
            "Form", u"Delete Record", None))
        self.delete_all.setText(QCoreApplication.translate(
            "Form", u"Delete All Records", None))
        self.out_filename.setPlaceholderText(
            QCoreApplication.translate("Form", u"xxx.pdf", None))
        self.extract.setText(
            QCoreApplication.translate("Form", u"Extract", None))
    # retranslateUi


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('pdf.png'))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.select.clicked.connect(self.select)
        self.ui.add.clicked.connect(self.add_one)
        self.ui.delete_one.clicked.connect(self.delete_one)
        self.ui.delete_all.clicked.connect(self.delete_all)
        self.ui.extract.clicked.connect(self.logout)
        self.ui.start.setMaximum(100000)
        self.ui.end.setMaximum(100000)
        self.ui.start.setMinimum(1)
        self.ui.end.setMinimum(1)
        self.writer = PdfFileWriter()
        self.filename = ''
        self.lst = []

    def select(self):
        file = QFileDialog.getOpenFileName(
            self, 'Select a file', '', 'PDF File(*.pdf)')[0]
        self.filename = file
        self.ui.select.setText(os.path.split(
            file)[-1] if file else 'Select file')

    def add_one(self):
        start = int(self.ui.start.value())
        end = int(self.ui.end.value())
        self.ui.list.addItem(
            f'{os.path.split(self.filename)[-1]} {start}-{end}')
        self.lst.append(f'{self.filename}--{start}-{end}')

    def delete_one(self):
        c = self.ui.list.currentItem()
        self.ui.list.takeItem(self.ui.list.row(c))
        del self.lst[self.ui.list.row(c)]

    def delete_all(self):
        self.ui.list.clear()
        self.lst = []

    def logout(self):
        out = self.ui.out_filename.text()
        for i in range(len(self.lst)):
            text = self.lst[i]
            path = text.split('--')[0]
            start, end = text.split('--')[1].split('-')
            reader = PdfFileReader(open(path, 'rb'))
            if not int(start) > int(end):
                for bbb in range(int(start)-1, int(end)):
                    page = reader.getPage(bbb)
                    self.writer.addPage(page)
            else:
                QMessageBox.information(self, '警告', f'第{i+1}行参数不正确！！！')
                return
        if not out.strip():
            QMessageBox.information(self, '警告', '文件名不正确。导出失败。')
            return
        with open(f'C:/Users/Administrator/Desktop/{out}', 'wb') as pdf:
            self.writer.write(pdf)
            print(difflib.get_close_matches('close', dir(self.writer)))
        self.writer = PdfFileWriter()
        QMessageBox.information(self, '成功', '导出成功！！！')


if __name__ == '__main__':
    a = QApplication([])
    w = Window()
    w.show()
    a.exec_()
