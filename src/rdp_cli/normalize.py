from operator import delitem
from utils.IO import load_data
from datatable import f
import datatable as dt
import numpy as np
import click


def _normalize(DT, col, mode):

    Cl = DT[:, col]
    rest = DT[:, [col != x for x in DT.names]]
    if mode == "minmax":
        min = (int)(Cl[:, dt.min(f[col])][0,0])
        max = (int)(Cl[:, dt.max(f[col])][0,0])
        for i in range(Cl.nrows): 
            if Cl[i,0]: Cl[i,0] = (int)((Cl[i,0]-min)/(max-min))
    elif mode == "std":
        mean = Cl[:, dt.mean(f[col])][0,0] 
        sd = Cl[:, dt.sd(f[col])][0,0]
        for i in range(Cl.nrows): 
            if Cl[i,0]: Cl[i,0] = (int)((Cl[i,0]-mean)/sd)

    Cl.cbind(rest)

    return Cl        


@click.command()
@click.option("--mode", default="minmax")
@click.option("--file")
@click.option("--col")
def normalize(mode, file, col):
    changed = False
    data = load_data(file)
    # try:
    #     col = int(col)
    # except:
    #     click.echo("only integer allowed for col!")
    #     return

    if mode in {"minmax", "std"}:
        data = _normalize(data, col, mode)
        changed = True
    else:
        click.echo("mode is invalid!")
    
    if changed == True:
        data.to_csv(file)
        click.echo("Success!")




