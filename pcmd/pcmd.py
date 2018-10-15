#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import division
from __future__ import with_statement
from __future__ import absolute_import
from __future__ import print_function
#from __future__ import unicode_literals

import json
import locale
import os
import sys
import subprocess

class PcmdException(Exception):
  None
  
class Pcmd():
  def __init__(self, debug = False, raise_exception = True):
    self.debug = debug
    self.raise_exception = raise_exception
    
  def run(self, command_line):
    self.command_line = command_line 
    self.output = ''
    self.status = -1

    p = subprocess.Popen('{0} 2>&1'.format(command_line), shell=True, stdout=subprocess.PIPE)
    self.output = p.stdout.read() # Remove codepage adjusting: .decode(locale.getdefaultlocale()[1])
    self.status = p.wait()
    # Replace os.open with subprocess.Popen for Windows supporting
    #p = os.popen(command_line)
    #self.output = p.read().decode(locale.getdefaultlocale()[1]).split('\n')
    #  self.status = p.close()
    #  self.status = 0 if self.status is None else self.status >> 8

    if self.debug:
      print('status:{0} command_line:{1} \noutput:{2}'.format(self.status, self.command_line, self.output))# Remove codepage adjusting .encode('utf8')))
      #Remove json dumps: print(json.dumps((self.status, self.command_line, self.output), indent = 2, ensure_ascii = False))
    if self.raise_exception and self.status:
      raise PcmdException('Return code {0} is not zero, when executing:{1} ; with output {2}'.format(self.status, self.command_line, self.output))
    return self.status

