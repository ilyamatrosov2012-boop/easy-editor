from PyQt5.QtWidgets import QApplication 

class Root:
    pass

class App(QApplication,Root):
    def __init__(self):
        QApplication.__init__(self,[])
        from model import Model
        from view import View
        from controller import Controller 
        from setup import Setup

        Root.setup = Setup()
        Root.model = Model()
        Root.controller = Controller()
        Root.view = View()

        