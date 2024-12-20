import unittest
import Runner as R

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = R.Runner('Bob')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)
    def test_run(self):
        runner1 = R.Runner('Bob')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)
    def test_challenge(self):
        runner1 = R.Runner('Bob')
        runner2 = R.Runner('Frank')
        for i in range(10):
            runner1.walk()
            runner2.run()
            self.assertNotEqual(runner1, runner2)

if __name__ == '__main__':
    unittest.main()

