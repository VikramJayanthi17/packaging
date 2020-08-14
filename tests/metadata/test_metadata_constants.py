# -*- coding: UTF-8 -*-

from packaging.metadata import Metadata
import json



VALID_PACKAGE_2_1_RFC822 = """Metadata-Version: 2.1
Name: sampleproject
Version: 2.0.0
Summary: A sample Python project
Home-page: https://github.com/pypa/sampleproject
Author: A. Random Developer
Author-email: author@example.com
License: UNKNOWN
Project-URL: Bug Reports, https://github.com/pypa/sampleproject/issues
Project-URL: Funding, https://donate.pypi.org
Project-URL: Say Thanks!, http://saythanks.io/to/example
Project-URL: Source, https://github.com/pypa/sampleproject/
Description: # A sample Python project
        
        ![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")
        
        A sample project that exists as an aid to the [Python Packaging User
        Guide][packaging guide]'s [Tutorial on Packaging and Distributing
        Projects][distribution tutorial].
        
        This project does not aim to cover best practices for Python project
        development as a whole. For example, it does not provide guidance or tool
        recommendations for version control, documentation, or testing.
        
        [The source for this project is available here][src].
        
        Most of the configuration for a Python project is done in the `setup.py` file,
        an example of which is included in this project. You should edit this file
        accordingly to adapt this sample project to your needs.
        
        ----
        
        This is the README file for the project.
        
        The file should use UTF-8 encoding and can be written using
        [reStructuredText][rst] or [markdown][md use] with the appropriate [key set][md
        use]. It will be used to generate the project webpage on PyPI and will be
        displayed as the project homepage on common code-hosting services, and should be
        written for that purpose.
        
        Typical contents for this file would include an overview of the project, basic
        usage examples, etc. Generally, including the project changelog in here is not a
        good idea, although a simple “What's New” section for the most recent version
        may be appropriate.
        
        [packaging guide]: https://packaging.python.org
        [distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
        [src]: https://github.com/pypa/sampleproject
        [rst]: http://docutils.sourceforge.net/rst.html
        [md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
        [md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
        
Keywords: sample,setuptools,development
Platform: UNKNOWN
Classifier: Development Status :: 3 - Alpha
Classifier: Intended Audience :: Developers
Classifier: Topic :: Software Development :: Build Tools
Classifier: License :: OSI Approved :: MIT License
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.5
Classifier: Programming Language :: Python :: 3.6
Classifier: Programming Language :: Python :: 3.7
Classifier: Programming Language :: Python :: 3.8
Classifier: Programming Language :: Python :: 3 :: Only
Requires-Python: >=3.5, <4
Description-Content-Type: text/markdown
Provides-Extra: dev
Provides-Extra: test
Requires-Dist: peppercorn
Requires-Dist: check-manifest ; extra == 'dev'
Requires-Dist: coverage ; extra == 'test'
"""


VALID_PACKAGE_2_1_DICT = Metadata._pkginfo_string_to_dict(VALID_PACKAGE_2_1_RFC822)

VALID_PACKAGE_2_1_JSON = json.dumps(VALID_PACKAGE_2_1_DICT, sort_keys=True)


VALID_PACKAGE_1_0_RFC822 = """Metadata-Version: 1.0
Name: sampleproject
Version: 2.0.0
Summary: A sample Python project
Home-page: https://github.com/pypa/sampleproject
Author: A. Random Developer
Author-email: author@example.com
License: UNKNOWN
Description: # A sample Python project
        A longer description
Keywords: sample,setuptools,development
Platform: UNKNOWN
"""

VALID_PACKAGE_1_0_REPEATED_DESC = """Metadata-Version: 1.0
Name: sampleproject
Version: 2.0.0
Summary: A sample Python project
Home-page: https://github.com/pypa/sampleproject
Author: A. Random Developer
Author-email: author@example.com
License: UNKNOWN
Description: # A sample Python project
        A longer description
Keywords: sample,setuptools,development
Platform: UNKNOWN

# This is the long description 

This will overwrite the Description field
"""
VALID_PACKAGE_1_0_SINGLE_LINE_DESC = """Metadata-Version: 1.0
Name: sampleproject
Version: 2.0.0
Summary: A sample Python project
Home-page: https://github.com/pypa/sampleproject
Author: A. Random Developer
Author-email: author@example.com
License: UNKNOWN
Description: # A sample Python project
Keywords: sample,setuptools,development
Platform: UNKNOWN
"""

VALID_PACKAGE_1_0_DICT = Metadata._pkginfo_string_to_dict(VALID_PACKAGE_1_0_RFC822)
VALID_PACKAGE_1_0_JSON = json.dumps(VALID_PACKAGE_1_0_DICT, sort_keys=True)


VALID_PACKAGE_1_2_RFC822 = """Metadata-Version: 1.2
Name: sampleproject
Version: 2.0.0
Summary: A sample Python project
Home-page: https://github.com/pypa/sampleproject
Author: A. Random Developer
Author-email: author@example.com
License: UNKNOWN
Description: # A sample Python project
        A longer description
Keywords: sample,setuptools,development
Platform: UNKNOWN
Requires-Python: >=3.5, <4
"""

VALID_PACKAGE_1_2_DICT = Metadata._pkginfo_string_to_dict(VALID_PACKAGE_1_2_RFC822)
VALID_PACKAGE_1_2_JSON = json.dumps(VALID_PACKAGE_1_2_DICT, sort_keys=True)

VALID_PACKAGE_1_1_RFC822 = """Metadata-Version: 1.1
Name: sampleproject
Version: 2.0.0
Summary: A sample Python project
Home-page: https://github.com/pypa/sampleproject
Author: A. Random Developer
Author-email: author@example.com
License: UNKNOWN
Description: # A sample Python project
        A longer description
Keywords: sample,setuptools,development
Platform: UNKNOWN
Classifier: Development Status :: 3 - Alpha
Classifier: Intended Audience :: Developers
Classifier: Topic :: Software Development :: Build Tools
"""

VALID_PACKAGE_1_1_DICT = Metadata._pkginfo_string_to_dict(VALID_PACKAGE_1_1_RFC822)
VALID_PACKAGE_1_1_JSON = json.dumps(VALID_PACKAGE_1_1_DICT, sort_keys=True)
