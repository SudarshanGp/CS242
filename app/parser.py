#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from svn.log import Log

sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
from bs4 import BeautifulSoup
import subprocess
from svn.list import List
from dateutil import parser


class Parser(object):

    def __init__(self, list_path, log_path, pull):
        """
        __init__ gets information for svn_list and svn_log from subversion by calling a subprocess
        it then parses the svn_list and svn_log information and returns the data to calling function
        :type pull: Checks whether we need to call subversion for files
        :param log_path: svn_log file path
        :param list_path: svn_list file path
        """
        if pull is True:
            cmd = \
                'svn list --xml --recursive https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/ > ' \
                + list_path + ';' \
                'svn log --verbose --xml https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/ > ' \
                + log_path + ';'
            p = subprocess.Popen(cmd, shell=True)
            p.wait()

        svn_list = self.soup_file(list_path)
        svn_log = self.soup_file(log_path)
        svn_list = self.parse_list(svn_list)
        svn_log = self.parse_log(svn_log)
        self._svn_list = svn_list
        self._svn_log = svn_log

    @property
    def svn_list(self):
        """
        Getter function for svn_list
        :return: size
        """
        return self._svn_list

    @svn_list.setter
    def svn_list(self, value):
        """
        Setter function for svn_list
        :param value: updated svn_list value
        :return: NA
        """
        self._svn_list = value

    @property
    def svn_log(self):
        """
        Getter function for svn_log
        :return: size
        """
        return self._svn_log

    @svn_log.setter
    def svn_log(self, value):
        """
        Setter function for svn_list
        :param value: updated svn_list value
        :return: NA
        """
        self._svn_log = value

    def soup_file(self, file_name):
        """
        soup_file takes in a file path and uses BeautifulSoup to return a parsed representation of the file
        :param file_name: File Path to the file to be run BeautifulSoup on
        :return: Returns a BeautifulSoup object
        """
        data = open(file_name)
        formatted = BeautifulSoup(data, 'lxml')
        return formatted

    def parse_list_file(self, list_data):
        """
        parse_list_file takes svn list_data and parses it into a dictionary of List objects
        :param list_data: svn list_data that is a BeautifulSoup object
        :return: Returns a dictionary that maps file names to List objects
        """
        data = {}

        for elem in list_data.findAll('entry'):
            kind = elem['kind']
            name = str(elem.find('name').text)
            commit = int(elem.commit['revision'])
            author = str(elem.commit.author.text)
            date = parser.parse(elem.commit.date.text)
            if elem.find('size'):
                size = int(elem.find('size').text)
            else:
                size = 0
            data[name] = List(
                kind,
                name,
                commit,
                author,
                date,
                size,
            )
        return data

    def parse_list_directory(self, data, hierarchy):
        """
        parse_list_directory takes in svn_list data and hierarchy and initializes all the directories that
        exist in svn_list into hierarchy
        :param data: svn list_data that is a BeautifulSoup object
        :param hierarchy: Dictionary of directories and files that exist on subversion
        :return: updates hierarchy that contains directory information
        """
        for (key, value) in data.iteritems():
            temp = hierarchy['root']
            paths = value.name.split('/')
            if 'dir' in value.kind:
                for (k, val) in enumerate(paths):
                    if k == len(paths) - 1:

                        # if its the last entry and it is a directory,
                        # we need to create an info entry to hold its list information
                        # and we need to create an emtpy children list

                        if any(d['text'] == val for d in
                               temp['nodes']):  # if the directory exists but it does not have an info value
                            match = next((d for d in temp['nodes']
                                          if d['text'] == val), None)
                            match['tags'] = ['Version : '
                                             + str(value.commit), 'Date : '
                                             + value.date.strftime("%Y-%m-%d %H:%M")]
                            match['href'] = \
                                'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' \
                                + value.name
                        else:
                            temp_insert = {
                                'text': val,
                                'tags': ['Version : ' + str(value.commit),
                                         'Date : ' + value.date.strftime("%Y-%m-%d %H:%M")],
                                'nodes': [],
                                'href': 'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' \
                                        + value.name,
                            }
                            temp['nodes'].append(temp_insert)  # look for the current directory and insert it into chidlren
                    elif any(d['text'] == val for d in temp['nodes']):
                        match = next((d for d in temp['nodes'] if d['text']
                                      == val), None)
                        temp = match
                    elif not any(d['text'] == val for d in temp['nodes']):
                        temp_insert = {
                            'text': val,
                            'tags': [],
                            'nodes': [],
                            'href': '',
                        }
                        temp['nodes'].append(temp_insert)
                        match = next((d for d in temp['nodes'] if d['text']
                                      == val), None)
                        temp = match
        return hierarchy

    def parse_list_files(self, data, hierarchy):
        """
        parse_list_directory takes in svn_list data and hierarchy and initializes all the files that
        exist in svn_list into hierarchy
        :param data: svn list_data that is a BeautifulSoup object
        :param hierarchy: Dictionary of directories and files that exist on subversion
        :return: updates hierarchy that contains file information
        """
        for (key, value) in data.iteritems():
            temp = hierarchy['root']
            paths = value.name.split('/')
            if 'file' in value.kind:
                for (k, val) in enumerate(paths):
                    if k == len(paths) - 1:
                        file_name = val.split('.')
                        if len(file_name) > 1:
                            extension = file_name[-1]
                        else:
                            extension = ''

                        # if its the last entry and it is a file,
                        # we need to update the children with a file entry

                        temp_insert = {'text': val, 'tags': ['Version : '
                                                             + str(value.commit), 'Date : '
                                                             + value.date.strftime("%Y-%m-%d %H:%M"),
                                                             'Size : ' + str(value.size),
                                                             'Type : ' + extension],
                                       'url': 'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' \
                                              + value.name}
                        temp['nodes'].append(temp_insert)  # look for the current directory and insert it into chidlren
                    elif any(d['text'] == val for d in temp['nodes']):

                        # Still looking for the right directory

                        match = next((d for d in temp['nodes'] if d['text']== val), None)
                        temp = match

        hierarchy['root']['nodes'] = sorted(hierarchy['root']['nodes'],
                                            key=lambda k: k['text'])
        return hierarchy

    def parse_list(self, list_data):
        """
        parse_list_file takes svn list_data and parses it to return a directory representation of the files
        and directories on subversion
        :param list_data:  svn list_data that is a BeautifulSoup object
        :return: hierarchy that contains file and directory information
        """
        data = self.parse_list_file(list_data)
        hierarchy = {'root': {}}
        hierarchy['root']['info'] = '/'
        hierarchy['root']['nodes'] = []
        hierarchy = self.parse_list_directory(data, hierarchy)
        hierarchy = self.parse_list_files(data, hierarchy)

        return hierarchy

    def parse_log(self,file):
        """
        Maps file name to its different log information : revision number, author, message, date
        :param file: BeautifulSoup object of the svn log file
        :return: Dictionary of file log data
        """

        data = {}
        for elem in file.findAll('logentry'):
            revision = int(elem['revision'])
            author = elem.author.text
            date = parser.parse(elem.date.text).strftime('%m/%d/%Y %H:%M')
            msg = elem.msg.text
            for path in elem.findAll('path'):
                name = path.text
                if name in data.keys():  # if file has appeared before
                    curr_list = data[name]
                    curr_list.append(Log(revision, author, date, msg))
                    data[name] = curr_list
                else:
                    curr_list = [Log(revision, author, date, msg)]
                    data[name] = curr_list

        return data
