# Rest API test automation framework - Python

## Virtual environments

If you wish to use a virtual environment, follow these steps in order to create a virtual environment first. Choose the steps based on your OS.
_Note_ _-_ _Using a virtual environment is optional_

https://docs.python.org/3/library/venv.html

## Installation
Installation is very easy. Python 3 and pip are assumeed to be pre-installed

1. Clone or fork the repository
2. Open the directory in a code editor, for example VSCode
3. Open a terminal and navigate to the root of the directory
4. Every package you need to run these tests is provided in the `requirements.txt` file. Use the following command to install everything

   `pip install -r requirements.txt`

## Running

Run the tests using the following command robot from the root of the repo

`robot -d results .\api\tests\Ping\PingTest.robot`

## Open source

Push to main is disaled. To make changes/improve the code please create a PR and it can be added in

## Usage

The idea is provide a base automation framework that can be used for creating api tests. To do that all that needs to be done is to replace the existing tests with required ones and in the framework supported format and you should be good to go
