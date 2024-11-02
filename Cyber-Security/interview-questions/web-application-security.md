Q1: What is SQL injection?

- SQL injection is a type of cyber attack in which an attacker injects malicious code into a web application's database through a vulnerable input field, such as a form or URL parameter. This allows the attacker to gain unauthorized access to sensitive data, modify or delete records, or execute other malicious actions on the database. For example, an attacker might use SQL injection to gain access to a database of user login credentials, or to alter the prices of products in an online store.

Q2: What is the difference between Authentication vs Authorization?

- Authentication is the process of verifying the identity of a user, device, or system. This usually involves providing some form of credentials, such as a username and password, and demonstrating that the credentials are correct.

Authorization, on the other hand, is the process of granting or denying access to certain resources or actions based on a user's identity and privileges. For example, after a user has been authenticated, the system might check to see if the user is authorized to perform certain actions, such as updating a database record or accessing a restricted file.

Q3: What is Security Testing?

- Security testing is the process of evaluating the security of a computer system, network, or application by simulating various types of cyber attacks and assessing the system's ability to withstand them. Security testing can help identify vulnerabilities and weaknesses in a system's security controls, and can be used to verify that the system is compliant with relevant security standards and regulations.

Q4: What is a DDOS attack?

- A distributed denial-of-service (DDoS) attack is a type of cyber attack in which an attacker attempts to make a website or other online service unavailable by overwhelming it with traffic from multiple sources. This is typically achieved by using a botnet (a network of compromised computers) to send a large number of requests to the target server, overwhelming its resources and rendering it unable to handle legitimate traffic. DDoS attacks can be very disruptive and can cause significant downtime for affected websites or services.

Q5: List the various methodologies in Security testing?

- Some common methodologies used in security testing include:

  Penetration testing: Simulating an attack on a system to identify vulnerabilities and assess the system's defenses.

  Vulnerability scanning: Automated scanning of a system to identify potential vulnerabilities.

  Risk assessment: Identifying and assessing potential risks to a system, and determining appropriate countermeasures.

  Compliance testing: Verifying that a system is compliant with relevant security standards and regulations.

  Ethical hacking: Simulating a cyber attack in a controlled environment to test a system's defenses.

  Security audit: A thorough review of a system's security controls and practices.

Q6: What is “Vulnerability”?

- A vulnerability is a weakness or flaw in a computer system, network, or application that can be exploited by an attacker to gain unauthorized access or perform other malicious actions. Vulnerabilities can exist in software, hardware, or other components of a system, and can be exploited through various means, such as exploiting a software bug or misconfiguration, or using a known password.

Q7: What is a botnet?

- A botnet is a network of compromised computers that have been hijacked by an attacker and are being controlled remotely. Botnets are often used to launch distributed denial-of-service (DDoS) attacks or to send spam or phishing emails. The individual computers in a botnet are called "bots" and are often owned by unsuspecting users who are unaware that their computers have been compromised. For example, an attacker might use a botnet to send a large number of requests to a website, overwhelming its servers and causing it to crash.

Q8: What is Cross-Site Scripting (XSS)?

- Cross-Site Scripting (XSS) is a type of web vulnerability that allows an attacker to inject malicious code into a website or web application. This code is typically executed in the browser of a user who visits the compromised website, and can be used to steal sensitive information, such as login credentials or financial data. XSS attacks are often launched through vulnerabilities in web forms, search boxes, or other user-input fields that do not properly validate or sanitize user-supplied data.

Q9: What is impersonation?

- Impersonation is the act of pretending to be someone else in order to gain access to sensitive information or resources. In a cybersecurity context, impersonation might involve using someone else's login credentials or creating a fake account in their name. Impersonation attacks can be launched through various means, such as phishing emails, social engineering, or malware.

Q10: What is Intrusion Detection System (IDS)?

- An Intrusion Detection System (IDS) is a security tool that monitors a network or system for suspicious activity and alerts administrators when potential threats are detected. IDS systems can be configured to look for specific types of threats, such as attempted network breaches or unauthorized access to sensitive data. They can also be configured to take automated actions, such as blocking a suspect IP address or triggering an alert to security personnel.

Q11: What is CORS and how to enable one?

- CORS (Cross-Origin Resource Sharing) is a security mechanism that allows web browsers to make requests to a server on a different domain than the one the browser is currently on. CORS is used to prevent malicious websites from making requests to your server without your knowledge. To enable CORS on your server, you will need to configure your server to allow requests from specific domains. This can typically be done using server-side programming languages such as PHP, Python, or Node.js.

Q12: Explain what threat arises from not flagging HTTP cookies with tokens as secure?

- HTTP cookies are small pieces of data that are stored in a user's browser and sent back to the server with every request. They are often used to store session information or other data that is needed to maintain the state of a web application. If an HTTP cookie is not flagged as secure, it can be transmitted over an unencrypted connection, which makes it vulnerable to interception by an attacker. This can potentially allow the attacker to steal sensitive information, such as login credentials or financial data, or to impersonate a legitimate user. To protect against this threat, it is important to flag HTTP cookies with tokens as secure, which will ensure that they are only transmitted over encrypted connections.

Q13: How to mitigate the SQL Injection risks?

- SQL injection risks can be mitigated in a number of ways, including:

  Using parameterized queries: Rather than constructing dynamic SQL queries using user-supplied input, use parameterized queries that separate the input from the query logic. This helps to prevent attackers from injecting malicious code into the query.

  Validating user input: Validate user input to ensure that it is of the expected type and format, and reject input that is invalid or malformed.

  Escaping special characters: Use appropriate character escaping techniques to prevent attackers from injecting malicious code into user input.

  Implementing input filters: Use input filters to block or sanitize input that contains potentially malicious code.

  Ensuring database access controls: Use database access controls to limit the types of actions that users can perform on the database, and to restrict access to sensitive data.

