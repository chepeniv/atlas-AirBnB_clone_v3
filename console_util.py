#!/usr/bin/python3
"""
this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import os
import cmd
import contextlib
from models import storage
from models.engine import valid_models


class HBNBCommand(cmd.Cmd):
    """ our reimplementation of cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        'creates a new instance of BaseModel'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            model_class = valid_models().get(args[0])
            if model_class is None:
                print("** class doesn't exist **")
                return
            else:
                self.process_key_value_pairs(model_class, args)
                model_class.save()
                print(new_obj.id)

    def do_show(self, args):
        'outputs representation of an instance given the class name and id'
        instance = self.get_instance(args)
        if instance is None:
            return
        else:
            print(str(instance))

    def do_destroy(self, arg):
        'delete instance given by the class name and id'
        instance = self.get_instance(arg)
        if instance is None:
            return
        else:
            key = storage.construct_key(instance)
            storage.all().pop(key)
            storage.save()

    def do_all(self, args):
        """ outputs string representations for every existing
        instance or for all of a class
        """
        obj_list = []

        if not args:
            for value in storage.all().values():
                obj_list.append(str(value))
        else:
            class_given = args.split()
            class_given = class_given[0]
            model_class = valid_models().get(class_given)
            if model_class is not None:
                for key, value in storage.all().items():
                    if key.startswith(class_given):
                        obj_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return

        print(obj_list)
        #for obj in obj_list:
        #    print(obj)
        #    print("----------------")

    def do_update(self, arg):
        """ updates the instance given by class_name and id.
        usage: update <class> <id> <attr> "<val>"
        """

        instance = self.get_instance(arg)
        if instance is None:
            return

        attr_val = self.parse_attributes(arg)
        if attr_val is None:
            return

        attr = attr_val[0]
        value = attr_val[1]

        self.update(instance, attr, value)

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    def do_exit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    do_EOF = do_quit

    def emptyline(self):
        pass

    def parse_attributes(self, args):
        'returns an touple with attribute and value'

        attr = args.split()
        attr = attr[2] if len(attr) > 2 else None
        if args.find('"') > 0:
            value = args.split('"')
            value = value[1] if len(value) > 1 else None
        elif args.find("'") > 0:
            value = args.split("'")
            value = value[1] if len(value) > 1 else None
        else:
            value = args.split()
            value = value[3] if len(value) > 3 else None

        if attr is None:
            print('** attribute name missing **')
            return None
        elif value is None:
            print('** value missing **')
            return None
        else:
            return (attr, value)

    def get_instance(self, args):
        args = args.split()
        class_name = args[0] if len(args) > 0 else None
        id_num = args[1] if len(args) > 1 else None
        model_class = valid_models().get(class_name)

        if class_name is None:
            print('** class name missing **')
            return None
        elif model_class is None:
            print("** class doesn't exist **")
            return None
        elif id_num is None:
            print('** instance id missing **')
            return None
        else:
            key = class_name + "." + id_num
            instance = storage.all().get(key)
            if instance is None:
                print('** no instance found **')
                return None
            return instance

    def process_key_value_pairs(self, obj, key_value_list):
        """
        parse arguments passed and set values accordingly
        """
        # create ClassName keyA="valueA" keyB="valueB" ...
        # allow double quotes with escape \
        # a number with a dot is a floats, without one it is an int

        key_value_dict = {}
        for key_value in key_value_list:
            try:
                (key, value) = key_value.split("=")
                if (value.startswith('"')
                    and value.endswith('"')):
                    value = self.clean_string(value)
                elif (number := self.string_to_number(value)) is not None:
                    value = number
                else:
                    continue
                # print(key, ": ", value, " - ", type(value))
                # (with open(os.devnull, 'w# ')
                # as devnull, contextlib.redirect_stdout(devnull)):
                #    self.update(obj, key, value)
            except ValueError:
                continue

    def string_to_number(self, num_string):
        if num_string.count(".") == 1:
            try:
                number = float(num_string)
            except ValueError:
                return None
        else:
            try:
                number = int(num_string)
            except ValueError:
                return None
        return number

    def clean_string(self, old_string):
        new_string = old_string.replace("_", " ")
        new_string = new_string[1:-1]
        new_string = new_string.replace('"', '\\"')
        return new_string

    def update(self, instance, attr, value):
        if hasattr(instance, attr):
            attr_type = type(getattr(instance, attr))
            try:
                value = attr_type(value)
            except (ValueError, TypeError):
                print("** value given could not be typecast correctly **")
                value = getattr(instance, attr)

            setattr(instance, attr, value)
            instance.save()
        else:
            print("** no such attribute found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
