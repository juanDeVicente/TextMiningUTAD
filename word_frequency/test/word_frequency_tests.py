import pytest
from word_frequency.src.word_frequency import word_frequency


def test_two_words():
    assert word_frequency('hola hola', 'spanish') == [('hola', 100)]


def test_three_same_words():
    assert word_frequency("hola hola hola", "spanish") == [("hola", 100)]


def test_two_different_words():
    assert word_frequency("hola adios", "spanish") == [("hola", 50), ("adios", 50)]


def test_three_different_words():
    assert word_frequency("hola adios perejil", "spanish") == [("hola", 33.3), ("adios", 33.3), ("perejil", 33.3)]


def test_two_same_words_one_word_different():
    assert word_frequency("hola adios hola", "spanish") == [("hola", 66.7), ("adios", 33.3)]


def test_param_integer():
    with pytest.raises(ValueError):
        word_frequency(124)


def test_param_float():
    with pytest.raises(ValueError):
        word_frequency(1.12334)


def test_param_bool():
    with pytest.raises(ValueError):
        word_frequency(False)


def test_param_none():
    with pytest.raises(ValueError):
        word_frequency(None)


def test_with_more_than_one_space():
    assert word_frequency("hola              hola        hola") == [("hola", 100)]


def test_two_words_german():
    assert word_frequency("hallo hallo", "german") == [("hallo", 100)]


def test_three_words_german():
    assert word_frequency("schwule hallo schwule", "german") == [("schwule", 66.7), ("hallo", 33.3)]


def test_words_upper_case_lower_case_german():
    assert word_frequency("schwule ScHWule SCHWULE SchWUle SCHWule", "german") == [("schwule", 100)]


def test_with_commas_german():
    assert word_frequency("Hallo, ich bin Raul und freue mich, Sie kennenzulernen. Ich bin Raul", "german") == [
        ("raul", 40),
        ("hallo", 20),
        ("freue", 20),
        ("kennenzulernen", 20)]


def test_use_stopwords_german():
    assert word_frequency("hallo vom hallo von vor hallo wann warum hallo was weiter hallo weitere hallo", "german") == [
        ("hallo", 66.7),
        ("wann", 11.1),
        ("warum", 11.1),
        ("weitere", 11.1)]


# Here are the tests in italian


def test_two_words_italian():
    assert word_frequency("ciao ciao", "italian") == [("ciao", 100)]


def test_three_words_italian():
    assert word_frequency("ciao ciao donna", "italian") == [("ciao", 66.7), ("donna", 33.3)]


def test_words_upper_case_lower_case_italian():
    assert word_frequency("DONNA donna DOnna DOnNA doNNA", "italian") == [("donna", 100)]


def test_with_commas_italian():
    assert word_frequency("Ciao, mi chiamo Raul, piacere di conoscerti, sono Raul", "italian") == [("raul", 33.3),
                                                                                               ("ciao", 16.7),
                                                                                               ("chiamo", 16.7),
                                                                                               ("piacere", 16.7),
                                                                                               ("conoscerti", 16.7)]


def test_use_stopwords_italian():
    assert word_frequency("ciao lungo ciao ma ciao me ciao meglio ciao molta", "italian") == [("ciao", 55.6), ('lungo', 11.1),
                                                                                          ('me', 11.1), ('meglio', 11.1),
                                                                                          ('molta', 11.1)]


def test_param_list():
    with pytest.raises(ValueError):
        word_frequency(['hola', 'adios', 'hola'])


def test_param_dict():
    with pytest.raises(ValueError):
        word_frequency({'hola': 2, 'adios': 5, '123': 25})


def test_words_upper_case_lower_case_same_words():
    assert word_frequency("hOla HOLA hoLa HOla holA", "spanish") == [("hola", 100)]


def test_words_upper_case_lower_case_different_words():
    assert word_frequency("hOla hoLa adios Adios adiOS HOLA") == [("hola", 50), ("adios", 50)]


def test_param_list():
    with pytest.raises(ValueError):
        word_frequency(['hola', 'adios', 'hola'])


def test_param_dict():
    with pytest.raises(ValueError):
        word_frequency({'hola': 2, 'adios': 5, '123': 25})


