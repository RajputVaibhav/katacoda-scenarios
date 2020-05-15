Now we will create an access point. For this, run the following command

<br/>

`aws s3control create-access-point --name reader --account-id <ACCOUNT_ID_HERE> --bucket <BUCKET_NAME_HERE> --public-access-block-configuration BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=true,RestrictPublicBuckets=true`

---

<br/>

Now put a file in the bucket and try to get it using the following command

<br/>

`aws s3api get-object --key <OBJECT_NAME_HERE> --bucket arn:aws:s3:<REGION>:<ACCOUNT_NUM>:accesspoint/<ACCESS_POINT_NAME> <DOWNLOAD_OBJECT_NAME>`

<br/>

This should work just fine
