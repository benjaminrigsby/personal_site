import pytest
import pathlib
import sys
app_path = str(pathlib.Path(__file__).parents[1])
sys.path.append(app_path)
print(sys.path)
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data  # Example content check


def test_contact_route(client):
    """Test the home page."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact" in response.data  # Example content check


def test_blog_route(client):
    """Test the Blog page."""
    response = client.get('/blog')
    assert response.status_code == 200
    assert b"Blog" in response.data  # Check if "Blog" is in the response content


def test_blog_post_route(client):
    """Test a single blog post page."""
    response = client.get('/blog/1')
    assert response.status_code == 200
    assert b"Overview" in response.data


def test_notes_route(client):
    """Test the Notes page."""
    response = client.get('/notes')
    assert response.status_code == 200
    assert b"Notes" in response.data


def test_notes_post_route(client):
    """Test a single notes post page."""
    response = client.get('/notes/1')
    assert response.status_code == 200
    assert b"Gear" in response.data


def test_projects_route(client):
    """Test the Projects page."""
    response = client.get('/projects')
    assert response.status_code == 200
    assert b"Projects" in response.data


def test_projects_post_route(client):
    """Test a single project post page."""
    response = client.get('/projects/1')
    assert response.status_code == 200
    assert b"MATLAB" in response.data


def test_404_route(client):
    """Test a non-existent route."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
