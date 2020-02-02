# coding:utf-8
"""
Convert a csv file to markdown format.
Syntax:
    python csv2md.py -csv <csv file> -md <markdown file> -csv_encoding <encoding>
in which <csv file> is the csv file to be converted; <markdown file> is the output path for the generated markdown file, optional;
<encoding> is the encoding of the csv file, optional, the default encoding is set to `latin`.

Created   :   2,  2, 2020
Revised   :   2,  2, 2020
All rights reserved
"""
__author__ = 'dawei.leng'

import os

def parse_csv_line(csv_line):
    items = csv_line.split(',')
    results = []
    for item in items:
        results.append(item.strip())
    return results

def parse_csv_file(csv_file, encoding='utf8'):
    with open(csv_file, mode='rt', encoding=encoding) as f:
        titles = parse_csv_line(f.readline().strip())
        records = []
        for line in f:
            record = parse_csv_line(line)
            records.append(record)
    return titles, records

def generate_markdown_table(titles, records):
    content = ''
    title_line = '|  '
    title_sep  = '| -'
    for item in titles:
        title_line += '%s  | ' % item
        title_sep  += '--- | '
    content += '%s\n' % title_line
    content += '%s\n' % title_sep
    for record in records:
        line = '|  '
        for item in record:
            line += '%s  | ' % item
        content += '%s\n' % line
    return content

if __name__ == '__main__':
    import argparse
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-csv', default=None, type=str, help='csv file, input')
    argparser.add_argument('-md', default=None, type=str, help='markdown file, output, optional')
    argparser.add_argument('-csv_encoding', default='latin', type=str, help='encoding of csv file, optional')
    args = argparser.parse_args()

    csv_file = args.csv
    md_file  = args.md
    csv_encoding = args.csv_encoding
    if md_file is None:
        md_file = os.path.splitext(os.path.basename(csv_file))[0] + '.md'

    titles, records = parse_csv_file(csv_file, csv_encoding)
    md_table = generate_markdown_table(titles, records)
    with open(md_file, encoding='utf8', mode='wt') as f:
        f.write(md_table)
    print('markdown file = %s' % os.path.abspath(md_file))
    print('All done~')








