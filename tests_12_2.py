import unittest
import main
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = main.Runner('Усейн', 10)
        self.runner_2 = main.Runner('Андрей', 9)
        self.runner_3 = main.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):

        for res in cls.all_results:
            print(res)

    def testTournament1(self):
        qwerty = main.Tournament(90, self.runner_1, self.runner_3)

        self.all_results.append(qwerty.start())
        self.assertTrue(self.all_results[-1][2] == 'Ник')

    def testTournament2(self):
        qwerty = main.Tournament(90, self.runner_2, self.runner_3)

        self.all_results.append(qwerty.start())
        self.assertTrue(self.all_results[-1][2] == 'Ник')

    def testTournament3(self):
        qwerty = main.Tournament(90, self.runner_1, self.runner_2, self.runner_3)

        self.all_results.append(qwerty.start())
        self.assertTrue(self.all_results[-1][3] == 'Ник')


