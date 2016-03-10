import pprint
import sys
from pandas import json

from svn.log.log import Log

sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
from bs4 import BeautifulSoup
import subprocess
from svn.list import List
from dateutil import parser


def init_files():
    # cmd = "svn list --xml --recursive https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2 > static/res/svn_list.xml;" \
    #       "svn log --verbose --xml https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2 > static/res/svn_log.xml;"
    # p = subprocess.Popen(cmd, shell=True)
    # p.wait()  # block util the cmd execute finish
    svn_list = soup_file('app/static/res/svn_list.xml')
    svn_log = soup_file('app/static/res/svn_log.xml')
    svn_list = parse_list(svn_list)
    svn_log = parse_log(svn_log)
    return svn_list, svn_log


def soup_file(file_name):
    data = open(file_name)
    formatted = BeautifulSoup(data, 'lxml')
    return formatted



def parse_list(file):
    data = {}

    for elem in file.findAll('entry'):
        kind = elem['kind']
        name = str(elem.find('name').text)
        commit = int(elem.commit['revision'])
        author = str(elem.commit.author.text)
        date = parser.parse(elem.commit.date.text)
        data[name] = List(kind, name, commit, author, date)

    hierarchy = {'root': {}}
    hierarchy['root']['info'] = '/'
    hierarchy['root']['nodes'] = []
    # structure=== of hierarchy
    '''
        info : contains the list object
        text : "name"
        tags : ["date", "revision"]
        nodes : [
                    files/directories
                ]
    '''
    for key, value in data.iteritems():
        # INIT  DIRECTORIES into hierarchy
        temp = hierarchy['root']
        paths = value.name.split('/')
        # print(paths)
        if 'dir' in value.kind:
            for k, val in enumerate(paths):
                # print(val)
                if k == len(paths) - 1:
                    # print("in end of path")
                    # if its the last entry and it is a directory,
                    # we need to create an info entry to hold its list information
                    # and we need to create an emtpy children list
                    if any(d['text'] == val for d in temp['nodes']):  # if the directory exists but it does not have an info value
                        # print("already init ppath and trying to set stuff")
                        # print(match)
                        match = next((d for d in temp['nodes'] if d['text'] == val), None)
                        # match['info'] = value
                        match['tags'] = [value.commit]
                        match['href'] = 'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' + value.name
                        # print(match)
                    else:
                        # print("not found it before")
                        # temp_insert = {'info': value, 'text': val, 'tags' : [value.commit, value.date], 'children': [], 'href' : 'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' + value.name}
                        temp_insert = {'text': val, 'tags' : [value.commit], 'nodes': [], 'href' : 'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' + value.name}
                        temp['nodes'].append(temp_insert) # look for the current directory and insert it into chidlren
                        # print("Appending")
                        # print(temp_insert)
                elif any(d['text'] == val for d in temp['nodes']):
                    # print("Found a match somewhere")
                    match = next((d for d in temp['nodes'] if d['text'] == val), None)
                    # print(match)
                    temp = match
                elif not any(d['text'] == val for d in temp['nodes']):
                    # print("Could not find match")
                    # temp_insert = {'info': -1, 'text': val, 'tags' : [], 'children': [], 'href' : ""}
                    temp_insert = { 'text': val, 'tags' : [], 'nodes': [], 'href' : ""}
                    temp['nodes'].append(temp_insert)
                    # print("creating new thing and appending it")
                    match = next((d for d in temp['nodes'] if d['text'] == val), None)
                    # print(match)
                    temp = match

    # pprint.pprint(hierarchy)

    for key, value in data.iteritems():
        # INIT FILES into hierarchy
        temp = hierarchy['root']
        paths = value.name.split('/')
        print("looking ")
        print(paths)
        if 'file' in value.kind:
            for k, val in enumerate(paths):
                print(val)
                if k == len(paths) - 1:
                    print("in end of path + adding file to child")
                    print(temp['text'])
                    # if its the last entry and it is a file,
                    # we need to update the children with a file entry
                    # temp_insert = {'info': value,'text': val, 'tags' : [value.commit, value.date], 'href' : 'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' + value.name}
                    temp_insert = {'text': val, 'tags' : [value.commit], 'url' : 'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/' + value.name}
                    temp['nodes'].append(temp_insert)  # look for the current directory and insert it into chidlren
                elif any(d['text'] == val for d in temp['nodes']):
                    # Still looking for the right directory
                    print("still looking for child and matched with = ")
                    match = next((d for d in temp['nodes'] if d['text'] == val), None)
                    print(match['text'])
                    temp = match
    return hierarchy


def parse_log(file):
    data = {}
    for elem in file.findAll('logentry'):
        revision = elem['revision']
        author = elem.author.text
        date = parser.parse(elem.date.text)
        msg = elem.msg.text
        paths = elem.paths.findAll('path')
        data[revision] = Log(revision, author, date, msg, paths)
    return data
