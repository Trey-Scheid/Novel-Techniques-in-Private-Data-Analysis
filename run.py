#!/usr/bin/env python

import sys
import json

from GD import GD
from SGD import SGD
from FTRLM import FTRLM
from ObjectivePerturbation import ObjPert


def main(targets):
    with open("params.json") as fh:
        params = json.load(fh)

    all_methods = ["gd", "sgd", "ftrlm", "objpert", "outpert"]
    all_objects = [GD, SGD, FTRLM, ObjPert]

    # if no target is specified, run all methods
    target_methods = set(all_methods).intersection(set(targets))
    if len(set(all_methods).intersection(set(targets))) == 0:
        target_methods = all_methods

    combined_df = []
    for method, obj in zip(all_methods, all_objects):
        if method not in target_methods:
            continue

        print(f"Running {method}")
        run = obj(**params)
        combine_df = run.run_all_plots(trials=3, repeats=3)
        combined_df.append(combine_df)

    print(combined_df)


if __name__ == "__main__":
    targets = sys.argv[1:]
    # Targets: gd, sgd, ftrlm, objpert, outpert
    main(targets)
