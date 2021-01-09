---
title: Building The Site (Part 11) - Making A Basic Deployer
date: 1609702771
---

Overview
--------




Started to build the deployer in the last session but found an issue where links weren't working. Now that that's solved, it's back to the deployer. 



---



EDIT: Points about 10:40 and some beffore when it showed the Access Key. Check all termial hits. 

Make sure to edit out when you fire up keychain access. 





### Steps to do

- Build the site 
- Deploy the site 
- Invalidate the site 


aws cloudfront create-invalidation --distribution-id E16XG7IV228BY3 --paths "/*"

link to permiossions. 

talk about dots in command line movement 

link pwc 

link putting things on the command line in /usr/local/bin 

Show How PATH works on the command line


TODO: Figure out how to make the CLI account just have CloudFront access to invalidations. 




### Links 

- TKTKTK Video on how to make bash functions as well as scripts 
- [amazon web services - Access Denied when calling the CreateInvalidation...](https://stackoverflow.com/questions/33616678/access-denied-when-calling-the-createinvalidation-operation-on-aws-cli)
- [An error occurred (IncompleteSignature) when calling the CreateInvalidation...](https://www.google.com/search?client=safari&rls=en&q=An+error+occurred+(IncompleteSignature)+when+calling+the+CreateInvalidation+operation&ie=UTF-8&oe=UTF-8)
- [aws cli cloudfront - Google Search](https://www.google.com/search?client=safari&rls=en&q=aws+cli+cloudfront&ie=UTF-8&oe=UTF-8)
- [aws cli sync - Google Search](https://www.google.com/search?client=safari&rls=en&q=aws+cli+sync&ie=UTF-8&oe=UTF-8)
- [aws cloudfront (IncompleteSignature) - Google Search](https://www.google.com/search?client=safari&rls=en&q=aws+cloudfront+(IncompleteSignature)&ie=UTF-8&oe=UTF-8)
- [aws s3 cp without recursive can produce a useless error message · Issue #2929...](https://github.com/aws/aws-cli/issues/2929)
- [chmod - Google Search](https://www.google.com/search?client=safari&rls=en&q=chmod&ie=UTF-8&oe=UTF-8)
- [chmod - Wikipedia](https://en.wikipedia.org/wiki/Chmod)
- [CloudFront API Permissions: Actions, Resources, and Conditions Reference -...](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html#required-permissions-invalidations)
- [cloudfront invalidation aws permission - Google Search](https://www.google.com/search?client=safari&rls=en&q=cloudfront+invalidation+aws+permission&ie=UTF-8&oe=UTF-8)
- [create-invalidation — AWS CLI 1.18.207 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/cloudfront/create-invalidation.html)
- [IncompleteSignature error when calling Cloudfront from Github action · Issue...](https://github.com/aws/aws-sdk-js/issues/3313)
- [Parameter validation failed: s3 aws cp - Google Search](https://www.google.com/search?client=safari&rls=en&q=Parameter+validation+failed:+s3+aws+cp&ie=UTF-8&oe=UTF-8)
- [sync — AWS CLI 1.18.207 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
- [This Is How To Code](https://www.thisishowtocode.com/)
- [Using Identity-Based Policies (IAM Policies) for CloudFront - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/access-control-managing-permissions.html)





















