class reverse_iter:
    def __init__(self, iter_object):
        self.iter_object = iter_object[-1::-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iter_object):
            raise StopIteration
        current_index = self.index
        self.index += 1
        return self.iter_object[current_index]