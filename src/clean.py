"""Syntax: python3 clean.py [-h|--help] [-i <input-folder>] [-o <output-folder>] [-c <config.csv>]

Options:
  -h|--help           get this help
  -i|--input-folder   specify input folder
  -o|--output-folder  specity output folder
  -c|--config-csv     specify config.csv filename

Config.csv:
	INPUT,f<ile1> [<file2> [...]]            files to process (default is *.csv)
	MIN,[NONE|<real>] [CLIP|CLAMP|<real>]    minimum value disposition (default is NONE)
	MAX,[NONE|<real>] [CLIP|CLAMP]<real>]    maximum value disposition (default is NONE)
	HOLD,[NONE|0|1] [ROW|COLUMN]             hold order (default is NONE)
	NA,[NONE|DROPROW|DROPCOL|<real>]         NA disposition (default is NONE)
	TIMEZONE,[NONE|AUTO|<locale>|<tzinfo>]   timezone correction (default is NONE)
	DATETIME,[NONE|<int>]                    datetime column (default is NONE)

Exit codes:
	E_OK (0)   normal exit
	E_USAGE    command line error
	E_INPUT    missing input folder
	E_OUTPUT   missing output folder
	E_CONFIG   missing config.csv file
"""
import sys, os
import getopt
import numpy, scipy, pandas

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

if not os.path.exists(input_folder):
	error(f"input folder '{input_folder}' does not exist",E_INPUT)
if not os.path.exists(output_folder):
	error(f"output folder '{output_folder}' does not exist",E_OUTPUT)
if not os.path.exists(config_csv):
	error(f"config file '{config_csv}' does not exist",E_CONFIG)

raise Exception("not fully implemented yet")

