# CSV to JSON converter in specific File Format

## Input:
CSV file

## Output:
JSON File

## Usage Method:
This script uses Python 3.x

### Command:
python csvToJSON.py inputFileName.csv outputFileName.json skippedRowsCount

inputFileName: mandatory
outputFileName: optional
skippedRowsCount: optional (It is basically starting rows of csv file that should be skipped, default: 5)

*Usage Examples:*
```python
python csvToJSON.py input.csv
python csvToJSON.py input.csv output.json 5
```
