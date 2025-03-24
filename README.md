# auto_qa: Automated Web Forms and Components Testing

This repository contains Python scripts for automated testing of web forms and components, utilizing Selenium, pytest, and Allure for comprehensive and insightful test reporting.

## Features

* **Web Form Automation:** Automates interaction with web forms, including input field population, form submission, and validation.
* **Component Testing:** Verifies the functionality and behavior of individual web components.
* **Selenium Integration:** Leverages Selenium for robust browser automation and interaction.
* **pytest Framework:** Uses pytest for test discovery, execution, and organization.
* **Allure Reporting:** Generates detailed and visually appealing test reports with Allure.
* **Modular and Reusable Scripts:** Scripts are designed for easy modification and reuse across different web applications.
* **Dependency Management:** Uses `requirements.txt` for consistent and reproducible environment setup.

## Getting Started

### Prerequisites

* Python 3.11
* pip (Python package installer)
* A web browser (Chrome, Firefox, etc.) with the corresponding WebDriver installed.

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/evgborovoy/auto_qa.git](https://github.com/evgborovoy/auto_qa.git)
    cd auto_qa
    ```

2.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Run tests with pytest:**

    ```bash
    pytest --alluredir=reports
    ```

2.  **Generate Allure report:**

    ```bash
    allure serve
    ```

    This will open the Allure report in your default web browser.


### Dependencies

* Selenium
* pytest
* Allure-pytest
* requirements.txt contain all dependencies

### Contributing

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write tests and ensure they pass.
4.  Commit your changes.
5.  Push to your fork.
6.  Submit a pull request.

### Author

* evgborovoy

### Future Improvements

* Implement CI/CD pipelines for automated test execution.
* Expand test coverage to include more complex web forms and components.
* Add more detailed documentation for each test script.
* Improve error handling and reporting.
* Add more configuration options, such as browser selection through command line arguments.

