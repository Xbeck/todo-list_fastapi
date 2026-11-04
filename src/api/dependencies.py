from ..repositories.tasks import TasksRepo
from ..repositories.users import UsersRepo
from ..services.tasks import TasksService
from ..services.users import UsersService




def tasks_service():
    return TasksService(TasksRepo)


def users_service():
    return UsersService(UsersRepo)


