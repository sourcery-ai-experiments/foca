"""Unit test for security.cors.py"""

from foca.security.cors import enable_cors
from flask import Flask


from unittest.mock import patch


@patch('foca.security.cors.CORS')
def test_enable_cors(test_patch):
    """Test that CORS is called with app as a parameter
    """
    app = Flask(__name__)
    assert enable_cors(app) is None
    test_patch.assert_called_with(app)
