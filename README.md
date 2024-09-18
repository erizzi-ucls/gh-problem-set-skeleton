# Problem Set Skeleton

![pipeline status](https://gitlab.ucls.uchicago.edu/ml-ai/problem-set-skeleton/badges/main/pipeline.svg)
![coverage](https://gitlab.ucls.uchicago.edu/ml-ai/problem-set-skeleton/badges/main/coverage.svg)

This folder contains a basic skeleton for a Python problem set and its
accompanying tests. It is intended to be used with Microsoft's `vscode`.

## Setup

There are three basic steps you need in order to get this project up and
running with type checking, linting, and unit testing enabled.

#### 0. Open the project's workspace

Open `vscode` and select `File` -> `Open Workspace from File`. Then, select the
`skeleton.code-workspace` file within this project folder.

#### 1. Install necessary extensions

On the left-most side of the `vscode` window, select the extensions tab (four
small squares making a larger square) and install the following extensions:

- `Python`
- `Pylance` (auto installed with `Python` extension)
- `Black Formatter`
- `isort`

> Note: be careful to select only the "Microsoft approved" extensions.

#### 2. Install necessary Python modules

Open the terminal window by selecting `Terminal` -> `New Terminal`. Then,
install `pytest` by typing `pip3 install pytest`.

