# -*- coding: utf-8 -*-

import csv
import codecs

def get_dict_data():
    f = codecs.open('data/ipa2phonetic.dict')
    csv_f = csv.DictReader(f, delimiter='\t')
    return csv_f

ipa_dict = get_dict_data()

def get_entry(ipa):
    for entry in get_dict_data():
        if entry['ipa'].decode('utf-8') == ipa:
            return entry
    return None

def get_max_match(raw_str):
    raw_str = raw_str[:3]
    while (raw_str):
        if get_entry(raw_str):
            break
        else:
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
    out = u""
    for seg in segs:
        if (not seg):
            continue
        entry = get_entry(seg)
        if (entry):
            out += entry[alpha3].decode('utf-8')
        else:
            if seg in [u"ˈ", u"(", u")"]:
                out += seg
            else:
                out += u"[%s]"%seg
    return out

if __name__ == "__main__":
    import sys
    args = sys.argv
    args.pop(0)
    f = codecs.open('test_data', 'r', encoding='utf8')
    for line in f.read().split('\n'):
        print "%s -> %s"%(line, trans(line, 'fra'))
