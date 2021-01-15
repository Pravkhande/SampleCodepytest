
**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/cache.html) for more information.

Pre-requistes:
Install below plugins using following commands:
pytest
selenium
pytest-html 

**pip install pytest** or **pip install -U pytest**

**pip install selenium**

**pip install pytest-html**


Command to execute:
Navigaate to the root directory and run below command:

``python -m pytest --html="reports/report.html" --junitxml="reports/report.xml"``

