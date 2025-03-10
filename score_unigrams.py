# Write a function called score_unigrams that takes three arguments:
#   - a path to a folder of training data 
#   - a path to a test file that has a sentence on each line
#   - a path to an output CSV file
#
# Your function should do the following:
#   - train a single unigram model on the combined contents of every .txt file
#     in the training folder
#   - for each sentence (line) in the test file, calculate the log unigram 
#     probability ysing the trained model (see the lab handout for details on log 
#     probabilities)
#   - write a single CSV file to the output path. The CSV file should have two
#     columns with headers, called "sentence" and "unigram_prob" respectively.
#     "sentence" should contain the original sentence and "unigram_prob" should
#     contain its unigram probabilities.
#
# Additional details:
#   - there is training data in the training_data folder consisting of the contents 
#     of three novels by Jane Austen: Emma, Sense and Sensibility, and Pride and Prejudice
#   - there is test data you can use in the test_data folder
#   - be sure that your code works properly for words that are not in the 
#     training data. One of the test sentences contains the words 'color' (American spelling)
#     and 'television', neither of which are in the Austen novels. You should record a log
#     probability of -inf (corresponding to probability 0) for this sentence.
#   - your code should be insensitive to case, both in the training and testing data
#   - both the training and testing files have already been tokenized. This means that
#     punctuation marks have been split off of words. All you need to do to use the
#     data is to split it on spaces, and you will have your list of unigram tokens.
#   - you should treat punctuation marks as though they are words.
#   - it's fine to reuse parts of your unigram implementation from HW3.

# You will need to use log and -inf here. 
# You can add any additional import statements you need here.
from math import log, inf
from pathlib import Path
import csv


#######################
# YOUR CODE GOES HERE #

def score_unigrams(training_dir, test, output):
    
    # my_path = Path('dirA')
    # for txt_file in my_path.glob('*.txt'):
    # with open(txt_file) as file:
    # # Do something with each file...
    counts = {}
    total_words = 0

    for txt_file in Path(training_dir).glob('*.txt'):
        with open(txt_file) as f:
            words = f.read().split()
            #print(txt)

            #str_lst = [x.lower() for x in words]
            
            for word in words:
                word = word.lower()
                counts[word] = counts.get(word,0) + 1
                total_words += 1
            # for key in counts:
            #     counts[key] = counts.get(key) / len(str_lst)
    
    probs = {}
    for word in counts:
        probs[word] = counts[word] / total_words
    
    results = []
    with open(test) as test_file:
        test_sentences = test_file.readlines()
    for sentence in test_sentences:
        sentence = sentence.strip()
        words = sentence.split()
        words = [word.lower() for word in words]

        log_prob = 0
        unknown_word_found = False
        for word in words:
            if word not in probs:
                unknown_word_found = True
                break
            else:
                word_prob = probs[word]
                log_prob += log(word_prob)
        result = {}
        result['sentence'] = sentence
        if unknown_word_found:
            result['unigram_prob'] = str(-inf)
        else:
            result['unigram_prob'] = str(log_prob)
        results.append(result)

    with open(output, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=['sentence', 'unigram_prob'])
        writer.writeheader()
        writer.writerows(results)


    # prob = 1
    # sentence_lst = [x.lower() for x in sentence_lst]
    # for word in sentence_lst:
    #     prob *= unigram_dict[word]
    # return prob
    


            
            
    

    
#######################



# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    score_unigrams('training_data','test_data/test_sentences.txt','output')
