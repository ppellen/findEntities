#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        try_read_xml.pp
# Purpose:
#
# Author:      SESA7161
#
# Created:     24/02/2018
# Copyright:   (c) ppellen 2018
# Licence:
# -------------------------------------------------------------------------------

__author__ = 'SESA7161'

import os

import xml.etree.ElementTree as ET

import utils.utils as UT
import io

stack = list()

_dir = r'C:\Users\PPELLEN\Documents\py\findEntities\synthese\test_iolib\[P-SG-0000119.25]_[CHM]_[eng]_Stand-alone_[2018-02-22_15_44_48]\system\product'

def print_the_3_first_lines_of_map_files():

    for xml_file in UT.discover_all_map_files(_dir):
        with io.open(_dir+os.sep+xml_file) as f:
            print xml_file, '---------------------'
            for i in range(0,3):
                print f.readline()
            print


def main():

    if False:
        mapid = 'D-SG-0011466'
        _file = UT.discover_xml_file(mapid, _dir)
        if _file is None:
            return
        tree = ET.parse(_dir+os.sep+_file)
        root = tree.getroot()

    maps_where_unity_is_found = []
    for xml_file in UT.discover_all_map_files(_dir):
        found = False
        where_found = []
        context = ET.iterparse(_dir + os.sep + xml_file, events=("start", "end"))
        for action, element in context:
            if action=='start':
                stack.append(element.tag)

                if (element.text is not None):
                    #  and len(element._children)==0:
                    # elements_with_possibly_no_text.add(element.tag)
                    if 'unity' in element.text.lower():
                        found = True
                        where_found.append (('text', element.tag, element.text))
                        try:
                            if maps_where_unity_is_found[-1] != xml_file:
                                maps_where_unity_is_found.append(xml_file)
                        except:
                            maps_where_unity_is_found.append(xml_file)
                if (element.tail is not None):
                    if 'unity' in element.tail.lower():
                        found = True
                        where_found.append (('tail', element.tag, element.tail))
                        try:
                            if maps_where_unity_is_found[-1] != xml_file:
                                maps_where_unity_is_found.append(xml_file)
                        except:
                            maps_where_unity_is_found.append(xml_file)

            elif action=='end':
                stack.pop()
            else:
                print "???"

        if found :
            print xml_file, '---------------------'
            for x in where_found:
                print x[0],x[1],x[2]
            print

    for _map in maps_where_unity_is_found:
        print(_map)

# print("%s: %s %s" % (action, elem.tag, elem.attrib['key']))
# print("%s: %s" % (action, elem.tag ))
# print("%s: %s %s" % (action, elem.tag, elem.text))

if __name__ == '__main__':
    main()
