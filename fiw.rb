#!/usr/bin/ruby

def fiw(number)
	dictionary = Hash[
		0 => "",
		1 => "one",
		2 => "two",
		3 => "three",
		4 => "four",
		5 => "five",
		6 => "six",
		7 => "seven",
		8 => "eight",
		9 => "nine",
		10 => "ten",
		11 => "eleven",
		12 => "twelve",
		13 => "thirteen",
		14 => "fourteen",
		15 => "fifteen",
		16 => "sixteen",
		17 => "seventeen",
		18 => "eighteen",
		19 => "nineteen",
		20 => "twenty",
		30 => "thirty",
		40 => "forty",
		50 => "fifty",
		60 => "sixty",
		70 => "seventy",
		80 => "eighty",
		90 => "ninety",
		100 => "hundred",
		1000 => "thousand",
		1000000 => "million",
		1000000000 => "billion"
	]

	return "negative " + fiw(number.abs) if number < 0
	return dictionary[number] if number <= 20
	return dictionary[(number / 10) * 10] + " " + fiw(number % 10) if number > 20
	return "zero" if number == 0 # TODO: Bring back zero
end


(-99..99).each { |number|
	puts "#{number}: #{fiw(number)}"
}