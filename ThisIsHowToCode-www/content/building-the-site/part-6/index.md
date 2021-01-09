---
title: "Building The Site (Part 6)"
tags:
- Work In Progress
---

### Notes

Amazon changes their web console all the time. Don't be surprised if things look different and you have to search for them a little. 

### The Plan

- Get the site served via CloudFront over HTTPS. 

### The Details

- Started off by showing where we left off with an S3 bucket being served out directly via it's "Static website hosting" option property. We turned that off since we only want traffic to be able to hit the bucket via CloudFront. 

- Once that was turned off, we jumped through the notes I put together to setup CloudFront. It almost worked. For some reason, the permission policy didn't get setup to let CloudFront to have access to the S3 bucket. 

- I found the details for how to setup the necessary policy on [this page](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#private-content-creating-oai). It looks like this:

        {
            "Version": "2012-10-17",
            "Id": "PolicyForCloudFrontPrivateContent",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EH1HDMB1FH2TC"
                    },
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::awsexamplebucket/*"
                }
            ]
        }

- Once that was in place, everything worked like a champ. 

This video is another example of how you have to dig into things sometimes. I must have skipped a step, or tweaked something that prevented the permission from being set. It's possible, it was related to something completely different. For example, there was still a policy set on the bucket to allow public access even though it was turned off in another location. 

Who knows? 

The key is that the only way through this stuff sometimes is to go down a rabbit hole. 

So, this one took a lot longer than expected, but if I hit the issue again, I'll know what to do (And you know too since you've seen it 👍)


### Prep Work

- [] show existing URL:

        http://thisishowyouprogram.com.s3-website-us-east-1.amazonaws.com
        
- [] Turn off public access for the S3 buckets (this is just because we turned it on in the last video, but we're going to use an S3 API instead because it follows the principal of Least Privilege  approach)

### Actual Work

NOTE: Make the cert before you do the CloudFront distritbution because you can't get to it otherwise without refreshing. 

NOTE: Could not update S3 permissions.  


- [] Create a new distribution in CloudFront - using Web distribution 

    - [] Set Origin Domain Name to the S3 bucket name. 
    - [] Check "Yes" for "Restrict Bucket Access"
    - [] Set "Origin Access Identity" to "Create A New Identity"
    - [] Add Comment under "Origin Access Identity" with:
            
            cloudfront-thisishowyouprogram

    - [] Set "Grant Read Permissions on Bucket" to "Yes, Update Bucket Policy"
    - [] Tick the box for "Redirect HTTP to HTTPS"
    - [] Under Distribution Settings -> Alternate Domain Names (CNAME), enter:

            thisishowyouprogram.com

    - [] Choose custom SSL cert (which is required if you're using a custom domain name)

    - [] Click Request or Import a Cert (see about walking through that) Make sure the CNAME matches. 

    - [] Set the default root document to:

            index.html

    - [] Click Create Distribution

    - After some time, the distribution should be up and I think it provides a DNS name that we can point to. 


### When things went wrong and it failed to update the S3 bucket Policy



Found the OAI user ID on:

    https://console.aws.amazon.com/cloudfront/home?region=us-east-1#oai:

TODO Check with AWS folks about 38 min in showing IDs for OAI


### Links

- TKTKTKT - Video on CDNs - CloudFront, Akamai, etc...
- [AWS Certificate Manager - Amazon Web Services (AWS)](https://aws.amazon.com/certificate-manager/)
- [AWS Certificate Manager features - Amazon Web Services (AWS)](https://aws.amazon.com/certificate-manager/features/)
- [aws s3 cloudfront allow - Google Search](https://www.google.com/search?client=safari&rls=en&q=aws+s3+cloudfront+allow&ie=UTF-8&oe=UTF-8)
- [cloudfront - Google Search](https://www.google.com/search?client=safari&rls=en&q=cloudfront&ie=UTF-8&oe=UTF-8)
- [Configuring a static website using a custom domain registered with Route 53 -...](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)
- [Content Delivery Network Tutorials | CDN, Setting up Amazon S3 Distribution|...](https://aws.amazon.com/cloudfront/getting-started/S3/)
- [Deploy static website to AWS with HTTPS - S3, Route 53, CloudFront,...](https://www.youtube.com/watch?v=lB4DTqMEumY)
- [Getting started with a simple CloudFront distribution - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.html)
- [gettings an amazon ssl cert - Google Search](https://www.google.com/search?client=safari&rls=en&q=gettings+an+amazon+ssl+cert&ie=UTF-8&oe=UTF-8)
- [Hosting a static website using Amazon S3 - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
- [How do I use Amazon CloudFront to serve a static website hosted on Amazon S3? - YouTube](https://www.youtube.com/watch?v=DiIaoIcoKNY)
- [Restricting Access to Amazon S3 Content by Using an Origin Access Identity -...](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
- [Restricting Access to Amazon S3 Content by Using an Origin Access Identity -...](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#private-content-creating-oai)
- [Serving compressed files - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html)
- [Setting up Amazon CloudFront - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/setting-up-cloudfront.html)
- [setup aws cloudfront - Google Search](https://www.google.com/search?client=safari&rls=en&q=setup+aws+cloudfront&ie=UTF-8&oe=UTF-8)
- [setup cloudfront - Google Search](https://www.google.com/search?client=safari&rls=en&q=setup+cloudfront&ie=UTF-8&oe=UTF-8)
- [Speeding up your website with Amazon CloudFront - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-cloudfront-walkthrough.html)
- [Use CloudFront to serve a static website hosted on Amazon S3](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/)
