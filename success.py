#!/usr/bin/python

import csv
	with open('resources.csv', 'r') as f1:
		r = csv.reader(f1, delimiter=',')
		your_list = list(r)
	f1.close()

	with open('resources.csv', 'w') as f:
		f.truncate()
		w = csv.writer(f, delimiter=',')
		data = [[your_list[0][0],your_list[0][1],'0']]
		w.writerows(data)
	f.close()
