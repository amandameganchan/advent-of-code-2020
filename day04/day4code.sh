#!/bin/bash

# verify passports contain the required fields: 
# byr, iyr, eyr, hgt, hcl, ecl, pid
# if check-restrictions=True, verify the data
# in each column against the specifications
if [ $# != 2 ]; then
  echo "Usage: ./day4code.sh <data-file> <check-restrictions>"
  echo "where <check-restrictions> is True|False"
  exit 1;
fi 

file=$1
check_res=$2

main() {

passport=""
field_counter=0 # passports with valid fields
data_counter=0 # passports with valid data
line_counter=0
last_line=$(wc -l $file | tr -s ' ' | cut -d' ' -f2)

while read line; do
	line_counter=$(($line_counter+1))
	#if blank line or last line, evaluate previous passport
	if [[ -z "$line" ]] || [[ "$last_line" == "$line_counter" ]] ; then
		# if last line, add the final line to passport
		if [[ "$last_line" == "$line_counter" ]]; then
			passport="${passport} $line"
		fi
		# if passport fields valid, increment counter and
		# check further restrictions if necessary
		valid=$(verify_fields $passport)
		if [[ "$valid" == "0" ]]; then
			field_counter=$(($field_counter+1))
			if $check_res; then
				valid_data=$(verify_restrictions $passport)
				if [[ "$valid_data" == "0" ]]; then
					data_counter=$(($data_counter+1))
				fi
			fi
		fi
		#clear passport data for the next one
		passport=""
	#else continue reading in passport
	else
		passport="${passport} $line"	
	fi
done < $file

echo Passports with valid fields: $field_counter
if $check_res; then echo Passports with valid data: $data_counter; fi
}

verify_fields() {
	# grep for each required category; if the passport
	# contains them all, resulting line will be the same 
	# as the input - return 0 if true, 1 if false
	result=$(echo "$*" | grep -w 'byr' | grep -w 'iyr' | grep -w 'eyr' | \
		grep -w 'hgt' | grep -w 'hcl' | grep -w 'ecl' | grep -w 'pid')
	if [[ "$result" == "$*" ]]; then
		echo 0
	fi 
}

verify_restrictions() {
	# collect all field values
	byr=$(echo "$*" | grep -oE 'byr:\d\d\d\d' | cut -c5-)
	iyr=$(echo "$*" | grep -oE 'iyr:\d\d\d\d' | cut -c5-)
	eyr=$(echo "$*" | grep -oE 'eyr:\d\d\d\d' | cut -c5-)
	hgt_num=$(echo "$*" | grep -oE 'hgt:\d*cm|hgt:\d*in' | grep -oE '\d\d\d?')
	hgt_unit=$(echo "$*" | grep -oE 'hgt:\d*cm|hgt:\d*in' | grep -oE 'cm|in')
	hcl=$(echo "$*" | grep -oE 'hcl:#[0-9a-f]{6}')
	ecl=$(echo "$*" | grep -woE 'ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth')
	pid=$(echo "$*" | grep -oE 'pid:[0-9]{9}')
	# verify values against restrictions
	# check hcl, ecl, and pid exist
	if [[ -n $hcl  && -n $ecl && -n $pid ]]; then
		# check byr, iyr, and eyr fall within specified ranges
		if (($byr >= 1920 && $byr <= 2002 && $iyr >= 2010 \
		&& $iyr <= 2020 && $eyr >= 2020 && $eyr <= 2030)); then
			# check hgt falls within specified range
			# corresponding to its unit of measurement
			if [[ "$hgt_unit" == "cm" ]]; then
				if (($hgt_num >= 150 && $hgt_num <= 193)); then
					echo 0
				fi
			elif [[ "$hgt_unit" == "in" ]]; then
				if (($hgt_num >= 59 && $hgt_num <= 76)); then
					echo 0
				fi
			fi
		fi
	fi
}

main
