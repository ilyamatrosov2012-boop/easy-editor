from root import Root
from windows import Win_00
from PyQt5.QtWidgets import QMessageBox, QFileDialog

class View(Root):
    def __init__(self):
        self.win_00 = Win_00()
    
    def stage_00(self):
        self.win_00.stage_00()

    def stage_01(self, *arg):
        self.win_00.stage_01(*arg)

    def stage_02(self, *arg):
        self.win_00.stage_02(*arg)

    def stage_03(self, *arg):
        self.win_00.stage_03(*arg)

    def stage_10(self):
        folder = QFileDialog.getExistingDirectory()
        if folder != '':
            self.controller.command(('select_folder', folder))


    def stage_11(self, file ):
        txt = self.setup.txt
        ok = QMessageBox.question(self.win_00, 
                                    txt('delete'),
                                    txt('delete_ok') + '«' + file + '»?',
                                    QMessageBox.Yes | QMessageBox.Cancel,
                                    QMessageBox.Cancel)
        if ok == QMessageBox.Yes:
            self.controller.command(('delete',))

if __name__ == '__main__':
    from root import App

    app = App()
    app.view.stage_00()
    app.exec_() 