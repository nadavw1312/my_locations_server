from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request
from app.deps import get_current_user
from app.service.user_service import UserService


from app.utils.security import create_access_token, create_refresh_token

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/register", summary="register")
async def register(request: Request):
    body = await request.json()
    UserService.create_user(body["username"], body["password"])
    return "created"


@router.post("/login", summary="login")
async def login(request: Request):
    body = await request.json()
    user = UserService.authenticate_user(body["username"], body["password"])
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    return {
        "access_token": create_access_token(user.username),
        "refresh_token": create_refresh_token(user.username),
    }


@router.post("/token", summary="get access token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserService.authenticate_user(
        form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/me', summary='Get details of currently logged in user')
async def get_me(user=Depends(get_current_user)):
    user = user.__dict__
    del user["password"]
    return user
