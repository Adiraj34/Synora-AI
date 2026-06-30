from app.models.user import User
from app.models.user import User
from app.utils.hash import (
    hash_password,
    verify_password
)

def register_user(db, user):

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(db):
    return db.query(User).all()

def login_user(
    db,
    email,
    password
):
    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    return user