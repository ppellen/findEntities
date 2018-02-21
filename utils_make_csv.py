#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        utils_make_csv
# Purpose:
#
# Author:      SESA7161
#
# Created:     21/02/2018
# Copyright:   (c) ppellen 2018
# Licence:
# -------------------------------------------------------------------------------

from utils_load_pickle import result_from_pickle_file_to_csv

def main():

    result_from_pickle_file_to_csv("Unity_found.pck")
    pass


if __name__ == '__main__':
    main()

