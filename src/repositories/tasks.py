from ..modells.tasks import TasksOrm
from ..utils.repository import SQLAlchemyRepository



class TasksRepo(SQLAlchemyRepository):
    model = TasksOrm