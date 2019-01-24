#!/usr/bin/env python
# encoding: utf-8


import argparse

parser = argparse.ArgumentParser(description="just test for argparse")
# parser.add_argument('echo')
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
parser.add_argument('-x', "--xint", default=1, type=int, help="the int for x")
args = parser.parse_args()
# print(args.echo)
if args.verbosity:
    print("verbosity turned on " + str(args.verbosity))
if args.xint:
    answer = args.xint ** 2
    print(answer)
