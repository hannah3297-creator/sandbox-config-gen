"""Sandbox Config Gen — Generate a Windows Sandbox .wsb file with a mapped folder and networking flag."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='sandbox_config_gen',
        description='Generate a Windows Sandbox .wsb file with a mapped folder and networking flag.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Sandbox Config Gen')
    print('A .wsb you can double-click.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
