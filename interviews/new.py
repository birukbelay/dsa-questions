def count(emails, urls):
    """ Approach
    1. Find the domain names with from the urls without the www. prefix
    2. iterate over the emails for each url and check whether the email contains that domain name
    3. create a dictionary and collect the count of each emails repetition   

    """
    # d={}
    # # iterate over each url
    # for i in urls:
    #     # get the url with out the www. prefix
    #     val = i.removeprefix("www.")
    #     # iterate over the emails to check if they contain the domain
    #     for email in emails:
    #         # check if the email contains the string and and update the dictionary value
    #         if val in email:
    #             d[i] +=1
    # return d

    """ changed aproach 2
    1. iterate over the email addresses 
    2. get the domain name from each  email address so that we dont have to iterate over the urls

    """
    urlDomains= {}
    for i in urls:
        val = i.removeprefix("www.")
        urlDomains[val] = urlDomains.get(val, 0) +1

    d={}
    for email in emails:
        s = email.split("@")
        
        url = s[1]
        if url in urlDomains:
            domain = "www."+url
            d[domain] = d.get(domain, 0) +1            
    return d

emails=['foo@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com']
urls=['www.a.com', 'www.b.com', 'www.c.com']

print(count(emails, urls ))



