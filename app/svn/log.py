import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')


class Log(object):
    """
    Log class holds information on each entry on subversion's log
    """
    def __init__(self, revision, author, date, msg):
        """
        Initializer function for the Log Class
        :param revision: Revision in svn log
        :param author: Author in svn log
        :param date: Date in svn log
        :param msg: Message in svn log
        :return: New Log Object
        """
        self._revision = revision
        self._author = author
        self._date = date
        self._msg = msg

    @property
    def revision(self):
        """
        Getter function for revision
        :return: Revision
        """
        return self._revision

    @revision.setter
    def revision(self, value):
        """
        Setter function for revision
        :param value: updated revision value
        :return: NA
        """
        self._revision = value

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
    def msg(self):
        """
        Getter function for msg
        :return: msg
        """
        return self._msg

    @msg.setter
    def msg(self, value):
        """
        Setter function for msg
        :param value: updated msg value
        :return: NA
        """
        self._msg = value

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)