---
title: Building The Site (Part 7) - Changing Nameserver from Hover to Route 53
tags:
- Work In Progress
---

### Overview

I registered the ThisIsHowYouProgram.com domain on Hover. I already had an account there and when I woke up at 3 in the morning with the idea for the site that's where I went. 

But, I want to use Amazon's Route 53 service to manage the domain so that everything is in the AWS ecosystem. Route 53 is designed to work with CloudFront in a way that other systems can't (via an [ALIAS record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html))

I've got two options to get the site managed by Route 53. 

1. Transfer the domain from Hover to Route 53
2. Just change the Name Servers to point to Route 53. 

For now, I'm doing the latter since transferring is a little more of a hassle. (You have to turn off some protection services and do some authorization. This is good stuff, otherwise it would be easy to steal domains. I'll do it eventually, but going the Name Server route lets me get moving faster)


NOTE: Did changes at 4:20. 

TODO: Figure out how to redirect www traffic to the non-www. 

Note that when you updated the Name Server on Hover, you had to remove the `.` at the end of the of the domain name. (AWS had it in their system)


### Links

- TKTKTK - www vs non-www reasoning. 
- TKTKTK - Caching DNS 
- TKTKTK - Video about A Records and DNS and Cloudfront 
- TKTKTK - Video on Route 53 ALIAS records - 
- https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html
- https://help.hover.com/hc/en-us/articles/217282477--Changing-your-domain-nameservers

- [a dns record - Google Search](https://www.google.com/search?client=safari&rls=en&q=a+dns+record&ie=UTF-8&oe=UTF-8)
- [amazon web services - Root domain behind AWS CloudFront - Stack Overflow](https://stackoverflow.com/questions/50305126/root-domain-behind-aws-cloudfront)
- [Changing your domain nameservers – Hover Help Center](https://help.hover.com/hc/en-us/articles/217282477--Changing-your-domain-nameservers)
- [Choosing between alias and non-alias records - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)
- [Configuring Amazon Route 53 as your DNS service - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)
- [Configuring DNSSEC signing in Amazon Route 53 - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html)
- [hover change nameserver - Google Search](https://www.google.com/search?client=safari&rls=en&q=hover+change+nameserver&ie=UTF-8&oe=UTF-8)
- [Making Route 53 the DNS service for a domain that's in use - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html#migrate-dns-change-name-servers-with-provider)
- [Making Route 53 the DNS service for a domain that's in use - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html#migrate-dns-create-hosted-zone)
- [Making Route 53 the DNS service for a domain that's in use - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html#migrate-dns-create-records)
- [Routing traffic for subdomains - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-routing-traffic-for-subdomains.html)
- [Routing traffic to an Amazon CloudFront web distribution by using your domain...](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html)
- [ThisIsHowYouProgram.com](https://d8tyl6rs7fmpy.cloudfront.net/)
- [use cloudfront for root domain - Google Search](https://www.google.com/search?client=safari&rls=en&q=use+cloudfront+for+root+domain&ie=UTF-8&oe=UTF-8)
- [wildcard dns - Google Search](https://www.google.com/search?client=safari&rls=en&q=wildcard+dns&ie=UTF-8&oe=UTF-8)
- [Wildcard DNS record - Wikipedia](https://en.wikipedia.org/wiki/Wildcard_DNS_record)


