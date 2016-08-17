#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
import psutil as ps

def check_shit():
    result = {}
    shit = ['^.ss ', 'atack.pl', 'ipatack.pl', 'wcgrid_', 'worldcommunitygrid', 'ypool', 'mining', 'sksapd', 'skysapd', 'atdd', 'kysapd', 'ksapd', 'miner', 'stratum', '/usr/bin/host', 'pickup', '^[\s.]{0,}IptabLe[sx]']
    regular = [re.compile(i) for i in shit]
    for proc in ps.process_iter():
        pinfo = proc.as_dict(attrs=['pid', 'name', 'exe'])
        for x in regular:
            if x.match(pinfo['name']):
                #result.append(pinfo['exe'])
                result[pinfo['pid']] = pinfo['exe']
    return result

res = check_shit()

if len(res) == 0:
    print "Ok"
else:
    for x,y in res.items():
        print "Shit running on PID: %s, process: %s " % (x,y)
