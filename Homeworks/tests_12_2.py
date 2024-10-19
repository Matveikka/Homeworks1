import Runner1 as R1
import unittest
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = R1.Runner('Usain', 10)
        self.runner2 = R1.Runner('Andrew', 9)
        self.runner3 = R1.Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f'{i}: {j}')

    def start_tournament_1(self):
        t1 = R1.Tournament(90, self.runner1, self.runner3)
        all_results = t1.start()
        self.assertTrue(all_results[2], self.runner3)

    def start_tournament_2(self):
        t2 = R1.Tournament(90, self.runner2, self.runner3)
        all_results = t2.start()
        self.assertTrue(all_results[2], self.runner3)

    def start_tournament_3(self):
        t3 = R1.Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results = t3.start()
        self.assertTrue(all_results[3], self.runner3)

if __name__ == '__main__':
    unittest.main()