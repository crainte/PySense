**Overview**

PySense is the fastest, easiest way to manage and automate your Sisense deployment. 

PySense is more than just an API wrapper. PySense handles all the complexities of the Sisense API for you so you can spend more time creating value for your customers. 

I've taken my years of experience both with implementing BI solutions myself and as a consultant managing implementations for large corporations to streamline what matters most. 

With PySense you can manage your BI implementation like a pro with barely any technical skills. 

**[Documentation](https://htmlpreview.github.io/?https://github.com/nathangiusti/PySense/blob/master/Documentation/index.html)**

**Prerequisites**

Required: 
- A basic understanding of a high level programing language (JS, Java, Python, C/C++/C#, etc)
- A basic understanding of the following programming concepts
    - Control Flows (if, for, while)
    - Objects (calling object methods)
    - Collections (arrays, lists)

Recommended:
- A basic understanding of Python 

If you lack the above but still wish to use PySense I recommend [CodeAcademy](https://www.codecademy.com/learn/learn-python-3)

**Getting Started**

You'll need to have Python 3.0+ and an IDE. Development of PySense was done with [PyCharm](https://www.jetbrains.com/pycharm/).

If you need help installing Python/PyCharm, see our [tutorial](https://github.com/nathangiusti/PySense/raw/master/Installing%20Python.pptx)

Install PySense with pip:
- pip install PySenseSDK

[Tutorial Videos](https://www.youtube.com/playlist?list=PL0xO3VH5OF2JD2KiZs_41zvKvPyebg6MW)

**V 0.3.7 Release Notes**

- Breaking changes
    - None
    
- Additions
    - Download and upload sdata files. 
        - py_client.import_sdata()
        - datamodel.export_to_sdata()
    - Manage your blox actions (endpoints not supported by Sisense)
        - py_client.get_blox_action()
        - py_client.add_blox_action()
        - py_client.delete_blox_action()
    - Manage UI settings
        - py_client.get_ui_settings
        - py_client.set_ui_settings
              
- Fixes
    - Cleaned up imports

- Known Issues
    - REST API sometimes becomes unresponsive on Linux builds
    - REST API sometimes fails uploading sdata files
    
