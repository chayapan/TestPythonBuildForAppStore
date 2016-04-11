# -*- coding: utf-8 -*-
#
#  main.py
#  TestPythonBuildForAppStore
#
#  Created by production on 11/04/2016.
#  Copyright (c) 2016 production. All rights reserved.
#

# import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import AppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
