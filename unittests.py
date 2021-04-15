from usemainwindow import useMainWindow
from PyQt5.QtWidgets import QMessageBox


class unitTest():
    def _init(self):
        print('Create main window')
        return

    def run(self, ui):
        print("run tests")
        try:
            self.TestOpenFile(ui)

            # self.TestSetC(ui)
            self.TestSetPascal(ui)
            self.TestFormatText(ui)

            self.TestSaveFile(ui)

        except AssertionError as ae:
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle('Не пройден тест')
            print(ae)
            mb.setText(str(ae))
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec()
        return

    def TestOpenFile(self, ui):
        ui.DefaultName = "Demo.pas"
        ui.OpenFile()

        text0 = 'program Demo;' + '\n' + \
                'var i:integer;' + '\n' + \
                'begin i:=0;' + '\n' + \
                'for i:=1 to 100 do begin k:=i+1; if a<b then a:=b; end;' + '\n' + \
                'end.' + '\n'
        assert text0 == ui.plainTextEditSource.toPlainText(), "Исходный текст заменен"
        return

    def TestSaveFile(self, ui):
        ui.DefaultName = "DemoFormatted.pas"
        ui.SaveFile()

        # загрузить обратно
        ui.OpenFile()
        # и проверить
        assert ui.plainTextEditSource.toPlainText() == ui.plainTextEditTarget.toPlainText(), "Не сохранился"
        return

    def TestSetC(self, ui):
        ui.SetC()
        text0 = 'begin = {' + '\n' + \
                'end = }' + '\n' + \
                'end. = }' + '\n' + \
                'end; = };' + '\n' + \
                'for = for' + '\n' + \
                'endfor = )' + '\n' + \
                'if = if' + '\n' + \
                'endif = )' + '\n'
        text = ui.plainTextEditDescription.toPlainText()
        # print(text)
        assert text0 == text, "Описание С"
        return

    def TestSetPascal(self, ui):
        ui.SetPascal()
        text0 = \
            'begin = begin' + '\n' + \
            'end = end' + '\n' + \
            'end. = end.' + '\n' + \
            'end; = end;' + '\n' + \
            'for = for' + '\n' + \
            'if = if' + '\n' + \
            'endif = then' + '\n' + \
            'endfor = do' + '\n'

        text = ui.plainTextEditDescription.toPlainText()
        assert text0 == text, "Описание Pascal"
        return

    def TestFormatText(self, ui):
        ui.FormatText()

        text0 = \
            'program Demo;' + '\n' + \
            'var i:integer;' + '\n' + \
            '  begin ' + '\n' + \
            '    i:=0;' + '\n' + \
            '    ' + '\n' + \
            '    for i:=1 to 100 do ' + '\n' + \
            '      ' + '\n' + \
            '      begin ' + '\n' + \
            '        k:=i+1;' + '\n' + \
            '        if a<b then ' + '\n' + \
            '          a:=b;' + '\n' + \
            '      end;' + '\n' + \
            '    ' + '\n' + \
            '    ' + '\n' + \
            '  end. ' + '\n' + \
            '' + '\n' + \
            '' + '\n'
        text = ui.plainTextEditTarget.toPlainText()
        assert text0 == text, "Форматирование"
        return
