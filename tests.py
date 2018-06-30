import unittest
from pset1 import *

class TestAssign1(unittest.TestCase):

    def test_permute_01(self):
        self.assertEqual(permute("a"), 'a')

    def test_permute_02(self):
        self.assertEqual(permute("ab"), ['ab', 'ba'])

    def test_permute_03(self):
        self.assertEqual(permute("abc"), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_permute_04(self):
        self.assertEqual(permute("abcd"), ['abcd', 'abdc', 'acbd', 'acdb', \
            'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', \
            'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', \
            'dbac', 'dbca', 'dcab', 'dcba'])

    def test_permute_05(self):
        self.assertEqual(permute("abcde"), ['abcde', 'abced', 'abdce', \
            'abdec', 'abecd', 'abedc', 'acbde', 'acbed', 'acdbe', 'acdeb', \
            'acebd', 'acedb', 'adbce', 'adbec', 'adcbe', 'adceb', 'adebc', \
            'adecb', 'aebcd', 'aebdc', 'aecbd', 'aecdb', 'aedbc', 'aedcb', \
            'bacde', 'baced', 'badce', 'badec', 'baecd', 'baedc', 'bcade', \
            'bcaed', 'bcdae', 'bcdea', 'bcead', 'bceda', 'bdace', 'bdaec', \
            'bdcae', 'bdcea', 'bdeac', 'bdeca', 'beacd', 'beadc', 'becad', \
            'becda', 'bedac', 'bedca', 'cabde', 'cabed', 'cadbe', 'cadeb', \
            'caebd', 'caedb', 'cbade', 'cbaed', 'cbdae', 'cbdea', 'cbead', \
            'cbeda', 'cdabe', 'cdaeb', 'cdbae', 'cdbea', 'cdeab', 'cdeba', \
            'ceabd', 'ceadb', 'cebad', 'cebda', 'cedab', 'cedba', 'dabce', \
            'dabec', 'dacbe', 'daceb', 'daebc', 'daecb', 'dbace', 'dbaec', \
            'dbcae', 'dbcea', 'dbeac', 'dbeca', 'dcabe', 'dcaeb', 'dcbae', \
            'dcbea', 'dceab', 'dceba', 'deabc', 'deacb', 'debac', 'debca', \
            'decab', 'decba', 'eabcd', 'eabdc', 'eacbd', 'eacdb', 'eadbc', \
            'eadcb', 'ebacd', 'ebadc', 'ebcad', 'ebcda', 'ebdac', 'ebdca', \
            'ecabd', 'ecadb', 'ecbad', 'ecbda', 'ecdab', 'ecdba', 'edabc', \
            'edacb', 'edbac', 'edbca', 'edcab', 'edcba'])

    def test_permute_06(self):
        self.assertEqual(permute(""), [""]) 

    def test_is_reachable_01(self):
        self.assertTrue(is_reachable(250))

    def test_is_reachable_02(self):
        self.assertTrue(is_reachable(84))

    def test_is_reachable_03(self):
        self.assertFalse(is_reachable(97))

    def test_is_reachable_04(self):
        self.assertFalse(is_reachable(92))

    def test_is_reachable_05(self):
        self.assertFalse(is_reachable(876))


if __name__ == "__main__":
    unittest.main()
