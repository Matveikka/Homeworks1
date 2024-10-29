import unittest
import Runner1 as R1
import Runner as R
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = R.Runner('Bob')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner1 = R.Runner('Bob')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = R.Runner('Bob')
        runner2 = R.Runner('Frank')
        for i in range(10):
            runner1.walk()
            runner2.run()
            self.assertNotEqual(runner1, runner2)
class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t1 = R1.Tournament(90, self.runner1, self.runner3)
        result = t1.start()
        self.assertTrue(result[2], self.runner3)
        self.all_results['test_tournament_1'] = result

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t2 = R1.Tournament(90, self.runner2, self.runner3)
        result = t2.start()
        self.assertTrue(result[2], self.runner3)
        self.all_results['test_tournament_2'] = result

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t3 = R1.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = t3.start()
        self.assertTrue(result[3], self.runner3)
        self.all_results['test_tournament_3'] = result

if __name__ == '__main__':
    unittest.main()