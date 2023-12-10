#!/usr/bin/python3
"""Console module for the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_show(self, arg):
        """prints the str rep of an instance"""
        class_name, obj_id = None, None
        args = arg.split()
        if len(args) > 0:
            class_name = args[0]

        if len(args) > 1:
            obj_id = args[1]

        if not args:
            print("** class name missing **")
            return

        elif not obj_id:
            print("** instance id missing **")
            return

        valid_class_list = ["BaseModel"]

        if class_name not in valid_class_list:
            print("** class doesn't exist **")
            return

        else:
            id_key = class_name + "." + obj_id
            obj = storage.all().get(id_key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """destroys an instance based on class name and id"""
        class_name, obj_id = None, None
        args = arg.split()

        if len(args) > 0:
            class_name = args[0]

        if len(args) > 1:
            obj_id = args[1]

        if not args:
            print("** class name missing **")
            return

        elif not obj_id:
            print("** instance id missing **")

        valid_class_list = ["BaseModel"]

        if class_name not in valid_class_list:
            print("** class doesn't exist **")
            return

        else:
            id_key = class_name + "." + obj_id
            obj = storage.all().get(id_key)
            if not obj:
                print("** no instance found **")
            else:
                del storage.all()[id_key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all existing instances"""
        obj_str_list = []

        if arg and arg[0]:
            class_name = arg
            valid_class_list = ["BaseModel"]
            if class_name not in valid_class_list:
                print("** class doesn't exist **")
                return

            for key, value in storage.all().items():
                if class_name in key:
                    obj_str_list.append(str(value))

        else:
            for key, value in storage.all().items():
                obj_str_list.append(str(value))

        print(obj_str_list)
                    
    def do_update(self, arg):
        args = arg.split()
        
        if len(args) < 4:
            print("** insufficient arguments **")
            return

        class_name = args[0]
        obj_id = args[1]
        attrbt_name = args[2]
        attrbt_value = args[3]

        valid_class_list = ["BaseModel"]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in valid_class_list:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        if not attrbt_name:
            print("** attribute name missing **")
            return

        if not attrbt_value:
            print("** value missing **")
            return

        id_key = class_name + "." + obj_id
        obj = storage.all().get(id_key)

        if not obj:
            print("** no instance found **")
            return

        # Update the attribute of the object if it exists and is updatable
        if hasattr(obj, attrbt_name) and not attrbt_name.startswith(('id', 'created_at', 'updated_at')):
            # Try to cast the attribute value to its original type
            try:
                attrbt_value = type(getattr(obj, attrbt_name))(attrbt_value)
            except (ValueError, TypeError):
                print("** value type not compatible with attribute **")
                return

            setattr(obj, attrbt_name, attrbt_value)
            obj.save()
        else:
            print("** attribute cannot be updated or does not exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
