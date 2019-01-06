from main import navigate
import pytest

@pytest.fixture
def url():
    return 'https://seo-psideodev81.b-com.hosting/CommunityPortal/ProgressivePortal/DB881BA0C4/App/Views/InformationPage/View.aspx?InformationPageID=3316'

def test_get_exhibitors(url):
    assert 2 == len([exhibitor for exhibitor in navigate(url)])



