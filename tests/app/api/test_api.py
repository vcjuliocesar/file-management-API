import os
import pytest
import tempfile
from fastapi.testclient import TestClient
from fastapi import status
from src.app.main import app
from src.infrastructure.configs.database import SessionLocal
from src.domain.exceptions.file_already_exists_exception import FileAlreadyExistsException
from src.domain.models.file_entity import FileEntity
from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService
from src.services.file_service import FileService
from src.infrastructure.repositories.user_repository import UserRepository
from src.infrastructure.repositories.file_repository import FileRepository

# WIP
@pytest.fixture
def mock_get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@pytest.fixture
def test_user_repository(mock_get_db):
    # Configurar la base de datos de pruebas o en memoria para UserRepository
    return UserRepository(db=mock_get_db)

@pytest.fixture
def test_file_repository(mock_get_db):
    # Configurar la base de datos de pruebas o en memoria para UserRepository
    return FileRepository(db=mock_get_db)


@pytest.fixture()
def client() -> TestClient:

    return TestClient(app)


@pytest.fixture()
def user_service(test_user_repository):

    return UserService(user_repository=test_user_repository)


@pytest.fixture()
def file_service(test_file_repository):

    return FileService(file_repository=test_file_repository)


@pytest.fixture()
def set_up(client: TestClient, user_service) -> None:

    new_user_schema = UserSchema(
        name="Jhon Doe",
        email="jhon.doe@example.com",
        password="MySr3cr3tP4ssw0rd_123",
        is_active=True,
        is_admin=False,
        files=[FileEntity()]
    )

    user_entity = user_service.create(new_user_schema)

    response = client.post(
        "/api/v1/login", json={"email": "jhon.doe@example.com", "password": "MySr3cr3tP4ssw0rd_123"})

    header = {"Authorization": f"Bearer {response.json()}"}

    #owner = user_entity.id

    yield header, user_entity


def search_file(file: str, path: str):

    for current_route, directories, files in os.walk(path):

        if file in files:

            route = os.path.join(current_route, file)

            print(f"Found! File path:{route}")

            if os.path.exists(route):

                os.remove(route)

            return None

    return None


def test_it_return_an_exception_if_user_is_not_exists_or_is_not_valid(client: TestClient):

    user = {"email": "fake_user@yopmail.com", "password": "123"}

    response = client.post('/api/v1/login', json=user)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED



def test_user_login(client: TestClient,set_up:set_up,user_service:user_service):

    header,user_entity = set_up
    
    response = client.post(
        "/api/v1/login", json={"email": "jhon.doe@example.com", "password": "MySr3cr3tP4ssw0rd_123"})

    assert response.status_code == status.HTTP_200_OK

    user_service.delete(user_entity.id)


def test_upload_file(client: TestClient, set_up: set_up, user_service):

    header, user_entity = set_up

    file_content = b"test"

    file_name = "test_file.pdf"

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:

        temp_file.write(file_content)

        temp_file.seek(0)

        params = {"name": "document_test",
                  "description": "this is a description"}

        files = {"file": (file_name, temp_file, "multipart/form-data")}

        response = client.post('/api/v1/file/upload',params=params, files=files, headers=header)

    assert response.status_code == status.HTTP_200_OK

    user_service.delete(user_entity.id)

    search_file('document_test.pdf', './uploads')


def test_get_by_id(client: TestClient, set_up: set_up,user_service,file_service):

    header, user_entity = set_up

    file_content = b"test"

    file_name = "test_file.pdf"

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:

        temp_file.write(file_content)

        temp_file.seek(0)

        params = {"name": "document_test",
                  "description": "this is a description"}

        files = {"file": (file_name, temp_file, "multipart/form-data")}

        client.post('/api/v1/file/upload',params=params, files=files, headers=header)

    file = file_service.find_one({"owner_id":user_entity.id})
    
    response = client.get(f'/api/v1/file/{file.id}',headers=header)
    
    assert response.status_code == status.HTTP_200_OK

    user_service.delete(user_entity.id)

    search_file('document_test.pdf', './uploads')



def test_get_all(client: TestClient, set_up: set_up,user_service:user_service):

    header, user_entity = set_up

    file_content = b"test"

    file_name = "test_file.pdf"

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:

        temp_file.write(file_content)

        temp_file.seek(0)

        params = {"name": "document_test",
                  "description": "this is a description"}

        files = {"file": (file_name, temp_file, "multipart/form-data")}

        client.post('/api/v1/file/upload',params=params, files=files, headers=header)

    response = client.get('/api/v1/files',headers=header)
    
    assert response.status_code == status.HTTP_200_OK

    user_service.delete(user_entity.id)

    search_file('document_test.pdf', './uploads')