import pytest
from entity import *
from race import *



class TestEntity:
    # @pytest.fixture
    # def class_for_sample(self):
    #     x = char_Class()
    #     return x

    @pytest.fixture
    def sample_entity(self):
        return Entity(elf_race)

    def test_initial_stats(self, sample_entity):
        assert sample_entity.__race == elf_race
        assert sample_entity.__health_points == 100

    def test_damage_taken(self, sample_entity):
        damage = sample_entity.receive_damage(10)
        assert damage == 90
        assert sample_entity.__health_points == 90

    def test_stats(self, sample_entity):
        assert sample_entity.stats['str'] 
