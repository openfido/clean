# OpenFIDO `clean` Pipeline

```
Syntax: python3 clean.py [-h|--help] [-i <input-folder>] [-o <output-folder>] [-c <config.csv>]

Options:
  -h|--help           get this help
  -i|--input-folder   specify input folder
  -o|--output-folder  specity output folder
  -c|--config-csv     specify config.csv filename

Config.csv:
	INPUT,<file1> [<file2> [...]]            files to process (default is *.csv)
	MIN,[NONE|<real>] [CLIP|CLAMP|<real>]    minimum value disposition (default is NONE)
	MAX,[NONE|<real>] [CLIP|CLAMP]<real>]    maximum value disposition (default is NONE)
	HOLD,[NONE|0|1] [ROW|COLUMN]             hold order (default is NONE)
	NA,[NONE|DROPROW|DROPCOL|<real>]         NA disposition (default is NONE)
	TIMEZONE,[NONE|AUTO|<locale>|<tzinfo>]   timezone correction (default is NONE)
	DATETIME,[NONE|<int>]                    datetime column (default is NONE)

Exit codes:
	E_OK (0)      normal exit
	E_USAGE (1)   command line error
	E_INPUT (2)   missing input folder
	E_OUTPUT (3)  missing output folder
	E_CONFIG (4)  missing config.csv file

```

See [Online Documentation](https://docs.gridlabd.us/index.html?owner=openfido&project=clean&branch=main&folder=&doc=/README.md) for details.
