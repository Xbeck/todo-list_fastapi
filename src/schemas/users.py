from pydantic import BaseModel, ConfigDict



class UserSchemaAdd(BaseModel):
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )

class UserSchema(UserSchemaAdd):
    id: int