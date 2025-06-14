#!/usr/bin/env python
'''
The execute function for unittests
'''

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

import unittest

class TestMethods(unittest.TestCase):
    '''
    Test
    '''

    def test_foo(self):
        '''
        A temp test
        '''

        self.assertEqual('FOO'.lower(), 'foo')


if __name__ == '__main__':
    unittest.main()
