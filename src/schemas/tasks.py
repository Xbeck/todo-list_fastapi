from pydantic import BaseModel, ConfigDict



class TaskSchemaAdd(BaseModel):
    title: str
    author_id: int
    assignee_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class TaskSchema(TaskSchemaAdd):
    id: int