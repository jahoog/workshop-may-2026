# SERVERLESS WORKSHOP

## Get Started

1. DynamoDB - Create Table

- Table Name: _Music_
- Partition Key: _Artist_
- Sort Key: _SongTitle_

Create some records and include these fields:

- _Album_
- _ReleaseYear_

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

```
npm install
npm run dev
```

- Create CodeCommit Repo called _web-app-test_
- Push to repo from VS Code, use following commands

```
git init
git remote add origin codecommit::us-east-1://web-app-test
git add .
git commit -m "Initial Commit"
git push --set-upstream origin master
```

- Create Amplify App

6. API Gateway - Deploy REST API

- Use [CFT Base Code Template](./code/ticketSystem-base.yml)

- Test with Postman

- Add new ticket (POST) to /dev/tickets

```
{
  "userId": "user-123",
  "issue": "Login page broken",
  "description": "Users cannot log in after the latest deployment",
  "severity": "High"
}
```

- Get tickets (GET) to /dev/tickets

7. Amplify Hosting - Update App

8. API Gateway - Deploy Full API with Authentication

- Use [CFT Final Template](./code/ticketSystem-rest-final.yml)

9. Amplify Hosting - Deploy Final App

10. AppSync - Create API from our Music Table

- include following fields:
  - Artist (PK)
  - SongTitle (PK)
  - Album
  - ReleaseYear

11. Test AppSync

12. Create a new app using Amplify to create the data model. Use _npx ampx sandbox_ See what it creates.
