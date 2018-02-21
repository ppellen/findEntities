#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        utils_load_pickle
# Purpose:
#
# Author:      SESA7161
#
# Created:     30/04/2017
# Copyright:   (c) ppellen 2017
# Licence:
# -------------------------------------------------------------------------------

__author__ = 'SESA7161'
import pickle

import csv

import os
import sys


def main():
    pass


def print_result_from_pickle_file( pickle_file, to_file_not_to_screen ):

    if to_file_not_to_screen:
        output_file = pickle_file.split('.')[0] + '.txt'

        stdout_ = sys.stdout #Keep track of the previous value.
        sys.stdout = open(output_file, 'w')

    f = open(pickle_file, 'rb')
    data = pickle.load(f)

    character_string_searched = data['Character string searched']
    map_numbers = {}

    total_maps_number = total_text_found = 0
    for result_for_chm in data['found_in']:
        chm_name = result_for_chm[0]
        for this_map, number_found_in_this_map in result_for_chm[1].items():
            total_maps_number += 1
            total_text_found += number_found_in_this_map
            try:
                this_map = this_map.split('_')[1].split('.')[0]
            except:
                pass

            if not this_map in map_numbers.keys():
                map_numbers[this_map] = number_found_in_this_map

    print 'Character string searched:', character_string_searched
    print "Raw total:", total_text_found, 'times in', total_maps_number, "maps"

    total_2 = i = _max = 0

    for this_map, number_found_in_this_map in map_numbers.items():
        i += 1
        total_2 += number_found_in_this_map

        if number_found_in_this_map > _max:
            _max = number_found_in_this_map
            map_of_max = this_map

        print i, this_map, number_found_in_this_map

    print 'Total (common maps counted once): ',  total_2, 'times in', i , 'unique maps.'
    try:
        print 'Maximum is', _max, 'in', map_of_max
    except:
        print 'No result found.'

    if to_file_not_to_screen:
        sys.stdout = stdout_ # restore the previous stdout.


def result_from_pickle_file_to_csv( pickle_file ):

    f = open(pickle_file, 'rb')
    data = pickle.load(f)
    f.close()

    output_file_name = pickle_file.split('.')[0] + '.csv'
    output_file = open(output_file_name, 'w')

    csv_writer = csv.writer(output_file, lineterminator='\n' )
    csv_writer.writerow(('#', "CHM", "map", "n",))

    character_string_searched = data['Character string searched']
    map_numbers = {}
    number_maps_strange = 0

    total_maps_number = total_text_found = 0
    for result_for_chm in data['found_in']:
        chm_name = result_for_chm[0]
        for this_map, number_found_in_this_map in result_for_chm[1].items():
            total_maps_number += 1
            total_text_found += number_found_in_this_map
            try:
                this_chm = this_map.split('_')[0]
                this_map2 = this_map.split('_')[1].split('.')[0]
            except:
                this_chm = chm_name
                this_map2 = this_map
                number_maps_strange +=1

            if not this_map in map_numbers.keys():
                map_numbers[this_map] = number_found_in_this_map

            csv_writer.writerow((total_maps_number, this_chm, this_map2, number_found_in_this_map,))

    output_file.close()

    print 'Character string searched:', character_string_searched
    print "Raw total:", total_text_found, 'times in', total_maps_number, "maps"
    print "Number of strange map names:", number_maps_strange




if __name__ == '__main__':
    main()

