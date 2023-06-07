import pytest
from PyQt5.QtWidgets import QApplication
from ..main import ArchiveViewer

@pytest.fixture
def app(qtbot):
    test_app = QApplication([])
    yield test_app
    test_app.quit()

def test_archive_viewer_fetch_data_from_table(app):
    viewer = ArchiveViewer()
