# CURA Healthcare Service Automated Testing

This repository contains a Pytest-based Selenium automation suite for testing the publicly available CURA Healthcare Service Demo App. The project performs two end-to-end flows:

* **Login Flow**
* **Make Appointment Flow**

All tests are written in Python using:

* **Pytest** for test framework and fixtures
* **Selenium WebDriver** (with `webdriver-manager` to handle ChromeDriver)
* **Allure** for reporting (screenshots automatically attached for failing tests and checkpoints)

---

## Table of Contents

* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)

  * [Running the Tests](#running-the-tests)
  * [Generating an Allure Report](#generating-an-allure-report)
* [Test Flows](#test-flows)

  * [test\_login.py](#test_loginpy)
  * [test\_makeAppointment.py](#test_makeappointmentpy)
* [Screenshots & Allure Results](#screenshots--allure-results)
* [Dependencies](#dependencies)
* [Credits](#credits)

---

## Project Structure

```
├── README.md
├── requirements.txt
├── screenshots/
│   ├── Login-landing.png
│   └── Appointment-schedule.png
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_makeAppointment.py
│   └── allure-results/
│       ├── [*.xml, *.png, *.txt, …]
│       └── ...
└── .gitignore
```

---

## Prerequisites

* Python ≥ 3.7
* Google Chrome (latest stable release)
* Internet access
* pip (Python package manager)

**Note:** You do *not* need to manually download ChromeDriver. The `webdriver-manager` package will handle that.

---

## Installation

```bash
git clone https://github.com/<your-username>/cura-healthcare-selenium.git
cd cura-healthcare-selenium

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate        # (on Linux/macOS)
venv\Scripts\activate.bat       # (on Windows)

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Usage

### Running the Tests

```bash
pytest --alluredir=tests/allure-results
```

This will store test results (including screenshots and metadata) in the `tests/allure-results/` folder.

### Generating an Allure Report

#### Install Allure CLI

**macOS:**

```bash
brew install allure
```

**Windows:**

```powershell
choco install allurecommandline
```

**Linux:**

```bash
wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/<LATEST_VERSION>/allure-<LATEST_VERSION>.zip
unzip allure-<LATEST_VERSION>.zip -d /opt/allure
export PATH=$PATH:/opt/allure/bin
```

#### Generate & Serve Report

```bash
allure generate tests/allure-results --clean -o allure-report
allure open allure-report
```

---

## Test Flows

### test\_login.py

* Navigate to CURA Healthcare homepage
* Click "Make Appointment"
* Enter Credentials:

  * Username: `John Doe`
  * Password: `ThisIsNotAPassword`
* Assert landing page is displayed (e.g., presence of Profile or Logout button)
* Take a screenshot `screenshots/Login-landing.png`
* Attach screenshot to Allure
* Log out and assert redirect to "We Care About Your Health"

### test\_makeAppointment.py

* Navigate and login with same credentials as above
* Fill in form:

  * Facility: `Seoul CURA Healthcare Center`
  * Check "Hospital readmission"
  * Healthcare Program: `Medicaid`
  * Visit Date: today/static date
  * Comment: `This is an automated appointment.`
* Submit and verify confirmation
* Screenshot: `screenshots/Appointment-schedule.png`
* Attach screenshot to Allure
* Logout and confirm return to homepage

---

## Screenshots & Allure Results

### Local Screenshots

Saved to `screenshots/` for:

* Login success
* Appointment confirmation

### Allure Attachments

Embedded directly in report:

```python
allure.attach(
    driver.get_screenshot_as_png(),
    name="<screenshot-name>",
    attachment_type=allure.attachment_type.PNG
)
```

### allure-results/

Allure test metadata and screenshots stored here automatically after running:

```bash
pytest --alluredir=tests/allure-results
```

---

## Dependencies

Listed in `requirements.txt`:

```txt
selenium>=4.0.0
pytest>=6.0.0
allure-pytest>=2.9.45
webdriver-manager>=3.5.2
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## .gitignore

```bash
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Python virtual environment
venv/
.env/

# Allure generated folders
tests/allure-results/
allure-report/

# Screenshots
screenshots/*.png
```

---

## Credits

* **Demo Site:** [Katalon CURA Healthcare Service](https://katalon-demo-cura.herokuapp.com/)
* **Allure Framework:** Qameta Software
* **WebDriver Manager:** Sergey Pugachev
* **Inspiration:** https://github.com/Aniket2683 
