import argparse
import sys
class CliParser:
    parser = argparse.ArgumentParser(prog='pylogex',description='filter textual input stream based on regular expression pattern and generate log in CSV or JSON format as output stream')

    def __init__(self) -> None:
       pass


    def logParser(self):

        self.parser.add_argument('-i','--INFILE',type=argparse.FileType('r'), default=sys.stdin, help="--input=INFILE read input (logs) from <INFILE>")
        self.parser.add_argument('-o','--OUTFILE', type=argparse.FileType('w'),default=sys.stdout, help="--output=OUTFILE save the extracted data to <OUTFILE>")
        self.parser.add_argument('REGEX', type=str, help='extract patterns matching this regular expressions from the input stream')
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument("-j", "--json", help="generate output in JSON format", action="store_true")
        group.add_argument("-c", "--csv", help="generate output in CSV format (default)", action="store_true")

        args = self.parser.parse_args()
        if((args.json and args.OUTFILE.name.endswith('.csv',0,len(args.OUTFILE.name))) or (args.csv and args.OUTFILE.name.endswith('.json',0,len(args.OUTFILE.name)))):
            raise Exception("Output format and flag do not match")

        return args





