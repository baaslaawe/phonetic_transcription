# -*- coding: utf-8 -*-

import csv

def get_dict_data():
    f = open('data/ipa2phonetic.dict')
    csv_f = csv.DictReader(f, delimiter='\t')
    dict_hmap = {}
    for row in csv_f:
        dict_hmap[row['ipa']] = row
    return dict_hmap

ipa_dict = get_dict_data()

def get_max_match(raw_str):
    raw_str = raw_str[:3]
    while (raw_str):
        try:
            ipa_dict[raw_str]
            break
        except KeyError:
            if (len(raw_str) <= 1):
                break
            raw_str = raw_str[:(len(raw_str)-1)]
    return raw_str

def split(raw_str):
    segments = []
    while (len(raw_str)):
        segment = get_max_match(raw_str)
        raw_str = raw_str[len(segment):len(raw_str)]
        segments.append(segment)
        if (len(raw_str) <= 1):
            segments.append(get_max_match(raw_str))
            break

    return segments

def trans(ipa, alpha3):
    segs = split(ipa)
    out = ""
    for seg in segs:
        try:
            out += ipa_dict[seg][alpha3]
        except KeyError:
            # if seg in ["'", "."]:
            #     out += seg
            # else:
            out += "["+seg+"]"
    return out

if __name__ == "__main__":
    import sys
    args = sys.argv
    args.pop(0)
    # print get_dict_data()
    # for arg in args:
    #     print trans(arg, 'fra')
    # print split(args[0])
    print trans(args[0], 'fra')
