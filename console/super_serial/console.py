#!/usr/bin/python3
"""
Console module for the Super Serial Project.
"""

import cmd
from models import storage
from models.base import BaseModel
from models.cereal import Cereal


class SuperSerial(cmd.Cmd):
    """
    Console class for the Super Serial Project.
    """

    prompt = '(SoSerial) '
    classes = {"BaseModel": BaseModel, "Cereal": Cereal}

    def do_EOF(self, arg):
        """
        Exit the console with the EOF command.

        Args:
            arg (str): Arguments passed to the command.

        Returns:
            bool: True to exit the console.
        """
        return True

    def emptyline(self):
        """
        Empty line + ENTER should not execute anything.
        """
        pass

    def default(self, line):
        """
        Method called on an input line when the command prefix is not recognized.

        Args:
            line (str): Input line.

        Returns:
            bool: False to continue the console loop.
        """
        args = line.split(".")
        if len(args) != 2:
            print("** command doesn't exist **")
            return False
        cls_name = args[0]
        method = args[1]
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return False
        if method == "all()":
            self.do_all(cls_name)
        else:
            print("** command doesn't exist **")
        return False

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): Arguments passed to the command.

        Returns:
            bool: True to exit the console.
        """
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel.

        Args:
            arg (str): Arguments passed to the command.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            new_model = globals()[args[0]]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance based on class name and id.

        Args:
            arg (str): Arguments passed to the command.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id.

        Args:
            arg (str): Arguments passed to the command.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances.

        Args:
            arg (str): Arguments passed to the command.
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in globals():
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if len(args) > 0 and args[0] not in globals():
                    if k.split('.')[0] == args[0]:
                        print(str(v))
                else:
                    print(str(v))

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.

        Args:
            arg (str): Arguments passed to the command.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()


if __name__ == '__main__':
    SuperSerial().cmdloop()
