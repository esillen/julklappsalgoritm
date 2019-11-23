#!/usr/bin/env python
# -*- coding: utf-8 -*-

users  = {
    'Alice' : {
        'email' : 'alice@christmasmail.com',
        'forbidden' : ['Bob', 'Dave', 'Carol', 'Eve']
    },
    'Bob' : {
        'email' : 'bob@christmasmail.com',
        'forbidden' : ['Alice']
    },
    'Carol' : {
        'email' : 'carol@christmasmail.com',
        'forbidden' : ['Alice', 'Dave', 'Eve']
    },
    'Dave' : {
        'email' : 'dave@christmasmail.com',
        'forbidden' : ['Alice', 'Carol', 'Eve']
    },
    'Eve' : {
        'email' : 'eve@christmasmail.com',
        'forbidden' : ['Alice', 'Carol', 'Dave']
    },
    'Faythe' : {
        'email' : 'faythe@christmasmail.com',
        'forbidden' : ['Grace', 'Heidi', 'Judy', 'Ivan']
    },
    'Grace' : {
        'email' : 'grace@christmasmail.com',
        'forbidden' : ['Faythe', 'Heidi', 'Ivan', 'Mallory']
    },
    'Heidi' : {
        'email' : 'heidi@christmasmail.com',
        'forbidden' : ['Faythe', 'Grace', 'Ivan']
    },
    'Ivan' : {
        'email' : 'ivan@christmasmail.com',
        'forbidden' : ['Faythe', 'Grace', 'Heidi']
    },
    'Judy' : {
        'email' : 'judy@christmasmail.com',
        'forbidden' : ['Faythe']
    },
    'Mallory' : {
        'email' : 'mallory@christmasmail.com',
        'forbidden' : ['Grace']
    },
}


# Checks that the forbidden lists contain valid names
def sanity_check():
    for key, value in users.iteritems():
        for forbidden in value['forbidden']:
            if forbidden not in users:
                raise ValueError('Each name should exist in the list. Did you misspell something?')
    return True

sanity_check()
