import argparse


parser = argparse.ArgumentParser(description="Demo of argparse")
parser.add_argument('-n','--name', default=' 5 ')
parser.add_argument('-y','--year', default='20')
args = parser.parse_args()
print(args)
a = args.name
b = args.year

print(type(a))
print(a+b)
