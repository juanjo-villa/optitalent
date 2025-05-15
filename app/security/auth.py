from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.models.employee import Employee
from app.security.utils import verify_password
from app.security.config import SECRET_KEY, ALGORITHM
from app.db.session import get_db

# Dependency for token-based authentication using OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Login logic: validate email and password
def authenticate_user(db: Session, email: str, password: str) -> Employee:
    user = db.query(Employee).filter(Employee.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

# Retrieve the currently logged-in user from the JWT token
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> Employee:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(Employee).filter(Employee.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    return user