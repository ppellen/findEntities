#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        find_bibinfos
# Purpose:     in folders of decompiled CHMs, find files with name of the kind 140NOC77101_D-SE-0002297.4.htm
#               140NOC77101_D-SE-0002297.4.htm   (with '.number' before the extension)
#               The map id (here D-SE-0002297) possibly denotes the one of the bibinfo for this CHM/Product.
#
# Author:      SESA7161
#
# Created:     25/02/2018
# Copyright:   (c) ppellen 2018
# Licence:
# -------------------------------------------------------------------------------

__author__ = 'SESA7161'

import os
import re

# ^[A-Za-z0-9]+_D-\w{2}-\d{7}\.\d+\.\d+\.htm$

htm_file_pattern=re.compile('^(?P<CHM>[A-Za-z0-9]+)_(?P<MAPID>D-\w{2}-\d{7})\.\d+\.htm[l]*$')

def discover_htm_file(this_directory=None):
    if os.path.isdir( this_directory ):
        for candidate in os.listdir(this_directory):
            if candidate.split('.')[-1] in ['htm', 'html']:
                yield candidate


def could_be_a_bibinfo(html_file_name):
    match_result = htm_file_pattern.match(html_file_name)
    if match_result is not None:
        return { 'CHM name':match_result.group('CHM'), 'bibinfo id': match_result.group('MAPID')} # group 0: CHM name. group 1: map id of the bibinfo.
    return None


def could_be_a_bibinfo_hashable(html_file_name):
    match_result = htm_file_pattern.match(html_file_name)
    if match_result is not None:
        return (match_result.group('CHM'), match_result.group('MAPID')) # group 0: CHM name. group 1: map id of the bibinfo.
    return None

def test_re():
    result_match = could_be_a_bibinfo('140NOC77101_D-SE-0002297.4.htm')
    if result_match is not None:
        print result_match['CHM name'], result_match['bibinfo id']
    pass

def main():
    path_to_chms = r'C:\pytmp\UnitySource'
    list_of_chms =[]
    for _dir in os.listdir(path_to_chms):
        if os.path.isdir(path_to_chms+os.sep+_dir):
            list_of_htms = [ htm for htm in discover_htm_file(path_to_chms+os.sep+_dir)]
            chm_bibinfo = set()
            for htm in list_of_htms:
                maybe_bibinfo = could_be_a_bibinfo_hashable(htm)
                if maybe_bibinfo is None:
                    list_of_htms.remove(htm)
                else:
                    chm_bibinfo.add(maybe_bibinfo)
            if len(chm_bibinfo) == 1:
                list_of_chms.append(chm_bibinfo)
            else:
                print "PB:", _dir

    print 'bibinfos = {'
    for x in list_of_chms:
        for y in x:
            print "'%s' : '%s'," % (y[0], y[1])
    print '}'

if __name__ == '__main__':
    main()

