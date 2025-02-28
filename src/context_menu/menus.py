from __future__ import annotations
import inspect
import sys
import os
import platform
from typing import Any

from typing import Tuple, Union, Literal
from types import FunctionType

from context_menu import windows_menus

ActivationType = Literal["FILES", "DIRECTORY", "DIRECTORY_BACKGROUND", "DRIVE", "DESKTOP"]
ItemType = Union["ContextMenu", "ContextCommand"]
MethodInfo = Tuple[str, str, str]


class ContextMenu:
    """
    The general menu class. This class generalizes the menus and eventually passes the correct values to the platform-specifically menus.
    """

    def __init__(self, name: str, type: ActivationType | str | None = None, icon_path: str = None) -> None:
        """
        Only specify type if it's the root menu.
        """

        self.name = name
        self.sub_items: list[ItemType] = []
        self.type = type
        self.icon_path = icon_path
        self.isMenu = True  # Needed to avoid circular imports

    def add_items(self, items: list[ItemType]) -> None:
        """
        Adds a list of items to the current menu.
        """
        self.sub_items.extend(items)

    def compile(self) -> None:
        """
        Recognizes the current platform and passes information to the respective menu. Creates the actual menu.
        """
        if self.type is None:
            raise Exception("type can't be None for top-level ContextMenu")

        windows_menus.RegistryMenu(self.name, self.sub_items, self.type, self.icon_path).compile()


class ContextCommand:
    """
    The general command class.

     A command is an executable entry in a context-menu, where menus hold other commands.

     Name = Name of the command
     Command = command to be ran from the shell
     python = function to be ran
     params = any other parameters to be passed
     command_vars = to help with the command
    """

    def __init__(
        self,
        name: str,
        python: FunctionType | None = None,
        params: dict[str, Any] | None = None,
        icon_path: str = None,
        python_path: str = sys.executable,
        func_name: str | None = None,
        func_file_name: str | None = None,
        func_dir_path: str | None = None,
    ) -> None:
        """
        Do not specify both 'python' and 'command', either pass a python function or a command but not both.
        """
        self.name = name
        self.isMenu = False
        self.python = python
        self.params = params
        self.icon_path = icon_path
        self.python_path = python_path

        self.func_name = func_name
        self.func_file_name = func_file_name
        self.func_dir_path = func_dir_path

    def get_method_info(self) -> MethodInfo:
        if self.func_name and self.func_file_name and self.func_dir_path:
            return (self.func_name, self.func_file_name, self.func_dir_path)

        assert self.python is not None
        func_file_path = os.path.abspath(inspect.getfile(self.python))

        func_dir_path = os.path.dirname(func_file_path).replace("\\", "/")
        func_name = self.python.__name__
        func_file_name = os.path.splitext(os.path.basename(func_file_path))[0]

        return (func_name, func_file_name, func_dir_path)


class FastCommand:
    """
    Used for fast creation of a command. Good if you don't want to get too involved and just jump start a program.

    Extremely similar methods to other classes, only slightly modified. View the documentation of the above classes for info on these methods.
    """

    def __init__(
        self,
        name: str,
        type: ActivationType | str,
        python: FunctionType | None = None,
        params: dict[str, Any] | None = None,
        icon_path: dict[str, Any] = None,
        python_path: str = sys.executable,
        func_name: str | None = None,
        func_file_name: str | None = None,
        func_dir_path: str | None = None,
    ) -> None:
        self.name = name
        self.type = type
        self.python = python
        self.params = params
        self.icon_path = icon_path
        self.python_path = python_path

        self.func_name = func_name
        self.func_file_name = func_file_name
        self.func_dir_path = func_dir_path

    # def get_method_info(self) -> MethodInfo:
    #     if func_name and func_file_name and func_dir_path:
    #         return (self.func_name, self.func_file_name, self.func_dir_path)

    #     assert self.python is not None
    #     func_file_path = os.path.abspath(inspect.getfile(self.python))

    #     func_dir_path = os.path.dirname(func_file_path).replace("\\", "/")
    #     func_name = self.python.__name__
    #     func_file_name = os.path.splitext(os.path.basename(func_file_path))[0]

    #     return (func_name, func_file_name, func_dir_path)

    def compile(self) -> None:

        windows_menus.FastRegistryCommand(self.name, self.type, self.python, self.params, self.icon_path, self.python_path, self.func_name, self.func_file_name, self.func_dir_path).compile()


try:

    def removeMenu(name: str, type: ActivationType | str) -> None:
        """
        Removes a menu/command entry from a context menu.

        Requires the name of the menu and type of the menu
        """

        windows_menus.remove_windows_menu(name, type)

except Exception as e:
    # For testing
    print(e)
    pass
