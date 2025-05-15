from fastapi import FastAPI
from app.controller.auth_controller import router as auth_router
from app.controller.employee_controller import router as employee_router
from app.controller.position_controller import router as position_router
from app.controller.schedule_controller import router as schedule_router
from app.controller.employee_schedule_controller import router as employee_schedule_router
from app.controller.count_employee_schedule_controller import router as count_employee_schedule_router  
from app.controller.payroll_controller import router as payroll_router
from app.controller.payroll_adjustments_controller import router as payroll_adjustments_router
from app.controller.status_controller import router as status_router
from app.controller.status_permission_controller import router as status_permission_router
from app.controller.performance_evaluation_controller import router as performance_evaluation_router
from app.controller.to_do_controller import router as to_do_router

app = FastAPI(
    title="OptiTalent RRHH API",
    version="1.0.0"
)

# Register all routers
app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(position_router)
app.include_router(schedule_router)
app.include_router(employee_schedule_router)
app.include_router(count_employee_schedule_router)  
app.include_router(payroll_router)
app.include_router(payroll_adjustments_router)
app.include_router(status_router)
app.include_router(status_permission_router)
app.include_router(performance_evaluation_router)
app.include_router(to_do_router)
