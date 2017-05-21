# -*- coding: utf-8 -*-



import unittest as ut


if __name__ == '__main__':
    if __package__ is None:
        from os import path as op
        import sys
        
        
        _path = op.dirname(op.abspath(__file__))
        _parent, __package__ = op.split(_path)
        
        sys.path.insert(1, _parent)
        
        __import__(__package__, globals(), locals(), [], 0)
    
    
    from . import *
    
    
    ut.main()
