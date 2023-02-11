### Algorithms

An algorithm is basically a procedure or a formula for solving a data snooping problem. An encryption algorithm is a set of mathematical procedure for performing encryption on data. Through the use of such an algorithm, information is made in the cipher text and requires the use of a key to transforming the data into its original form. This brings us to the concept of cryptography that has long been used in information security in communication systems.

### Cryptography

Cryptography is a method of using advanced mathematical principles in storing and transmitting data in a particular form so that only those whom it is intended can read and process it. Encryption is a key concept in cryptography - It is a process whereby a message is encoded in a format that cannot be read or understood by an eavesdropper. The technique is old and was first used by Caesar to encrypt his messages using Caesar cipher. A plain text from a user can be encrypted to a ciphertext, then send through a communication channel and no eavesdropper can interfere with the plain text. When it reaches the receiver end, the ciphertext is decrypted to the original plain text.

### Cryptography Terms

**Encryption**: It is the process of locking up information using cryptography. Information that has been locked this way is encrypted.

**Decryption**: The process of unlocking the encrypted information using cryptographic techniques.

**Key**: A secret like a password used to encrypt and decrypt information. There are a few different types of keys used in cryptography.

**Steganography**: It is actually the science of hiding information from people who would snoop on you. The difference between steganography and encryption is that the would-be snoopers may not be able to tell there's any hidden information in the first place.

What is Symmetric Encryption?

#### Symmetric Encryption

