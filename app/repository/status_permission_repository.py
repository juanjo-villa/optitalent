from sqlalchemy.orm import Session
from app.models.status_permission import StatusPermission
from app.schemas.status_permission_schema import StatusPermissionCreate, StatusPermissionUpdate

def create_status_permission(db: Session, payload: StatusPermissionCreate) -> StatusPermission:
    perm = StatusPermission(**payload.dict())
    db.add(perm)
    db.commit()
    db.refresh(perm)
    return perm

def update_status_permission(db: Session, permission_id: int, payload: StatusPermissionUpdate) -> StatusPermission | None:
    perm = get_status_permission_by_id(db, permission_id)
    if perm:
        for key, value in payload.dict().items():
            setattr(perm, key, value)
        db.commit()
        db.refresh(perm)
    return perm

def delete_status_permission(db: Session, permission_id: int) -> bool:
    perm = get_status_permission_by_id(db, permission_id)
    if perm:
        db.delete(perm)
        db.commit()
        return True
    return False

def get_status_permission_by_id(db: Session, permission_id: int) -> StatusPermission | None:
    return db.query(StatusPermission).filter(StatusPermission.id == permission_id).first()