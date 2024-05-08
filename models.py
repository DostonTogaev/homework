import enum

class TodoType(enum.Enum):
    SHOPPING = 'SHOPPING'
    PERSONAL = 'PERSONAL'

class UserStatus(enum.Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    INBLOKED = 'INBLOKED'

class UserRole(enum.Enum):
    SUPPER_ADMIN = 'SUPPER_ADMIN'
    ADMIN = 'ADMIN'
    USER = 'USER'

class User:
    def __init__(self,
                 username: str,
                 password: str,
                 user_id: int | None = None,
                 role: UserRole | None = None,
                 status: UserStatus | None = None,
                 login_try_count: int | None = None
                 ):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.role = role or UserRole.User.value
        self.status = status.INACTIVE.value
        self.login_try_count = login_try_count or 0

    def __repr__(self) -> str:
        return f'{self.id} - {self.username} - {self.role}'

class Todo:
    def __init__(self,
                 title: str,
                 user_id: int,
                 todo_id: int | None = None,
                 todo_type: TodoType | None = None
                 ):
        self.title = title
        self.user_id = user_id
        self.todo_id = todo_id
        self.todo_type = todo_type or TodoType.PERSONAL.value

    def __repr__(self) -> str:
        return f'{self.id} - {self.title} - {self.user_id}'

