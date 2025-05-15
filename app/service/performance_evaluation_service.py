from sqlalchemy.orm import Session
from app.repository import performance_evaluation_repository
from app.schemas.performance_evaluation_schema import PerformanceEvaluationCreate, PerformanceEvaluationUpdate
from app.models.performance_evaluation import PerformanceEvaluation

def create_evaluation_service(db: Session, payload: PerformanceEvaluationCreate) -> PerformanceEvaluation:
    return performance_evaluation_repository.create_evaluation(db, payload)

def update_evaluation_service(db: Session, evaluation_id: int, payload: PerformanceEvaluationUpdate) -> PerformanceEvaluation | None:
    return performance_evaluation_repository.update_evaluation(db, evaluation_id, payload)

def delete_evaluation_service(db: Session, evaluation_id: int) -> bool:
    return performance_evaluation_repository.delete_evaluation(db, evaluation_id)

def get_evaluation_service(db: Session, evaluation_id: int) -> PerformanceEvaluation | None:
    return performance_evaluation_repository.get_evaluation_by_id(db, evaluation_id)
