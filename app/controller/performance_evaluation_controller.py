from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.performance_evaluation_schema import PerformanceEvaluationCreate, PerformanceEvaluationUpdate, PerformanceEvaluationOut
from app.service import performance_evaluation_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/performance-evaluations", tags=["PerformanceEvaluations"])

@router.post("/", response_model=PerformanceEvaluationOut, status_code=201)
def create_evaluation(payload: PerformanceEvaluationCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return performance_evaluation_service.create_evaluation_service(db, payload)

@router.put("/{evaluation_id}", response_model=PerformanceEvaluationOut)
def update_evaluation(evaluation_id: int, payload: PerformanceEvaluationUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = performance_evaluation_service.update_evaluation_service(db, evaluation_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Evaluation not found")
    return updated

@router.delete("/{evaluation_id}")
def delete_evaluation(evaluation_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = performance_evaluation_service.delete_evaluation_service(db, evaluation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Evaluation not found")
    return {"message": "Evaluation deleted"}

@router.get("/{evaluation_id}", response_model=PerformanceEvaluationOut)
def get_evaluation(evaluation_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    evaluation = performance_evaluation_service.get_evaluation_service(db, evaluation_id)
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation not found")
    return evaluation
