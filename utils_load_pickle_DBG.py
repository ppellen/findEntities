#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        utils_load_pickle_DBG
# Purpose:     Debug utils_load_pickle
#
# Author:      Administrateur
#
# Created:     2017
# Copyright:   (c) Administrateur 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import utils_load_pickle
import pickle


temp_pickle_file = "M580_found.pck"  # "advantys_found.pck"  #  "X80_found.pck" #

utils_load_pickle.print_result_from_pickle_file(temp_pickle_file, False) # 2nd param: creates a txt file if True.
    #  #####################################################################################

#  Comment added for test of git/github with VSCode
#  Comment added for test of git/github with PyCharm