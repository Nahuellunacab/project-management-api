from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.services.project_service import (
    create_project,
    get_projects,
    get_project_by_id,
    update_project,
    delete_project
)
from app.api.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=ProjectResponse)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_project(db, project, current_user.id)


@router.get("", response_model=list[ProjectResponse])
def read_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_projects(db, current_user.id)


@router.get("/{project_id}", response_model=ProjectResponse)
def read_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = get_project_by_id(db, project_id, current_user.id)

    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return project


@router.put("/{project_id}", response_model=ProjectResponse)
def update_existing_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = get_project_by_id(db, project_id, current_user.id)

    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return update_project(db, project, project_data)


@router.delete("/{project_id}")
def delete_existing_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = get_project_by_id(db, project_id, current_user.id)

    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    delete_project(db, project)

    return {"message": "Proyecto eliminado"}
