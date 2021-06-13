class ElementNotFoundException(Exception):

    def __init__(self):
        self.err_msg = 'The item you are looking for is not present in the given array'
