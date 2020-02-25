import unittest
import task



class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testArea(self):
        expected = 3.14
        self.assertAlmostEqual(expected, task.circleArea(1))


if __name__ == "__main__":
    unittest.main()