def test_words_upper_case_lower_case_same_words():
    assert word_frequency("hOla HOLA hoLa HOla holA", "spanish") == [("hola", 100)]


def test_words_upper_case_lower_case_different_words():
    assert word_frequency("hOla hoLa adios Adios adiOS HOLA") == [("hola", 50), ("adios", 50)]


def test_with_commas():
    assert word_frequency("Hola, me llamo Juan, encantado de conocerte soy Juan", "spanish") == [("juan", 33.3), ("hola", 16.7),
                                                                                             ("llamo", 16.7),
                                                                                             ("encantado", 16.7),
                                                                                             ("conocerte", 16.7)]


def test_using_stopwords_spanish():
    assert word_frequency("hola hola de hola la hola o hola y hola y y hola ante a el la los las", "spanish") == [
        ("hola", 100)]


def test_using_stop_words_english():
    assert word_frequency("hello hello hello shouldn't aren't hello ourselves a hello a a a a", "english") == [("hello", 100)]


def test_example_english():
    assert word_frequency("Hello, my name is Juan. Nice to meet you. i'm juan", "english") == [("juan", 28.6), ("hello", 14.3),
                                                                                           ("name", 14.3), ("nice", 14.3),
                                                                                           ("meet", 14.3), ("i'm", 14.3)]


def test_stop_words_apostophe_english():
    assert word_frequency("You're amazing", "english") == [("amazing", 100)]


def test_stop_words_apostophe_and_puntuation_english():
    assert word_frequency("you're,,,,,,, amazing.....", "english") == [("amazing", 100)]


def test_text_with_more_than_one_space_english():
    assert word_frequency("hello   buddy") == [("hello", 50), ("buddy", 50)]
    # MIRAR PORQUE NO SE WHY CON ESPACIOS PARES NO FUNCIONA PERO CON ESPACIOS PARES, SI


def test_only_stop_words_english():
    assert word_frequency("how are you", "english") == []


def test_with_exclamations_and_interrogations_english():
    assert word_frequency("today!!!!! is a great day???????") == [("today", 33.3), ("great", 33.3), ("day", 33.3)]


def test_two_word_french():
    assert word_frequency('salut salut', 'french') == [('salut', 100)]


def test_three_word_french():
    assert word_frequency('salut adieu salut', 'french') == [('salut', 66.7), ('adieu', 33.3)]


def test_words_upper_case_lower_case_french():
    assert word_frequency('sAlut Salut SALUT sAlUt saluT', 'french') == [('salut', 100)]


def test_with_commas_french():
    assert word_frequency("Bonjour, je m'appelle Juan, revi de vous rencontrer, je suis Juan", 'french') == [('juan', 33.3),
                                                                                                         ('bonjour', 16.7),
                                                                                                         (
                                                                                                             "m'appelle",
                                                                                                             16.7),
                                                                                                         ('revi', 16.7),
                                                                                                         ('rencontrer',
                                                                                                          16.7)]


def test_wikipedia_definition_text_french():
    assert word_frequency("Un texte est une série orale ou écrite de mots perçus comme constituant " \
                      "un ensemble cohérent, porteur de sens et utilizant les structures", 'french') == [('texte', 6.7),
                                                                                                         ('série', 6.7),
                                                                                                         ('orale', 6.7),
                                                                                                         ('écrite', 6.7),
                                                                                                         ('mots', 6.7),
                                                                                                         ('perçus', 6.7),
                                                                                                         ('comme', 6.7), (
                                                                                                             'constituant',
                                                                                                             6.7), (
                                                                                                             'ensemble',
                                                                                                             6.7),
                                                                                                         (
                                                                                                             'cohérent',
                                                                                                             6.7),
                                                                                                         ('porteur', 6.7),
                                                                                                         ('sens', 6.7),
                                                                                                         ('utilizant',
                                                                                                          6.7),
                                                                                                         ('les', 6.7), (
                                                                                                             'structures',
                                                                                                             6.7)
                                                                                                         ]


def test_punctuation_signs():
    assert word_frequency('¿¿¿¿????? ¡¡¡¡ ???? !!!!! ... ,,,,') == []


def test_empty_list():
    '''
    Encontrado el fallo por el usuario de github https://github.com/enriquesanchezb
    '''
    assert word_frequency('') == []