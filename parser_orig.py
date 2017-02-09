#!/usr/bin/env python

import xml.etree.ElementTree as etree
from urllib2 import urlopen as UO

fd = UO('http://it-svn.corp/svn/stages-info.xml')

root = etree.parse(fd).getroot()

envs = {env.tag: env for env in root.find("environments").getchildren()}

for key, value in envs.items():
    print("Game: " + key)
    for child in value.getchildren():
        print("  EnvType: " + child.tag)
        for stage in child:
            print("    Name: " + stage.attrib['name'])
            for s in stage.getchildren():
                if s.tag in ['AppHostName', 'AppHostName2', 'dbHostName', 'mariaDBhostName']:
                    print("\t" + s.tag + ": " + s.text)
            print
