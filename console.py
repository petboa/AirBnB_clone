#!/usr/bin/env python3
"""
Hbnb Console
==================
This module is a Command Line Interpretor for an AirBnb Clone

Example Usage:
----------------


Class:
-----

"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place_amenity import PlaceAmenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Beginning of code starts here


class HBNBCommand(cmd.Cmd):
    """
- HBNBCommand: The class of the interpretor.
    It inherits the cmd.Cmd class

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

    prompt = '(hbnb) '

    def precmd(self, line: str):
        if '.' in line:
            obj, command = line.split(".")

            verb, attrs = command.split('(')
            attrs = attrs.replace(')', '').replace('"', '')\
                .replace('\'', '')
            line = f'{verb} {obj} {attrs}'
        return line

    def do_create(self, line):
        """Creates an instance"""
        if len(line) == 0:
            print('** class name missing **')
        elif line not in storage.models.keys():
            print("** class doesn't exist **")
        else:
            new_obj = storage.models[line]()
            new_obj.save()
            print(new_obj.id)

    def do_all(self, line):
        """Displays all saved instances"""
        instances = storage.all()
        for _, value in instances.items():
            if len(line) == 0:
                print(value)
            elif value.__class__.__name__ == line:
                print(value)
        if line not in storage.models.keys():
            print("** class doesn't exist **")

    def do_count(self, line):
        """Counts the number of a specific model saved"""
        instances = storage.all()
        if len(line) == 0:
            print(len(instances))
        if line not in storage.models.keys():
            print("** class doesn't exist **")
        else:
            counter = 0
            for _, value in instances.items():
                if value.__class__.__name__ == line:
                    counter += 1
            print(counter)

    def do_show(self, line):
        """Shows a single instance"""
        print(line)
        words = line.split()
        if len(words) == 2:
            found = False
            obj, obj_id = words
            if obj not in storage.models.keys():
                print("** class doesn't exist **")
            else:
                for value in storage.all().values():
                    if value.id == obj_id and\
                            value.__class__.__name__ == obj:
                        print(value)
                        found = True
            if not found:
                print('** no instance found **')

        elif len(words) == 1 and words[0]\
                not in storage.models.keys():
            print("** class doesn't exist **")
        elif len(words) == 1:
            print('instance id missing')
        else:
            print('** class name missing **')

    def do_update(self, line):
        """Updates an instance"""
        words = line.split()
        if len(words) == 4:
            found = False
            obj, obj_id, attribute, new_value = words
            if obj not in storage.models.keys():
                print("** class doesn't exist **")
            else:
                for value in storage.all().values():
                    if value.id == obj_id and\
                            value.__class__.__name__ == obj:
                        key = obj + '.' + obj_id
                        setattr(storage.all()[key], attribute, new_value)
                        found = True
            if not found:
                print('** no instance found **')

        elif len(words) == 1 and words[0] \
                not in storage.models.keys():
            print("** class doesn't exist **")
        elif len(words) == 1:
            print('instance id missing')
        elif len(words) == 2:
            print('** attribute name missing **')
        elif len(words) == 3:
            print('** value missing **')
        else:
            print('** class name missing **')
        storage.save()

    def do_destroy(self, line):
        """Deletes an instance"""
        words = line.split()
        if len(words) == 2:
            obj, obj_id = words
            if obj not in storage.models.keys():
                print(" class doesn't exist")
            else:
                try:
                    del storage.all()[f'{obj}.{obj_id}']
                    storage.save()
                except KeyError:
                    print('** no instance found **')

        elif len(words) == 1:
            print('instance id missing')
        else:
            print('** class name missing **')

    def emptyline(self):
        """No command"""
        pass

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
        sys.exit(0)

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
        sys.exit(0)

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
    HBNBCommand().cmdloop()
