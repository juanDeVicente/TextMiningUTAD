import pytest
from word_count.src.word_count import word_count


def test_two_words():
    assert word_count('hola hola', 'spanish') == [('hola', 2)]


def test_three_same_words():
    assert word_count("hola hola hola", "spanish") == [("hola", 3)]


def test_two_different_words():
    assert word_count("hola adios", "spanish") == [("hola", 1), ("adios", 1)]


def test_three_different_words():
    assert word_count("hola adios perejil", "spanish") == [("hola", 1), ("adios", 1), ("perejil", 1)]


def test_two_same_words_one_word_different():
    assert word_count("hola adios hola", "spanish") == [("hola", 2), ("adios", 1)]


def test_param_integer():
    with pytest.raises(ValueError):
        word_count(124)


def test_param_float():
    with pytest.raises(ValueError):
        word_count(1.12334)


def test_param_bool():
    with pytest.raises(ValueError):
        word_count(False)


def test_param_none():
    with pytest.raises(ValueError):
        word_count(None)


def test_with_more_than_one_space():
    assert word_count("hola              hola        hola") == [("hola", 3)]


def test_two_words_german():
    assert word_count("hallo hallo", "german") == [("hallo", 2)]


def test_three_words_german():
    assert word_count("schwule hallo schwule", "german") == [("schwule", 2), ("hallo", 1)]


def test_words_upper_case_lower_case_german():
    assert word_count("schwule ScHWule SCHWULE SchWUle SCHWule", "german") == [("schwule", 5)]


def test_with_commas_german():
    assert word_count("Hallo, ich bin Raul und freue mich, Sie kennenzulernen. Ich bin Raul", "german") == [
        ("raul", 2),
        ("hallo", 1),
        ("freue", 1),
        ("kennenzulernen", 1)]


def test_use_stopwords_german():
    assert word_count("hallo vom hallo von vor hallo wann warum hallo was weiter hallo weitere hallo", "german") == [
        ("hallo", 6),
        ("wann", 1),
        ("warum", 1),
        ("weitere", 1)]


# Here are the tests in italian


def test_two_words_italian():
    assert word_count("ciao ciao", "italian") == [("ciao", 2)]


def test_three_words_italian():
    assert word_count("ciao ciao donna", "italian") == [("ciao", 2), ("donna", 1)]


def test_words_upper_case_lower_case_italian():
    assert word_count("DONNA donna DOnna DOnNA doNNA", "italian") == [("donna", 5)]


def test_with_commas_italian():
    assert word_count("Ciao, mi chiamo Raul, piacere di conoscerti, sono Raul", "italian") == [("raul", 2),
                                                                                               ("ciao", 1),
                                                                                               ("chiamo", 1),
                                                                                               ("piacere", 1),
                                                                                               ("conoscerti", 1)]


def test_use_stopwords_italian():
    assert word_count("ciao lungo ciao ma ciao me ciao meglio ciao molta", "italian") == [("ciao", 5), ('lungo', 1),
                                                                                          ('me', 1), ('meglio', 1),
                                                                                          ('molta', 1)]


def test_param_list():
    with pytest.raises(ValueError):
        word_count(['hola', 'adios', 'hola'])


def test_param_dict():
    with pytest.raises(ValueError):
        word_count({'hola': 2, 'adios': 5, '123': 25})


def test_words_upper_case_lower_case_same_words():
    assert word_count("hOla HOLA hoLa HOla holA", "spanish") == [("hola", 5)]


def test_words_upper_case_lower_case_different_words():
    assert word_count("hOla hoLa adios Adios adiOS HOLA") == [("hola", 3), ("adios", 3)]


def test_param_list():
    with pytest.raises(ValueError):
        word_count(['hola', 'adios', 'hola'])


def test_param_dict():
    with pytest.raises(ValueError):
        word_count({'hola': 2, 'adios': 5, '123': 25})


