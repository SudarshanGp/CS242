class Path(object):
    def __init__(self, action, kind, file):
        """
        Initializer for Path class
        :param action: Type of that was the result of this path entyr
        :param kind: Kind of file affected by this path
        :param file: File name that is associated with this path
        :return:  NA
        """
        self._action = action
        self._kind = kind
        self._file = file

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = value

    @property
    def file(self):
        return self._action

    @file.setter
    def file(self, value):
        self._file = value

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)