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
        for key in sorted(cls.all_results.keys()):
            result_dict = cls.all_results[key]
            formatted_result = {i: j.name for i, j in result_dict.items()}
            print(formatted_result)

    def test_tournament_1(self):
        t1 = R1.Tournament(90, self.runner1, self.runner3)
        result = t1.start()
        self.assertTrue(result[2], self.runner3)
        self.all_results['test_tournament_1'] = result

    def test_tournament_2(self):
        t2 = R1.Tournament(90, self.runner2, self.runner3)
        result = t2.start()
        self.assertTrue(result[2], self.runner3)
        self.all_results['test_tournament_2'] = result

    def test_tournament_3(self):
        t3 = R1.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = t3.start()
        self.assertTrue(result[3], self.runner3)
        self.all_results['test_tournament_3'] = result

if __name__ == '__main__':
    unittest.main()

