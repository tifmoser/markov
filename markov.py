'''
Markov Chain Sentence Generator (include shitposting capabilities)
'''

import json, os

START = 1
END = 0

def buildChain (text: str) -> dict:
    chain = {START: {'A': 0}}

    lastWord = START
    for word in text:
        # add word to chain
        if not chain[lastWord]:
            chain[lastWord] = {}
        if not chain[lastWord][word]:
            chain[lastWord][word] = 0
        #TODO: include end characters

        # increment word counter
        chain[lastWord][word] += 1

        lastWord = word
    return chain

def generateSentence (chain: dict):
    #TODO: generate sentence
    pass


def main():
    # read the input file
    text_file = open('input_file.txt')
    text = text_file.read()

    text.replace(' ', '\n')
    #TODO: separate punctuation also

    chain = buildChain(text)

    print(generateSentence(chain))

    return
