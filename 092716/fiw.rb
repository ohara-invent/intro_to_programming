#!/usr/bin/ruby

def main(test_nums)
	test_nums.each { |num|
		print num
		print ": "
		print nums_to_words(num)
		print "\n"
	}
end

def nums_to_words(number)
	# puts number
	if (number == 0)
		return "zero"
	elsif (number <= 9)
		return extract_ones(number)
	elsif (number < 100)
		return extract_tens(number)
	elsif (number < 1000)
		return extract_hundreds(number)
	else
		return extract_thousands(number)
	end
end

def extract_thousands(number)
	if (number % 1000 == 0)
		return extract_tens(number / 1000) + " thousand"
	elsif (number % 1000 < 100 )
		return extract_tens(number / 1000) + " thousand and " + extract_tens(number % 1000)
	else
		return extract_tens(number / 1000) + " thousand, " + extract_hundreds(number % 1000)
	end		
end


def extract_hundreds(number)
	if (number % 100 == 0)
		return extract_ones(number / 100) + " hundred"
	else
		return extract_ones(number / 100) + " hundred and " + extract_tens(number % 100)
	end		
end


def extract_tens(number)
	tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	if (number < 10)
		return extract_ones(number)
	elsif (number < 20)
		return extract_teens(number)
	elsif (number <= 100)
		return tens[number / 10] + " " + extract_ones(number % 10)
	end
end

def extract_teens(number)
	teens = %w(ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen)
	return teens[number - 10]
end


def extract_ones(number)
	ones  = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	return ones[number]
end


test_nums = [
	0,
	6,

	10,
	16,

	20,
	26,

	100,
	106,
	110,
	116,
	120,
	126,

	1000,
	1006,
	1010,
	1016,
	1020,
	1026,

	1100,
	1106,
	1110,
	1116,
	1120,
	1126,

	13100,
	13106,
	13110,
	13116,
	13120,
	13126,

	# 131000,
	# 131006,
	# 131010,
	# 131016,
	# 131020,
	# 131026,

	# 1301100,
	# 1301106,
	# 1301110,
	# 1301116,
	# 1301120,
	# 1301126,

	# 13453100,
	# 13453106,
	# 13453110,
	# 13453116,
	# 13453120,
	# 13453126
]

main(test_nums)