# -*- coding: utf-8 -*-

import csv

def get_dict_data():
    f = open('data/ipa2phonetic.dict')
    csv_f = csv.DictReader(f, delimiter='\t')
    dict_hmap = {}
    for row in csv_f:
        dict_hmap[row['ipa']] = row
    return dict_hmap

def trans(ipa, alpha3):
    dict_data = get_dict_data()
    out = ""
    for char in ipa:
        out += dict_data[char][alpha3]
    return out

if __name__ == "__main__":
    print get_dict_data()
    print trans('tu', 'fra')
