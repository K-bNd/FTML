"""
Study the law of large numbers on a simple random variable and compare the speed
of using loops versus array operations
"""

import numpy as np
import cProfile
import pstats


# instantiate a Pseudo-random number generator (PRNG)
rng = np.random.default_rng()


def empirical_average_loop(n_samples: int) -> float:
    result = 0
    for _ in range(n_samples):
        z1_sample = rng.uniform(1, 2) ** 2
        result += z1_sample
    return result / n_samples


def empirical_average_array(n_samples: int) -> float:
    """
    EDIT THIS FUNCTION
    """
    return 1


def main() -> None:
    n_samples = int(1e5)
    print(empirical_average_loop(n_samples=n_samples))
    print(empirical_average_array(n_samples=n_samples))


if __name__ == "__main__":
    # enable profiling
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    # save profiling to file
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumtime")
    stats_data_file = "profile.prof"
    stats.dump_stats(stats_data_file)
