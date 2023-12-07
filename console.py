#!/usr/bin/python3
"""Console module for the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """This command quits or exits the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal exits program cleanly """
        return True

    def emptyline(self):
        """Does nothing when no args and ENTER key is pressed"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
