# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# USAGE:
#
# superpy report [ inventory | revenue | profit | date ] [ --today | --yesterday | --date <date> ]
# superpy buy --product <name> --price <price> --quantity <quantity> --expires <date>
# superpy sell --product <name> --price <price> --quantity <quantity>
# superpy --set-date <date>
# superpy --advance-date <days>
# superpy --list-expired [<date>]


import argparse
import csv
from datetime import date


def main():
    pass


# TODO:
# def parse_args(args):
# def report(subject, when):
# def buy(product, quantity, price, expires):
# def sell(product, price, quantity):
# def set_date(date):
# def advance_date(days):
# def list_expired(date):


if __name__ == "__main__":
    main()
