from operator import delitem
from utils.IO import load_data
from datatable import f
import datatable as dt
import numpy as np
import click


def _impute(DT, col, fun):

    funs_dict = {"mean": dt.mean, "median": dt.median}

    Cl = DT[:, col]
    rest = DT[:, [col != x for x in DT.names]]
    if fun != "zero":

        m = Cl[:, funs_dict[fun](f[col])][0,0]
        if Cl.stype == dt.stype.int32 or Cl.stype == dt.stype.int64:
            m = int(m)
        
        Cl.replace(None, m)
    else:
        Cl = Cl[:,f[:].extend({f"{col}_ind": f[col] == None})]
        Cl.replace(None, 0)
    
    Cl.cbind(rest)

    return Cl        


@click.command()
@click.option("--method", default="mean")
@click.option("--file")
@click.option("--col")
def impute(method, file, col):
    changed = False
    data = load_data(file)
    # try:
    #     col = int(col)
    # except:
    #     click.echo("only integer allowed for col!")
    #     return

    if method in {"mean", "median", "zero"}:
        data = _impute(data, col, method)
        changed = True
    else:
        click.echo("method not impletemented")
    
    if changed == True:
        data.to_csv(file)
        click.echo("Success!")




