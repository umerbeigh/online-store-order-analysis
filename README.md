
# Online Store Order Analysis

Analyze customer orders from an online store dataset.

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
   - [Running Tests](#running-tests)
   - [Running the Program](#running-the-program)

4. [Contact](#contact)


## Introduction

This project analyzes customer orders from an online store dataset. It computes total revenue for each month, product, and customer. Additionally, it identifies the top 10 customers by revenue.

## Getting Started

This section explains how users can set up and run the project on their local machines.

### Prerequisites

- Docker installed on your machine

### Installation

Clone the repository:

```bash
    git clone https://github.com/umerbeigh/online-store-order-analysis.git
    cd online-store-order-analysis
```

## Usage

## Running Tests

To run tests, execute the following command:
### Build the test Docker image
```bash
docker build -t online-store-tests --target test-runner .
```
### Run the Docker container for tests
```bash
docker run online-store-tests
```

## Running the Program
After running the tests, you can run the main program to analyze the dataset. Use the following command:

### Build the program Docker image
```bash
docker build -t online-store-program --target program-runner .
```
### Run the Docker container for the program
```bash
docker run online-store-program
```

## Contact
For any inquiries, please contact:

Umer Beigh

+91 7006947414

https://www.linkedin.com/in/umerbeigh848/





