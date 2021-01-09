---
title: Setting Up Multi-Factor Authentication (MFA) On AWS Accounts
---

### In This Episode

Started out by talking a little about what Multi-Factor Authentication (MFA) is and why you'd want to use it. 

Added MFA to the web console user which was no problem. 

Adding it to the CLI user turned into more of a trick. I thought all you had to do was assign MFA to a [programatic access user](/tktktk/) and it would be enforced, but that's not the case. The Access Key and Secret Key still work just fine. 

Getting MFA to be enforced for programmatic access requires putting in a policy. The way we did it was:

{{< highlight bash >}}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BlockAccessUnlessSignedInWithMFA",
            "Effect": "Deny",
            "NotAction": [
                "iam:ResyncMFADevice"
            ],
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": "false"
                }
            }
        }
    ]
}
{{< /highlight >}}

Once that was in place, MFA locked down as expected. 

### Links

- [Apps you can use for MFA on AWS](https://aws.amazon.com/iam/features/mfa/)
- TKTKTK: Video on how to setup Encrypted AWS credentials
- TKTKTK: Install AWS Command Line
- [Authenticate access using MFA through the AWS CLI](https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/)
- [aws cli mfa - Google Search](https://www.google.com/search?client=safari&rls=en&q=aws+cli+mfa&ie=UTF-8&oe=UTF-8)
- [aws setup cli - Google Search](https://www.google.com/search?client=safari&rls=en&q=aws+setup+cli&ie=UTF-8&oe=UTF-8)
- [Enabling a virtual multi-factor authentication (MFA) device (console) - AWS...](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)
- [Enabling and managing virtual MFA devices (AWS CLI or AWS API) - AWS Identity...](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_cliapi.html)
- [Enabling MFA devices for users in AWS - AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable.html)
- [Enforce MFA authentication for IAM users that use the AWS CLI](https://aws.amazon.com/premiumsupport/knowledge-center/mfa-iam-user-aws-cli/)
- [Grammar of the IAM JSON policy language - AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html)
- [how long does it take to enable mfa aws - Google Search](https://www.google.com/search?newwindow=1&client=safari&rls=en&ei=WrPnX7qxFLHz5gK5-4OwBA&q=how+long+does+it+take+to+enable+mfa+aws+)
- [Managing access keys for IAM users - AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html?icmpid=docs_iam_console)
- [qr code - Google Search](https://www.google.com/search?q=qr+code)
- [Step 3.1: Set Up the AWS Command Line Interface (AWS CLI) - Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/setup-aws-cli.html)
- [Using multi-factor authentication (MFA) in AWS - AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [Visual Studio Code User and Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings)
- [vs code config file - Google Search](https://www.google.com/search?client=safari&rls=en&q=vs+code+config+file&ie=UTF-8&oe=UTF-8)

