import random
import string
import datetime
from random import randrange
from datetime import timedelta
import json 
import django 

def middle_initial():
	upper_alpha = string.ascii_uppercase
	initial = random.choice(upper_alpha)
	return initial

def fake_dob():
	start = datetime.datetime.strptime('1/1/1900','%m/%d/%Y')
	end = datetime.datetime.strptime('1/1/2010','%m/%d/%Y')
	delta = end - start
	int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	random_second = randrange(int_delta)
	dob = start + timedelta(seconds=random_second)
	return dob

def main():
	# Filenames
	first_name_list = "firstnames.txt"
	last_name_list = "lastnames.txt"
	address_list = "addresses.txt"
	drug_name_list = "drugs.txt"
	prescriber_list = "prescribers.txt"
	
	phile = open('PHIle_output.txt', 'a')
	
	i = 0

	top_count = 1000	

	first_name_memlist = open(first_name_list).read().splitlines()
	last_name_memlist = open(last_name_list).read().splitlines()
	addr_memlist = open(address_list).read().splitlines()
	drug_name_memlist = open(drug_name_list).read().splitlines()
	print "Lists read into memory..."

	phile.write("===============================================\n")
	phile.write(" NOTICE: THIS IS NOT REAL PHI	            \n")
	phile.write(" This is randomly-generated data designed to   \n")
	phile.write(" mimic the look of PHI for security testing    \n")
	phile.write("===============================================\n")
	phile.write("\n\n")

	while i <= top_count:
		first_name = random.choice(first_name_memlist)
		middle_i = middle_initial()
		last_name = random.choice(last_name_memlist)
		dob = str(fake_dob())[:-9]
		address = random.choice(addr_memlist)
		drug_name = random.choice(drug_name_memlist)
		i=i+1
		phile.write(first_name + " " + middle_i + " " + last_name + "\t" + dob + "\t" + address + "\t" + drug_name + "\n")

	
if __name__ == '__main__':
	main()
