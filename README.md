# Generate a ZIP file from the repository contents

This Github action allows you to generate a ZIP file from the repostitory contents, excluding selected files.

## Input Variables

* `output-path`: Absolute path with filename of the ZIP file to create
* `exclude-patterns`: File patterns to exclude from ZIP file. Patterns must be white space separated. Patterns are `glob` patterns, compared with pythons's `fnmatch` function and are compared against the whole path of each file. Comparisons are case insensitive. Absolute paths always begin with `./`, so the pattern must 

## Usage

```yaml
on:
  release:
    types: [published]

jobs:
  package:
    runs-on: ubuntu-latest
    name: Build ZIP
    steps:
      - uses: actions/checkout@v2
        with:
          submodules: "recursive"
          token: ${{ secrets.PAT_TOKEN }}
      - id: zip
        uses: ci4rail/zip-action@v1
        with:
          output-path: "/tmp/my.zip"
          exclude-patterns: |
            *.FCStd 
            ./simulation/*
```