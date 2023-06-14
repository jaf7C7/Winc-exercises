# USAGE:
#
# superpy report [ inventory | revenue | profit | date ] [ --today | --tomorrow | --yesterday | --date <date=today> ]
# superpy buy --product <name> --price <price> --quantity <quantity=1> [ --expires <date=None> ]
# superpy sell --product <name> --price <price> --quantity <quantity=1>
# superpy set-date <date>
# superpy advance-date [<days=1> ]
# superpy list-expired [ --today | --tomorrow | --yesterday | --date <date=today> ]

from super import *


class TestParseArgs:
    def test_report(self):
        for subject in "inventory", "revenue", "profit", "date":
            for when in (
                "--today",
                "--tomorrow",
                "--yesterday",
                "--date 2060-05-30",
            ):
                args = parse_args(f"report {subject} {when}".split())
                assert args.subcommand == "report" and args.subject == subject
                if when == "--today":
                    assert args.today == True
                elif when == "--yesterday":
                    assert args.yesterday == True
                elif when == "--tomorrow":
                    assert args.tomorrow == True
                else:
                    assert hasattr(args, "date")

