# Context Menu Plugin Manager

![screenshot_1](screenshots/screenshot_1.png)
![screenshot_2](screenshots/screenshot_2.png)
![screenshot_3](screenshots/screenshot_3.png)

This project manages context menu plugins to extend functionality in various directories. It allows dynamic addition and removal of context menu items using Python scripts.

## Features

- **Plugin Development:** Easily create plugins with metadata and functionality.
- **Dynamic Menu Modification:** Add or remove context menu items on the fly.
- **Extensible:** Customize and extend functionality by creating new plugins.
- **Generate Plugin using AI:** Generate a plugin using AI to automate the process.
- **Drag and Drop:** Drag and drop files to add plugins to the context menu.
- **Configuration:** Configure plugins with parameters to customize behavior.
- **Customization:** Customize the appearance of the application with themes.

## Installation

First make sure you have Python 3.13.1 or above installed. If not, you can download it from [here](https://www.python.org/downloads/).

1. Clone the repository:

   ```
   git clone https://github.com/abdxdev/Context-Menu-Plugin-Manager.git
   ```

2. Go inside the repository:

   ```
   cd Context-Menu-Plugin-Manager
   ```

3. Create a virtual environment

   ```
   python -m venv .venv
   ```

4. Activate the virtual environment

   ```
    .venv\Scripts\activate
   ```

5. Install the requirements

   ```
   pip install -r requirements.txt
   ```

6. Run the program

   ```
   python src/app.py
   ```

## Creating a Plugin

This is a template plugin to help you get started with creating your own plugins.

## Usage for Plugin Development

The `driver` function receives two arguments:

- `items`: A list of strings representing the selected folders/files.
- `params`: A dictionary containing the configuration parameters.

You can access the configuration parameters in the 'Configure Plugin' tab.

## Example

```python
# The `driver` function is the entry point for the Python script.
# Only this line of code is required to create a plugin
def driver(items: list[str] = [], params: dict = {}):

    # Example code to print the items and params
    print("Folders/Files:")
    for item in items:
        print(item)
    print("Params:")
    for key, value in params.items():
        print(f"{key}: {value}")

    # Keep the console open by waiting for user input
    input("Press Enter to exit")


# Only here for testing purposes. 
# This block is not executed when triggered as a plugin
if __name__ == "__main__":
    params = {
        "param1": "value1",
        "param2": "value2",
    }
    driver(["file1.txt", "file2.txt"], params)

```

## License

This project is licensed under the [BSD License](https://github.com/abdxdev/context-menu-plugin-manager/blob/main/LICENSE).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## Credits

Big thanks to these awesome creators!

- [@Flet Dev Community](https://github.com/flet-dev) for the [`flet`](https://flet.dev/) - A framework based on flutter for creating desktop applications.
- [@saleguas](https://github.com/saleguas) for the [`context-menu`](https://github.com/saleguas/context_menu) - A library to customize the context menu.
- [@Wanna-Pizza](https://github.com/Wanna-Pizza) for the [`FletDropZone`](https://github.com/Wanna-Pizza/FletDropZone) - A drag and drop feature for `flet`.
