*** Settings ***
Resource    ../../keywords/TemplateKeywords.robot

# HOW TO USE THIS TEMPLATE
# ─────────────────────────
# 1. Copy this file to api/tests/<your-feature>/YourTest.robot
# 2. Copy api/keywords/TemplateKeywords.robot to api/keywords/YourKeywords.robot
# 3. Update the Resource path above to point to your new keyword file
# 4. Add your endpoints to lib/config.py under ENDPOINTS
# 5. Add any request payload JSON files under api/data/
# 6. Replace the test cases below with your own
#
# Each test case calls one keyword from your keyword file.
# Keep test cases short — logic belongs in keywords, not test cases.
#
# TAG CONVENTION
# ──────────────
# smoke      — fast, critical happy path tests. Run on every push and before deploys.
# regression — full suite. Run on schedule or after releases.
# critical   — must never fail in prod. Subset of smoke for the most important flows.

*** Test Cases ***
# Replace test case names with something descriptive (what you're verifying, not how).

Create Resource
    [Tags]    smoke    regression
    # Calls the 'Create Resource' keyword and stores the created ID as a suite variable
    Create Resource

Get Resource
    [Tags]    smoke    regression
    # Uses the suite variable ${RESOURCE_ID} set by the create step
    Get Resource    ${RESOURCE_ID}

Update Resource
    [Tags]    regression
    Update Resource    ${RESOURCE_ID}

Partial Update Resource
    [Tags]    regression
    Partial Update Resource    ${RESOURCE_ID}    ${{{"field": "new_value"}}}

Delete Resource
    [Tags]    regression
    Delete Resource    ${RESOURCE_ID}
