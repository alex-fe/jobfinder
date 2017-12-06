class Job(object):

    def __init__(self, data):
        self.__dict__ = data

    def __str__(self):
        print 'nope'
