
class List(object):
    """
    List class holds information on each file and directory on subversion's list
    """
    def __init__(self, kind, name, commit, author, date, size):
        """
        Initializes a new List object
        :param kind: Directory or File
        :param name: Name of object
        :param commit: Revision Number
        :param author: Author who wrote this object
        :param date: Date of Commit
        :param size: Size of file
        :return: New List Object
        """
        self._kind = kind
        self._name = name
        self._commit = commit
        self._author = author
        self._date = date
        self._size = size

    @property
    def kind(self):
        """
        Getter function for kind
        :return: kind
        """
        return self._kind

    @kind.setter
    def kind(self, value):
        """
        Setter function for kind
        :param value: updated kind value
        :return: NA
        """
        self._kind = value

    @property
    def name(self):
        """
        Getter function for name
        :return: name
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter function for name
        :param value: updated name value
        :return: NA
        """
        self._name = value

    @property
    def commit(self):
        """
        Getter function for commit
        :return: commit
        """
        return self._commit

    @commit.setter
    def commit(self, value):
        """
        Setter function for commit
        :param value: updated commit value
        :return: NA
        """
        self._commit = value

    @property
    def author(self):
        """
        Getter function for author
        :return: author
        """
        return self._author

    @author.setter
    def author(self, value):
        """
        Setter function for author
        :param value: updated author value
        :return: NA
        """
        self._author = value

    @property
    def date(self):
        """
        Getter function for date
        :return: date
        """
        return self._date

    @date.setter
    def date(self, value):
        """
        Setter function for date
        :param value: updated date value
        :return: NA
        """
        self._date = value

    @property
    def size(self):
        """
        Getter function for size
        :return: size
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter function for size
        :param value: updated size value
        :return: NA
        """
        self._size = value

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)