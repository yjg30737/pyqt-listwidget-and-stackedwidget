from setuptools import setup, find_packages

setup(
    name='pyqt-listwidget-and-stackedwidget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_listwidget_and_stackedwidget.style': ['list_widget.css']},
    description="PyQt QStackedWidget which can be set current widget by clicking QListWidget's item.",
    url='https://github.com/yjg30737/pyqt-listwidget-and-stackedwidget.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)