from operator import delitem
from utils.IO import load_data
from datatable import f, as_type
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
@click.argument("file")
@click.option("--col")
@click.option("--force_int", is_flag = True)
@click.option("--force_float", is_flag = True)
def impute(method, file, col, force_int = False, force_float = False):
    changed = False
    if force_float == force_int == True:
        click.echo("Not possible...") 
        return

    data = load_data(file)
    if force_float:
        c = data[:, as_type(f[col], float)]
        data[col] = c
    elif force_int:
        c = data[:, as_type(f[col], int)]
        data[col] = c
        
    # try:
    #     col = int(col)
    # except:
    #     click.echo("only integer allowed for col!")
    #     return

    if method in {"mean", "median", "zero"}:
        data = _impute(data, col, method)
        changed = True
    elif method == "dummy":
        changed = True
    else:
        click.echo("method not impletemented")

    if changed == True:
        data.to_csv(file)
        click.echo("Success!")




