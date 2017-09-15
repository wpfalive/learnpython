class Map(object):

    def __init__(self, start_scene):
        pass


class Engine(object):

    def __init__(self, scene_map):
        print scene_map
        self.scene_map = scene_map

a_map = Map('central_corridor')
str = "abc"
a_game = Engine(a_map)
b_game = Engine(str)
