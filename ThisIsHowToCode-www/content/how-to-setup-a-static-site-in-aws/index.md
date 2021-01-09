---
title: How-To Setup A Static Site In AWS Using Route 53, Certificate Manager, CloudFront, and S3 
tags:
- AWS  
- Work In Progress 
- How To 
date: 1609557054
---

### Steps

- Make sure you have setup your AWS Account
- Go got https://aws.amazon.com
- Click "Sign In To the Console" 
- Search for and click on Route 53 
- Scroll down to "Register domain" 
- Put in the domain name you





### Before We Begin 

- Th

- AWS Changes the design of their pages all the time. Don't be surprised if things look different. Look around a little and you'll find it. 

- TKTKTK Talk about and Add link talking about why to use Route 53 for AWS services.

- Note that I've alread got a couple domains setup under "Hosted Zones". It'll look a little different for you until you do as well. (TKTKTK put in screenshot showing what it looks like without hosted zones.)



### Overview 

This is how to buy and setup a domain to host a static web site on Amazon's AWS using the S3, CloudFront, Route 53, and Certificate Manager services. The setup includes routing all traffic from the four basic domains to a single address. For example, these three domains:

    - http://example.com/
    - https://example.com/
    - http://www.example.com/

would all redirect to:

    https://www.example.com/ 

You'll need and Amazon AWS account to get started. (TKTKTK Link to AWS Signup Session) 


### Purchase Your Website name (aka) Domain 



- https://console.aws.amazon.com/route53/v2/home#Dashboard




# Create The Main S3 Bucket

1. Make an `index.html` file on your computer. It can be as simple as:

        Hello, World!

2. Make an S3 bucket 








--------------------------------------------------------------------------------

Original Notes

--------------------------------------------------------------------------------



### Process


- Note at the start that you're doing everyting with defaults. Check out the other session for more in depth details about the different options.

- Start with S3 so the file is there. 
- Do Route 53 next since you'll need that for the cert. 
- Do Cert Manager next since you'll need that for CloudFront. 
- Back to Route 53 to setup the DNS to point the domain toward cloudfront 
- Finish with CloudFront 

- Note that creating the cert can take up to 30 minutes 
- Note that making the CloudFront distribution can take a while


- Setup S3
    - [] Create index.html file
    - [] Create S3 bucket 
    - [] Upload the index.html file to the S3 bucket 

- Setup CloudFront
    - [] URL: https://console.aws.amazon.com/cloudfront/home?region=us-east-1#
    - [] Click "Create Distribution" (show what it looks like before you have one)
    - [] On the "Select a delivery method for your content" page, click "Get Started" under "Web"
    - [] On the "Create Distribution" Page
        - Under "Origin Domain Name" there will be a list of S3 buckets in the dropdown. Pick the bucket you just created. It'll be named with your S3 bucket followed by `s3.amazonaws.TKTKTK` This is just a name to keep track of things it doesn't have any impact on your setup. 
    - [] Origin ID should populate automatically, but if it doesn't you can add `S3-BUCKETNAME`
    - TKTKTK Verify it's fine to skip "Restrict Bucket Access" as long as you haven't set the S3 bucket to public. 
    - TKTKTK show how to setup the Restrict Bucket Access in another video.
    - Switch Viewer Protocol Policy to "Redirect HTTP to HTTPS" 
    - [] Set "Compress Objects Automatically" to "Yes"
    - [] Add your domain name to "Alternate Domain Names (CNAMES)". Don't put the `
    - [] Make sure CloudFront can talk to S3 

    - when setting up the origin, use the domain name from S3, and not the autocomplete one. 
        
        S3 one will look like this:
        thisishowtocode.com.s3-website-us-east-1.amazonaws.com
        
        Compared to the autocomplete one you shouldn't use that looks like this:
        thisishowtocode.com.s3.amazonaws.com

    Note that on the non-www version, don't turn on the HTTP->HTTPS redirect. That just adds another step in the redirect chain. 


- Route 53

    - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html
    - Note on using `www` vs non-www. https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/
    - Another page on www vs. non - https://www.yes-www.org - https://www.yes-www.org/why-use-www/
    - setup the `www` records as well. 


- Certificate Manager 
    - Setup:

        - example.com, and
        - *.example.com 

    - Show how to do the DNS Validation. 
    - Note that you can just click the button to update Route 53. 

