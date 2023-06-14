# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# USAGE:
#
# superpy report [ inventory | revenue | profit | date ] [ --today | --tomorrow | --yesterday | --date <date=today> ]
# superpy buy --product <name> --price <price> --quantity <quantity=1> [ --expires <date=None> ]
# superpy sell --product <name> --price <price> --quantity <quantity=1>
# superpy set-date <date>
# superpy advance-date [<days=1> ]
# superpy list-expired [ --today | --tomorrow | --yesterday | --date <date=today> ]


import argparse
import csv
from datetime import date


def main():
    pass


def parse_args(args):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand")

    report_parser = subparsers.add_parser("report")
    report_parser.add_argument(
        "subject", choices=["inventory", "revenue", "profit", "date"]
    )
    report_parser.add_argument("--today", action="store_true", default=True)
    report_parser.add_argument("--tomorrow", action="store_true")
    report_parser.add_argument("--yesterday", action="store_true")
    report_parser.add_argument("--date", dest="date")

    buy_parser = subparsers.add_parser("buy")
    buy_parser.add_argument("--product", required=True)
    buy_parser.add_argument("--price", required=True, type=float)
    buy_parser.add_argument("--quantity", type=int, default=1)
    buy_parser.add_argument("--expires")

    sell_parser = subparsers.add_parser("sell")
    sell_parser.add_argument("--product", required=True)
    sell_parser.add_argument("--price", required=True, type=float)
    sell_parser.add_argument("--quantity", type=int, default=1)

    set_date_parser = subparsers.add_parser("set-date")
    set_date_parser.add_argument("date")

    advance_date_parser = subparsers.add_parser("advance-date")
    advance_date_parser.add_argument("days", type=int, nargs="?", default=1)

    return parser.parse_args(args)


# TODO:
# def report(subject, when):
# def buy(product, quantity, price, expires):
# def sell(product, price, quantity):
# def set_date(date):
# def advance_date(days):
# def list_expired(date):


if __name__ == "__main__":
    main()
