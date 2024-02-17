#!/usr/bin/python3
"""The entry point for the command interpreter"""
import re
import os
#import models
import json
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
from models import storage
from shlex import split
import faulthandler; faulthandler.enable()

def tknize(line: str) -> list:
    """A string delimited by space is split into tokens"""
    tkn = re.split(r"[ .(),]", line)
    return tkn


class HBNBCommand(cmd.Cmd):
    """The class console"""
    prompt = '(hbnb) '

    def handle_errors(self, line, n_args):
        """Display the error messages to the user"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        err = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(err[0])
            return 1
        args = line.split()
        if n_args >= 1 and args[0] not in classes:
            print(err[1])
            return 1
        elif n_args == 1:
            return 0
        if n_args >= 2 and len(args) < 2:
            print(err[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if n_args >= 2 and key not in d:
            print(err[3])
            return 1
        elif n_args == 2:
            return 0
        if n_args >= 4 and len(args) < 3:
            print(err[4])
            return 1
        if n_args >= 4 and len(args) < 4:
            print(err[5])
            return 1
        return 0

    def empty_line(self, line):
        """Remove empty lines"""
        return False

    def do_quit(self, line):
        """The 'quit' command handler"""
        return True

    def do_EOF(self, line):
        """Handle ctrl+d to quit command interpreter"""
        return True

    def do_create(self, line):
        """Handles creation of new @cls_name class instances
        and prints the new ID instances
        """
        if (self.handle_errors(line, 1) == 1):
            return
        args = line.split(" ")

        obj = eval(args[0])()
        obj.save()

        print(obj.id)

    def do_clear(self, line):
        """Clears screen"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def do_show(self, line):
        """To print an instance string representation"""
        if (self.handle_errors(line, 2) == 1):
            return
        args = line.split()
        d = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(d[key])

    """
    def do_destroy(self, line):
        Removes a certain class instance
        if (self.handle_errors(line, 2) == 1):
            return
        args = line.split()
        d = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        del d[key]
        storage.save()
    """

    def do_destroy(self, arg: str) -> None:
        """Deletes an instance based on the class name and id"""

        tkn = tknize(arg)
        if arg == "":
            print("** class name missing **")
        elif tkn[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        elif len(tkn) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tkn[0], tkn[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Displays all or certain class instances"""
        d = storage.all()
        if not line:
            print([str(x) for x in d.values()])
            return
        args = line.split()
        if (self.handle_errors(line, 1) == 1):
            return
        print([str(v) for v in d.values()
               if v.__class__.__name__ == args[0]])

    def do_update(self, line):
        """Adds or updates an attribute to an
        instance based on the class name or id
        """
        if (self.handle_errors(line, 4) == 1):
            return
        args = line.split()
        d = storage.all()
        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        attr_k = args[2]
        attr_v = args[3]
        try:
            if attr_v.isdigit():
                attr_v = int(attr_v)
            elif float(attr_v):
                attr_v = float(attr_v)
        except ValueError:
            pass
        class_attr = type(d[key]).__dict__
        if attr_k in class_attr.keys():
            try:
                attr_v = type(class_attr[attr_k])(attr_v)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(d[key], attr_k, attr_v)
        storage.save()

    def my_count(self, class_n):
        """Counts instances of a certain class"""
        count_inst = 0
        for instance_object in storage.all().values():
            if instance_object.__class__.__name__ == class_n:
                count_inst += 1
        print(count_inst)

    def default(self, line):
        """"Handle the commands"""
        names = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]
        commands = {"all": self.do_all,
                    "count": self.my_count,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "update": self.do_update}

        args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if args:
            args = args.groups()
        if not args or len(args) < 2 or args[0] not in names \
                or args[1] not in commands.keys():
            super().default(line)
            return

        if args[1] in ["all", "count"]:
            commands[args[1]](args[0])
        elif args[1] in ["show", "destroy"]:
            commands[args[1]](args[0] + ' ' + args[2])
        elif args[1] == "update":
            prms = re.match(r"\"(.+?)\", (.+)", args[2])
            if prms.groups()[1][0] == '{':
                dic_p = eval(prms.groups()[1])
                for k, v in dic_p.items():
                    commands[args[1]](args[0] + " " + prms.groups()[0] +
                                      " " + k + " " + str(v))
            else:
                rest = prms.groups()[1].split(", ")
                commands[args[1]](args[0] + " " + prms.groups()[0] + " " +
                                  rest[0] + " " + rest[1])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
