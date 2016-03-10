import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
from flask import Flask, render_template, request, json
from flask import render_template
import parser

import json
import pprint
from collections import OrderedDict

app = Flask(__name__)
svn_list = {}
svn_log = {}


@app.route('/')
@app.route('/index')
def index():
    pprint.pprint(svn_list)
    return render_template("base.html",
                           title='CS 242 Portfolio',
                           posts=svn_list['root']['nodes'])


# @app.route('/subversion', methods=['POST'])
# def route_code():
#     print(request.json['url'])
#     return render_template("base.html", url =request.json['url'] )


@app.errorhandler(Exception)
def exception_handler(error):
    return "!!!!" + repr(error)


if __name__ == '__main__':
    svn_list, svn_log = parser.init_files()
    app.run()
