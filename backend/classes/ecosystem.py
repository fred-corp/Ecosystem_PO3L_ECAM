class Ecosystem:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)

    def get_index(self, object):
        return self.objects.index(object)

    def get_object_by_coord(self, x, y):
        for object in self.objects:
            if x == object.x and y == object.y:
                return object
