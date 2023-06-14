# USAGE:
#
# superpy report [ inventory | revenue | profit | date ] [ --today | --yesterday | --date <date> ]
# superpy buy --product <name> --price <price> --quantity <quantity> [ --expires <date> ]
# superpy sell --product <name> --price <price> --quantity <quantity>
# superpy set-date <date>
# superpy advance-date <days>
# superpy list-expired [ --date <date> | --today | --tomorrow ]
#
# DEFAULTS:
# <no args> defaults to 'help'
# <when> defaults to '--today'
# '--quantity' defaults to 1
# 'advance-date' defaults to 1


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

