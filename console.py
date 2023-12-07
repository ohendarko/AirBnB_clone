#!/usr/bin/python3
"""Console module for the command interpreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines  the HBNBCommand interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal exits program cleanly """
        return True

    def emptyline(self):
        """Does nothing when no args and ENTER key is pressed"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
            saves to the JSON file, prints the id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        valid_class_list = ["BaseModel"]

        if class_name not in valid_class_list:
            print("** class doesn't exist **")
            return

        create_instance = BaseModel()
        create_instance.save()
        print(create_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
