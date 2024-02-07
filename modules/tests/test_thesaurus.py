import modules
import modules.src.thesaurus as thesaurus
import requests
"""
TO DO:
1. Update thesaurus.py so it actually will see whether the string put in is right (ie has the word synonym)
2. Update tests appropriately
3. Figure out assert?
4. Examine project requirements again
5. In jarvis.py, figure out how to make it seem more chatbot-y

"""
def test_thesaurus():
    print(thesaurus.process('synonyms for justice'))
    print(thesaurus.process('jreojakljlk'))
    assert (thesaurus.process('comfort synonyms')['success'] == True)
    assert (thesaurus.process("jfskljfslkajlkfa")['success'] == False)


    # assert ('thesaurus' == thesaurus.process('comfort synonyms'))
    # assert ('thesaurus' == modules.process_query('synonyms for fancy')[0])
    # assert ('thesaurus' != modules.process_query('something random')[0])


if __name__ == '__main__':
    print("Hello world!")
    test_thesaurus()

