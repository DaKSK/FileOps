import pytest

from unittest.mock import mock_open, MagicMock, patch
from file_operations import TextFile


class TestInit:

    def test_empty_path(self):

        with pytest.raises(ValueError):
            text_file = TextFile("")

    # @pytest.mark.skip
    def test_none_path(self):
        with pytest.raises(ValueError):
            text_file = TextFile(None)

    # @pytest.mark.skip
    def test_path_ok(self):
        text_file = TextFile("test_path_ok_file.txt")
        assert isinstance(text_file, TextFile)
        assert text_file.f_path == "test_path_ok_file.txt"


class TestRead:

    # @pytest.mark.skip
    def test_empty(self):
        # mock = MagicMock()
        # mock.return_value = []

        text_file = TextFile("test_read_file.txt")

        # with patch("builtins.open", mock):
        with patch('builtins.open', mock_open(read_data="")):
            content = text_file.read()

        assert content == []

    @pytest.mark.skip
    def test_not_exists(self):
        pass

    @pytest.mark.skip
    def test_has_content(self):
        pass