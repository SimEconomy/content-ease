import pytest
from easegen.content_creation import generate_content
def test_generate_content():
    assert generate_content('technology') == 'Generated content for topic technology'