import pyglet
import classFile
from Class.dimension import *

class game(pyglet.event.EventDispatcher):
    def __init__(self,position = point2D(0,0),scale = 1):
        self.window = pyglet.window.Window(width = 640,height = 480,fullscreen = False,resizable = True)
        self.camera = position
        self.scale = scale
        self.delta_time = 0

        @self.window.event
        def on_draw():
            self.dispatch_event("start")
            self.dispatch_event("draw")

        def update(delta_time):
            self.dispatch_event("update")
            self.delta_time = delta_time

        self.register_event_type('start')
        self.register_event_type('update')
        self.register_event_type('draw')

        pyglet.clock.schedule_interval(update, 1/60.)

if __name__ == "__main__":
    game = game()
    classFile.setup(game)
    pyglet.app.run()