![](https://www.ssl2buy.com/wiki/wp-content/uploads/2015/12/Symmetric-Encryption.png)

This is the simplest kind of encryption that involves only one secret key to cipher and decipher information. Symmetric encryption is an old and best-known technique. It uses a secret key that can either be a number, a word or a string of random letters. It is a blended with the plain text of a message to change the content in a particular way. The sender and the recipient should know the secret key that is used to encrypt and decrypt all the messages. Blowfish, AES, RC4, DES, RC5, and RC6 are examples of symmetric encryption. The most widely used symmetric algorithm is AES-128, AES-192, and AES-256.

The main disadvantage of the symmetric key encryption is that all parties involved have to exchange the key used to encrypt the data before they can decrypt it.

**Algorithm of Symmetric Encryption**

- [3DES](https://en.wikipedia.org/wiki/Triple_DES) - Symmetric-key block cipher (or Triple Data Encryption Algorithm (TDEA or Triple DEA), which applies the Data Encryption Standard (DES) cipher algorithm three times to each data block.
- [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) - Symmetric-key block cipher algorithm and U.S. government standard for secure and classified data encryption and decryption (also known as Rijndael).
- [Blowfish](<https://en.wikipedia.org/wiki/Blowfish_(cipher)>) - Symmetric-key block cipher, designed in 1993 by Bruce Schneier. Notable features of the design include key-dependent S-boxes and a highly complex key schedule.

What is Asymmetric Encryption?

#### Asymmetric Encryption

![](https://www.ssl2buy.com/wiki/wp-content/uploads/2015/12/Asymmetric-Encryption.png)

Asymmetric encryption is also known as public key cryptography, which is a relatively new method, compared to symmetric encryption. Asymmetric encryption uses two keys to encrypt a plain text. Secret keys are exchanged over the Internet or a large network. It ensures that malicious persons do not misuse the keys. It is important to note that anyone with a secret key can decrypt the message and this is why asymmetric encryption uses two related keys to boosting security. A public key is made freely available to anyone who might want to send you a message. The second private key is kept a secret so that you can only know.

A message that is encrypted using a public key can only be decrypted using a private key, while also, a message encrypted using a private key can be decrypted using a public key. Security of the public key is not required because it is publicly available and can be passed over the internet. Asymmetric key has a far better power in ensuring the security of information transmitted during communication.

Asymmetric encryption is mostly used in day-to-day communication channels, especially over the Internet. Popular asymmetric key encryption algorithm includes EIGamal, RSA, DSA, Elliptic curve techniques, PKCS.

**Algorithm of ASymmetric Encryption**

- [DH](https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange) - A method of exchanging cryptographic keys securely over a public channel. Unlike RSA, the Diffie-Hellman Key Exchange is not encryption, and is only a way for two parties to agree on a shared secret value. Since the keys generated are completely pseudo-random, DH key exchanges can provide forward secrecy (<https://en.wikipedia.org/wiki/Forward_secrecy>).
- [ECC](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) - Public-key cryptosystems based on the algebraic structure of elliptic curves over finite fields.
- [RSA](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>) - One of the first practical public-key cryptosystems and is widely used for secure data transmission. In RSA, this asymmetry is based on the practical difficulty of factoring the product of two large prime numbers, the factoring problem.

##### Asymmetric Encryption in Digital Certificates

To use asymmetric encryption, there must be a way of discovering public keys. One typical technique is using digital certificates in a client-server model of communication. A certificate is a package of information that identifies a user and a server. It contains information such as an organization's name, the organization that issued the certificate, the users' email address and country, and users public key.

When a server and a client require a secure encrypted communication, they send a query over the network to the other party, which sends back a copy of the certificate. The other party's public key can be extracted from the certificate. A certificate can also be used to uniquely identify the holder.

SSL/TLS uses both asymmetric and symmetric encryption, quickly look at digitally signed SSL certificates issued by trusted certificate authorities (CAs).

#### Difference Between Symmetric and Asymmetric Encryption

- Symmetric encryption uses a single key that needs to be shared among the people who need to receive the message while asymmetric encryption uses a pair of public key and a private key to encrypt and decrypt messages when communicating.
- Symmetric encryption is an old technique while asymmetric encryption is relatively new.
- Asymmetric encryption was introduced to complement the inherent problem of the need to share the key in symmetric encryption model, eliminating the need to share the key by using a pair of public-private keys.
- Asymmetric encryption takes relatively more time than the symmetric encryption.

| **Key Differences**      | **Symmetric Encryption**                                                   | **Asymmetric Encryption**                                                                    |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Size of cipher text**  | Smaller cipher text compares to original plain text file.                  | Larger cipher text compares to original plain text file.                                     |
| **Data size**            | Used to transmit big data.                                                 | Used to transmit small data.                                                                 |
| **Resource Utilization** | Symmetric key encryption works on low usage of resources.                  | Asymmetric encryption requires high consumption of resources.                                |
| **Key Lengths**          | 128 or 256-bit key size.                                                   | RSA 2048-bit or higher key size.                                                             |
| **Security**             | Less secured due to use a single key for encryption.                       | Much safer as two keys are involved in encryption and decryption.                            |
| **Number of keys**       | Symmetric Encryption uses a single key for encryption and decryption.      | Asymmetric Encryption uses two keys for encryption and decryption                            |
| **Techniques**           | It is an old technique.                                                    | It is a modern encryption technique.                                                         |
| **Confidentiality**      | A single key for encryption and decryption has chances of key compromised. | Two keys separately made for encryption and decryption that removes the need to share a key. |
| **Speed**                | Symmetric encryption is fast technique                                     | Asymmetric encryption is slower in terms of speed.                                           |
| **Algorithms**           | RC4, AES, DES, 3DES, and QUAD.                                             | RSA, Diffie-Hellman, ECC algorithms.                                                         |

Ref : <https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences>

### Password Storage Concepts

#### Salting

A salt is a unique, randomly generated string that is added to each password as part of the hashing process. As the salt is unique for every user, an attacker has to crack hashes one at a time using the respective salt rather than calculating a hash once and comparing it against every stored hash. This makes cracking large numbers of hashes significantly harder, as the time required grows in direct proportion to the number of hashes.

Salting also protects against an attacker pre-computing hashes using rainbow tables or database-based lookups. Finally, salting means that it is impossible to determine whether two users have the same password without cracking the hashes, as the different salts will result in different hashes even if the passwords are the same.

[Modern hashing algorithms](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Password_Storage_Cheat_Sheet.md#password-hashing-algorithms) such as Argon2id, bcrypt, and PBKDF2 automatically salt the passwords, so no additional steps are required when using them.

#### Peppering

A [pepper](https://www.ietf.org/archive/id/draft-ietf-kitten-password-storage-04.html#section-4.2) can be used in addition to salting to provide an additional layer of protection. The purpose of the pepper is to prevent an attacker from being able to crack any of the hashes if they only have access to the database, for example, if they have exploited a SQL injection vulnerability or obtained a backup of the database.

One of several peppering strategies is to hash the passwords as usual (using a password hashing algorithm) and then HMAC or encrypt the hashes with a symmetrical encryption key before storing the password hash in the database, with the key acting as the pepper. Peppering strategies do not affect the password hashing function in any way.

- The pepper is **shared between stored passwords**, rather than being *unique* like a salt.
- Unlike a password salt, the pepper **should not be stored in the database**.
- Peppers are secrets and should be stored in "secrets vaults" or HSMs (Hardware Security Modules).
- Like any other cryptographic key, a pepper rotation strategy should be considered.
