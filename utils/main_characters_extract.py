import spacy
import codecs

def main_characters_extract(plot, character_list):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(plot)
    main_characters = []
    pos_tagged = [(token.text, token.tag_) for token in doc]

    for text, tag in pos_tagged:
        finished_flag = False
        if tag == 'NNP':
            for character in character_list:
                # in case the character has a first name and a last name, check both
                for name in character.split():
                    if (name == text) and (character not in main_characters):
                        main_characters.append(character)
                        finished_flag = True
                        break
                if finished_flag:
                    break
    return main_characters

