from knowledge import *
import random

random.seed("aima-python")


def test_current_best_learning():
    examples = restaurant
    hypothesis = [{'Alt': 'Yes'}]
    h = current_best_learning(examples, hypothesis)
    values = []
    for e in examples:
        values.append(guess_value(e, h))

    assert values == [True, False, True, True, False, True, False, True, False, False, False, True]

    examples = animals_umbrellas
    initial_h = [{'Species': 'Cat'}]
    h = current_best_learning(examples, initial_h)
    values = []
    for e in examples:
        values.append(guess_value(e, h))

    assert values == [True, True, True, False, False, False, True]

    examples = party
    initial_h = [{'Pizza': 'Yes'}]
    h = current_best_learning(examples, initial_h)
    values = []
    for e in examples:
        values.append(guess_value(e, h))

    assert values == [True, True, False]


def test_version_space_learning():
    V = version_space_learning(party)
    results = []
    for e in party:
        guess = False
        for h in V:
            if guess_value(e, h):
                guess = True
                break

        results.append(guess)

    assert results == [True, True, False]
    assert [{'Pizza': 'Yes'}] in V


def test_minimal_consistent_det():
    assert minimal_consistent_det(party, {'Pizza', 'Soda'}) == {'Pizza'}
    assert minimal_consistent_det(party[:2], {'Pizza', 'Soda'}) == set()
    assert minimal_consistent_det(animals_umbrellas, {'Species', 'Rain', 'Coat'}) == {'Species', 'Rain', 'Coat'}
    assert minimal_consistent_det(conductance, {'Mass', 'Temp', 'Material', 'Size'}) == {'Temp', 'Material'}
    assert minimal_consistent_det(conductance, {'Mass', 'Temp', 'Size'}) == {'Mass', 'Temp', 'Size'}


party = [
    {'Pizza': 'Yes', 'Soda': 'No', 'GOAL': True},
    {'Pizza': 'Yes', 'Soda': 'Yes', 'GOAL': True},
    {'Pizza': 'No', 'Soda': 'No', 'GOAL': False}
]

animals_umbrellas = [
    {'Species': 'Cat', 'Rain': 'Yes', 'Coat': 'No', 'GOAL': True},
    {'Species': 'Cat', 'Rain': 'Yes', 'Coat': 'Yes', 'GOAL': True},
    {'Species': 'Dog', 'Rain': 'Yes', 'Coat': 'Yes', 'GOAL': True},
    {'Species': 'Dog', 'Rain': 'Yes', 'Coat': 'No', 'GOAL': False},
    {'Species': 'Dog', 'Rain': 'No', 'Coat': 'No', 'GOAL': False},
    {'Species': 'Cat', 'Rain': 'No', 'Coat': 'No', 'GOAL': False},
    {'Species': 'Cat', 'Rain': 'No', 'Coat': 'Yes', 'GOAL': True}
]

conductance = [
    {'Sample': 'S1', 'Mass': 12, 'Temp': 26, 'Material': 'Cu', 'Size': 3, 'GOAL': 0.59},
    {'Sample': 'S1', 'Mass': 12, 'Temp': 100, 'Material': 'Cu', 'Size': 3, 'GOAL': 0.57},
    {'Sample': 'S2', 'Mass': 24, 'Temp': 26, 'Material': 'Cu', 'Size': 6, 'GOAL': 0.59},
    {'Sample': 'S3', 'Mass': 12, 'Temp': 26, 'Material': 'Pb', 'Size': 2, 'GOAL': 0.05},
    {'Sample': 'S3', 'Mass': 12, 'Temp': 100, 'Material': 'Pb', 'Size': 2, 'GOAL': 0.04},
    {'Sample': 'S4', 'Mass': 18, 'Temp': 100, 'Material': 'Pb', 'Size': 3, 'GOAL': 0.04},
    {'Sample': 'S4', 'Mass': 18, 'Temp': 100, 'Material': 'Pb', 'Size': 3, 'GOAL': 0.04},
    {'Sample': 'S5', 'Mass': 24, 'Temp': 100, 'Material': 'Pb', 'Size': 4, 'GOAL': 0.04},
    {'Sample': 'S6', 'Mass': 36, 'Temp': 26, 'Material': 'Pb', 'Size': 6, 'GOAL': 0.05},
]

def r_example(Alt, Bar, Fri, Hun, Pat, Price, Rain, Res, Type, Est, GOAL):
    return {'Alt': Alt, 'Bar': Bar, 'Fri': Fri, 'Hun': Hun, 'Pat': Pat,
            'Price': Price, 'Rain': Rain, 'Res': Res, 'Type': Type, 'Est': Est,
            'GOAL': GOAL}

restaurant = [
    r_example('Yes', 'No', 'No', 'Yes', 'Some', '$$$', 'No', 'Yes', 'French', '0-10', True),
    r_example('Yes', 'No', 'No', 'Yes', 'Full', '$', 'No', 'No', 'Thai', '30-60', False),
    r_example('No', 'Yes', 'No', 'No', 'Some', '$', 'No', 'No', 'Burger', '0-10', True),
    r_example('Yes', 'No', 'Yes', 'Yes', 'Full', '$', 'Yes', 'No', 'Thai', '10-30', True),
    r_example('Yes', 'No', 'Yes', 'No', 'Full', '$$$', 'No', 'Yes', 'French', '>60', False),
    r_example('No', 'Yes', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Italian', '0-10', True),
    r_example('No', 'Yes', 'No', 'No', 'None', '$', 'Yes', 'No', 'Burger', '0-10', False),
    r_example('No', 'No', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Thai', '0-10', True),
    r_example('No', 'Yes', 'Yes', 'No', 'Full', '$', 'Yes', 'No', 'Burger', '>60', False),
    r_example('Yes', 'Yes', 'Yes', 'Yes', 'Full', '$$$', 'No', 'Yes', 'Italian', '10-30', False),
    r_example('No', 'No', 'No', 'No', 'None', '$', 'No', 'No', 'Thai', '0-10', False),
    r_example('Yes', 'Yes', 'Yes', 'Yes', 'Full', '$', 'No', 'No', 'Burger', '30-60', True)
]
