# Auto Factorial

[![HitCount](http://hits.dwyl.io/AlbertSuarez/auto-factorial.svg)](http://hits.dwyl.io/AlbertSuarez/auto-factorial)
![Python application](https://github.com/AlbertSuarez/auto-factorial/workflows/Python%20application/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/auto-factorial.svg)](https://GitHub.com/AlbertSuarez/auto-factorial/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/auto-factorial.svg)](https://GitHub.com/AlbertSuarez/auto-factorial/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/AlbertSuarez/auto-factorial.svg)](https://github.com/AlbertSuarez/auto-factorial)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/auto-factorial.svg)](https://GitHub.com/AlbertSuarez/auto-factorial/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/auto-factorial.svg)](https://github.com/AlbertSuarez/auto-factorial/blob/master/LICENSE)

📝 Docker image that clocks you in daily on Factorial

## How to run

TODO

## Python requirements

This project is using Python3.7. All these requirements have been specified in the `requirements.lock` file.

1. [Selenium](https://selenium-python.readthedocs.io/): used for simulating the action of clocking in.
2. [APScheduler](https://apscheduler.readthedocs.io/en/stable/): used for scheduling jobs in a certain time.

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run this script, please execute the following from the root directory:

1. Setup virtual environment

2. Install dependencies

    ```bash
    pip3 install -r requirements.lock
    ```

3. Build Docker container locally

    ```bash
    docker build --tag auto_factorial_dev:0.1 .
    ```

4. Run container setting needed environment variables

    ```bash
    docker run -d -e "DEVELOPMENT_MODE=true" -e "FACTORIAL_EMAIL_ADDRESS=redacted" -e "FACTORIAL_PASSWORD=redacted" --name auto_factorial_dev auto_factorial_dev:0.1
    ```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © Auto Factorial
