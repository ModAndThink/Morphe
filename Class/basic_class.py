import pyglet
from Class.dimension import *

class basic_object(object):
    def __init__(self, parent, child, game, name = "object"):
        self.parent = parent
        self.child = child
        self.name = name
        self.game = game

class entity_element(basic_object):
    def __init__(self, parent, child, game, name = "object", position = point2D(0,0), image = None, size = size2D(100,100)):
        super().__init__(parent, child, game, name)

        self.position = position
        self.image = None
        self.size = size
        self.basic_size = size

        try:
            self.image = pyglet.image.load(image)
        except:
            print("image not found")
            self.image = pyglet.image.load("Images/NotFound.png")
        
        self.sprite = pyglet.sprite.Sprite(self.image)

        def draw():
            self.game.push_handlers(start)
            self.game.push_handlers(update)
            
            self.sprite.scale = self.game.scale
            self.sprite.draw()

        def start():
            pass

        def update():
            pass

        self.game.push_handlers(draw)
