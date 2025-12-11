# test_defiyieldfetch.py
"""
Tests for DefiYieldFetch module.
"""

import unittest
from defiyieldfetch import DefiYieldFetch

class TestDefiYieldFetch(unittest.TestCase):
    """Test cases for DefiYieldFetch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DefiYieldFetch()
        self.assertIsInstance(instance, DefiYieldFetch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DefiYieldFetch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
