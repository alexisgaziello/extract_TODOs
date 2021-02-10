# extract_TODOs
A Python script to extract TODOs from a project.


## Usage

### Command line

```
python path_to_script path_to_directory path_to_csv/filename.csv
```

- **path_to_script**: path to the following file: _/extract_TODOs/extract_TODOs/extract_TODOs.py_.
- **path_to_directory**: path to the target directory to explore.
- **path_to_csv/filename.csv**: filename and the path to the csv file where you want to save results.

### As python dataframe

Import the function _extract_TODOs(directory)_ from the package _extract_TODOs_.

The argument is the path to the directory to explore. 

### Result


Description	| File	| Full Path	| Line
------------ | ------------- | ------------- | ------------- 
Content of line where TODO was found | File where TODO was found | Full path to file where TODO was found | Line number where TODO was found
