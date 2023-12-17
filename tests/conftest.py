import pytest
from selene.support.shared import config, browser


@pytest.fixture
def set_options_in_browser():
    config.window_width = 1920
    config.window_height = 1080
    config.base_url = 'https://demoqa.com/'
