import cProfile

def slow_function():
    time.sleep(2)

def fast_function():
    time.sleep(0.5)

def main():
    for _ in range(3):
        slow_function()
        fast_function()

if __name__ == "__main__":
    cProfile.run('main()')
