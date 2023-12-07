#!/usr/bin/python3
"""Console module for the command interpreter"""


import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """This command quits or exits the program"""
        return True

    #was testing aliasing, will delete later
    do_flee = do_quit
    
    def do_EOF(self, arg):
        """This command uses EOF signal to exit the program"""
        return True

    def emptyline(self):
       """ Executes nothing when empty line + ENTER"""
       pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
