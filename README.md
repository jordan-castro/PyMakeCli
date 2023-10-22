# PyMakeCli

This is made to build C/C++ projects easily using YAML. It is not a replacement for CMake. 
Rather it is an automation to be used instead of CMake but if you know CMake then you should use it in conjection.

**Note:** This is still in development and may not work as expected.

## Installation

```bash
pip install pymake-cli
```

## Usage

```bash
pymake-cli --help
```

## Example

To use this you need to create a `.yaml` file in the root of your project.
**hint**: You can also specify the path of the `.yaml` file in each command.
**hint**: The `config_file_path` is optional and will default to `config.yaml` in the current directory.

### Init
    
```bash
pymake-cli init <config_file_path> [-d]
```

### Build
    
```bash
pymake-cli build <config_file_path> [-d] [-s]
```

### Run
```bash
pymake-cli run <config_file_path>
```

### Update
This command will update the `.yaml` file with the current config structure.
```bash
pymake-cli update <config_file_path> 
```

### Options
On each command you can specify the following options:
    - `<config_file_path>`: The path to the `.yaml` file.
    - `-d` or `--debug`: This will print debug information.

The `-s` or `--shell` option allows you to run shell commands as defined in the config file.
### Try it out
You can try it out by cloning this repo and running the following commands:
```bash
# Clone repo
git clone https://github.com/james-garfield/PyMakeCli.git

# Change directory
cd PyMakeCli

# Install package
pip install -e .

# Change into example directory
cd example

# Run commands
pymake-cli build
pymake-cli run
```