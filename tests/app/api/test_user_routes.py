import os
import pytest
import tempfile
from fastapi.testclient import TestClient
from fastapi import status
from src.app.main import app
from src.domain.models.file_entity import FileEntity
from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService
from src.services.file_service import FileService

# WIP


@pytest.fixture()
def client() -> TestClient:

    return TestClient(app)


@pytest.fixture()
def user_service():

    return UserService()


@pytest.fixture()
def file_service():

    return FileService()


@pytest.fixture()
def setUp(client: TestClient, user_service) -> None:

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

    owner = user_entity.id

    yield header, owner

    # user_service.delete(user_entity.id)


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


def test_user_login(client: TestClient, user_service):

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

    assert response.status_code == status.HTTP_200_OK

    user_service.delete(user_entity.id)


def test_upload_file(client: TestClient, setUp: setUp, user_service):

    header, owner = setUp

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

    user_service.delete(owner)

    search_file('document_test.pdf', './uploads')


def test_get_by_id(client: TestClient, setUp: setUp,user_service,file_service):

    header, owner = setUp

    file_content = b"test"

    file_name = "test_file.pdf"

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:

        temp_file.write(file_content)

        temp_file.seek(0)

        params = {"name": "document_test",
                  "description": "this is a description"}

        files = {"file": (file_name, temp_file, "multipart/form-data")}

        client.post('/api/v1/file/upload',params=params, files=files, headers=header)

    file = file_service.find_one({"owner_id":owner})
    
    response = client.get(f'/api/v1/file/{file.id}',headers=header)
    
    assert response.status_code == status.HTTP_200_OK

    user_service.delete(owner)

    search_file('document_test.pdf', './uploads')



def test_get_all(client: TestClient, setUp: setUp,user_service):

    header, owner = setUp

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

    user_service.delete(owner)

    search_file('document_test.pdf', './uploads')