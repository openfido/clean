# OpenFIDO `clean` Pipeline

## Syntax

~~~
python3 clean.py [-h|--help] [-i <input-folder>] [-o <output-folder>] [-c <config.csv>]
~~~

## Description

The `clean` pipeline perform data cleaning operations on unlabeled and labeled data.  Current the following cleaning operations are available.

  - **Range limits**: `MIN` and `MAX` may be used to impose range limits on the data.  
  - **NA disposition**: `NA` may be used to drop rows or columns with missing data
  - **Data hold**: `HOLD` may be used to fill missing data.
  - **Date/time correction**: `DATETIME` and `TIMEZONE` may be used to correct timezones.

## Options

The following command line options are recognized.

### `-h|--help`

Get this help

### `-i|--input-folder`

Specify input folder

### `-o|--output-folder`

Specity output folder

### `-c|--config-csv` 

Specify config.csv filename

## Config.csv

The `config.csv` controls the clean operations.

### `DATETIME`

~~~
DATETIME,[NONE|<int>]
~~~

Datetime column (default is `NONE`)

### `HOLD`

~~~
HOLD,[NONE|0|1] [ROW|COLUMN]
~~~

Hold order (default is `NONE`).

### `INPUT`

~~~
INPUT,<file1> [<file2> [...]]
~~~

Files to process (default is `*.csv`).

### `MIN`

~~~
MIN,[NONE|<real>] [CLIP|CLAMP|<real>]
~~~

Minimum value disposition (default is `NONE`).

### `MAX`

~~~
MAX,[NONE|<real>] [CLIP|CLAMP]<real>]
~~~

Maximum value disposition (default is `NONE`).

### `NA`

~~~
NA,[NONE|DROPROW|DROPCOL|<real>]
~~~

NA disposition (default is `NONE`)

### `TIMEZONE`
~~~
TIMEZONE,[NONE|AUTO|<locale>|<tzinfo>]
~~~

Timezone correction (default is `NONE`)

## Exit codes

  - E_OK (0)       normal exit
  - E_USAGE (1)    command line error
  - E_INPUT (2)    missing input folder
  - E_OUTPUT (3)   missing output folder
  - E_CONFIG (4)   missing config.csv file
