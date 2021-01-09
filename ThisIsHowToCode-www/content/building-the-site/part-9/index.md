---
title: Building The Site (Part 9) - Configuring the Domains With Redirects
date: 1609530317
---

The Plan
--------

- Setup both domains:

    - thisishowtocode.com, and
    - www.thisishowtocode.com 

- Make sure they both have SSL/TLS certs 

- Redirect traffic from the non-www to the www version. 


### Process

- Create S3 bucket



### Links

- SSL/TLS Certs - 

- TKTKTKT CNAME - DNS Types. 





---

- [x] http://ThisIsHowToCode.com
- [x] https://ThisIsHowToCode.com
- [x] http://www.ThisIsHowToCode.com

-> https://www.ThisIsHowToCode.com


---

TODO: confirm we don't need static hosting on the www.example.com bucket. 





### Links

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
