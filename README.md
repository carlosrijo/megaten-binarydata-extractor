# Description

This is a simple project to automatically do a bulk-convert .sbin files to .xml given a path to a directory containing .sbin or .bin files and an output directory to save .xml or .tsv files.

## References

This tool uses `comp_decrypt` and `comp_bdpatch` to convert the files. You can learn more about it here:

- [Private Server Repo](https://github.com/comphack/comp_hack)
- [comp_decrypt](https://github.com/comphack/comp_hack/tree/develop/tools/decrypt)
- [comp_bdpatch](https://github.com/comphack/comp_hack/tree/develop/tools/bdpatch)

Credits to the team for the amazing tools 🙂

# Documentation

## Configuration

Make sure you setup everything correctly on config.pyc:

- `comp_decrypt_tool_path` - Full path to the comp_decrypt tool
- `comp_bdpatch_tool_path` - Full path to the comp_bdpatch tool
- `base_client_binary_data_directory` - Path of the directory where the .sbin and .bin reside
- `base_output_directory_xml_or_tsv` - Path of the directory where the .bin and .xml|.tsv files will be saved

## Usage

This only runs on Window's Command Line (cmd) for now.

Open a command line session and run:

- `python main.py [flatten|load]`

> `load` is the default argument so you just have to run main.py
