# The file valence_data/winter_2016_senses_valence.csv contains data from an 
# experiment that asked people to provide valence ratings for words associated
# with each of the five senses (touch, taste, smell, sight, sound). The file has
# three columns: Word, Modality, and Val. Word contains the word, Modality the
# sensory modality, and Val contains the mean valence rating for that word,
# where higher valence corresponds to more positive emotional states.

# The question we'll try to answer is whether certain sensory modalities have 
# higher or lower mean valences than others.
# 
#  Write a function called get_mean_valence that takes a Path to a CSV file
#  as input. You can assume the file will be formatted as described above.
#  Your function should return a dictionary with keys corresponding to each
#  of the five modalities. The value for each key should be its mean valence
#  score across all of the words in the CSV file.

# The data are from the paper 
#
# Winter, B. (2016). Taste and smell words form an affectively loaded and emotionally
# flexible part of the English lexicon. Language, Cognition and Neuroscience, 31(8), 
# 975-988.

#######################
# YOUR CODE GOES HERE #
import csv
def get_mean_valence(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        # d = {}

        # [...]

        # if key in d:
        #   d[key].append(value)
        # else:
        #   d[key] = [ value ]
        mean_valences = {}
        for dct in data:
            modality = dct['Modality']
            valence = float(dct['Val'])

            if modality in mean_valences:
                mean_valences[modality].append(valence)
            else:
                mean_valences[modality] = [valence]
        
        for key, valences in mean_valences.items():
            mean_valences[key] = sum(valences)/len(valences)
        return mean_valences



#######################


# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    print(get_mean_valence('valence_data/winter_2016_senses_valence.csv'))
