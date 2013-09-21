#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bottle import route, run, template, view
#from bottle import jinja2_view
from invoice_prize import *

@route('/hello')
def hello():
    return "Hello World!"

@route('/invoice')
@view('invoice_template')
def invoive():
    (results, date) = get_result()
    date = date[0].decode('UTF-8')

    special = prize(results, 0)
    first = prize(results, 1)
    second = prize(results, 2)
    third = prize(results, 3)
    fourth = prize(results, 4)
    fifth = prize(results, 5)
    sixth = prize(results, 6)
    sixth_plus = prize(results, 7)
    special2 = prize(results, 8)

    return dict(date=date, special2=special2, special=special,
     first=first, second=second, third=third, fourth=fourth,
     fifth=fifth, sixth=sixth, sixth_plus=sixth_plus)

@route('/invoice_M')
@view('invoiceM_template')
def invoive():
    (results, date) = get_result()
    date = date[0].decode('UTF-8')

    special = prize(results, 0)
    first = prize(results, 1)
    second = prize(results, 2)
    third = prize(results, 3)
    fourth = prize(results, 4)
    fifth = prize(results, 5)
    sixth = prize(results, 6)
    sixth_plus = prize(results, 7)
    special2 = prize(results, 8)

    return dict(date=date, special2=special2, special=special,
     first=first, second=second, third=third, fourth=fourth,
     fifth=fifth, sixth=sixth, sixth_plus=sixth_plus)

run(host='localhost', port=8080, debug=True, reloader=True)
