from concurrent.futures import thread
from email.policy import default
from utils.IO import load_data
import datatable as dt
from datatable import f
import datatable.models as dtm
import numpy as np
import os
import click




@click.command()
@click.argument('data')
@click.option("--threshold", default = 0)
def nzv(data, threshold = 0):
    if threshold == 0:
        threshold = 1e-6
    df = load_data(data)
    names = df.names
    remove = []
    for col in names:
        if df[:, dt.sd(f[col])][0,0] < threshold:
           remove.append(col) 

    del df[:, remove]

    df.to_csv(data)
    click.echo("Success!")