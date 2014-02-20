#encoding:utf-8
from __future__ import unicode_literals

from xml.dom.minidom import parseString

from get_response import get_source

def xml_parser(source):
    dom = parseString(source)
    print dom.
