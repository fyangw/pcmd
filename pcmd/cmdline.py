# -*- coding: UTF-8 -*-
"""
Command line entry

Authors: fyangw
Date:    2018/10/14
"""

from __future__ import division
from __future__ import with_statement
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

__all__ = [
    'main',
]

def main(args=None):
    """main"""
    from . import demo
    if args is None:
        import sys
        args = sys.argv[1:]

    d = demo.Demo()
    return d.run(*args)

