# -*- coding: utf-8 -*-
#
#  AppDelegate.py
#  TestPythonBuildForAppStore
#
#  Created by production on 11/04/2016.
#  Copyright (c) 2016 production. All rights reserved.
#

from Foundation import *
from AppKit import *

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
