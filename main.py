import argparse
from pathlib import Path
from graph import Graph


def main():
	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('-f','--path', help='Path for the data file', required=True)
	parser.add_argument('-n','--degree', help='Degree of the regression', required=True)
	parser.add_argument('-x','--xlabel', help='X axis label', required=False)
	parser.add_argument('-y','--ylabel', help='Y axis label', required=False)
	args = vars(parser.parse_args())

	file = Path(args['path'])
	if file.is_file():
		if args['xlabel'] is not None and args['ylabel'] is not None:
			Graph(args['path'], int(args['degree']), args['xlabel'], args['ylabel'])
		else:
			Graph(args['path'], int(args['degree']))
	else:
		print("Introduce un archivo valido miloco")
	#main function

if __name__ == '__main__':
	main()
