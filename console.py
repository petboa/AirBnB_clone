#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.reviews import Review


class MyCommand(cmd.Cmd):
    intro = 'Welcome to the My Console. Type help or ? to list commands.\n'
    prompt = '(myconsole) '
    file = None

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        if arg == '':
            print('** class name missing **')
        elif arg not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print('** class doesn\'t exist **')
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        if arg == '':
            print('** class name missing **')
        elif arg not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print('** class doesn\'t exist **')
        elif ' ' not in arg:
            print('** instance id missing **')
        else:
            args = arg.split(' ')
            try:
                obj = eval(args[0]).get(args[1])
                print(obj)
            except:
                print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        objects = []
        if arg not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'] and arg != '':
            print('** class doesn\'t exist **')
        else:
            for obj in storage.all().values():
                if arg == '' or arg == type(obj).__name__:
                    objects.append(str(obj))
            print(objects)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
        if arg == '':
            print('** class name missing **')
        elif arg not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print('** class doesn\'t exist **')
        elif ' ' not in arg:
            print('** instance id missing **')
        else:
            args = arg.split(' ')
            try:
                obj = eval(args[0]).get(args[1])
                obj.delete()
                storage.save()
            except:
                print('** no instance found **')

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""

        if arg == '':
            print('** class name missing **')
        elif arg not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print('** class doesn\'t exist **')
        elif ' ' not in arg:
            print('** instance id missing **')
        else:
            args = arg.split(' ')
            try:
                obj = eval(args[0]).get(args[1])
                if len(args) == 2:
                    print('** attribute name missing **')
                elif len(args) == 3:
                    print('
