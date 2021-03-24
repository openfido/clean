# OpenFIDO `clean` Pipeline

```
Syntax: python3 clean.py [-h|--help] [-i <input-folder>] [-o <output-folder>] [-c <config.csv>]

Options:
  -h|--help           get this help
  -i|--input-folder   specify input folder
  -o|--output-folder  specity output folder
  -c|--config-csv     specify config.csv filename

Config.csv:
	INPUT,<file1> [<file2> [...]]   files to process (default is *.csv)
	MIN,[NONE|<real>] [CLIP|CLAMP|<real>] [ROW <rows>|COLUMN <columns>]
	                                minimum value disposition (default is NONE)
	MAX,[NONE|<real>] [CLIP|CLAMP]<real>] [ROW <rows>|COLUMN <columns>]
	                                maximum value disposition (default is NONE)
	HOLD,[NONE|<int>] [ROW [<rows>]|COLUMN [<columns>]]
	                                hold order (default is NONE)
	NA,[NONE|DROP|<real>][ROW <rows>|COLUMN <columns>]
	                                NA disposition (default is NONE)
	INTERPOLATE,[NONE|<order> [ROW [<rows>]|COLUMN [<columns>]]
	                                interpolate data (default is NONE)
	TIMEZONE,[NONE|AUTO|<locale>|<tzinfo>][ROW <rows>|COLUMN <columns}]
	                                timezone correction (default is NONE)
	DATETIME,[NONE|ROW <rows>|COLUMN <columns>]
	                                datetime column (default is NONE)
	COLUMNS,[NONE|AUTO|<labels>]    column labels (default is NONE)
	ROWS,[NONE|AUTO|<labels>]       row labels (default is NONE)
	FILTER,[NONE|<tf>] [ROW <rows>|COLUMN <columns>]
	                                filter using a discrete transfer function

Exit codes:
	E_OK (0)      normal exit
	E_USAGE (1)   command line error
	E_INPUT (2)   missing input folder
	E_OUTPUT (3)  missing output folder
	E_CONFIG (4)  missing config.csv file

```

See [Online Documentation](https://docs.gridlabd.us/index.html?owner=openfido&project=clean&branch=main&folder=&doc=/README.md) for details.