Q14: What is Cross Site Scripting (XSS)?

- Cross Site Scripting (XSS) is a type of web vulnerability that allows an attacker to inject malicious code into a website or web application. This code is typically executed in the browser of a user who visits the compromised website, and can be used to steal sensitive information, such as login credentials or financial data. XSS attacks are often launched through vulnerabilities in web forms, search boxes, or other user-input fields that do not properly validate or sanitize user-supplied data.

Q15: What is DOM-based XSS?

- DOM-based XSS (Cross-Site Scripting) is a variant of XSS that occurs when a web application's client-side code (JavaScript, for example) processes user input in an insecure manner, allowing an attacker to inject malicious code into the web page. Unlike traditional XSS attacks, which inject malicious code into the server-side code of a web application, DOM-based XSS attacks target the client-side code of the application, which is executed in the user's browser.

Q16: How can we Protect Web Applications From Forced Browsing?

- There are several ways to protect web applications from forced browsing attacks:

  Implementing access controls: Use access controls to restrict access to sensitive resources and pages to authorized users only.

  Validating user input: Validate user input to ensure that it is of the expected type and format, and reject input that is invalid or malformed.

  Filtering user input: Use input filters to block or sanitize input that contains potentially malicious code.

  Implementing security measures: Use security measures such as firewalls, intrusion detection systems, and web application firewalls to protect against unauthorized access to web applications.

  Enforcing strong passwords: Encourage users to choose strong, unique passwords and to change them regularly.

Q17: Mention what flaw arises from session tokens having poor randomness across a range of values?

- If session tokens have poor randomness across a range of values, they may be more susceptible to being guessed or predicted by an attacker. This can lead to a vulnerability known as session prediction, in which an attacker can guess or predict a valid session token and use it to gain unauthorized access to a web application or other protected resource. To prevent this flaw, it is important to ensure that session tokens are generated using strong randomness algorithms, and that they are sufficiently long and complex to make them difficult to guess or predict.

Q18: What is Session Hijacking?

- Session hijacking is a type of cyber attack in which an attacker takes over an existing session between a user and a website or application. The attacker can then use the hijacked session to gain unauthorized access to the website or application, or to perform actions on behalf of the legitimate user.

  For example, consider a user who is logged into a web-based email account. If an attacker is able to hijack the user's session, they could potentially read, delete, or send email messages as if they were the legitimate user.

  Session hijacking can occur through various means, such as stealing a user's session cookie (a small piece of data that identifies the user's session), intercepting unencrypted session data, or using social engineering techniques to trick the user into revealing their session information.

Q19: What is Content Security Policy?

- Content Security Policy (CSP) is a security feature that allows web developers to specify which sources of content are allowed to be loaded on a webpage. CSP is designed to help prevent various types of attacks, such as cross-site scripting (XSS) and malicious code injection, by limiting the types of content that can be loaded on a webpage.

  For example, consider a website that allows users to post comments on articles. Without a CSP, an attacker could potentially inject malicious code into a comment, which could then be executed in the browser of any user who views the comment. By implementing a CSP, the website can specify that only content from specific, trusted sources is allowed to be loaded, helping to prevent the execution of malicious code.

Q20: How can I prevent XSS?

- There are several steps that can be taken to prevent cross-site scripting (XSS) attacks:

  - Input validation: Validate user input to ensure that it is of the expected type and format, and reject input that is invalid or malformed.

  - Output encoding: Encode user input when displaying it on a webpage to prevent it from being interpreted as HTML or JavaScript.

  - Content Security Policy (CSP): Use a CSP to specify which sources of content are allowed to be loaded on a webpage, helping to prevent the execution of malicious code.

  - Sanitizing user input: Use input filters to block or sanitize input that contains potentially malicious code.

Q27: What is the difference between encryption, encoding, and hashing?Related To: Cryptography

- Encryption, encoding, and hashing are all techniques used to protect data and prevent unauthorized access. However, they are used for different purposes and have different characteristics.

  Encryption
  Encryption is the process of converting plaintext data into an encoded form that can only be decrypted (unlocked) with a secret key. Encryption is used to protect sensitive data, such as financial transactions or confidential communications, from being read by unauthorized parties.

  For example, consider a person sending an email message containing sensitive information. To protect the message from being intercepted and read by an attacker, the sender can encrypt the message using a secret key. The recipient can then use the same key to decrypt the message and read its contents.

  Encoding
  Encoding is the process of converting data from one format into another, typically to make it easier to transmit or store. Encoding does not involve the use of secret keys or other security measures, and the encoded data can usually be easily decoded by anyone who has access to the appropriate decoding tools.

  For example, consider a website that displays text in a non-Latin alphabet, such as Chinese or Arabic. To display the text correctly in a web browser, the website must encode the text using a specific character encoding standard, such as UTF-8 or ISO-8859-1. The web browser can then decode the encoded text and display it correctly to the user.

  Hashing
  Hashing is the process of generating a fixed-size output (a hash) from a variable-size input (a message). Hashes are often used to verify the integrity of data, such as to ensure that a file has not been tampered with or corrupted.

  For example, consider a software developer who wants to distribute a new version of their software to users. To ensure that the software has not been tampered with during distribution, the developer can generate a hash of the software file and include it with the distribution. The user can then generate their own hash of the downloaded file and compare it to the original hash to verify that the file is genuine and has not been altered.

  In summary:

  Encryption is used to protect data by encoding it in a way that can only be unlocked with a secret key.
  Encoding is used to convert data from one format to another, typically for the purpose of making it easier to transmit or store.
  Hashing is used to generate a fixed-size output (a hash) from a variable-size input, typically for the purpose of verifying the integrity of data.
