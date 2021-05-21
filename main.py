class MyIterator:
    def __init__(self, iterable):
        self.object_to_iterate = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.object_to_iterate):
            raise StopIteration('End of iterable object')
        return self.object_to_iterate[self.index]


if __name__ == '__main__':
    elements = [1, 2, 3, 4, 56, 7, 8]
    element = iter(MyIterator(elements))
    print(next(element))
    print(next(element))
    print(next(element))
    print(next(element))
    print(next(element))
    print(next(element))
    print(next(element))
    print(next(element))
