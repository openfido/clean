# OpenFIDO `clean` Pipeline

# Syntax

~~~
python3 clean.py [-h|--help] [-i <input-folder>] [-o <output-folder>] [-c <config.csv>]
~~~

# Options

## `-h|--help`

Get this help

## `-i|--input-folder`

Specify input folder

## `-o|--output-folder`

Specity output folder

## `-c|--config-csv` 

Specify config.csv filename

# Config.csv

## `INPUT`

~~~
INPUT,<file1> [<file2> [...]]
~~~

Files to process (default is `*.csv`).

## `MIN`

~~~
MIN,[NONE|<real>] [CLIP|CLAMP|<real>]
~~~

Minimum value disposition (default is `NONE`).

## `MAX`

~~~
MAX,[NONE|<real>] [CLIP|CLAMP]<real>]
~~~

Maximum value disposition (default is `NONE`).

## `HOLD`

~~~
HOLD,[NONE|0|1] [ROW|COLUMN]
~~~

Hold order (default is `NONE`).

## `NA`

~~~
NA,[NONE|DROPROW|DROPCOL|<real>]
~~~

NA disposition (default is `NONE`)

## `TIMEZONE`
~~~
TIMEZONE,[NONE|AUTO|<locale>|<tzinfo>]
~~~

Timezone correction (default is `NONE`)

## `DATETIME`

~~~
DATETIME,[NONE|<int>]
~~~

Datetime column (default is `NONE`)

# Exit codes

  - E_OK (0)       normal exit
  - E_USAGE (1)    command line error
  - E_INPUT (2)    missing input folder
  - E_OUTPUT (3)   missing output folder
  - E_CONFIG (4)   missing config.csv file
