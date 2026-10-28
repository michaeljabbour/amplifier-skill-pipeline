#!/usr/bin/env python3
"""Meaningful local functional checks; no provider calls or production activation."""
import asyncio
import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

m=load('apr',ROOT/'skills/pipeline/scripts/apr.py')
def fixture():
    return {'apr':{'version':'1.0','stages':[{'name':'ci','jobs':[{'name':'test','runner':'ubuntu-latest','timeout_minutes':10,'steps':[{'type':'run','command':'python -m unittest'}]}]},{'name':'release','depends_on':['ci'],'jobs':[{'name':'publish','runner':'ubuntu-latest','timeout_minutes':5,'steps':[{'type':'run','command':'build-only'}]}]}]}}
class Gate(unittest.TestCase):
    def test_valid_dependency_design(self):self.assertTrue(m.validate(fixture())['valid'])
    def test_cross_stage_cycle_is_rejected(self):
        f=fixture();f['apr']['stages'][0]['jobs'][0]['depends_on']=['publish'];r=m.validate(f)
        self.assertFalse(r['valid']);self.assertIn('Job/stage dependency cycle',r['errors'])
    def test_undeclared_secret_and_unknown_artifact_consumer(self):
        f=fixture();f['apr']['stages'][0]['jobs'][0]['steps'][0]['secrets']=['MISSING'];f['apr']['artifacts']=[{'name':'build','produced_by':'test','consumed_by':['absent']}]
        r=m.validate(f);self.assertFalse(r['valid']);self.assertTrue(any('Undeclared secret' in x for x in r['errors']));self.assertTrue(any('consumer missing' in x for x in r['errors']))

if __name__=='__main__':unittest.main(verbosity=2)
