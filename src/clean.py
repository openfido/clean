"""Syntax: python3 clean.py [-h|--help] [-i <input-folder>] [-o <output-folder>] [-c <config.csv>]

Options:
  -h|--help           get this help
  -i|--input-folder   specify input folder
  -o|--output-folder  specity output folder
  -c|--config-csv     specify config.csv filename

Config.csv:
	INPUT,<file1> [<file2> [...]]   files to process (default is *.csv)
	MIN,[NONE|<real>] [CLIP|CLAMP|<real>] [ROW <rows>|COLUMN <columns}]
	                                minimum value disposition (default is NONE)
	MAX,[NONE|<real>] [CLIP|CLAMP]<real>] [ROW <rows>|COLUMN <columns}]
	                                maximum value disposition (default is NONE)
	HOLD,[NONE|<int>] [ROW [<rows>]|COLUMN [<columns>]]
	                                hold order (default is NONE)
	NA,[NONE|DROP|<real>][ROW <rows>|COLUMN <columns}]
	                                NA disposition (default is NONE)
	INTERPOLATE,[NONE|<order> [ROW [<rows>]|COLUMN [<columns>]]
	                                interpolate data (default is NONE)
	TIMEZONE,[NONE|AUTO|<locale>|<tzinfo>][ROW <rows>|COLUMN <columns}]
	                                timezone correction (default is NONE)
	DATETIME,[NONE|ROW <rows>|COLUMN <columns>]
	                                datetime column (default is NONE)
	COLUMNS,[NONE|AUTO|<labels>]    column labels (default is NONE)
	ROWS,[NONE|AUTO|<labels>]       row labels (default is NONE)

Exit codes:
	E_OK (0)      normal exit
	E_USAGE (1)   command line error
	E_INPUT (2)   missing input folder
	E_OUTPUT (3)  missing output folder
	E_CONFIG (4)  missing config.csv file
"""
import sys, os, getopt
import csv, pandas

E_OK = 0
E_USAGE = 1
E_INPUT = 2
E_OUTPUT = 3
E_CONFIG = 4

input_folder = "."
output_folder = "."
config_csv = "config.csv"

def help(full=False):
	if full:
		print(sys.modules[__name__].__doc__)
	else:
		print(sys.modules[__name__].__doc__.split("\n")[0])

def error(msg,code=None):
	print(f"ERROR [clean.py]: {msg}")
	if type(code) is int:
		exit(code)

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:c:",["help","input-folder","output-folder","config-csv"])
except:
	help(full=False)
	exit(E_USAGE)

for opt, arg in opts:
	if opt in ["-h","--help"]:
		help(full=True)
		exit(E_OK)
	elif opt in ["-i","--input-folder"]:
		input_folder = arg
	elif opt in ["-o","--output-folder"]:
		output_folder = arg
	elif opt in ["-c","--config-csv"]:
		config_csv = arg
	else:
		raise Exception(f"option {opt}={arg} is not valid")

# check command line options
if not os.path.exists(input_folder):
	error(f"input folder '{input_folder}' does not exist",E_INPUT)
if not os.path.exists(output_folder):
	error(f"output folder '{output_folder}' does not exist",E_OUTPUT)
if not os.path.exists(config_csv):
	error(f"config file '{config_csv}' does not exist",E_CONFIG)

config = {
	"INPUT" : [],
	"MIN" : None,
	"MAX" : None,
	"NA" : None,
}
with open(config_csv) as fh:
	reader = csv.reader(fh)
	for row in reader:
		if not row[0] in config.keys():
			raise Exception(f"{row}: config key is not valid")

