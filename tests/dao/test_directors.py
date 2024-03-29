import pytest

from project.dao import DirectorsDAO
from project.models import Director


class TestDirectorDAO:

    @pytest.fixture
    def directors_dao(self, db):
        return DirectorsDAO(db.session)

    @pytest.fixture
    def director_1(self, db):
        director = Director(name='Квентин Тарантино')
        db.session.add(director)
        db.session.commit()
        return director

    @pytest.fixture
    def director_2(self, db):
        director = Director(name='Джеймс Мэнголд')
        db.session.add(director)
        db.session.commit()
        return director

    def test_get_by_id(self, director_1, directors_dao):
        assert directors_dao.get_by_id(director_1.id) == director_1

    def test_get_genre_by_id_not_found(self, directors_dao):
        assert not directors_dao.get_by_id(1)

    def test_get_all(self, directors_dao, director_1, director_2):
        assert directors_dao.get_all() == [director_1, director_2]

    def test_get_all_with_page(self, app, directors_dao, director_1, director_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert directors_dao.get_all(page=1) == [director_1]
        assert directors_dao.get_all(page=2) == [director_2]
        assert directors_dao.get_all(page=3) == []
