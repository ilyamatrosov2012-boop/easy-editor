from root import Root
class Controller(Root):
    def __init__(self):
        self.mode = 0
    
    def start(self):
        self.command(('start',))

    def command(self, request):
        cmd = request[0]
        if len(request) == 2:
            arg = request[1]
        else:
            arg = ''

        print(f'команда: {cmd: <20}{arg}')

        if cmd == 'start':
            self.view.stage_00()

        elif cmd == 'press_folder':
            self.view.stage_10()

        elif cmd == 'select_folder':
            self.model.edit.reset()
            self.view.stage_01(self.model.files.find_files(arg))
            self.view.stage_03()

        elif cmd == 'select_file':
            picture = self.model.files.open(arg)
            if picture:
                self.model.edit.set_picture(picture)
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'left':
            if self.model.edit.check_picture():
                self.model.edit.do_left()
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'right':
            if self.model.edit.check_picture():
                self.model.edit.do_right()
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'mirror':
            if self.model.edit.check_picture():
                self.model.edit.do_mirror()
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'sharpness':
            if self.model.edit.check_picture():
                self.model.edit.do_sharp()
                self.view.stage_02(self.model.edit.get_pixmap())
        
        elif cmd == 'contrast':
            if self.model.edit.check_picture():
                self.model.edit.do_contrast()
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'blur':
            if self.model.edit.check_picture():
                self.model.edit.do_blur()
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'gray':
            if self.model.edit.check_picture():
                self.model.edit.do_gray()
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'cancel':
            if self.model.edit.check_picture():
                self.model.edit.cancel()
                self.view.stage_02(self.model.edit.get_pixmap())

        elif cmd == 'delete_ok':
            if self.model.edit.check_picture():
                self.view.stage_11(self.model.files.get_file())

        elif cmd == 'delete':
            self.model.files.delete()
            self.model.edit.reset()
            self.view.stage_01(self.model.files.refresh())
            self.view.stage_03()

        elif cmd == 'save':
            if self.model.edit.check_picture():
                self.model.files.save(self.model.edit.get_picture())
                self.view.stage_01(self.model.files.refresh(), self.model.files.get_file())
                

    