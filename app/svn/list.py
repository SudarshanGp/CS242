
class List(object):
    def __init__(self, kind, name, commit, author, date):
        self._kind = kind
        self._name = name
        self._commit = commit
        self._author = author
        self._date = date

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def commit(self):
        return self._commit

    @commit.setter
    def commit(self, value):
        self._commit = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)