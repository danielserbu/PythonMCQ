questions = [
    {
        "question": "Which of the following headers helps in preventing the Clickjacking attack?",
        "choices": ["Strict-Transport-Security", "Access-Control-Allow-Origin", "X-Frame-Options", "X-Content-Type-Options"],
        "correct": "3",
        "explanation": "test"
    },
    {
        "question": "Which of the following directives in a Content-Security-Policy HTTP response header, can be used to prevent a Clickjacking attack?",
        "choices": ["script-src", "object-src", "frame-ancestors", "base-uri"],
        "correct": "3",
        "explanation": "test"
    },
    {
        "question": "Based on the request below, which of the following statements is true?\nHTTP/1.1 200 OK\nAccept-Ranges: bytes\nAge: 359987\nCache-Control: max-age=604800\nContent-Type: text/html; charset=UTF-8\nDate: Fri, 02 Dec 2022 18:33:05 GMT\nExpires: Fri, 09 Dec 2022 18:33:05 GMT\nLast-Modified: Mon, 28 Nov 2022 14:33:18 GMT\nServer: Microsoft-IIS/6.0\nX-AspNet-Version: 2.0.50727\nVary: Accept-Encoding\nX-Powered-By: ASP.NET\nContent-Length: 1256",
        "choices": ["The application is using an outdated server technology.", "The application is disclosing the server version.", "The application is disclosing the version of framework used.", "All of the above"],
        "correct": "4",
        "explanation": "test"
    },
    {
        "question": "After purchasing an item on an ecommerce website, a user can view their order details by visiting the URL: https://example.com/?order_id=53870\n\nA security researcher pointed out that by manipulating the order_id value in the URL, a user can view arbitrary orders and sensitive information associated with that order_id.\nThere are two fixes:\n\n ####\nFix 1(Bob's Fix):\nIn order to fix this vulnerability, a developer called Bob devised a fix so that the URL does not disclose\n  the numeric value of the order_id but uses a SHA1 hash of the order_id value in the URL, such as:\nhttps://example.com/?order_id=1ff0f7e61f599536d1326418124a261bc98b8ea1\nNote: that the SHA1 value of 53870 is 1ff0f7e61f599536d1326418124a261bc98b8ea1\n ####\n Fix 2(John's Fix):\nAnother developer called John devised a different fix so that the URL does not disclose the numeric value of the order_id and uses a Base64 encoded value of the order_id in the URL, such as:\nhttps://example.com/?order_id=NTM4NzAK\nNote: that the Base64 encoded value of 53870 is NTM4NzAK\n####\nWhich of the following is correct?",
        "choices": ["Both the solutions are adequate to fix the problem.", "Both the solutions are inadequate and the vulnerability is still not fixed.", "Only John's solution fixes the problem.", "Only Bob's solution fixes the problem."],
        "correct": "2",
        "explanation": "test"
    }
]