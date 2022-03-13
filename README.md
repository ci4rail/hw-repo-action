# Generate a ZIP file from the repostitory contents

This Github action allows you to generate a ZIP file from the repostitory contents, excluding selected files.

## Input Variables

* `output-path`: Absolute path with filename of the ZIP file to create"
* `exclude-patterns`: File patterns to exclude from ZIP file. Patterns must be white space separated. Patterns are `glob` patterns, compared with pythons's `fnmatch` functions and are compared against the whole path of each file. Comparisons are case insensitive.

## Usage

