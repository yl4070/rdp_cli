from utils.IO import load_data
import datatable as dt
import datatable.models as dtm
import numpy as np
import os
import click



@click.command()
@click.option("--nsplits", default="3")
@click.option("--seed", default="1")
@click.argument("data")
def kfold_split(data, nsplits, seed):
    if not os.path.isdir("folds"):
        os.mkdir("folds")

    df = load_data(data) 
    kf = dtm.kfold_random(nrows = df.nrows, nsplits= int(nsplits), seed = int(seed))

    for i, fold in enumerate(kf):
        
        df[fold[0], :].to_csv(f"folds/train{i}.csv")
        df[fold[1], :].to_csv(f"folds/test{i}.csv")
    
    click.echo("Success!")



