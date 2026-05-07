# SERVERLESS WORKSHOP

## Get Started

1. DynamoDB - Create Table

- Table Name: _Music_
- Partition Key: _Artist_
- Sort Key: _SongTitle_

2. Lambda - Create Write Function

- Use code: [dynamodb-write.py](./code/dynamodb-write.py)

3. Lambda - Create Read Function

- Use code: [dynamodb-read.py](./code/dynamodb-read.py)

4. API Gateway - Create API

- Add _/music_ Resource and _GET_ Method
- Setup proxy integration to Lambda

5. Amplify Hosting - Create App

- Open base-code in VS Code
- Test Locally
- Create CodeCommit Repo
- Push to repo
- Create Amplify App

6. API Gateway - Deploy REST API

- Use [CFT Base Code Template](./code/ticketSystem-base.yml)

7. Amplify Hosting - Update App

8. API Gateway - Deploy Full API with Authentication

- Use [CFT Final Template](./code/ticketSystem-rest-final.yml)

9. Amplify Hosting - Deploy Final App
