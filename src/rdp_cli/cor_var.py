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
@click.argument("data")
@click.option("--threshold", default = 0.8)
def cor_rm(data, threshold):
    df = load_data(data)
    names = df.names
    remove = []
    for i, col in enumerate(names):
        if i+1 > len(names)-1: break

        cor_df = df[:, dt.corr(f[col], f[names[i+1:]])]
        rhs = names[i+1:]
        # break
        for j, n in enumerate(rhs):
            # print(j)
            if cor_df[0, j] == None:
                click.secho("Warning: some column may have zero variance!", fg = "yellow")
                continue
            elif cor_df[0, j] > threshold:
                remove.append(n)

    del df[:, remove]

    df.to_csv(data)
    click.echo("Success!")


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
        try:
            if df[:, dt.sd(f[col])][0,0] < threshold:
                remove.append(col) 
        except:
            click.secho("String columns are skipped!", fg = "yellow")

    del df[:, remove]

    df.to_csv(data)
    click.echo("Success!")