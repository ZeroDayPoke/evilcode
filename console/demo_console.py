#!/usr/bin/env python3
"""Demo console application"""

import cmd

class Demo_Console(cmd.Cmd):
    prompt = 'Demo_Console> '

    def do_greet(self, name):
        """greet [name] - Greet the named person"""
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

    def do_exit(self, arg):
        """exit - Exit the interpreter"""
        print("Exiting...")
        return True

    def do_EOF(self, line):
        """Ctrl+D - Exit the interpreter"""
        return self.do_exit(line)

    def do_import(self, line):
        """import [module] - Import a module"""
        try:
            exec(f"import {line}")
        except ModuleNotFoundError:
            print(f"Module {line} not found")

if __name__ == '__main__':
    Demo_Console().cmdloop()
