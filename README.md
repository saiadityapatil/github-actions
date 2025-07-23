🧮 Math API with AWS Lambda, API Gateway & GitHub Actions
=========================================================

This project is a simple **Python-based AWS Lambda function** deployed via **API Gateway**, fully automated using **GitHub Actions CI/CD** and **AWS SAM (Serverless Application Model)**.

🚀 Features
-----------
- Python Lambda function that supports:
  - `add(a, b)`
  - `subtract(a, b)`
  - `multiply(a, b)`
- Triggered via **HTTP POST** request
- Automated:
  - ✅ CI: Run unit tests on every push
  - ✅ CD: Deploy Lambda & API Gateway to AWS

🗂️ Project Structure
---------------------
```
github-actions/
├── app.py                     # Lambda logic
├── requirements.txt           # Dependencies (empty for now)
├── test_app.py                # Unit tests
├── template.yaml              # AWS SAM template (Lambda + API Gateway)
└── .github/
    └── workflows/
        ├── main.yml           # CI: Run tests on push
        └── deploy.yml         # CD: Deploy Lambda & API Gateway
```
💡 How It Works
----------------
### 🔁 CI Workflow: `python-app.yml`
- Automatically runs `pytest` on every push or pull request to `main`.
- Ensures your logic (`add`, `subtract`, etc.) works correctly before deployment.

### 🚀 CD Workflow: `deploy.yml`
- On push to `main`, builds and deploys your:
  - AWS Lambda function (`my-math-lambda`)
  - API Gateway endpoint (`/math`)
- Uses **AWS SAM** to manage and deploy infrastructure as code

🔧 Setup Instructions
----------------------
### ✅ 1. Prerequisites
- AWS account with a created **S3 bucket** (for deployment packages)
- IAM user with programmatic access and this minimum policy:

```
{
  "Effect": "Allow",
  "Action": [
    "lambda:*",
    "cloudformation:*",
    "apigateway:*",
    "s3:*",
    "iam:PassRole"
  ],
  "Resource": "*"
}
```

### 🔐 2. GitHub Secrets
Go to: GitHub Repo → Settings → Secrets and Variables → Actions

Add:
| Secret Name             | Description                       |
|-------------------------|-----------------------------------|
| `AWS_ACCESS_KEY_ID`     | IAM user's access key             |
| `AWS_SECRET_ACCESS_KEY` | IAM user's secret key             |

### 📝 3. Replace S3 Bucket in Workflow
In `.github/workflows/deploy.yml`, replace:
```
--s3-bucket your-s3-bucket-name
```
with your actual **S3 bucket name**.

🔁 Running CI Workflow (`python-app.yml`)
----------------------------------------
Every time you push or open a pull request, GitHub Actions will:
- Set up Python (3.8–3.10)
- Install dependencies
- Run `pytest` to ensure `app.py` is working

✅ Example Test (`test_app.py`)
```python
from app import add, subtract

def test_add():
    assert add(3, 4) == 7

def test_subtract():
    assert subtract(10, 5) == 5
```

🚀 Deploying Lambda + API Gateway (`deploy.yml`)
-------------------------------------------------
Pushing to `main` will:
- Build your Lambda using AWS SAM
- Upload code to S3
- Deploy the function and HTTP API Gateway via CloudFormation

📡 Using the API
-----------------
Once deployed, your endpoint will look like:
https://<api-id>.execute-api.<region>.amazonaws.com/Prod/math

🔁 Example Request
```
POST /Prod/math
Content-Type: application/json

{
  "operation": "add",
  "a": 10,
  "b": 5
}
```

✅ Response
```json
{
  "result": 15
}
```

📦 Local Testing with SAM
--------------------------
```bash
sam build
sam local invoke MathFunction --event event.json
```

event.json:
```
{
  "body": "{"operation": "subtract", "a": 8, "b": 3}"
}
```
