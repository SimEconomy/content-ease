# Development Environment Setup

## Introduction

This document outlines the steps to set up the development environment for ContentEase. This includes the installation of necessary tools and dependencies to facilitate the development process.

## Steps

1. **Install Python**: Ensure that Python 3.8 or higher is installed. You can download it from https://www.python.org/downloads/.

2. **Virtual Environment Setup**: Create a virtual environment to manage project dependencies. Use the following command to create a virtual environment named `env`:
```sh
python -m venv env
```

3. **Activate the Virtual Environment**:
- **On Windows**:
  ```sh
  .\env\Scripts\activate
  ```
- **On macOS and Linux**:
  ```sh
  source env/bin/activate
  ```

4. **Install Dependencies**: Once the virtual environment is activated, you can install the required dependencies from `requirements.txt` using the following command:
```sh
pip install -r requirements.txt
```

5. **Environment Variables**: Set up any necessary environment variables in the `.env` file. These should include paths to key resources or API keys required for the project.