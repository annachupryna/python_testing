import pytest

from human import Human


@pytest.fixture(scope='function')
def create_human():
    human = Human('Olena', 20, 'female')
    yield human
    print('TEARDOWN')


@pytest.fixture
def create_human_with_custom_params():
    def __create_human(name, age, gender):
        human = Human(name=name, age=age, gender=gender)
        return human

    return __create_human
