from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"


class TaskCreate(TaskBase):
    project_id: int


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True
