from root import Root

class Setup(Root):
    def __init__(self):
        self.settings = {
            'filter': ['jpg', 'jpeg', 'png', 'tga', 'pcx', 'bmp', 'tif', 'tiff']
        }
        self.texts = {
            'title': 'easy editor',
            'folder': 'Папка',
            'picture': 'картинка',
            'left': 'Влево',
            'right': 'Вправо',
            'mirror':'Зеркало',
            'sharpness':'Резкость',
            'blur':'Размытие',
            'contrast':' Контраст',
            'gray':'Серое',
            'cancel':'Отмена',
            'delete':'Удалить',
            'delete_ok':'Вы уверены, что хотите удалить файл ',
            'save':'Сохранить'
            }
    
    def cfg(self,key):
        if key in self.settings:
            return self.settings[key]
        else:
            return None
    def txt(self,key):
        if key in self.texts:
            return self.texts[key]
        else:
            return 'None'