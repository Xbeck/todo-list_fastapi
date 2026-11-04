from ..modells.users import UsersOrm
from ..utils.repository import SQLAlchemyRepository


class UsersRepo(SQLAlchemyRepository):
    model = UsersOrm