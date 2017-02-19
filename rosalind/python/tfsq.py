#!/usr/bin/env python

from sys import argv



def parseFQ(file_name):
    with open(file_name) as in_file:
        while True:
            header = in_file.readline().strip()
            seq = in_file.readline().strip()
            nothing = in_file.readline()#skipped
            qual = in_file.readline()#skipped quality


            if header == "" or seq == "":
                break
            else:
                print(">{}\n{}".format(header[1:], seq))


parseFQ(argv[1])
