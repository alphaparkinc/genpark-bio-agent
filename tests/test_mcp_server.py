# -*- coding: utf-8 -*-
import unittest
from genpark_bio.server import run_test

class TestMCPServer(unittest.TestCase):
    def test_mcp_self_test(self):
        self.assertTrue(run_test())

if __name__ == "__main__":
    unittest.main()
