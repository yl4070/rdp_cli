from operator import delitem
from utils.IO import load_data
import numpy as np
import click


def __impute_mean(data, col):
    m = np.nanmean(data[:, col])
    idx = np.argwhere(np.isnan(data[:,col])).tolist()

    for i in idx:
        data[i[0], col] = m
    
    return data

@click.command()
@click.option("--method", default="mean")
@click.option("--file")
@click.option("--col")
def impute(method, file, col):
    changed = False
    data = load_data(file)
    try:
        col = int(col)
    except:
        click.echo("only integer allowed for col!")
        return

    if method == "mean":
        data = __impute_mean(data, col)
        changed = True
    else:
        click.echo("method not impletemented")
    
    if changed == True:
        np.savetxt(file, data, delimiter=",")
        click.echo("Success!")




