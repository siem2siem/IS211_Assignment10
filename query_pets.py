#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment10 - sqlite3 query_pets.py"""

import sqlite3
import sys

con = None

try:
    con = sqlite3.connect('pets.db')
    con.row_factory = sqlite3.Row

    while True:
        personselect = raw_input('\nPlease enter a Person ID number between 1-4 or enter -1 to exit: \n')

        if personselect == '-1':
            print ('\nYou have entered -1, the program will now exit.\n')
            break
        
        else:
            try:
                personselect = int(personselect)

            except:
                print '\nInvalid entry!  Please enter ID number from 1 - 4.\n'
                continue

        cur = con.cursor()
        cur.execute('SELECT * FROM person WHERE id =?', [(personselect)])
        row = cur.fetchone()

        if row == None:
            print 'The ID you have entered is invalid, please select person id 1-4.'
            continue

        print row['first_name'] + ' ' + row['last_name'] + ' is ' + str(
            row['age']) + ' yrs old.\n'


        for row in con.execute(
            "SELECT * FROM person_pet WHERE person_id =?", [(personselect)]):

            for name in con.execute(
                "SELECT * FROM person WHERE id =?", [(personselect)]):
                pet_owner = name['first_name'] + ' ' + name['last_name']


            for row_pet in con.execute(
                "SELECT * FROM pet WHERE id =?", [(row['pet_id'])]):

                if row_pet['dead'] == 0:
                    print (pet_owner + ' has a pet named ' + row_pet[
                    'name'] + '.  ' +  row_pet['name'] + ' was a ' + row_pet['breed'] + ' who was ' + str(
                        row_pet['age']) + ' years old.\n')
            else:
                if row_pet['dead'] != 0:
                    print (pet_owner + ' had a pet named ' + row_pet[
                        'name'] + '.  ' + row_pet['name'] + ' is a ' + row_pet['breed'] + ' who is ' + str(
                            row_pet['age']) + ' years old.\n')

except sqlite3.Error as e:
    print "Closing."
    print "Error: %s " % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()