def test_words_upper_case_lower_case_same_words():
    assert word_count("hOla HOLA hoLa HOla holA", "spanish") == [("hola", 5)]


def test_words_upper_case_lower_case_different_words():
    assert word_count("hOla hoLa adios Adios adiOS HOLA") == [("hola", 3), ("adios", 3)]


def test_with_commas():
    assert word_count("Hola, me llamo Juan, encantado de conocerte soy Juan", "spanish") == [("juan", 2), ("hola", 1),
                                                                                             ("llamo", 1),
                                                                                             ("encantado", 1),
                                                                                             ("conocerte", 1)]


def test_using_stopwords_spanish():
    assert word_count("hola hola de hola la hola o hola y hola y y hola ante a el la los las", "spanish") == [
        ("hola", 7)]


def test_using_stop_words_english():
    assert word_count("hello hello hello shouldn't aren't hello ourselves a hello a a a a", "english") == [("hello", 5)]


def test_example_english():
    assert word_count("Hello, my name is Juan. Nice to meet you. i'm juan", "english") == [("juan", 2), ("hello", 1),
                                                                                           ("name", 1), ("nice", 1),
                                                                                           ("meet", 1), ("i'm", 1)]


def test_stop_words_apostophe_english():
    assert word_count("You're amazing", "english") == [("amazing", 1)]


def test_stop_words_apostophe_and_puntuation_english():
    assert word_count("you're,,,,,,, amazing.....", "english") == [("amazing", 1)]


def test_text_with_more_than_one_space_english():
    assert word_count("hello   buddy") == [("hello", 1), ("buddy", 1)]
    # MIRAR PORQUE NO SE WHY CON ESPACIOS PARES NO FUNCIONA PERO CON ESPACIOS PARES, SI


def test_only_stop_words_english():
    assert word_count("how are you", "english") == []


def test_with_exclamations_and_interrogations_english():
    assert word_count("today!!!!! is a great day???????") == [("today", 1), ("great", 1), ("day", 1)]


def test_two_word_french():
    assert word_count('salut salut', 'french') == [('salut', 2)]


def test_three_word_french():
    assert word_count('salut adieu salut', 'french') == [('salut', 2), ('adieu', 1)]


def test_words_upper_case_lower_case_french():
    assert word_count('sAlut Salut SALUT sAlUt saluT', 'french') == [('salut', 5)]


def test_with_commas_french():
    assert word_count("Bonjour, je m'appelle Juan, revi de vous rencontrer, je suis Juan", 'french') == [('juan', 2),
                                                                                                         ('bonjour', 1),
                                                                                                         (
                                                                                                             "m'appelle",
                                                                                                             1),
                                                                                                         ('revi', 1),
                                                                                                         ('rencontrer',
                                                                                                          1)]


def test_wikipedia_definition_text_french():
    assert word_count("Un texte est une série orale ou écrite de mots perçus comme constituant " \
                      "un ensemble cohérent, porteur de sens et utilizant les structures", 'french') == [('texte', 1),
                                                                                                         ('série', 1),
                                                                                                         ('orale', 1),
                                                                                                         ('écrite', 1),
                                                                                                         ('mots', 1),
                                                                                                         ('perçus', 1),
                                                                                                         ('comme', 1), (
                                                                                                             'constituant',
                                                                                                             1), (
                                                                                                             'ensemble',
                                                                                                             1),
                                                                                                         (
                                                                                                             'cohérent',
                                                                                                             1),
                                                                                                         ('porteur', 1),
                                                                                                         ('sens', 1),
                                                                                                         ('utilizant',
                                                                                                          1),
                                                                                                         ('les', 1), (
                                                                                                             'structures',
                                                                                                             1)
                                                                                                         ]


def test_punctuation_signs():
    assert word_count('¿¿¿¿????? ¡¡¡¡ ???? !!!!! ... ,,,,') == []


def test_empty_list():
    '''
    Encontrado el fallo por el usuario de github https://github.com/enriquesanchezb
    '''
    assert word_count('') == []