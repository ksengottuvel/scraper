#! /usr/bin/env python

import urllib2


def main(url):
    pass


def save_result(file_path, url):
    with open(file_path, 'a') as result_file:
        result_file.write(url)


def scrap(url):
    print 'Scrapping url', url

    try:
        resp = urllib2.urlopen(url).read()
    except (ValueError, urllib2.URLError) as e:
        print e
        return

    if 'jquery.js' in resp:
        print 'jquery.js found'
        save_result('accepted.csv', url)
    else:
        print 'jquery.js not found'
        save_result('accepted.csv', url)


if __name__ == '__main__':

    with open('data.txt', 'r') as data_file:
        for url in data_file:
            scrap(url)
