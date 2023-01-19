#!/usr/bin/env python3
import time
from tqdm import tqdm

# Example 1: Simple progress bar for a for loop
for i in tqdm(range(100)):
    # Do something
    time.sleep(0.01)
    pass

# Example 2: Progress bar for an iterable
items = [1, 2, 3, 4, 5]
for item in tqdm(items):
    # Do something
    time.sleep(0.01)
    pass

# Example 3: Progress bar with manual updates
pbar = tqdm(total=100)
for i in range(10):
    # Do something
    time.sleep(0.01)
    pbar.update(10)
pbar.close()

# Example 4: Progress bar with a description
for i in tqdm(range(100), desc='Example 4'):
    # Do something
    time.sleep(0.01)
    pass

# Example 5: Progress bar as a context manager
with tqdm(total=100) as pbar:
    for i in range(10):
        # Do something
        time.sleep(0.01)
        pbar.update(10)

# Example 6: Progress bar with nested loops
for i in tqdm(range(10)):
    for j in tqdm(range(100), leave=False):
        # Do something
        time.sleep(0.01)
        pass
