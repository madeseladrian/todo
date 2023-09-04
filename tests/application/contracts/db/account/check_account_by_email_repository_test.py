from src.application.contracts.db.account import CheckAccountByEmailRepository

from inspect import isabstract


class TestCheckAccountByEmailRepository:
    def test_1_should_CheckAccountByEmailRepository_is_an_abstract_class(self):
        assert isabstract(CheckAccountByEmailRepository)
