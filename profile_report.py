import cProfile
import pstats

def slow_function():
    time.sleep(2)

def fast_function():
    time.sleep(0.5)

def main():
    for _ in range(3):
        slow_function()
        fast_function()

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    profiler.dump_stats('profil_output.prof')

    with open("profil_output.txt", "w") as f:
        ps = pstats.Stats(profiler, stream=f)
        ps.strip_dirs().sort_stats('cumulative').print_stats()
