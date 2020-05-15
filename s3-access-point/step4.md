Now we try to put an object inside the bucket using the same access point

<br/>

`aws s3api put-object --bucket arn:aws:s3:<REGION>:<ACCOUNT_NUM>:accesspoint/<ACCESS_POINT_NAME> --key <OBJECT_NAME> --body <OBJECT_PATH_ON_LOCAL>`

<br/>

That also worked, but we want to create a read-only access point. So, we create a policy to deny Put-Object operation