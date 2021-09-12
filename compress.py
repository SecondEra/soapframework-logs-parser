import argparse
from datetime import datetime

coeff = 1624
delimiter = '#'

parser = argparse.ArgumentParser(description='Compress Soap Framework logs.')
parser.add_argument('decompressed_logs_file', type=argparse.FileType('r'))
parser.add_argument('compressed_logs_file', type=argparse.FileType('a'))

args = parser.parse_args()

args.compressed_logs_file.write(bytearray([int(int(line.split(delimiter)[1]) / coeff) for line in args.decompressed_logs_file.readlines()]).decode())
