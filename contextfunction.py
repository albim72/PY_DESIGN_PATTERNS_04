from contextlib import contextmanager

@contextmanager
def get_state(name):
    print(f"wprowadzenie: {name}")
    yield name
    print(f"wyjście: {name}")

with get_state("Czerwony") as A:
    with get_state("Zielony") as B:
        with get_state("Czarny") as C:
            print(f"działenia wewnątrz with: {A}, {B}, {C}")
