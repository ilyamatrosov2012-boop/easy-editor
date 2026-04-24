from root import Root
import os
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from PyQt5.QtGui import QImage, QPixmap
import re

class Model(Root):
    def __init__(self):
        self.files = self.Files()
        self.edit = self.Edit()

    class Files:
        def __init__(self):
            self.file = ''
            self.work_dir = ''
            self.files_list = []
            self.filter = Model.setup.cfg('filter')
        
        def find_files(self, dir):
            self.work_dir = dir
            self.files_list.clear()
            all_files = os.listdir(self.work_dir)
            for file in all_files:
                for ext in self.filter:
                    if file.endswith('.'+ ext):
                        self.files_list.append(file)
                        break
            return self.files_list

        def open(self, file):
            try:
                self.file = file
                return Image.open(os.path.join(self.work_dir, self.file))
            except:
                return False

        def refresh(self):
            return self.find_files(self.work_dir)
        
        def get_file(self):
            return self.file

        def delete(self):
            if os.path.exists(self.file):
                os.remove(self.file)
                self.file = ''

        def save(self, picture):
            name , extension = os.path.splitext(self.file)
            files = self.find_files(self.work_dir)
            test = re.search('^.*\(\d+\)$',name)
            if test:
                counter_txt = re.findall('\(\d+\)',name)[-1]
                counter_len = len(counter_txt)
                counter = int(counter_txt[1:-1])
                name = name[:-counter_len].rstrip()
                counter += 1
            else:
                counter = 1
            while True:
                name_new = name + ' (' + str(counter) + ')' + extension 
                if name_new in files:
                    counter +=1
                else:
                    break
            picture.save(os.path.join(self.work_dir, name_new))
            

    class Edit:
        def __init__(self):
            self.picture_old = []
            self.reset()

        
        def reset(self):
            self.picture_new = None
            self.picture_old.clear()
        
        def set_picture(self, picture):
            self.picture_new = picture
            self.picture_old.clear()
            self.picture_old.append(picture)
        
        def get_picture(self):
            return self.picture_new

        def check_picture(self):
            if self.picture_new == None:
                return False
            else:
                return True

        def cancel(self):
            if self.picture_old:
                self.picture_new = self.picture_old.pop()

        def backup(self):
            self.picture_old.append(self.picture_new)

        def do_gray(self):
            self.backup()
            self.picture_new = self.picture_new.convert('L')

        def do_left(self):
            self.backup()
            # self.picture_new = self.picture_new.rotate(90)
            self.picture_new = self.picture_new.transpose(Image.ROTATE_90)

        def do_right(self):
            self.backup()
            self.picture_new = self.picture_new.transpose(Image.ROTATE_270)

        def do_mirror(self):
            self.backup()
            self.picture_new = self.picture_new.transpose(Image.FLIP_LEFT_RIGHT)

        def do_blur(self):
            self.backup()
            self.picture_new = self.picture_new.filter(ImageFilter.BLUR)

        def do_contrast(self):
            self.backup()
            self.picture_new = ImageEnhance.Contrast(self.picture_new).enhance(1.5)

        def do_sharp(self):
            self.backup()
            self.picture_new = ImageEnhance.Sharpness(self.picture_new).enhance(3)

        def get_pixmap(self):
            if self.picture_new.mode == 'L' or self.picture_new.mode == 'LA':
                picture_out = self.picture_new.convert('RGBA')

            elif self.picture_new.mode == 'RGB':
                r,g,b = self.picture_new.split()
                picture_out = Image.merge('RGB',(b, g, r)).convert('RGBA')

            elif self.picture_new.mode == 'RGBA':
                r,g,b,a = self.picture_new.split()
                picture_out = Image.merge('RGB',(b, g, r, a)).convert('RGBA')

            elif self.picture_new.mode == 'P':
                picture_out = self.picture_new.convert('RGBA')
                r,g,b,a = self.picture_new.split()
                picture_out = Image.merge('RGB',(b, g, r, a)).convert('RGBA')

            data = picture_out.tobytes('raw', 'RGBA')
            qimage = QImage(data, self.picture_new.size[0], self.picture_new.size[1], QImage.Format_ARGB32)
            pixmap = QPixmap.fromImage(qimage)
            return pixmap

        





if __name__ == '__main__':
    from root import App
    app = App()
    # print(app.model.cards)
    # print(app.model.next())
    print(app.model.notes)
    print(app.model.note)
    # app.model.new_note('куку')
    # app.model.del_note('куку')
    app.model.select_note('куку')
    app.model.save_note('sjkjkfsjk')
