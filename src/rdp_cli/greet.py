from numba import jit
import click
import numpy as np
import time


x = np.arange(100).reshape(10, 10)

@jit(nopython=True)
def go_fast(a): # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

@click.command()
@click.option("--who", default="world")
def rdap(who):
    start = time.time()
    go_fast(x)
    end = time.time()
    dt = end-start
    click.echo(f"Hey {who}, it take {dt}s to run the demo!")

