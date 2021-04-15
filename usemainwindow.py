from mainwindow import Ui_DialogMain
import sys, os  # для работы с файлами
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPlainTextEdit


class useMainWindow(Ui_DialogMain):
    def _init(self):
        print('Create main window')
        return

    def SetMainActions(self, application):
        # обработчики
        self.pushButtonOpenFile.clicked.connect(self.OpenFile)
        self.pushButtonSaveFile.clicked.connect(self.SaveFile)

        self.pushButtonC.clicked.connect(self.SetC)
        self.pushButtonPascal.clicked.connect(self.SetPascal)

        self.pushButtonFormat.clicked.connect(self.FormatText)
        self.application = application  # может пригодиться. А может и нет
        self.DefaultName = ""

        return

    def LoadFileToPlainText(self, plaintext):
        fname = self.filename[0]

        statinfo = os.stat(fname)
        size = statinfo.st_size

        if size == 0:
            print("No file")
            return

        f = open(fname, 'r')
        text = f.read()
        plaintext.setPlainText(text)

        f.close()
        return

    def SaveFileFromPlainText(self, plaintext):
        f = open(self.filename[0], 'w')
        text = plaintext.toPlainText()
        f.write(text)
        f.close()
        return

    def OpenFile(self):
        # открыть файл
        print(self.DefaultName)
        if self.DefaultName == "":
            print("Dialog Open")
            q = QFileDialog()
            self.filename = q.getOpenFileName()
        else:
            self.filename = [self.DefaultName]

        # print(self.filename[0])
        self.LoadFileToPlainText(self.plainTextEditSource)
        return

    def SaveFile(self):
        # открыть файл
        if self.DefaultName == "":
            print("Dialog save")
            q = QFileDialog()
            self.filename = q.getSaveFileName()
        else:
            self.filename = [self.DefaultName]

        # print(self.filename[0])

        self.SaveFileFromPlainText(self.plainTextEditTarget)
        return

    def SetC(self):
        print("C Language")
        self.filename = ["c.description"]
        self.LoadFileToPlainText(self.plainTextEditDescription)
        return

    def SetPascal(self):
        print("Pascal Language")
        self.filename = ["pascal.description"]
        self.LoadFileToPlainText(self.plainTextEditDescription)
        return

    ###############################################################
    # правила форматирования
    # ключевое слово begin должно находиться на новой строке
    # отступ увеличивается
    # ключевое слово end должно находиться на новой строке
    # отступ уменьшается
    # ключевые слова for и if
    # оставляют на строке все до endfor/endif и переходят на новую строку
    # отступ для следующей строки увеличивается
    #
    # Описание оформляется в виде
    # ключевое слово = ключевое слово в языке
    # например begin = {
    ###############################################################

    def EncodeDescription(self):
        print("Encode description")
        s = self.plainTextEditDescription.toPlainText()
        # print(s)
        if s == None:
            print("Empty!")
            return
        # вместо mapping используются параллельные списки
        self.keylist = []
        self.valuelist = []

        while s != "":
            # print(s)
            # выделить ключевое слово
            p = s.find(" = ")
            # print("end of key = ",p)
            if p < 0: break  # ошибка в описании или конец файла
            keyword = s[0:p].strip()
            # print("key = ",keyword)
            s = s[p + 3:]
            # print("truncated = ",s)
            # выделить его определение
            p = s.find("\n")
            # print("end of value = ",p)
            keyvalue = s[0:p].strip()
            # print("value = ",keyvalue)
            s = s[p:]
            # добавить в списки
            self.keylist.append(keyword)
            self.valuelist.append(keyvalue)

        # print(self.keylist)
        # print(self.valuelist)

        return

    def IfNewLine(self):
        # print('IfNewLine')
        if self.textOut[len(self.textOut) - 1] != '\n':
            self.textOut += "\r\n"
        return

    def NewLine(self):
        # print('NewLine')
        self.textOut += "\r\n"
        return

    def Tabulate(self):
        # print('Tabulate')
        for i in range(1, self.tab):
            self.textOut += self.tabulation  # нужное количество табуляций
        return

    # найти самый ближний символ из template
    def FindAny(self, template, s):
        if s == "": return -1
        min = -1
        for t in template:
            p = s.find(t)
            if p >= 0 and (min < 0 or p < min): min = p
        return min

    def ApplyFormat(self):
        self.textOut = ""  # с пустого текста
        self.tab = 1  # отступ
        self.tabulation = "  "  # что использовать как табуляцию
        self.textIn += '\n'  # гарантировать наличие конца последней строки

        while self.textIn != "":  # пока не кончится входной текст
            p = self.textIn.find("\n")  # найти конец строки
            if p < 0: break  # досрочный выход
            # print("StrLen = ",p)
            s = self.textIn[0:p]
            s = s.strip()  # выделить строку
            # print("Line = ",s, "p = ",p)

            self.textIn = self.textIn[p + 1:]  # остаток текста
            # print("tabs = ",self.tab)
            self.Tabulate();

            while s != "":  # пока есть что выводить
                # print("tail = ",s)
                # выделить слово

                # p = s.find(" ");
                p = self.FindAny(" ;", s)
                # print(p," in ",s)
                # input()

                if p < 0:  # нет пробела или другого разделителя
                    word = s.strip()
                    s = ""
                    c = " "
                else:
                    word = s[0:p].strip()
                    c = s[p]
                    s = s[p + 1:].strip()

                # print("word = ",word,c)
                # если оно ключевое
                if word.lower() in self.valuelist:
                    k = self.valuelist.index(word.lower())
                else:
                    k = -1
                # print(word, " index = ",k)
                if k < 0:
                    # просто вывести
                    self.textOut += word + c;
                    continue  # while s
                # если это ключевое слово, выполнить специальные действия с ним
                # self.textOut += "<"+self.keylist[k]+">"+" "
                if self.keylist[k] == "begin":  # если это волшебное слово нАчать
                    # print('begin')
                    self.tab += 1
                    self.IfNewLine()
                    self.Tabulate()
                    self.textOut += word + c
                    self.NewLine()
                    self.tab += 1
                    self.Tabulate()

                if self.keylist[k] == "end" or self.keylist[k] == "end." or self.keylist[
                    k] == "end;":  # слово "кончить"
                    # print('end')
                    self.IfNewLine()
                    self.tab -= 1
                    self.Tabulate()
                    self.textOut += word + c
                    self.NewLine()
                    self.tab -= 1
                    self.Tabulate()

                if self.keylist[k] == "for" or self.keylist[k] == "if":
                    # print('for/if')
                    self.NewLine()
                    self.Tabulate()
                    self.textOut += word + c

                if self.keylist[k] == "endfor" or self.keylist[k] == "endif":
                    # print('endfor/endif')
                    self.textOut += word + c
                    # вставить строку
                    self.IfNewLine()
                    # вывести на одну больше чем нужно "табуляций"
                    self.tab += 1
                    self.Tabulate()
                    self.tab -= 1
            self.NewLine()  # новая строка
        return

    def FormatText(self):
        print("Format")
        self.textIn = self.plainTextEditSource.toPlainText()
        self.EncodeDescription()
        self.ApplyFormat()
        self.plainTextEditTarget.setPlainText(self.textOut)
        return
