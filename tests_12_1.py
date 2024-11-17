import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        a_walker = runner.Runner('walker')
        for i in range(0, 10):
            a_walker.walk()
        self.assertEqual(a_walker.distance, 50)

    def test_run(self):
        a_runner = runner.Runner('runner')
        for i in range(0, 10):
            a_runner.run()
        self.assertEqual(a_runner.distance, 100)

    def test_challenge(self):
        a_walker = runner.Runner('walker')
        a_runner = runner.Runner('runner')
        for i in range(0, 10):
            a_walker.walk()
            a_runner.run()
        self.assertNotEqual(a_runner.distance, a_walker.distance)
