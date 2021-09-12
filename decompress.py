import argparse
from datetime import datetime

coeff = 1624
delimiter = '#'

parser = argparse.ArgumentParser(description='Decompress Soap Framework logs.')
parser.add_argument('compressed_logs_file', type=argparse.FileType('r'))
parser.add_argument('decompressed_logs_file', type=argparse.FileType('a'))

args = parser.parse_args()

for c in args.compressed_logs_file.read().encode():
	line = datetime.now().strftime("%d/%m/%Y@%H:%M:%S") + delimiter + str(c * coeff) + '\n'
	args.decompressed_logs_file.write(line)
