#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.reviews import Review


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the AirBnB console. Type help or ? to list commands.\n'
    prompt = '(malik)'
    file = None

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            args = arg.split("")
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        elif arg.find(' ') == -1:
            print('** instance id missing **')
        elif arg.id != 'BaseModel':
            print('** no instance found **')
        else:
            obj = BaseModel()
            obj.__str__()
            print(obj)

    def do_eof(self, arg):
        'Exit the console'
        print('Thank you for using AirBnB')
        return -1

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            obj = BaseModel()
            obj.__str__()
            for i in obj:
                print(i)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        elif arg.find(' ') == -1:
            print('** instance id missing **')
        elif arg.id != 'BaseModel':
            print('** no instance found **')
        else:
            obj = BaseModel()
            obj.delete()

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""

        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        elif arg.find(' ') == -1:
            print('** instance id missing **')
        elif arg.id != 'BaseModel':
            print('** no instance found **')
        elif arg.find(' ') == -1:
            print('** attribute name missing **')
        elif arg.find(' ') == -1:
            print('** value missing **')
        else:
            arg = arg.split()
            arg[1] = arg[1].replace('"', '')
            arg[2] = arg[2].replace('"', '')
            obj = BaseModel()
            obj.__dict__[arg[1]] = arg[2]
            obj.save()
            obj.__str__()
            print(obj)

    def do_quit(self, arg):
        'Prints a farewell message and exits the console'
        print('Thank you for using AirBnB')
        return -1

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        pass

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'
        cmd.Cmd.do_help(self, arg)

    def default(self, line):
        'Called on an input line when the command prefix is not recognized.'
        print('*** Unknown syntax: {}'.format(line))


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
