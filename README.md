# Python GUI Programming use PyQt5

A collection of examples to quickstart Python GUI application with Qt.

## Preview

Hello world

![Hello world](screenshot/pyqt5-helloworld.png)

Grid layout

![Grid layout](screenshot/pyqt5-grid_layout.png)

Form layout

![Form layout](screenshot/pyqt5-form_layout.png)

Horizontal layout

![Horizontal layout](screenshot/pyqt5-horizontal_layout.png)

Vertical layout

![Vertical layout](screenshot/pyqt5-vertical_layout.png)

Dialog

![Dialog](screenshot/pyqt5-dialog.png)

Calculator

![Calculator](screenshot/pyqt5-calculator.png)

Autocomplete

![Autocomplete](screenshot/pyqt5-autocomplete.png)

Tabs

![Tabs](screenshot/pyqt5-tabs.png)

Toolbox

![Toolbox](screenshot/pyqt5-toolbox.png)

## Setup PyQt5 Environment

We use anaconda to setup environment for develop Python GUI application.

Create conda env with this command:

```
conda create -n pygt5-env python=3
conda activate pygt5-env
conda install -c anaconda pyqt
conda deactivate
```

## QtCreator

QtCreator is a tool for create Qt UI quickly with drag & drop which provide by Qt company.

Install QtCreator on ubuntu

```shell
sudo apt install qtcreator
```

Start QtCrearor with this command

```shell
qtcreator
```

## Qt Designer

Install QT Designer on Ubuntu 18.04+

```shell
sudo apt-get install qttools5-dev-tools
sudo apt-get install qttools5-dev
```

Start Qt Designer

```shell
$ designer
```