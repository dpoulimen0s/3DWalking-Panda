from . import panda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--no-panda", help="Panda Disappears",
                        action="store_true")
    parser.add_argument("--small-panda", help="Small Panda",
                        action="store_true")
    parser.add_argument("--giant-panda", help="Giant Panda",
                        action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
