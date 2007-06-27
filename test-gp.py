#!/usr/bin/python
# test-gp.py - test suite for libgphoto2 bindings
# Copyright (C) 2006,2007 Hans Ulrich Niedermann <gp@n-dimensional.de>
# Best used with Makefile's "installcheck" targets.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import sys
import os
from pprint import pprint
import unittest
import modulefinder


class TestRunner(unittest.TestCase):

    def setUp(self):
        import gphoto2

    def test_000_version_short(self):
        import gphoto2
        #print "gphoto2 version", gphoto2.version()

    def test_010_ports(self):
        import gphoto2
        self.ports = gphoto2.ports()
        self.ports.load()
        print self.ports.count(), " ports found:"
        for port in range(0, self.ports.count()):
            print self.ports[port]

    def xtest_020_cameras(self):
        import gphoto2
        self.a_l = gphoto2.abilities_list()
        self.a_l.load()
        print self.a_l.count(), " cameras found:"
        for i in range(0, self.a_l.count()):
            print self.a_l[i]

    def test_030_camera(self):
        import gphoto2
        print("Creating camera...")
        self.cam = gphoto2.camera()
        pprint(dir(self.cam))

    def test_007_long(self):
        import gphoto2
        pprint(gphoto2.library_version(False))
        pprint(gphoto2.library_version(True))

    def test_050_foo(self):
        import gphoto2
        pprint(dir(gphoto2))


if __name__ == '__main__':
    unittest.main()
