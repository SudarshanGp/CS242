import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
from flask import Flask, render_template, request, json
from flask import render_template
from app import parser

import json
import pprint
from collections import OrderedDict

app = Flask(__name__)
svn_list = {}
svn_log = {}


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'CS 242'}
    svn_list_data = []
    # pprint.pprint(svn_list)
    alternateData = [{
        'text': 'LAME 1',
        'tags': ['2'],
        'nodes': [{
            'text': 'Child 1',

            'tags': ['3'],
            'nodes': [{
                'text': 'Grandchild 1',

                'tags': ['6']
            }, {
                'text': 'Grandchild 2',

                'tags': ['3']
            }]
        }, {
            'text': 'Child 2',

            'tags': ['3']


        }]
    }, {
        'text': 'Parent 2',

        'tags': ['7']
    }, {
        'text': 'Parent 3',

        'icon': 'glyphicon glyphicon-earphone',
        'href': '#demo',
        'tags': ['11']
    }, {
        'text': 'Parent 4',

        'icon': 'glyphicon glyphicon-cloud-download',
        'href': '/demo.html',
        'tags': ['19'],
        'selected': 'true'
    }, {
        'text': 'Parent 5',

        'icon': 'glyphicon glyphicon-certificate',
        'color': 'pink',
        'backColor': 'red',
        'href': 'http://www.tesco.com',
        'tags': ['available', '0']
    }]

    return render_template("base.html",
                           title='CS 242 Portfolio',
                           user=user,
                           posts=svn_list,
                           alternateData =svn_list['root']['nodes'], src= "")


@app.route('/subversion', methods=['POST'])
def route_code():
    print(request.json['url'])
    return render_template("base.html", url =request.json['url'] )


# @app.errorhandler(Exception)
# def exception_handler(error):
#     return "!!!!" + repr(error)


if __name__ == '__main__':
    svn_list, svn_log = parser.init_files()
    app.run()
