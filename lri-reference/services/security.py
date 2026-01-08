from fastapi import HTTPException, Depends
from typing import Dict, Optional
import jwt
import time

# Simple Role-Based Access Control (RBAC) DB
# In a real app, this would be in a database with hashed passwords.
USERS_DB: Dict[str, Dict] = {
    "admin": {"role": "admin", "password": "adminpass"},
    "observer": {"role": "observer", "password": "observerpass"},
    "agent_user": {"role": "agent", "password": "agentpass"},
}

SECRET_KEY = "supersecretkey"

def authenticate_user(username: str, password: str):
    user = USERS_DB.get(username)
    if user and user["password"] == password:
        # Create token with 1 hour expiration
        token = jwt.encode({
            "user": username,
            "role": user["role"],
            "exp": time.time() + 3600
        }, SECRET_KEY, algorithm="HS256")
        return token
    return None

def get_current_user(token: str = ""):
    if not token:
        raise HTTPException(status_code=401, detail="Missing authentication token")
    try:
        # Decode and validate token
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def require_role(user: Dict, role: str):
    # Simple hierarchy or strict check? Let's do strict for this PoC
    # Or allow admin to do everything.
    if user["role"] == "admin":
        return
    if user["role"] != role:
        raise HTTPException(status_code=403, detail=f"Role '{role}' required")

def encrypt_data(data: str):
    # placeholder: replace with AES or Fernet in production
    return data[::-1]

def decrypt_data(data: str):
    return data[::-1]
