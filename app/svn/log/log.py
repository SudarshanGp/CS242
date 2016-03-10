from path import Path
import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
from bs4 import BeautifulSoup


class Log(object):
    def __init__(self, revision, author, date, msg, paths):
        """
        :param revision: Revision in svn log
        :param author: Author in svn log
        :param date: Date in svn log
        :param msg: Message in svn log
        :param paths: Bs4.element.tag object of paths
        :return:
        """
        self._revision = revision
        self._author = author
        self._date = date
        self._msg = msg
        temp_path = []
        for i, val in enumerate(paths):
            temp_path.append(Path(val['action'],val['kind'], val.text))
        self._paths = temp_path

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)