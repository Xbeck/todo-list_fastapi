from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from ..db.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            qry = select(self.model)
            result = await session.execute(qry)
            res = [row[0].to_read_model() for row in result.all()]
            return res
