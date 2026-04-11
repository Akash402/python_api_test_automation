# REST API Test Automation Framework — Python

A lightweight, fork-and-go API test automation framework built with **Robot Framework** and **Python**. Clone it, point it at your API, and you have a working test suite in minutes.

The included examples run against the [Restful Booker API](https://restful-booker.herokuapp.com/) — a public practice API. Delete the `examples/` folder when you're ready to write your own tests.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Robot Framework](https://robotframework.org/) | Test execution and reporting |
| [pabot](https://pabot.org/) | Parallel test execution |
| [Python 3](https://www.python.org/) | Core language |
| [requests](https://docs.python-requests.org/) | HTTP client |
| [robotframework-jsonlibrary](https://pypi.org/project/robotframework-jsonlibrary/) | JSON handling in tests |

---

## Project Structure

```
├── lib/
│   ├── config.py                    # Environments, auth strategy, endpoint map
│   ├── auth.py                      # Auth handling (Basic, OAuth, API Key)
│   └── methods.py                   # HTTP helper functions (GET, POST, etc.)
├── api/
│   ├── data/                        # Request payloads and test data (JSON)
│   ├── keywords/
│   │   ├── CommonKeywords.robot     # Reusable response assertions
│   │   ├── TemplateKeywords.robot   # Starting point for your own keywords
│   │   ├── PingKeywords.robot       # Example
│   │   └── BookingKeywords.robot    # Example
│   └── tests/
│       ├── examples/                # Example tests — safe to delete
│       │   ├── PingTest.robot
│       │   └── BookingCRUDTest.robot
│       └── template/                # Copy this to start your own suite
│           └── TemplateTest.robot
├── .env.example                     # Copy to .env and fill in credentials
├── requirements.txt
└── .github/workflows/main.yml       # CI/CD — smoke on push, regression on schedule
```

---

## Quick Start

**1. Fork and clone**

```bash
git clone <your-fork-url>
cd python_api_test_automation
```

**2. Create a virtual environment (recommended)**

```bash
# macOS/Linux
python3 -m venv venv && source venv/bin/activate

# Windows
python -m venv venv && venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure credentials**

```bash
cp .env.example .env
```

Open `.env` and fill in your values. The framework will raise a clear error at startup if any required variables are missing.

**5. Run the example tests**

```bash
robot -d results api/tests/examples
```

Open `results/report.html` in a browser to view the test report.

---

## Configuration

All config lives in `lib/config.py`, driven by environment variables set in `.env`.

### Environments

Set `ENV` to switch between environments without changing any code:

```bash
ENV=staging robot -d results api/tests/
```

Add your URLs to `.env`:

```bash
ENV=dev
DEV_URL=https://your-dev-api.com/
STAGING_URL=https://your-staging-api.com/
PROD_URL=https://your-api.com/
```

### Auth strategies

Set `AUTH_TYPE` in your `.env` to one of:

| `AUTH_TYPE` | Required env vars | Use when |
|---|---|---|
| `basic` | `API_USERNAME`, `API_PASSWORD` | Username/password auth |
| `oauth` | `TOKEN_URL`, `CLIENT_ID`, `CLIENT_SECRET` | OAuth 2.0 client credentials |
| `api_key` | `API_KEY`, `API_KEY_HEADER` | Static API key in a header |
| `none` | — | Open/public APIs |

OAuth tokens are fetched once, cached, and refreshed automatically before expiry — no manual token management needed.

### Endpoints

Add your API endpoints to the `ENDPOINTS` dict in `lib/config.py`:

```python
ENDPOINTS = {
    "your_resource": "your/path",
}
```

Reference them in keywords as `${ENDPOINTS['your_resource']}`.

---

## Building Your Own Tests

1. Copy `.env.example` to `.env` and fill in your credentials and URLs
2. Add your endpoints to `lib/config.py`
3. Add any request payload JSON files under `api/data/`
4. Copy `api/keywords/TemplateKeywords.robot` → `api/keywords/YourResourceKeywords.robot` and follow the comments
5. Copy `api/tests/template/TemplateTest.robot` → `api/tests/your-feature/YourTest.robot` and follow the comments
6. Delete `api/tests/examples/` when you no longer need the reference tests

### Tags

Use tags to control which tests run in which context:

| Tag | When to use |
|---|---|
| `smoke` | Fast, critical happy path tests. Run on every push and before deploys. |
| `regression` | Full suite. Run on schedule or after releases. |
| `critical` | Must never fail in prod. Apply to your most important flows. |

```bash
# Run only smoke tests
robot -d results --include smoke api/tests/

# Run only regression tests in parallel
pabot --processes 4 -d results --include regression api/tests/
```

### Common assertions

`CommonKeywords.robot` provides reusable assertions — import it in any keyword file:

```robot
Resource    ../../keywords/CommonKeywords.robot
```

| Keyword | Arguments |
|---|---|
| `Status Code Should Be` | `${response}`, `${expected_status}` |
| `Response Should Be Successful` | `${response}` |
| `Response Should Contain Field` | `${response}`, `${field}` |
| `Response Field Should Equal` | `${response}`, `${field}`, `${expected_value}` |
| `Response Should Not Be Empty` | `${response}` |

---

## Running Tests

### PyCharm

Install the [Robot Framework Language Server](https://plugins.jetbrains.com/plugin/16086-robot-framework-language-server) plugin first, then:

1. Open **Run → Edit Configurations**
2. Click **+** and select **Robot Framework**
3. Set:
   - **Name:** `Example Tests`
   - **Script path:** `api/tests/examples`
   - **Output directory:** `results`
   - **Working directory:** repo root
4. Under **Environment variables**, add your values from `.env` (at minimum `ENV`, `DEV_URL`, `AUTH_TYPE`, `API_USERNAME`, `API_PASSWORD`)
5. Click **OK**

### Command line

```bash
# Run all tests
robot -d results api/tests/

# Run a specific suite
robot -d results api/tests/examples/BookingCRUDTest.robot

# Run by tag
robot -d results --include smoke api/tests/

# Run in parallel (4 workers)
pabot --processes 4 -d results api/tests/

# Retry failed tests and merge into a single report
robot -d results api/tests/
robot -d results/rerun --rerunfailed results/output.xml api/tests/
rebot --merge -d results results/output.xml results/rerun/output.xml
```

---

## CI/CD

The pipeline has two jobs:

| Job | Trigger | Command |
|---|---|---|
| **Smoke** | Every push to `main` | `robot --include smoke` |
| **Regression** | Daily at 9 AM UTC + manual | `pabot --processes 4 --include regression` |

Both jobs automatically retry failed tests once before marking them as failed. The retry results are merged into a single report using `rebot --merge`, so the final artifact always reflects the true outcome after retries.

### Setting up CI for your fork

Add the following to your repository's **Settings → Secrets and variables**:

**Secrets** (sensitive values):

| Secret | Required for |
|---|---|
| `API_USERNAME` | `AUTH_TYPE=basic` |
| `API_PASSWORD` | `AUTH_TYPE=basic` |
| `TOKEN_URL` | `AUTH_TYPE=oauth` |
| `CLIENT_ID` | `AUTH_TYPE=oauth` |
| `CLIENT_SECRET` | `AUTH_TYPE=oauth` |
| `API_KEY` | `AUTH_TYPE=api_key` |

**Variables** (non-sensitive values):

| Variable | Default |
|---|---|
| `ENV` | `dev` |
| `DEV_URL` | `https://restful-booker.herokuapp.com/` |
| `STAGING_URL` | — |
| `PROD_URL` | — |
| `AUTH_TYPE` | `basic` |
| `API_KEY_HEADER` | `x-api-key` |

---

## Contributing

Push to `main` is disabled. To contribute, create a branch and open a pull request.
