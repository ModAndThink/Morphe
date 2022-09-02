"""Put class here"""

from Class.basic_class import *

"""setup fonction"""

def setup(game):
    t = basic_object(game,{},game,"test")
    t.child["entity"] = entity_element(t,{},game,"entity")
