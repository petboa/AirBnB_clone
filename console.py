#!/usr/bin/env python3
import cmd
"""
Hbnb Console
==================
This module is a Command Line Interpretor for an AirBnb Clone

Example Usage:
----------------


Class:
-----

- HbnbConsole: The class of the interpretor. It inherits the cmd.Cmd class

    Attributes:
        prompt (str) : Prompt
        last_output (str) : Previous Output

    Methods:

    - do_quit(self, arg):
         Quit the program

    - do_EOF(self, arg):
         Quit the program

    - help_quit(self):
         Shows how to use the 'quit' command

    - help_EOF(self):
         Shows how to use the 'EOF' command
"""

# Beginning of code starts here


class HbnbConsole(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quits Hello Shell

        Args:
            None

        Returns:
            True

        Usage:
        ./console.py
         Welcome to HelloShell CLI
         ===========================
         HelloShell: quit
         Quitting HelloShell...
        """
        return True

    def do_EOF(self, arg):
        """
        Quits Hello Shell

        Args:
            None

        Returns:
            True

        Usage:
        ./console.py
         Welcome to HelloShell CLI
         ===========================
         HelloShell: EOF
         Quitting HelloShell...
        """
        return True

# Doc Functions

    def help_quit(self):
        """
        Shows how to use the 'quit' command

        Args:
            None

        Returns:
            None

        Usage:
            ./console.py
            Welcome to HelloShell CLI
            ===========================
            HelloShell: help quit
            type quit
            Quits Hello Shell
            HelloShell:
        """
        print("type quit\nQuits Hello Shell")

    def help_EOF(self):
        """
        Shows how to use the 'EOF' command

        Args:
            None

        Returns:
            None

        Usage:
            ./console.py
            Welcome to HelloShell CLI
            ===========================
            HelloShell: help EOF
            type quit
            Quits Hello Shell
            HelloShell:
        """
        print("EOF or 'CTRL + D'\nQuits Hello Shell")


if __name__ == '__main__':
    HbnbConsole().cmdloop()
