import sys
from datetime import date,time
import argparse

def make(my_date=None, title=None, input_file=None):

	if my_date is None:
		my_date=input("Enter Date in MM/DD/YYYY:\t")

	if(my_date in ["today","Today","TODAY","T",""]):
		prefix = date.today().strftime("%Y-%m-%d")
	else:
		flip=my_date.replace('/','-')
		prefix=flip[-4:]+'-'+flip[:-5]

	if title is None:
		title='-'.join(input("Title:\t").lower().split())
	else:
		title='-'.join(title.lower().split())

	with open('_posts/{}-{}.MARKUP'.format(prefix,title),'w') as f:
		f.write('---\nlayout: post\ntitle: "{}"\n---\n'.format(title.replace('-'," ").title()))
		if input_file is not None:
			with open(input_file,'r') as f2:
				for l in f2.readline():
					f.write(l)
		else:
			print('vim {}'.format('_posts/{}-{}.MARKUP'.format(prefix,title)))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
	        description='Some useful utilities for this project.')
	parser.add_argument('-d', '--date', default=None)
	parser.add_argument('--title', '-t', default=None)
	parser.add_argument('--input_file', '-i', default=None)
	args = parser.parse_args()

	make(args.date, args.title, args.input_file)
