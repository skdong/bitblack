import cProfile
import pstats
from bitblack.swall.samples import people


def test():
    people.generate(10000000)


def perform():
    cProfile.run("test()", filename="result.out", sort="cumulative")


def show():
    p = pstats.Stats("result.out")
    p.strip_dirs().sort_stats("cumulative", "name").print_stats()


#perform()
show()