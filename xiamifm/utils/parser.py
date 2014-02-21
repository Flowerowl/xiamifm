#encoding:utf-8
from __future__ import unicode_literals

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def xml_parser(source):
    root = ET.fromstring(source)
    for child in root.iter():
        print child.tag, child.text

