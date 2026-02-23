import csv
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description="Чтение CSV файла")
parser.add_argument("--files", nargs="+", required=True)
parser.add_argument("--report", required=True, help="Файл для сохранения результата")

args = parser.parse_args()

total =0 
count = 0
def process_economic_data(filenames):
	data = {}
	for filename in args.files:
		with open(filename, newline="", encoding="utf-8") as f:
			reader = csv.DictReader(f)
			for row in reader:
				country = row["country"]
				gdp = row["gdp"]
				if country not in data:
					data[country] = {'total_gdp': 0, 'count': 0}
				data[country]['total_gdp'] += float(gdp)
				data[country]['count'] += 1
	return data
def save_report(data, file):
	table = []
	with open(f"{file}.csv", "w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["country", "gdp"])
		for country, stats in data.items():
			average = stats['total_gdp'] / stats['count']
			writer.writerow([country, f"{average:.2f}"])
			table.append([country, f"{average:.2f}"])
		
	return print(tabulate([ [i, *row] for i, row in enumerate(table, start=1) ], headers=["", "country", "gdp"], tablefmt="psql"))

if __name__ == "__main__":
	process_economic_data(args.files)
	data = process_economic_data(args.files)
	save_report(data, args.report)