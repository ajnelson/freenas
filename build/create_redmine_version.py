#!/usr/local/bin/python

import sys, getopt
from redmine import Redmine

def main(argv):
    key = ''
    vers = ''
    descrpt = ''
    try:
        opts, args = getopt.getopt(argv,"hk:v:d:", ["key=","version=","description="])
    except getopt.GetoptError:
        print 'create_version.py -k <key> -v <version> -d <description>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'create_version.py -k <key> -v <version> -d <description>'
            sys.exit(2)
        elif opt in ("-k", "--key"):
            key = arg
        elif opt in ("-v", "--version"):
            vers = arg
        elif opt in ("-d", "--description"):
            descrpt = arg
    if key == '':
        print '<key> cannot be blank'
        sys.exit(2)
    if vers == '':
        print '<version> cannot be blank'
        sys.exit(2)
    redmine = Redmine('https://bugs.freenas.org', key=key)
    rm_project = redmine.project.get('freenas')
    version = redmine.version.new()
    version.project_id = rm_project.id
    version.name = vers
    version.description = descrpt
    version.status = 'closed'
    version.sharing = 'none'
    result = version.save()
    if result:
         print "Version %s successfully created" % vers
    else:
         print "Error creating version %s" % vers

if __name__ == "__main__":
   main(sys.argv[1:])