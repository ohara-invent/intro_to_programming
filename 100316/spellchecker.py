from collections import Counter


def spellcheck(text_filename, output_filename):
	print("Checking for errors...")

	original_text = read_file(text_filename)
	words = extract_words(original_text)
	words_list = extract_words(original_text)
	corrected_words = extract_words(original_text)
	
	wrong_words_index = []

	num_words = len(words)
	for index, word in enumerate(words):
		print_progress(index, num_words)

		normalised_word = normalise(word)
		if not is_valid([word]):
			correct_word = get_correction(word)
			highligted_word = "**{}/{}**".format(normalised_word, correct_word)
			wrong_words_index.append((index, word, correct_word))

			words[index] = word.replace(normalised_word, highligted_word)
			corrected_words[index] = word.replace(normalised_word, correct_word)


	marked_text = " ".join(words)
	corrected_text = " ".join(corrected_words)

	write_file(output_filename, marked_text)

	print("\n")
	print("Document has been successfully checked, and errors have been marked. What do you want to do next?\n")
	return original_text, corrected_text, words, wrong_words_index


def apply_corrections_interactively(filename, words_list, wrong_words_index):
	for correction in wrong_words_index:

		index = correction[0]
		wrong_word = correction[1]
		correct_word = correction[2]

		while True:
			answer = input("Change {0} to {1}?(y/n):".format(wrong_word, correct_word))
			if answer.lower() == 'y':
				print(correction[2])
				words_list[index] = wrong_word.replace(normalise(wrong_word), correct_word)
				break
			elif answer.lower() == 'n':
				words_list[index] = wrong_word.replace(normalise(wrong_word), wrong_word)
				print(correction[1])
				break
			else:
				print("Incorrect option!")

	write_file(filename, " ".join(words_list))



def read_file(filename):
	with open(filename, 'r') as file:
		return file.read()


def extract_words(text):
	text = text.replace("-", " ")
	words = text.split()
	return [word for word in words]


def print_progress(index, num_words):
	progress_text = "\rProcessing word {0}  of {1}".format(index + 1, num_words)
	print(progress_text, end= " ")



def normalise(word):
	punctions = ",:.?\"!;:()[]\{\}\\/'"
	return word.strip(punctions)


def write_file(filename, data):
	with open(filename, 'w') as file:
		file.write(data)


def get_words(text):
	return [normalise(word) for word in text.split()]








with open('big.txt', 'r') as file:
    corpus = file.read()
    word_counts = Counter(get_words(corpus))

def get_probability(word, N=sum(word_counts.values())):
    "return probability of 'word'."
    return word_counts[word] / N

def get_correction(word):
    "Return most probable spelling correction for 'word'."
    return max(candidate_corrections(word), key=get_probability)

def candidate_corrections(word):
    "Return possible spelling corrections for 'word'."
    return (is_valid([word]) or is_valid(edits1(word)) or is_valid(edits2(word)) or [word])

def is_valid(words):
    "Return all the words in 'words' that appear in 'word_counts'."
    return set(word for word in words if word in word_counts)

def edits1(word):
    "Return all the edits that are 1 edit away from 'word'."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "Return all the edits that are 2 edits away from 'word'."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))