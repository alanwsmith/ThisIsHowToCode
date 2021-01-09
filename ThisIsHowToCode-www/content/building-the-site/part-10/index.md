---
title: Building The Site (Part 10) - Building A Deployer but then dealing with index files not showing up
date: 1609640253
---

Started off by building a deployer but then discovered our index.html files weren't showing up. Fix is a Lambda@Edge function that looks for calls that need to add the files and adds them. 

Was thinking about trying to remove the trailing slashes, but that's begging for problems. Also, realized that it would take hacking Hugo itself to deal with removing the slashes since it puts them in the URLs when it makes them. 


- [Adding Triggers for a Lambda@Edge Function - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-add-triggers.html)
- [AWS Hugo Hosting, HowTo · Joseph Lust](https://lustforge.com/2016/02/27/hosting-hugo-on-aws/)
- [aws sync s3 - Google Search](https://www.google.com/search?client=safari&rls=en&q=aws+sync+s3&ie=UTF-8&oe=UTF-8)
- [CloudFront Events That Can Trigger a Lambda Function - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-cloudfront-trigger-events.html)
- [cloudfront hugo - Google Search](https://www.google.com/search?client=safari&rls=en&q=cloudfront+hugo&ie=UTF-8&oe=UTF-8)
- [cloudfront not doing index.html - Google Search](https://www.google.com/search?client=safari&rls=en&q=cloudfront+not+doing+index.html&ie=UTF-8&oe=UTF-8)
- [Creating a Lambda@Edge Function in the Lambda Console - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-create-in-lambda-console.html)
- [Edge Computing| CDN, Global Serverless Code, Distribution | AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/)
- [Hosting The Hugo QuickStart Project on AWS Cloudfront with Lambda@Edge - DEV...](https://dev.to/starpebble/hosting-the-hugo-quickstart-project-on-aws-cloudfront-with-lambda-edge-5g5f)
- [HowTo: Deploying Hugo on S3 and Cloudfront - tips & tricks - HUGO](https://discourse.gohugo.io/t/howto-deploying-hugo-on-s3-and-cloudfront/2800)
- [https://www.thisishowtocode.com/think-of-variables-like-placeholders/](https://www.thisishowtocode.com/think-of-variables-like-placeholders/)
- [Implementing Default Directory Indexes in Amazon S3-backed Amazon CloudFront...](https://aws.amazon.com/blogs/compute/implementing-default-directory-indexes-in-amazon-s3-backed-amazon-cloudfront-origins-using-lambdaedge/)
- [lambda edge see response - Google Search](https://www.google.com/search?client=safari&rls=en&q=lambda+edge+see+response&ie=UTF-8&oe=UTF-8)
- [Lambda@Edge Example Functions - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-general-examples)
- [make lambda edge function - Google Search](https://www.google.com/search?client=safari&rls=en&q=make+lambda+edge+function&ie=UTF-8&oe=UTF-8)
- [Specifying a Default Root Object - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html)
- [Specifying a Default Root Object - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html#DefaultRootObjectHowToDefine)
- [Think Of Variables As Place Holders · This Is How To Code](https://www.thisishowtocode.com/think-of-variables-like-placeholders/index.html)
- [This Is How To Code](https://www.thisishowtocode.com/)
- [This Is How To Code](https://www.thisishowtocode.com/page/2/index.html)

