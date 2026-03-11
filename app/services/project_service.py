from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


def create_project(db: Session, project_data: ProjectCreate, owner_id: int):

    project = Project(
        name=project_data.name,
        description=project_data.description,
        owner_id=owner_id
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_projects(db: Session, owner_id: int):

    return db.query(Project).filter(Project.owner_id == owner_id).all()


def get_project_by_id(db: Session, project_id: int, owner_id: int):

    return (
        db.query(Project)
        .filter(Project.id == project_id, Project.owner_id == owner_id)
        .first()
    )


def update_project(db: Session, project: Project, project_data: ProjectUpdate):

    project.name = project_data.name
    project.description = project_data.description

    db.commit()
    db.refresh(project)

    return project


def delete_project(db: Session, project: Project):

    db.delete(project)
    db.commit()

    return project