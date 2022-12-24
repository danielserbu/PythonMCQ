questions = [
    {
        "question": "Which of the following headers helps in preventing the Clickjacking attack?",
        "choices": ["Strict-Transport-Security", "Access-Control-Allow-Origin", "X-Frame-Options", "X-Content-Type-Options"],
        "correct": "3",
        "explanation": "https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html and https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options"
    },
    {
        "question": "Which of the following directives in a Content-Security-Policy HTTP response header, can be used to prevent a Clickjacking attack?",
        "choices": ["script-src", "object-src", "frame-ancestors", "base-uri"],
        "correct": "3",
        "explanation": "https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html and https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors"
    },
    {
        "question": "Based on the request below, which of the following statements is true?\nHTTP/1.1 200 OK\nAccept-Ranges: bytes\nAge: 359987\nCache-Control: max-age=604800\nContent-Type: text/html; charset=UTF-8\nDate: Fri, 02 Dec 2022 18:33:05 GMT\nExpires: Fri, 09 Dec 2022 18:33:05 GMT\nLast-Modified: Mon, 28 Nov 2022 14:33:18 GMT\nServer: Microsoft-IIS/6.0\nX-AspNet-Version: 2.0.50727\nVary: Accept-Encoding\nX-Powered-By: ASP.NET\nContent-Length: 1256",
        "choices": ["The application is using an outdated server technology.", "The application is disclosing the server version.", "The application is disclosing the version of framework used.", "All of the above"],
        "correct": "4",
        "explanation": "The application should not disclose any information regarding the server version."
    },
    {
        "question": "After purchasing an item on an ecommerce website, a user can view their order details by visiting the URL: https://example.com/?order_id=53870\n\nA security researcher pointed out that by manipulating the order_id value in the URL, a user can view arbitrary orders and sensitive information associated with that order_id.\nThere are two fixes:\n\n ####\nFix 1(Bob's Fix):\nIn order to fix this vulnerability, a developer called Bob devised a fix so that the URL does not disclose\n  the numeric value of the order_id but uses a SHA1 hash of the order_id value in the URL, such as:\nhttps://example.com/?order_id=1ff0f7e61f599536d1326418124a261bc98b8ea1\nNote: that the SHA1 value of 53870 is 1ff0f7e61f599536d1326418124a261bc98b8ea1\n ####\n Fix 2(John's Fix):\nAnother developer called John devised a different fix so that the URL does not disclose the numeric value of the order_id and uses a Base64 encoded value of the order_id in the URL, such as:\nhttps://example.com/?order_id=NTM4NzAK\nNote: that the Base64 encoded value of 53870 is NTM4NzAK\n####\nWhich of the following is correct?",
        "choices": ["Both the solutions are adequate to fix the problem.", "Both the solutions are inadequate and the vulnerability is still not fixed.", "Only John's solution fixes the problem.", "Only Bob's solution fixes the problem."],
        "correct": "2",
        "explanation": "The proposed fixes are incorrect because order_id's can still be simply guessed by an attacker. \nLet's say developer nr 3 comes with the idea of hashing with SHA512 instead of the weaker SHA1 (and the even weaker method, encoding with base64).\nAn attacker can still guess that the order_id is referring to numbers and he can use burp intruder(or anything else for that matter)\nto generate a list of numbers, apply payload processing to each payload and hash to SHA512 before trying the hack.\nThe correct fix to the problem is to create an authorization mechanism and disallow the current user from accessing other users orders.\nCheck this for more details: https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html"
    },
    {
        "question": "If an attacker manages to get an application to execute an SQL query created by the attacker, then such attacks are called as _________",
        "choices": ["SQL attacks","SQL injection attacks","SQL usage attack","SQL destroyer attack"],
        "correct": "2",
        "explanation": "If an attacker manages to get an application to execute an SQL query created by the attacker, then such attacks are called as SQL injection attacks."
    },
    {
        "question": "An attack on a website that stores and displays text to a user is known as ______ attack",
        "choices": ["SQL attack","XSS attack","XRP attack","None of the mentioned"],
        "correct": "2",
        "explanation": "An attack on a website that stores and displays text to a user is known as XSS attack. It is called as cross site scripting attack."
    },
    {
        "question": "State true or false: Password leakage is a major security problem",
        "choices": ["True","False"],
        "correct": "1",
        "explanation": "Password leakage is a major security problem because the leaked password grants access to malicious visitors."
    },
    {
        "question": "What are man in the middle attacks?",
        "choices": ["Users are forced to use a second server which causes the attack","Users are forced to divert to a fake site where the attack takes place","Users are fooled by similar GUI and data is extracted from them.","None of the mentioned"],
        "correct": "2",
        "explanation": "Man in the middle attacks are those attacks in which the users are forced to divert to a fake site where the attack takes place. The fake site is then used to obtain the data from the user."
    },
    {
        "question": "What is the sequence of a TCP connection?",
        "choices": ["SYN ACK FIN","SYN SYN-ACK ACK","SYN ACK","SYN SYN ACK"],
        "correct": "2",
        "explanation": "x"
    },
    {
        "question": "What port number does FTP & HTTPS respectively use?",
        "choices": ["21 & 443","25 & 440","23 & 80","80 & 21"],
        "correct": "1",
        "explanation": "x"
    },
    {
        "question": "_________ is an attack which forces an end user to execute unwanted actions on a web application in which he/she is currently authenticated.",
        "choices": ["Two-factor authentication","Cross-site request forgery","Cross-site scripting","Cross-site scoring scripting"],
        "correct": "2",
        "explanation": "Cross-site request forgery, also known as a one-click attack or session riding and abbreviated as CSRF or XSRF."
    },
    {
        "question": "Cross-site request forgery, also known as a one-click attack or session riding and abbreviated as CSRF or XSRF.",
        "choices": ["Broken Authentication and Server Memory Leak","Broken Authentication and Insecure Deserialization","Server Memory Leak and Insecure Deserialization","Broken Authentication, Server Memory Leak and Insecure Deserialization"],
        "correct": "2",
        "explanation": "x"
    },
    {
        "question": "According to the OWASP Top 10, which of the following is not a type of cross-site scripting?",
        "choices": ["Reflected XSS","Stored XSS","DOM XSSS","Virtual XSS"],
        "correct": "4",
        "explanation": "x"
    },
    {
        "question": "______ attack is a type of attack against an application that parses XML input.",
        "choices": ["Injection","HTML","XXE","XSS"],
        "correct": "3",
        "explanation": "x"
    },
    {
        "question": "If a website does not validate authorization of a user for direct references to restricted files, then to which threat such a website is vulnerable?",
        "choices": ["Insecure Direct Object References","Injection","Cross Site Scripting","XML External Entity"],
        "correct": "1",
        "explanation": "x"
    },
    {
        "question": "For every link or form which invoke state-changing functions with an unpredictable token for each user what attack can be prevented?",
        "choices": ["OS Commanding","Cross-site Scripting","Cross-site Request Forgery","Cross-site tracing"],
        "correct": "3",
        "explanation": "x"
    },
    {
        "question": "Which attack can execute scripts in the user's browser and is capable of hijacking user sessions, defacing websites or redirecting the user to malicious sites?",
        "choices": ["SQL Injection","Cross Site Scripting","Malware Uploading","Man in the Middle"],
        "correct": "2",
        "explanation": "x"
    },
    {
        "question": "How to prevent CSRF attacks?",
        "choices": ["Prepare statement","Sanitization","Tokens","Referer"],
        "correct": "3",
        "explanation": "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html"
    },
    {
        "question": "SameSite cookies were used to prevent .....",
        "choices": ["SQL Injection","Path Traversal","XSS","CSRF"],
        "correct": "4",
        "explanation": "https://owasp.org/www-community/SameSite and https://www.geeksforgeeks.org/what-is-samesite-cookies-and-csrf-protection/"
    },
    {
        "question": "",
        "choices": ["x","y","w","z"],
        "correct": "x",
        "explanation": "x"
    }
]