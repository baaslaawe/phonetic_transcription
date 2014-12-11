# -*- coding: utf-8 -*-

import csv

def get_dict_data():
    f = open('dict/fra.dict')
    csv_f = csv.reader(f, delimiter='\t')
    dict_hmap = {}
    for ipa, trans in csv_f:
        dict_hmap[ipa] = trans
    return dict_hmap

def trans(ipa):
    dict_data = get_dict_data()
    out = ""
    for char in ipa:
        out += dict_data[char]
    return out

if __name__ == "__main__":
    print trans("tu")
