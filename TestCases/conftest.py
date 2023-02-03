'''
Created on 03-Oct-2022
@author: saipr
'''
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    
    global driver
    
    driver = webdriver.Chrome("C:\\Users\\saipr\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
    
    return driver


def pytest_configure(config):
    
    config._metadata['Project Name'] = 'smsTest'
    
    config._metadata['Module Name'] = 'Users'
    
    config._metadata['Tester'] = 'Unknown'
    

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
    
    
def pytest_addoption(parser):
    parser.addoption("--garageName")
    parser.addoption("--fileEntry")
    parser.addoption("--fileExit")
   
@pytest.fixture(scope="class",autouse=True)
def garageName(request):
    return request.config.getoption("--garageName")

@pytest.fixture(scope="class",autouse=True)
def userEntry(request):
    return request.config.getoption("--userEntry")

@pytest.fixture(scope="class",autouse=True)
def userExit(request):
    return request.config.getoption("--userExit")
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            driver.save_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra



