## 🌐 CO1 — WEB BASICS & HTTP Notes

---

### 💻 Web Basics & Architecture

* **Internet vs WWW**
    * **Internet:** A global network of interconnected computers (hardware and infrastructure). 

[Image of internet network topology]
 It provides the infrastructure for communication.
    * **WWW (World Wide Web):** A system of interlinked hypertext documents accessed via the Internet. It is a service *on* the Internet, using HTTP.

* **Web Architecture (Client–Server Model)**
    * The basic architecture for web communication.
    * **Client (e.g., Web Browser):** Requests resources (like a webpage) from the server.
    * **Server (e.g., Web Server):** Stores resources and processes the client's request, sending back the requested resource or an error message.

* **Role of Web Browser**
    * Sends HTTP requests to the web server.
    * Receives HTTP responses.
    * Renders HTML, processes CSS, and executes JavaScript to display the webpage to the user.

* **Role of Web Server**
    * Listens for HTTP requests on a specific port (default 80 for HTTP, 443 for HTTPS).
    * Processes the request, locates the requested resource (e.g., a file), or executes a script.
    * Constructs and sends an HTTP response back to the client.

* **URL Structure**
    * A Uniform Resource Locator (URL) is the address used to access a resource on the web.
    * **Format:** `scheme://authority/path?query#fragment`
        * **`scheme`** (Protocol): e.g., `http`, `https`, `ftp`.
        * **`authority`**: Includes `hostname` (or IP address) and optional `port` (e.g., `www.example.com:8080`).
        * **`path`**: Specific location of the resource on the server (e.g., `/products/item123`).
        * **`query`**: Optional parameters passed to the server (e.g., `?sort=price&color=blue`).
        * **`fragment`**: Optional pointer to a secondary resource or a location within the primary resource (e.g., `#section-title`).

---

### 📥 HTTP Protocol

* **HTTP Protocol (Hypertext Transfer Protocol)**
    * An **Application Layer** protocol that governs the transfer of data (hypertext) between a web browser (client) and a web server.
    * It is **stateless**, meaning each request from a client is independent of any previous request.

* **Request Format**
    1.  **Request Line:** `METHOD URI HTTP/VERSION` (e.g., `GET /index.html HTTP/1.1`)
    2.  **Request Headers:** Key-value pairs providing context (e.g., `Host`, `User-Agent`, `Accept`).
    3.  **Blank Line**
    4.  **Request Body (Optional):** Used to send data to the server (e.g., with `POST` or `PUT`).

* **Response Format**
    1.  **Status Line:** `HTTP/VERSION STATUS_CODE REASON_PHRASE` (e.g., `HTTP/1.1 200 OK`)
    2.  **Response Headers:** Key-value pairs providing context (e.g., `Content-Type`, `Date`, `Cache-Control`).
    3.  **Blank Line**
    4.  **Response Body (Optional):** The requested resource data (e.g., HTML content, image).

* **HTTP Methods (Verbs)**

| Method | Purpose | Safe | Idempotent |
| :--- | :--- | :--- | :--- |
| **GET** | Retrieve a resource. | Yes | Yes |
| **HEAD** | Retrieve resource headers only (no body). | Yes | Yes |
| **POST** | Submit data to be processed to a specified resource (creates new resource or triggers an action). | No | No |
| **PUT** | Upload/Replace an entire resource with the payload. | No | Yes |
| **DELETE** | Delete the specified resource. | No | Yes |
| **OPTIONS** | Describe the communication options for the target resource. | Yes | Yes |
| **PATCH** | Apply partial modifications to a resource. | No | No |

* **Safe vs. Unsafe Methods**
    * **Safe:** Methods that do not modify the server state (e.g., `GET`, `HEAD`, `OPTIONS`). They are typically read-only. Browsers can re-issue them automatically.
    * **Unsafe:** Methods that can change the server state (e.g., `POST`, `PUT`, `DELETE`, `PATCH`).

* **Idempotent Methods**
    * An operation is **idempotent** if applying it multiple times has the same effect as applying it once.
    * **Idempotent:** `GET`, `HEAD`, `PUT`, `DELETE`, `OPTIONS`. If you send a `DELETE` request 5 times, the resource is deleted only once (first time) and the subsequent 4 times will result in the same final state (resource remains deleted).
    * **Not Idempotent:** `POST`, `PATCH`. Sending a `POST` request multiple times typically creates multiple resources.

* **HTTP Status Codes**
    * 3-digit codes in the response status line, grouped into five classes:
        * **1xx:** Informational (e.g., `100 Continue`)
        * **2xx:** Success (e.g., `200 OK`, `201 Created`, `204 No Content`)
        * **3xx:** Redirection (e.g., `301 Moved Permanently`, `304 Not Modified`)
        * **4xx:** Client Error (e.g., `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`)
        * **5xx:** Server Error (e.g., `500 Internal Server Error`, `503 Service Unavailable`)

---

### 🔒 HTTP Security & Connection

* **HTTPS (HTTP Secure)**
    * It is **HTTP over TLS/SSL**.
    * **How Secured:** The standard HTTP communication is encrypted using **Transport Layer Security (TLS)**, the successor to Secure Sockets Layer (SSL).
    * **Process:**
        1.  **DNS Lookup** (Finds server IP).
        2.  **TCP Handshake** (Establishes connection).
        3.  **TLS Handshake** (Negotiates encryption keys and algorithms, verifies server certificate). 
        4.  **Encrypted HTTP Exchange** (Request and Response are encrypted).

* **DNS Lookup**
    * The process of translating a human-readable domain name (e.g., `google.com`) into a machine-readable IP address (e.g., `142.250.68.14`).
    * The browser queries a **DNS Resolver**, which may query **Root Name Servers**, **TLD (Top-Level Domain) Name Servers**, and finally the **Authoritative Name Server** to find the correct IP address.

* **TCP Handshake (Three-Way Handshake)**
    * A mechanism used by the Transport Control Protocol (TCP) to establish a reliable connection before data transfer.
    * **Steps (SYN, SYN-ACK, ACK):**
        1.  Client sends **SYN** (Synchronize) packet.
        2.  Server receives SYN and replies with **SYN-ACK** (Synchronize-Acknowledge) packet.
        3.  Client receives SYN-ACK and replies with **ACK** (Acknowledge) packet.
    * Connection is established, and data transfer can begin.

* **TLS/SSL Basics**
    * A cryptographic protocol for securing communication.
    * Uses a **Public Key Infrastructure (PKI)** with **Digital Certificates** to authenticate the server (and optionally the client).
    * Negotiates a **symmetric session key** during the handshake, which is then used for fast bulk data encryption.

---

### 🚀 Advanced Concepts

* **Caching Concepts**
    * Storing copies of resources closer to the client (e.g., in the browser cache, proxy cache) to reduce latency and server load.
    * **Headers involved:** `Cache-Control`, `Expires`, `Last-Modified`, `ETag`.
    * `304 Not Modified` status code is sent by the server when the client's cached copy is still valid (based on headers like `If-Modified-Since` or `If-None-Match`).

* **Proxy Server**
    * A server that acts as an intermediary for requests from clients seeking resources from other servers.
    * **Advantages:** Caching (improving performance), security (hiding client/server identity), filtering, logging.
    * **Disadvantages:** Added latency, potential security risk if the proxy is compromised, single point of failure.
        * *Types:* Forward proxy (client-side), Reverse proxy (server-side).

* **Cookies vs. Sessions**
    * **Cookies:** Small pieces of data stored *on the client's browser* by the server, primarily used for **client-side state management** (e.g., tracking user preferences, storing login tokens).
    * **Sessions:** A server-side mechanism for storing user-specific data *on the server*. The client usually holds a **Session ID** (often in a cookie) that links their request to their data on the server.

* **HTTP vs. WebSocket**
    * **HTTP:** Unidirectional (client requests, server responds), connection closes after response, **stateless**, *Polling* is needed for real-time data.
    * **WebSocket:** Bidirectional (full-duplex) communication channel, persistent connection (kept open), **stateful**, ideal for real-time applications (e.g., chat, games).

* **HTTP vs. Server-Sent Events (SSE)**
    * **HTTP:** Client-initiated request/response.
    * **SSE:** Provides a **one-way continuous flow of updates from the server to the client** over a single, long-lived HTTP connection. The client does not need to repeatedly poll for new data. Good for real-time news feeds or stock tickers where the client only needs to receive updates.

---
The video [How DNS works - DNS LOOKUP | DNS forward Look up explained STEP BY STEP with EXAMPLES | domain name](https://www.youtube.com/watch?v=eSrC-7yeF7c) explains the DNS lookup process, which is a key part of how web communication is initiated before the HTTP protocol is used.


http://googleusercontent.com/youtube_content/0


## Suggestions sheet:

That's a great idea! Getting a detailed review of HTTP methods and status codes is essential for understanding web communication.

Here are the details on **HTTP Methods** and **HTTP Status/Response Codes** in a comprehensive Markdown format.

## 🚀 HTTP Methods (Verbs) and Characteristics

HTTP methods define the action to be performed on the resource identified by the URI.

| Method | Description | Safe | Idempotent | Body Allowed | Typical Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | Retrieves a representation of the specified resource. | **Yes** | **Yes** | No | Fetching a webpage, an image, or data from an API. |
| **HEAD** | Asks for the headers that would be returned by a `GET` request, but *without* the response body. | **Yes** | **Yes** | No | Checking resource existence, size, or modification date. |
| **POST** | Submits data to be processed to the identified resource. The data is included in the request body. | No | No | **Yes** | Creating a new resource, submitting a form, or sending data that triggers an action. |
| **PUT** | Replaces all current representations of the target resource with the uploaded content in the request body. | No | **Yes** | **Yes** | Fully updating an existing resource (requires the full resource state). |
| **DELETE** | Removes the specified resource. | No | **Yes** | No | Deleting a resource (e.g., a specific record or file). |
| **CONNECT**| Establishes a tunnel to the server identified by the target resource. | No | No | No | Used primarily by proxies to change to an HTTPS connection. |
| **OPTIONS**| Describes the communication options (methods) available for the target resource. | **Yes** | **Yes** | No | Used by clients (e.g., CORS pre-flight requests) to check server capabilities. |
| **TRACE** | Performs a message loop-back test along the path to the target resource. Used for debugging. | **Yes** | **Yes** | No | Rarely used in production; shows how a request is processed by intermediate servers. |
| **PATCH** | Applies *partial modifications* to a resource. | No | No | **Yes** | Partially updating an existing resource (e.g., changing only a user's email, not their whole profile). |

---

### Key HTTP Method Characteristics

#### 1. Safe Methods
* **Definition:** A method is "safe" if it is essentially read-only and does not modify the state of the server.
* **Benefit:** Clients (like browsers and caches) can re-issue safe requests automatically without fear of side effects.
* **Examples:** `GET`, `HEAD`, `OPTIONS`, `TRACE`.

#### 2. Idempotent Methods
* **Definition:** A method is "idempotent" if executing it multiple times yields the same result as executing it once.
* **Benefit:** Useful for handling network interruptions; if a client doesn't get a response, it can safely re-issue the request.
* **Examples:** `GET`, `HEAD`, `PUT`, `DELETE`, `OPTIONS`.
    * *Note on `DELETE`:* While the first `DELETE` succeeds, subsequent calls will result in the same final state (the resource is still deleted), typically returning a `404 Not Found` or `204 No Content`, making it idempotent in effect.
    * *Note on `PUT`:* Repeated `PUT` requests will overwrite the resource with the exact same content every time.

---

## 🚦 HTTP Status/Response Codes

Status codes are returned in the response's status line to indicate the result of the attempt to understand and satisfy the client's request. 

### 1xx: Informational
The request has been received, continuing process.

| Code | Name | Description |
| :--- | :--- | :--- |
| **100** | Continue | The client should continue with its request (used by a client with a request body to ask for approval before sending the data). |
| **101** | Switching Protocols | The server understands and is willing to comply with the client's request to switch protocols (e.g., HTTP to WebSocket). |

### 2xx: Success
The action was successfully received, understood, and accepted.

| Code | Name | Description |
| :--- | :--- | :--- |
| **200** | OK | Standard response for successful HTTP requests. The response body contains the requested data. |
| **201** | Created | The request has succeeded and a new resource has been created as a result (typically following a `POST` or `PUT`). |
| **202** | Accepted | The request has been accepted for processing, but the processing has not been completed yet (often for asynchronous operations). |
| **204** | No Content | The server successfully processed the request, but is not returning any content (often used for successful `DELETE` or `PUT` requests). |
| **206** | Partial Content | The server is delivering only part of the resource due to a range header sent by the client (used for file downloads/streaming). |

### 3xx: Redirection
Further action needs to be taken by the user agent (browser) to fulfill the request.

| Code | Name | Description |
| :--- | :--- | :--- |
| **301** | Moved Permanently| The requested resource has been permanently moved to a new URI (location header specifies the new URL). **Search engines update their links.** |
| **302** | Found | (Formerly "Moved Temporarily") The requested resource resides temporarily under a different URI. **Search engines should not update their links.** |
| **303** | See Other | The response to the request can be found under another URI using the `GET` method. Typically follows a `POST` request. |
| **304** | Not Modified | The client's cached copy of the resource is still valid. The server is not sending a response body, instructing the client to use its cached version. |
| **307** | Temporary Redirect | The requested resource is temporarily under a different URI, and the client should *not* change the request method (unlike `302`). |
| **308** | Permanent Redirect | The requested resource is permanently under a different URI, and the client should *not* change the request method (unlike `301`). |

### 4xx: Client Error
The request contains bad syntax or cannot be fulfilled.

| Code | Name | Description |
| :--- | :--- | :--- |
| **400** | Bad Request | The server cannot process the request due to perceived client error (e.g., malformed request syntax, invalid parameters). |
| **401** | Unauthorized | The request has not been applied because it lacks valid authentication credentials for the target resource. |
| **403** | Forbidden | The client does not have access rights to the content (authorization failed). Unlike `401`, re-authenticating won't help. |
| **404** | Not Found | The server can't find the requested resource. This is perhaps the most famous error code. |
| **405** | Method Not Allowed| The request method (e.g., `POST`) is known by the server but has been disabled or is not supported for the target resource. |
| **408** | Request Timeout | The server would like to shut down this unused connection because the client did not produce a request within the time the server was prepared to wait. |
| **409** | Conflict | The request could not be completed because of a conflict with the current state of the target resource (e.g., a concurrent update conflict). |
| **429** | Too Many Requests | The user has sent too many requests in a given amount of time ("rate limiting"). |

### 5xx: Server Error
The server failed to fulfill an apparently valid request.

| Code | Name | Description |
| :--- | :--- | :--- |
| **500** | Internal Server Error| A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |
| **501** | Not Implemented | The server does not support the functionality required to fulfill the request (e.g., an unsupported request method). |
| **502** | Bad Gateway | The server, while acting as a gateway or proxy, received an invalid response from an upstream server it accessed in attempting to fulfill the request. |
| **503** | Service Unavailable| The server is not ready to handle the request (common when the server is overloaded or down for maintenance). |
| **504** | Gateway Timeout | The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server. |
---
Would you like me to elaborate on a specific status code or method, or perhaps provide an example of a typical HTTP request and response exchange?

## PYQ:
This is a comprehensive set of questions covering Web Basics and HTTP. I will answer all parts of both options (a) and (b) from the provided images, using the detailed notes format.

## 📝 Answers to HTTP & Web Basics Questions

### Block [1] (a)

#### i) Describe with examples the format of an HTTP URL with mandatory and optional parts.

A **URL (Uniform Resource Locator)** is the address used to specify the location of a resource on the Internet.
| Part | Description | Mandatory/Optional | Example |
| :--- | :--- | :--- | :--- |
| **Scheme (Protocol)** | Defines the protocol used to access the resource. | **Mandatory** | `http` or `https` |
| **Authority** | Specifies the server hosting the resource. | **Mandatory** | `www.example.com:8080` |
|     *Hostname* | The domain name or IP address of the server. | Mandatory | `www.example.com` |
|     *Port* | The TCP port number. Defaults to 80 (HTTP) or 443 (HTTPS) if omitted. | Optional | `:8080` |
| **Path** | Identifies the specific location of the resource on the server. | Optional | `/documents/index.html` |
| **Query** | Contains key-value pairs of data passed to the server, often for database queries or filtering. Preceded by `?`. | Optional | `?category=books&sort=price` |
| **Fragment** | Points to a specific section/anchor within the resource itself. Preceded by `#`. | Optional | `#chapter5` |

**Example URL and Parts:**
`https://docs.google.com/forms/d/edit?usp=sharing#response=A`

  * **Scheme:** `https`
  * **Authority (Hostname):** `docs.google.com` (Port 443 is assumed)
  * **Path:** `/forms/d/edit`
  * **Query:** `usp=sharing`
  * **Fragment:** `response=A`

#### ii) Explain HyperText Transfer Protocol (HTTP) with examples.

**HTTP (HyperText Transfer Protocol)** is an **Application Layer protocol** used to transfer hypertext (web pages, images, data) between a web client (browser) and a web server.

  * **Stateless:** HTTP is inherently stateless; the server treats each request as independent and does not remember past interactions (cookies/sessions are used to manage state).
  * **Request-Response Cycle:** It operates based on a request-response paradigm.
    1.  The **Client** opens a connection and sends an **HTTP Request** (e.g., to fetch a page).
    2.  The **Server** receives the request, processes it, and sends back an **HTTP Response** (e.g., the HTML content).
    3.  The connection is often closed (non-persistent or kept alive briefly).

**Example:**

  * **Action:** A user types `http://example.com/products/item1` into the browser.
  * **Client Request (Simplified):**
    ```http
    GET /products/item1 HTTP/1.1
    Host: example.com
    User-Agent: Mozilla/5.0
    ```
  * **Server Response (Simplified):**
    ```http
    HTTP/1.1 200 OK
    Content-Type: text/html
    Content-Length: 1024

    <!DOCTYPE html>... (HTML content for item1)
    ```

#### iii) Explain with examples the types of the header field in HTTP.

HTTP header fields are key-value pairs that provide essential metadata about the request or response, the entity being transferred, and the connection itself.
| Type | Description | Example Headers |
| :--- | :--- | :--- |
| **General Headers** | Apply to both the request and the response, but are not related to the data being transmitted. | `Cache-Control: no-cache`, `Connection: close`, `Date: Mon, 15 Dec 2025...` |
| **Request Headers** | Specific to the client request, providing context about the client, the resource requested, or expected response formats. | `Host: example.com`, `User-Agent: Chrome`, `Accept: text/html`, `Authorization: Bearer <token>` |
| **Response Headers** | Specific to the server response, providing information about the server, the response entity, or access control. | `Server: Apache`, `Allow: GET, POST`, `WWW-Authenticate: Basic`, `Set-Cookie: sessionID=xyz` |
| **Entity Headers** | Describe the body of the message (either in request or response), such as its content type, length, or encoding. | `Content-Type: application/json`, `Content-Length: 1280`, `Content-Encoding: gzip`, `Last-Modified: Sat, 13 Dec 2025...` |

### Block [1] (b)

#### i) Identify the different parts of the following URL.

`http://www.it.just.ac.in:8765/result.jsp?name=student&sort=byMarks#top`

| URL Part | Value | Type |
| :--- | :--- | :--- |
| **Scheme** | `http` | Protocol |
| **Hostname** | `www.it.just.ac.in` | Domain Name |
| **Port** | `8765` | TCP Port |
| **Path** | `/result.jsp` | Resource Location on Server |
| **Query** | `name=student&sort=byMarks` | Data Parameters (Key-Value) |
| **Fragment** | `top` | Internal Anchor/Section |

#### ii) Discuss differences between GET and POST methods of the HTTP protocol.

| Feature | GET | POST |
| :--- | :--- | :--- |
| **Purpose** | Retrieve data from the server. | Send data to the server to create or update a resource. |
| **Data Location** | Data is appended to the URL as query parameters. | Data is sent in the request body. |
| **Security** | Less secure as data is visible in the URL and browser history. | More secure as data is not exposed in the URL. |
| **Idempotency** | **Idempotent** (Multiple requests have the same effect as one). | **Not Idempotent** (Multiple requests usually create multiple resources). |
| **Safeness** | **Safe** (Does not change server state). | **Unsafe** (Changes server state). |
| **Caching** | Can be easily cached by browsers and proxies. | Generally not cached. |
| **Data Limit** | Limited data size due to URL length restrictions. | No practical limit on data size. |

#### iii) Explain how HTML form elements can be used to upload data to the server.

HTML forms are the primary way for users to input data and send it to a web server.

1.  **`<form>` Tag:** The data submission process is defined by the `<form>` tag's attributes:

      * **`action`:** Specifies the URL on the server (the resource) that will handle the form data.
      * **`method`:** Specifies the HTTP method to use, typically **`GET`** or **`POST`**.
      * **`enctype`:** Specifies how form data should be encoded. For file uploads, it must be set to **`multipart/form-data`**.

2.  **Input Elements:** Form elements like `<input type="text">`, `<textarea>`, `<select>`, and specifically `<input type="file">` collect the data. The `name` attribute of the input is used as the field key when sending data to the server.

3.  **Data Submission:**

      * If `method="GET"`, the browser collects all field names and values and appends them to the `action` URL as a query string.
      * If `method="POST"`, the browser collects all field names and values and packages them into the **HTTP Request Body**. This is the method used for file uploads and large amounts of data.

4.  **Server Processing:** The server-side script (e.g., Python, PHP, Java servlet) at the `action` URL receives the HTTP request, parses the data from the query string (GET) or the request body (POST), and performs the required action (e.g., saving data to a database, saving an uploaded file to disk).

### Block [1] (a) - Second Image

#### i) Write the advantages and disadvantages of proxy servers.

A **Proxy Server** acts as an intermediary for requests from clients seeking resources from other servers.
**Advantages:**

  * **Performance/Caching:** Stores local copies of frequently requested resources, speeding up access for clients and reducing server load.
  * **Security & Filtering:** Can block access to malicious websites or filter inappropriate content. It can also hide the client's internal IP address, increasing anonymity.
  * **Access Control:** Can be used to restrict client access to specific resources or websites (e.g., in a corporate setting).
  * **Load Balancing (Reverse Proxy):** Distributes incoming client requests across a group of backend servers, preventing any single server from becoming overwhelmed.

**Disadvantages:**

  * **Latency:** Introducing an extra hop in the network path can potentially increase the time it takes for a request to be fulfilled, especially if the proxy is slow or busy.
  * **Security Risk:** If the proxy server itself is compromised, all client traffic passing through it could be intercepted.
  * **Complexity:** Setting up and managing a large proxy infrastructure adds administrative overhead.
  * **Single Point of Failure (if not redundant):** If a single proxy server fails, all clients relying on it may lose access to the internet or specific resources.

#### ii) Describe with concrete examples how you can make HTTP secured.

HTTP is secured by using **HTTPS (HTTP Secure)**, which involves layering the standard HTTP protocol over the **Transport Layer Security (TLS)** protocol (the successor to SSL).

**Concrete Steps to Secure HTTP:**

1.  **Obtain an SSL/TLS Certificate:**

      * A web server owner purchases or obtains a certificate from a **Certificate Authority (CA)**.
      * *Example:* Obtaining a certificate for `secureapp.com` that contains the public key and server identity.

2.  **Install the Certificate:**

      * The certificate is installed on the web server (e.g., Apache, Nginx).
      * The server is configured to listen for connections on port **443** (the default port for HTTPS) instead of port 80.

3.  **TLS Handshake:**

      * When a client (browser) connects using `https://`, the **TLS Handshake** is initiated.     \* *Example:* The browser sends a `ClientHello`. The server responds with a `ServerHello` and its digital certificate. The browser verifies the certificate's validity using the public key of the CA.

4.  **Key Exchange and Encryption:**

      * During the handshake, the client and server agree upon a **session key** (symmetric key) and encryption algorithms.
      * *Example:* The browser uses the server's public key (from the certificate) to encrypt the session key and sends it to the server. The server uses its private key to decrypt the session key.

5.  **Encrypted Data Transfer:**

      * All subsequent HTTP requests and responses are encrypted using the established session key before being sent over the network.
      * *Example:* When the client sends `GET /data`, the actual message sent over the wire is unreadable encrypted text. The server decrypts it, processes the HTTP request, encrypts the HTTP response, and sends it back.

#### iii) Write the format of an HTTP request message.

An HTTP Request Message consists of four main parts, each separated by a newline character.

1.  **Request Line:**

      * Specifies the **Method**, the **Request-URI**, and the **HTTP Protocol Version**.
      * **Format:** `METHOD URI HTTP/VERSION`
      * **Example:** `GET /users/profile HTTP/1.1`

2.  **Request Headers:**

      * Key-value pairs that pass context about the request, the client, and acceptable content types.
      * **Format:** `Header-Name: Header-Value`
      * **Examples:**
        ```http
        Host: api.example.com
        User-Agent: My-Client-App/1.0
        Accept: application/json, */*
        Authorization: Bearer <token-string>
        ```

3.  **Blank Line (CRLF):**

      * A single blank line that signals the end of the header section.

4.  **Request Body (Message Body):**

      * Optional data payload sent to the server, primarily used with methods like `POST` and `PUT`.
      * **Example:** For a `POST` request creating a new user:
        ```json
        {
          "username": "jdoe",
          "email": "jdoe@example.com"
        }
        ```

**Full Example Request:**

```http
POST /submit-form HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Connection: keep-alive

name=John+Doe&age=30&city=London
```

### Block [1] (b) - Second Image

#### i) What are Safe and unsafe methods?

| Characteristic | Safe Methods | Unsafe Methods |
| :--- | :--- | :--- |
| **Definition** | Methods that do not modify the state of the server or the resource. They are read-only operations. | Methods that have the potential to change the state of the server or the resource. |
| **Server State** | No side effects on the server (only data retrieval). | Can lead to data creation, modification, or deletion. |
| **Re-issuance** | Browsers/caches can re-issue them automatically if they fail. | Must not be automatically re-issued by clients without user confirmation. |
| **Examples** | `GET`, `HEAD`, `OPTIONS`, `TRACE`. | `POST`, `PUT`, `DELETE`, `PATCH`, `CONNECT`. |

#### ii) Suppose URL's of ten thousand image files are stored in a file. Write the pseudo-code to download all these images.

The pseudo-code below outlines a process that reads the URLs from a file and iteratively sends HTTP `GET` requests to download each image. For efficiency, it uses a mechanism to handle network operations.

```pseudocode
// Define Constants
MAX_RETRIES = 3
URLS_FILE = "image_urls.txt"
DOWNLOAD_DIRECTORY = "downloaded_images/"

// Function to download a single image
FUNCTION download_image(url, filename):
    FOR attempt FROM 1 TO MAX_RETRIES DO
        BEGIN
            TRY
                // 1. Send HTTP GET Request
                RESPONSE = HTTP_GET(url)

                IF RESPONSE.STATUS_CODE IS 200 THEN
                    // 2. Save the image content
                    SAVE_FILE(DOWNLOAD_DIRECTORY + filename, RESPONSE.BODY)
                    PRINT "Successfully downloaded: " + filename
                    RETURN SUCCESS
                ELSE IF RESPONSE.STATUS_CODE IS 404 THEN
                    PRINT "Error 404: Image not found at " + url
                    RETURN FAILURE
                ELSE
                    PRINT "Download failed for " + url + " with status: " + RESPONSE.STATUS_CODE
                    WAIT(2 ^ attempt * 1000) // Exponential backoff
            CATCH EXCEPTION as e:
                PRINT "Network error for " + url + ": " + e
                WAIT(2 ^ attempt * 1000) // Exponential backoff
        END
    END
    PRINT "Failed to download " + url + " after " + MAX_RETRIES + " attempts."
    RETURN FAILURE

// Main Program
FUNCTION main():
    CREATE_DIRECTORY_IF_NOT_EXISTS(DOWNLOAD_DIRECTORY)
    
    // 1. Read URLs from file
    URL_LIST = READ_ALL_LINES_FROM_FILE(URLS_FILE)

    FOR url IN URL_LIST DO
        BEGIN
            // Extract filename from URL (e.g., from path or generate unique name)
            filename = EXTRACT_FILENAME_FROM_URL(url) 
            
            // 2. Trigger the download function (can be run concurrently for efficiency)
            // Note: In a real environment, this loop would launch concurrent tasks/threads for performance.
            download_image(url, filename)
        END
    END
    PRINT "Download process complete."

// Run the main program
CALL main()
```

#### iii) Write the format of an HTTP response message.

An HTTP Response Message is sent from the server back to the client and consists of four main parts.

1.  **Status Line:**

      * Specifies the **HTTP Protocol Version**, the **Status Code**, and a corresponding **Reason Phrase**.
      * **Format:** `HTTP/VERSION STATUS_CODE REASON_PHRASE`
      * **Example:** `HTTP/1.1 200 OK` or `HTTP/1.1 404 Not Found`

2.  **Response Headers:**

      * Key-value pairs that provide context about the response, the server, and the entity being sent.
      * **Format:** `Header-Name: Header-Value`
      * **Examples:**
        ```http
        Server: Apache/2.4.1 (Unix)
        Content-Type: text/html; charset=utf-8
        Content-Length: 5120
        Cache-Control: max-age=3600
        Set-Cookie: sessionId=abc1234; HttpOnly
        ```

3.  **Blank Line (CRLF):**

      * A single blank line that signals the end of the header section.

4.  **Response Body (Message Body):**

      * The payload data being returned to the client (e.g., HTML content, JSON data, image bytes). This is absent in responses like `204 No Content` or `304 Not Modified`.
      * **Example:** The HTML source code for the requested webpage.

**Full Example Response:**

```http
HTTP/1.1 200 OK
Date: Mon, 15 Dec 2025 02:30:00 GMT
Server: Nginx
Content-Type: application/json
Content-Length: 48

{
  "status": "success",
  "data": {"id": 1, "name": "widget"}
}
```
