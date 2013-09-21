#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
import re
import socket
from bs4 import BeautifulSoup

def http_reader(url):
    headers = {
        "Accept" : "text/html",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22"
    }
    request = urllib2.Request(url, headers = headers)
    try:
        response = urllib2.urlopen(request, timeout = 10)
    except Exception, e:
        if isinstance(e, urllib2.HTTPError):
            print 'http error: {0}'.format(e.code)
        elif isinstance(e, urllib2.URLError) and isinstance(e.reason, socket.timeout):
            print 'url error: socket timeout {0}'.format(e.__str__())
        else:
            print 'misc error: ' + e.__str__()
    else:
        content = response.read()
        return content

def get_result():
    url = 'http://invoice.etax.nat.gov.tw'
    #url = 'http://www.etax.nat.gov.tw/etwmain/front/ETW183W2?id=13c705555ae000008b1e384e209a4729'
    html = http_reader(url)
    #soup = BeautifulSoup(html, "lxml")
    soup = BeautifulSoup(html)
    results = [i.encode_contents().strip() for i in soup.find_all('span', class_='t18Red')]
    date = [i.encode_contents().strip() for i in soup.find_all('h2', limit=1)]
    return results, date

def get_item(results):
    for item in results:
        return item

def prize(results, index):
    first_prize =  results[2]
    if index == 1:
        return '頭獎 ' + first_prize
    elif index == 2:
        return '二獎 ' + 'x' + first_prize[1:8] + '、'+'x' + first_prize[12:19] + '、'+'x' + first_prize[23:31]
    elif index == 3:
        return '三獎 ' + 'xx' + first_prize[2:8] + '、'+'xx' + first_prize[13:19] + '、'+'xx' + first_prize[24:31]
    elif index == 4:
        return '四獎 ' + 'xxx' + first_prize[3:8] + '、'+'xxx' + first_prize[14:19] + '、'+'xxx' + first_prize[25:31]
    elif index == 5:
        return '五獎 ' + 'xxxx' + first_prize[4:8] + '、'+'xxxx' + first_prize[15:19] + '、'+'xxxx' + first_prize[26:31]
    elif index == 6:
        return '六獎 ' + 'xxxxx' + first_prize[5:8] + '、'+'xxxxx' + first_prize[16:19] + '、'+'xxxxx' + first_prize[27:31]
    elif index == 7:
        tmp = results[3:4]
        return '增開六獎 ' + tmp[0]
    elif index == 8:
        tmp = results[0:1]
        return '特別奬 ' + tmp[0]
    elif index == 0:
        tmp = results[1:2]
        return '特獎 ' + tmp[0]

def print_prize(results, date):
    for t in date:
        print t
    first_prize =  results[2]
    print '特別奬'
    for item1 in results[0:1]:
        print item1

    print '特獎'
    for item2 in results[1:2]:
        print item2

    print '頭獎'
    for item3 in results[2:3]:
        print item3

    print '二獎'
    print 'x' + first_prize[1:8] + '、'+'x' + first_prize[12:19] + '、'+'x' + first_prize[23:31]

    print '三獎'
    print 'xx' + first_prize[2:8] + '、'+'xx' + first_prize[13:19] + '、'+'xx' + first_prize[24:31]

    print '四獎'
    print 'xxx' + first_prize[3:8] + '、'+'xxx' + first_prize[14:19] + '、'+'xxx' + first_prize[25:31]

    print '五獎'
    print 'xxxx' + first_prize[4:8] + '、'+'xxxx' + first_prize[15:19] + '、'+'xxxx' + first_prize[26:31]

    print '六獎'
    print 'xxxxx' + first_prize[5:8] + '、'+'xxxxx' + first_prize[16:19] + '、'+'xxxxx' + first_prize[27:31]

    print '增開六獎'
    for item in results[3:4]:
        print item

def main():
    (results, date) = get_result()
    print_prize(results, date)

if __name__ == '__main__': 
    main()

