from sqlalchemy.orm import Session
from app.repository import status_permission_repository
from app.schemas.status_permission_schema import StatusPermissionCreate, StatusPermissionUpdate
from app.models.status_permission import StatusPermission

def create_status_permission_service(db: Session, payload: StatusPermissionCreate) -> StatusPermission:
    return status_permission_repository.create_status_permission(db, payload)

def update_status_permission_service(db: Session, permission_id: int, payload: StatusPermissionUpdate) -> StatusPermission | None:
    return status_permission_repository.update_status_permission(db, permission_id, payload)

def delete_status_permission_service(db: Session, permission_id: int) -> bool:
    return status_permission_repository.delete_status_permission(db, permission_id)

def get_status_permission_service(db: Session, permission_id: int) -> StatusPermission | None:
    return status_permission_repository.get_status_permission_by_id(db, permission_id)