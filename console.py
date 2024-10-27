#!/usr/bin/python3
"""
this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import cmd
from console_util import cmd_utils
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
                key_value_dict = cmd_utils.process_key_value_pairs(args[1:])
                new_obj = model_class(**key_value_dict)
                new_obj.save()
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
            instance.delete()
            # key = storage.construct_key(instance)
            # storage.all().pop(key)
            # storage.save()

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

        attr_val = cmd_utils.parse_attributes(arg)
        if attr_val is None:
            return

        attr = attr_val[0]
        value = attr_val[1]

        cmd_utils.update(instance, attr, value)

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    def do_exit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    do_EOF = do_quit

    def emptyline(self):
        pass

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
