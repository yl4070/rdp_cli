from operator import delitem
from utils.IO import load_data
from datatable import f,as_type
import datatable as dt
import numpy as np
import click


def _normalize(DT, col, mode):

    Cl = DT[:, col]
    
    rest = DT[:, [col != x for x in DT.names]]
    if mode == "minmax":
        min = Cl[:, dt.min(f[col])][0,0]
        max = Cl[:, dt.max(f[col])][0,0]
        # xnew = (x-min)/(max-min)
        for i in range(Cl.nrows): 
            if Cl[i,0]: Cl[i,0] = as_type((Cl[i,0]-min)/(max-min), Cl.stype)
    elif mode == "std":
        mean = Cl[:, dt.mean(f[col])][0,0] 
        sd = Cl[:, dt.sd(f[col])][0,0]
        # xnew = (x-mean)/standard_derivation
        for i in range(Cl.nrows): 
            if Cl[i,0]: Cl[i,0] = as_type((Cl[i,0]-mean)/sd, Cl.stype)

    Cl.cbind(rest)

    return Cl        


@click.command()
@click.option("--mode", default="minmax")
@click.argument("file")
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




