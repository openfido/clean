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

### `COLUMNS`

~~~
COLUMNS=[NONE|AUTO]
~~~

Specify how the columns are labeled. Use `NONE` for unlabeled data and `AUTO` for labeled data.  Default is `NONE`. 

If columns are specified explicitly, then unlabeled data becomes labeled, and labeled data is relabeled.  In this case the number of labels must match the number of columns. 


### `DATETIME`

~~~
DATETIME,[NONE| ROW <rows>|COLUMN <columns>]
~~~

Specifies the column(s) the contain date/time values to which `TIMEZONE` cleaning must be applied.  Default is `NONE`.

### `HOLD`

~~~
HOLD,[NONE|<int>] [ROW [<rows>]|COLUMN [<columns>]]
~~~

Specifies the hold order to be applied. Use 0 for a zero-order hold and 1 for a first-order hold.  Higher order holds are not supported.  The default is `NONE`.

If `ROW` or `COLUMN` is specified the hold is applied on the horizontal or vertical axis, respectively.  The default is `COLUMN`.  If `<rows>` or `<columns>` is specified, the hold is limited to those, otherwise it is applied to all rows or columns.

### `INPUT`

~~~
INPUT,<file1> [<file2> [...]]
~~~

Files to process (default is `*.csv`).

### `INTERPOLATE`

~~~
INTERPOLATE,[NONE|<order> [ROW [<rows>]|COLUMN [<columns>]]
~~~

Specifies the interpolation order to be applied to missing data. Use 0 for nearest, 1 for a for linear, 2 for quadratic, 3 for cubic spline.  The default is `NONE`.

If `ROW` or `COLUMN` is specified the interpolation is limited on the horizontal or vertical axis, respectively.  If neither is specified a 2D interpolation is used. If `<rows>` or `<columns>` is specified, the interpolation is limited to those, otherwise it is applied to all rows or columns.

### `MIN`

~~~
MIN,[NONE|<real>] [CLIP|CLAMP|<real>] [ROW <rows>|COLUMN <columns>]
~~~

Specifies the minimum value disposition (default is `NONE`).

### `MAX`

~~~
MAX,[NONE|<real>] [CLIP|CLAMP]<real>] [ROW <rows>|COLUMN <columns>]
~~~

Maximum value disposition (default is `NONE`).

### `NA`

~~~
NA,[NONE|DROPROW|DROPCOL|<real>]
~~~

NA disposition (default is `NONE`)

### `ROWS`

~~~
ROWS=[NONE|AUTO|<row-1>,<row-2>,...,<row-N>]
~~~

Specify how the rows are labeled. Use `NONE` for unlabeled data and `AUTO` for labeled data.  Default is `NONE`. 

If rows are specified explicitly, then unlabeled data becomes labeled, and labeled data is relabeled.  In this case the number of labels must match the number of rows. 

### `TIMEZONE`
~~~
TIMEZONE,[NONE|AUTO|<locale>|<tzinfo>] [ROW <rows>|COLUMN <columns>]
~~~

Timezone correction (default is `NONE`)

## Exit codes

  - E_OK (0)       normal exit
  - E_USAGE (1)    command line error
  - E_INPUT (2)    missing input folder
  - E_OUTPUT (3)   missing output folder
  - E_CONFIG (4)   missing config.csv file
