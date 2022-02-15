#! /usr/bin/env python3

"""Entry point."""

from controllers.MainMenuController import MainMenuController


if __name__ == "__main__":
    try:
        MainMenuController()
    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
