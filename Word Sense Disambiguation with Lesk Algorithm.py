import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import wordnet
from nltk import word_tokenize
from nltk.corpus import stopwords


# Function to disambiguate a word in a sentence and find the best sense
def disambiguate(word, sentence, stopwords):

        word_senses = wordnet.synsets(word)
        best_sense = word_senses[0]
        max_overlap = 0
        context = set(word_tokenize(sentence))

        for sense in word_senses:
            signature = tokenized_gloss(sense)
            overlap = compute_overlap(signature, context, stopwords)
            if overlap > max_overlap:
                max_overlap = overlap
                best_sense = sense

        return best_sense


# Function to extract all tokens about definition of sense
def tokenized_gloss(sense):

        tokens = set(word_tokenize(sense.definition()))

        for example in sense.examples():
            tokens.union(set(word_tokenize(example)))

        return tokens


# Function to compute the overlap of words
def compute_overlap(signature, context, stopwords):

        gloss = signature.difference(stopwords)

        return len(gloss.intersection(context))


stopwords = set(stopwords.words('english'))
sentence = ("They eat a meal")
context = set(word_tokenize(sentence))
word = 'eat'
syn = wordnet.synsets('eat')[1]
signature = tokenized_gloss(syn)


# Result 1
print("Word :", word)
print("Sense :", syn.name())
print("Definition :", syn.definition())
print("Sentence :", sentence)


# Result 2
print(signature)
print(compute_overlap(signature, context, stopwords))
print("Best sense: ", disambiguate(word, sentence, stopwords))