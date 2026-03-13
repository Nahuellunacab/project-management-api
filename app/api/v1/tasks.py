from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import (
    create_task,
    get_task_by_id,
    update_task,
    delete_task
)
from app.services.project_service import get_project_by_id
from app.api.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskResponse)
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = get_project_by_id(db, task.project_id, current_user.id)

    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return create_task(db, task)


@router.put("/{task_id}", response_model=TaskResponse)
def update_existing_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    project = get_project_by_id(db, task.project_id, current_user.id)

    if not project:
        raise HTTPException(status_code=403, detail="No autorizado")

    return update_task(db, task, task_data)


@router.delete("/{task_id}")
def delete_existing_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    project = get_project_by_id(db, task.project_id, current_user.id)

    if not project:
        raise HTTPException(status_code=403, detail="No autorizado")

    delete_task(db, task)

    return {"message": "Tarea eliminada"}
