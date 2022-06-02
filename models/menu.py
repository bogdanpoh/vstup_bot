from models.base import BaseModel


class MenuButton(BaseModel):
    def __init__(self, identifier, text, keyboard=None):
        self.identifier = identifier
        self.text = text
        self.keyboard = keyboard


class MenuAction(BaseModel):
    def __init__(self, identifier=None, text=None, image=None, images=None, keyboard=None):
        self.identifier = identifier
        self.text = text
        self.image = image
        self.images = images
        self.keyboard = keyboard

