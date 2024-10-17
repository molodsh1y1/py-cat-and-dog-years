def get_human_age(cat_age: int, dog_age: int) -> list:
    if not is_valid_age(cat_age) or not is_valid_age(dog_age):
        raise ValueError
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year


def is_valid_age(age: int) -> bool:
    return 0 <= age <= 100
