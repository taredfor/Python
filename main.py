import unittest


class Test1:
    def __init__(self):
        self.l1 = []
        self.l2 = ['1, 2']
        self.l3 = ['1, 2']
        self.l4 = ['3, 4']


class TestService(unittest.TestCase):

    def test_1(self):
        self.test_1 = Test1()
        self.test_1.l1.append('1, 2')
        self.assertEqual(self.test_1.l1, self.test_1.l2)
        self.test_1.l3.extend(self.test_1.l4)
        self.assertEqual(self.test_1.l3, ['1, 2', '3, 4'])


if __name__ == '__main__':
    unittest.main()