---

In S3 turn on Static Web Hosting, 
    flick the switch for Redirect with:

        www.thisishowtocode.com/
    
    (don't put `https://` at the start)
    
    Set it via the protocol

        https 




- CloudFront

---

Note that for CloudFront you have to put in a lambda edge function to deal with serving index.html files when only a directory (e.g. `/blog/` is called)








### Plan 

- Register in Route 53
- Setup Cert in Certificate Manager
- Setup S3 Bucket
- Setup CloudFront
- Tie it All Together
- Add https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html

### Misc

[Some of the notes](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) about setting up the system for `www.example.com` and the `example.com` version without the third level domain talk about setting up two S3 buckets. Confirm that that's not necessary. 





### Links

(Get links from the other build parts, but these are some of them)


- [(Optional) Configuring a webpage redirect - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html#redirect-endpoint-host)
- [amazon cloudfront redirect www traffic to non-www - Google Search](https://www.google.com/search?client=safari&rls=en&q=amazon+cloudfront+redirect+www+traffic+to+non-www&ie=UTF-8&oe=UTF-8)
- [Amazon S3 Redirect and Cloudfront - Stack Overflow](https://stackoverflow.com/questions/22740084/amazon-s3-redirect-and-cloudfront)
- [Choosing between www and non-www URLs - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Choosing_between_www_and_non-www_URLs)
- [cloudfront redirect - Google Search](https://www.google.com/search?client=safari&rls=en&q=cloudfront+redirect&ie=UTF-8&oe=UTF-8)
- [cloudfront redirect s3 www - Google Search](https://www.google.com/search?client=safari&rls=en&q=cloudfront+redirect+s3+www&ie=UTF-8&oe=UTF-8)
- [Cloudfront redirect www to naked domain with ssl - Stack Overflow](https://stackoverflow.com/questions/28675620/cloudfront-redirect-www-to-naked-domain-with-ssl/42869783#42869783)
- [cloudfront s3 policy - Google Search](https://www.google.com/search?client=safari&rls=en&q=cloudfront+s3+policy&ie=UTF-8&oe=UTF-8)
- [Configuring a static website using a custom domain registered with Route 53 -...](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)
- [Failed to open page](https://thisishowtocode.com/)
- [Getting started with Amazon Route 53 - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html)
- [How internet traffic is routed to your website or web application - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html)
- [How to forward non WWW to WWW with AWS Amazon Cloud front behind HTTPS cloud...](https://stackoverflow.com/questions/36265027/how-to-forward-non-www-to-www-with-aws-amazon-cloud-front-behind-https-cloud-fro)
- [https://d15pzq9ux7jg75.cloudfront.net](https://d15pzq9ux7jg75.cloudfront.net/)
- [https://d1gvnj3dmmvze0.cloudfront.net](https://d1gvnj3dmmvze0.cloudfront.net/)
- [Redirecting a domain with HTTPS using Amazon S3 and CloudFront — Simone Carletti](https://simonecarletti.com/blog/2016/08/redirect-domain-https-amazon-cloudfront/)
- [Redirecting non-www to www website in AWS CloudFront | by Chris Pointon | Medium](https://medium.com/@chrispointon/redirecting-non-www-to-www-website-in-aws-cloudfront-658d97764b42)
- [Redirects in AWS CloudFront](https://www.goguardian.com/blog/engineering/redirects-in-aws-cloudfront/)
- [Requiring HTTPS for Communication Between Viewers and CloudFront - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html)
- [Restricting Access to Amazon S3 Content by Using an Origin Access Identity -...](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
- [Restricting Access to Amazon S3 Content by Using an Origin Access Identity -...](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#private-content-granting-permissions-to-oai)
- [Routing traffic to a website that is hosted in an Amazon S3 bucket - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html)
- [Serving private content with signed URLs and signed cookies - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
- [To WWW or not WWW | Netlify](https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/)
- [Use Your CloudFront Distribution to Restrict Access to an Amazon S3 Bucket](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amazon-s3/)
- [using www vs non-www - Google Search](https://www.google.com/search?client=safari&rls=en&q=using+www+vs+non-www&ie=UTF-8&oe=UTF-8)
- [What Is AWS Certificate Manager? - AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)
- [Why use www? | www. is not deprecated](https://www.yes-www.org/why-use-www/)


