# Template Plugin

This is a template plugin to help you get started with creating your own plugins.

## Usage

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