# -*- coding: UTF-8 -*-
"""
Demo

Authors: fyangw
Date:    2018/10/11 17:24:38
"""

from __future__ import division
from __future__ import with_statement
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from pcmd.pcmd import Pcmd

class Demo(object):
    """demo"""
    def run(self, name="demo", *args):
        """entrance
        Args:
            name: name
        Returns:
            int
        Raises:
            ValueError: name invalid
        """
        return self.exception_style_example()
        #if not name:
        #    raise ValueError(name)
        #return 0

    def condition_style_example(self):
      cmd = Pcmd(True, True)
      if (cmd.run('ls | grep py')):
        return -1
      if (cmd.run('cat {0}'.format(cmd.output.split('\n')[0]))):
        return -1
      return 0

    def exception_style_example(self):
      cmd = Pcmd(True, True)
      cmd.run('ls | grep py')
      cmd.run('cat {0}'.format(cmd.output.split('\n')[0]))
      return 0

