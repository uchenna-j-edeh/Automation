import re
import sys

def process_one_multipath_node(cmd_output, prog, start):
    len_output = len(cmd_output)
    print 'Found a new node, lets print it'
    counter = 0

    for j in range(len_output):
        #import pdb; pdb.set_trace()
        is_match = prog.search(cmd_output[j])
        if is_match is not None:
            counter = 1 + counter
            print is_match.group('san_path')
        else:
            break

    return counter

def process_mutipath_cmd(cmd_output):
    end_point = None # set end point
    prog = re.compile(r'(?P<san_path>[0-9]+:[0-9]+:[0-9]+:[0-9]+)')

    i = 0
    len_cmd = len(cmd_output)
    while i < len_cmd:
        is_match = prog.search(cmd_output[i])
        if is_match is not None:
            end_point = process_one_multipath_node(cmd_output[i:], prog, i)
            if end_point > 0:
                i = end_point + i
                end_point = None # reset end point
                continue
            else:
                break

        i = i + 1


cmd_output = [
'35000c5000357625b dm-2 SEAGATE,ST340008SSUN0.4',
'[size=373G][features=0][hwhandler=0]',
'    \_ round-robin 0 [prio=2][active]',
'    \_ 1:0:1:0  sdb 8:0    [active][ready]',
'    \_ 2:0:1:0  sde 8:192  [active][ready]',
'35000c5000357625b dm-2 SEAGATE,ST340008SSUN0.4',
'[size=373G][features=0][hwhandler=0]',
'    \_ round-robin 0 [prio=2][active]',
'    \_ 0:0:0:0  sda 8:0    [active][ready]',
'    \_ 1:0:0:0  sdm 8:192  [active][ready]',
'mpath1 (3600d0230003228bc000339414edb8101)',
'[size=10 GB][features="0"][hwhandler="0"]',
'\_ round-robin 0 [prio=1][active]',
' \_ 2:0:0:6 sdb 8:16 [active][ready]',
'\_ round-robin 0 [prio=1][enabled]',
' \_ 3:0:0:6 sdc 8:64 [active][ready]',
'  3600d0230000000000e13955cc3757801 dm-10 WINSYS,SF2372',
"  size=269G features='0' hwhandler='0' wp=rw",
"  |-+- policy='round-robin 0' prio=1 status=enabled",
"  | `- 19:0:0:108 sdc 8:32  active ready  running",
"  | `- 19:0:0:109 sdc 8:32  active ready  running",
"  | `- 19:0:0:110 sdc 8:32  active ready  running",
"  | `- 19:0:0:111 sdc 8:32  active ready  running",
"  `-+- policy='round-robin 0' prio=1 status=enabled",
"    `- 18:0:0:1 sdh 8:112 active ready  running",
"    3600d0230000000000e13955cc3757803 dm-2 WINSYS,SF2372",
"    size=125G features='0' hwhandler='0' wp=rw",
"    `-+- policy='round-robin 0' prio=1 status=active",
'      |- 19:0:0:3 sde 8:64  active ready  running',
'        `- 18:0:0:3 sdj 8:144 active ready  running',
'        `- 18:0:0:4 sdj 8:144 active ready  running',
'        `- 18:0:0:5 sdj 8:144 active ready  running',
'        `- 18:0:0:6 sdj 8:144 active ready  running',
'        `- 18:0:0:7 sdj 8:144 active ready  running',
'        `- 18:0:0:8 sdj 8:144 active ready  running',
'        `- 18:0:0:9 sdj 8:144 active ready  running'
]


process_mutipath_cmd(cmd_output)


