#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import os

import yaml


def get_json_keys(directory, filename):
    input_file = open(directory + filename)
    try:
        data_loaded = yaml.safe_load(input_file)
    except yaml.YAMLError as exc:
        print(f"[ERROR] Failed to load {filename}")
    return set(data_loaded.keys())

def filter_acl_papers(semantic_scholar_path, venues, sigs):
    acl_venue_papers = []

    for file in os.listdir(os.fsencode(semantic_scholar_path)):
        filename = os.fsdecode(file)

        if filename.endswith(".json"):
            input_file = open(semantic_scholar_path + filename, 'r')

            for line in input_file.readlines():
                data = json.loads(line)
                paper_venues = data['venue'].replace('-', ' ').split()
                print(paper_venues)
                for v in paper_venues:
                    if v in venues or v in sigs:
                        acl_venue_papers.append(data)
                        continue

    outfile = open(semantic_scholar_path + 'acl.json', 'w')
    for paper in acl_venue_papers:
        outfile.write(json.dumps(paper) + '\n')
    outfile.close()

    print(f'Successfully filtered {len(acl_venue_papers)} ACL Anthology venue papers')


if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='Filters ACL papers from the Semantic Scholar open corpus.')
    parser.add_argument('--semantic_scholar_path', required=True,
                        help='Semantic Scholar open corpus directory')
    parser.add_argument('--acl_data_path', required=True,
                        help='ACL Anthology YAML data path')
    args = parser.parse_args()

    venues = get_json_keys(args.acl_data_path, 'venues.yaml')
    sigs = get_json_keys(args.acl_data_path, 'sigs.yaml')
    filter_acl_papers(args.semantic_scholar_path, venues, sigs)
