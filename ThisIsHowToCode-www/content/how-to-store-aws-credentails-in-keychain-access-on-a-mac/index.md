---
title: "How-To: Store AWS CLI Credentials In Keychain Access On A Mac"
date: 1609632301
draft: true
---

Overview


### Command To Add Credentials To Keychain Access  


    security add-generic-password -U -a MAC_USER_NAME -s IAM_USER_NAME -w '{ "Version": 1, "AccessKeyId": "AWS_ACCESS_KEY", "SecretAccessKey": "AWS_SECRET_KEY" }'



### Command To Use Credentials

Setup your `~/.aws/credentials` file with:

    [default]
    credential_process = security find-generic-password -w -a MAC_USER_NAME -s IAM_USER_NAME




Note that in the video you added a space in front of the ACCESS_KEY. it worked for S3, but threw an error with:

    An error occurred (IncompleteSignature) when calling the CreateInvalidation operation

Removing the space fixed it. 


































Overview
--------

This is how you can move your AWS CLI credentials into macOS's Keychain Access application for storage. While not significantly more secure than storing them in the normal `~/.aws/credentials` file it prevents the possibility of accidentally showing them on screen if you open the file. 

Plus, I just don't like any of my credentials being stored un-encrypted. 






















































### Put The Credentials In Keychain Access 

security add-generic-password -U -a MAC_USER_NAME -s IAM_USER_NAME -w '{ "Version": 1, "AccessKeyId": "AWS_ACCESS_KEY", "SecretAccessKey": "AWS_SECRET_KEY" }'













### Setup ~/.aws/credentails 


credential_process = security find-generic-password -w -a alans -s A_Test_User_CLI







































### Links 

- TKTKTK: How-To: Store AWS CLI Credentials In Windows 
- [AWS CLI - Sourcing credentials with an external process](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html)
- [Setting Up Credentails](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)









