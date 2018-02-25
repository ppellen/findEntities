#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        utils.py
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
import re

map_file_pattern=re.compile('^D-\w{2}-\d{7}\.\d+\.xml$')

def discover_xml_file(mapid, this_directory=None):
    if os.path.isdir( this_directory ):
        for candidate in os.listdir(this_directory):
            if candidate.split('.')[-1] == 'xml'\
                    and candidate.startswith(mapid):
                return candidate
    return None

def discover_all_map_files(this_directory=None):
    list_of_xml_files = []
    if os.path.isdir( this_directory ):
        for candidate in os.listdir(this_directory):
            match_result = map_file_pattern.match(candidate)
            if match_result is not None:
                list_of_xml_files.append(candidate)
        return list_of_xml_files
    return list_of_xml_files

def main():
    pass