bibinfos = {
'1000se' : 'D-SE-0061763',
'1001se' : 'D-SE-0060835',
'1003se' : 'D-SE-0061317',
'1004se' : 'D-SE-0061450',
'140NOC77101' : 'D-SE-0002297',
'140NRP3120x' : 'D-SE-0032487',
'addendum' : 'D-SE-0055381',
'AEC920' : 'D-SG-0003416',
'Amt' : 'D-SA-0021108',
'AMTs' : 'D-SA-0023313',
'analogp' : 'D-SA-0009336',
'analogs' : 'D-SA-0021793',
'asciimq' : 'D-SG-0013199',
'asibusm' : 'D-SA-0026532',
'asibusp' : 'D-SA-0011275',
'asibusq' : 'D-SG-0015275',
'baselib' : 'D-SG-0006349',
'bmecxm' : 'D-SE-0048349',
'BMENOC0321' : 'D-SE-0056713',
'BMENOC03x1' : 'D-SE-0034163',
'BMENOP0300' : 'D-SE-0064129',
'BMENOS0300' : 'D-SE-0056460',
'bmxetm02' : 'D-SE-0058393',
'bmxngd0100' : 'D-SE-0059637',
'BMXNOC0401' : 'D-SE-0005174',
'bmxnom02' : 'D-SE-0069586',
'CanHard' : 'D-SA-0021320',
'catmg' : 'D-SE-0048647',
'ccotfq' : 'D-SE-0008076',
'clclib' : 'D-SG-0006352',
'clkmodq' : 'D-SG-0012870',
'comcanop' : 'D-SA-0011201',
'comcans' : 'D-SA-0022363',
'comdrive' : 'D-SA-0014577',
'cometh' : 'D-SA-0010767',
'comfipas' : 'D-SA-0014808',
'comfpio' : 'D-SA-0009131',
'comfpw' : 'D-SA-0010069',
'comibus' : 'D-SA-0010343',
'comlink' : 'D-SA-0009672',
'comlinks' : 'D-SA-0022355',
'commbpq' : 'D-SG-0015322',
'commdbp' : 'D-SA-0014113',
'commlib' : 'D-SG-0006351',
'comprof' : 'D-SA-0011553',
'comref' : 'D-SA-0008893',
'convcc' : 'D-SG-0012941',
'convpl7' : 'D-SA-0006909',
'count200' : 'D-SA-0022348',
'count800' : 'D-SA-0026704',
'countp' : 'D-SA-0007820',
'countssi' : 'D-SE-0011232',
'cprules' : 'D-SE-0045005',
'diaglib' : 'D-SG-0006353',
'disciob' : 'D-SA-0021236',
'disciop' : 'D-SA-0008898',
'discioq' : 'D-SG-0014902',
'erts' : 'D-SE-0019475',
'esy007' : 'D-SA-0020901',
'ethq' : 'D-SG-0015024',
'Eths' : 'D-NA-0011051',
'faq' : 'D-SE-0053295',
'FCM340' : 'D-SA-0025031',
'Fibernet' : 'D-SA-0015882',
'gndcab' : 'D-SG-0014404',
'hardM580' : 'D-SE-0025974',
'hardprem' : 'D-SA-0007563',
'hardquan' : 'D-SG-0010340',
'hards' : 'D-SA-0022356',
'hartaio' : 'D-SE-0030715',
'hsbyp' : 'D-SA-0022842',
'hsbyq' : 'D-SG-0014517',
'hscntq' : 'D-SG-0015111',
'infolibs' : 'D-SE-0068251',
'infom340' : 'D-SE-0067995',
'infom580' : 'D-SE-0068252',
'infoquan' : 'D-SE-0068253',
'interrq' : 'D-SG-0014607',
'io800q' : 'D-SG-0014900',
'iolib' : 'D-SG-0006355',
'ip67p' : 'D-SA-0011468',
'lexfpio' : 'D-SA-0018895',
'm580ccotf' : 'D-SE-0030871',
'm580cmlx' : 'D-SE-0053258',
'm580hsby' : 'D-SE-0052525',
'm580rio' : 'D-SE-0026069',
'm580sman' : 'D-SE-0068361',
'm580spg' : 'D-SE-0026591',
'm580sspg' : 'D-SE-0062656',
'mfblib' : 'D-SA-0021109',
'mislib' : 'D-SG-0006354',
'momdp' : 'D-SG-0005806',
'mometh' : 'D-NA-0005939',
'momfpio' : 'D-SA-0018787',
'momib' : 'D-SG-0013210',
'momio' : 'D-SG-0006074',
'momM1M1E' : 'D-SE-0024310',
'mommbp' : 'D-NA-0002698',
'mot85' : 'D-SA-0020747',
'motcayp' : 'D-SA-0009942',
'motccyp' : 'D-SA-0012333',
'motcfyp' : 'D-SA-0011045',
'motcsyp' : 'D-SA-0014354',
'motion1q' : 'D-SG-0012720',
'motlib' : 'D-SG-0006398',
'motpto' : 'D-SA-0025743',
'netmodq' : 'D-SG-0014901',
'noc77100' : 'D-NA-0013930',
'NOP85000' : 'D-SE-0048459',
'nrps' : 'D-SE-0018898',
'ofsts' : 'D-SE-0022148',
'opmod' : 'D-SG-0011957',
'osload' : 'D-SA-0009977',
'PMESE' : 'D-SE-0032057',
'prioam' : 'D-SE-0002446',
'procctlp' : 'D-SA-0008122',
'psxcs' : 'D-SE-0043577',
'psxctrl' : 'D-SE-0008442',
'psxdio' : 'D-SE-0008423',
'psxgspg' : 'D-SE-0008056',
'psxrio' : 'D-SE-0007684',
'psxts' : 'D-SE-0022862',
'ref' : 'D-SA-0006894',
'rtus' : 'D-SE-0004667',
's9082m580' : 'D-SE-0062827',
'safeins' : 'D-SE-0050149',
'safelib' : 'D-SE-0062704',
'sandsw' : 'D-SE-0049079',
'sercosq' : 'D-SG-0015481',
'sim' : 'D-SG-0008643',
'stamp1q' : 'D-SG-0012620',
'stamp2q' : 'D-SE-0018444',
'stamp3q' : 'D-SE-0032410',
'stdcert' : 'D-SE-0069429',
'stdcerts' : 'D-SE-0074239',
'systlib' : 'D-SG-0006356',
'tbxp' : 'D-SA-0011204',
'tcpipq' : 'D-SG-0014898',
'tcplib' : 'D-SG-0012466',
'trending' : 'D-SE-0026226',
'TSXETC100' : 'D-NA-0014136',
'TSXETC101' : 'D-SE-0004377',
'u984lib' : 'D-SE-0005428',
'u984opmo' : 'D-SE-0005891',
'upgm340' : 'D-SE-0052225',
'upgm580' : 'D-SE-0059758',
'upgquan' : 'D-SE-0049264',
'weighp' : 'D-SA-0012697',
'X80rackpws' : 'D-SE-0065079',
}
