from sqlalchemy.orm import Session
from app.models.performance_evaluation import PerformanceEvaluation
from app.schemas.performance_evaluation_schema import PerformanceEvaluationCreate, PerformanceEvaluationUpdate

def create_evaluation(db: Session, payload: PerformanceEvaluationCreate) -> PerformanceEvaluation:
    evaluation = PerformanceEvaluation(**payload.dict())
    db.add(evaluation)
    db.commit()
    db.refresh(evaluation)
    return evaluation

def update_evaluation(db: Session, evaluation_id: int, payload: PerformanceEvaluationUpdate) -> PerformanceEvaluation | None:
    evaluation = get_evaluation_by_id(db, evaluation_id)
    if evaluation:
        for key, value in payload.dict().items():
            setattr(evaluation, key, value)
        db.commit()
        db.refresh(evaluation)
    return evaluation

def delete_evaluation(db: Session, evaluation_id: int) -> bool:
    evaluation = get_evaluation_by_id(db, evaluation_id)
    if evaluation:
        db.delete(evaluation)
        db.commit()
        return True
    return False

def get_evaluation_by_id(db: Session, evaluation_id: int) -> PerformanceEvaluation | None:
    return db.query(PerformanceEvaluation).filter(PerformanceEvaluation.id == evaluation_id).first()