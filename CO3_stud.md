# 💻 CO3 — JAVASCRIPT & AJAX: Study Lecture Notes

These notes cover JavaScript fundamentals, DOM manipulation, closures, callbacks, and AJAX, drawing from common syllabus requirements and important concepts.

-----

## 🚀 I. JavaScript Fundamentals

### 1\. What is JavaScript?

JavaScript (JS) is a high-level, interpreted, dynamically-typed scripting language primarily used to make web pages **interactive**. Along with HTML and CSS, it is one of the three core technologies of the World Wide Web.

  * **HTML:** Defines the content and structure of web pages.
  * **CSS:** Controls the layout and presentation (style).
  * **JavaScript:** Provides the interactive behavior.

### 2\. Key JavaScript Features

  * **Interpreted:** Executes code line by line through an interpreter (unlike compiled languages).
  * **Object-Oriented:** Supports object-oriented programming (OOP) principles (e.g., objects, inheritance, polymorphism).
  * **Client-Side Execution:** Primarily runs on the user's web browser, reducing server load.
  * **Dynamically-Typed:** Variable types are checked during runtime, not compile-time.
  * **Asynchronous:** Capable of handling non-blocking operations, crucial for modern web apps (like AJAX).
  * **Prototypal Inheritance:** Uses prototypes for inheritance instead of classes (though ES6 introduced `class` syntax as syntactic sugar).
  * **Cross-Platform:** Runs in any browser on any OS.

### 3\. Variables

Variables are containers for storing data values.

| Keyword | Scope | Re-declaration | Re-assignment | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| `var` | Function-scoped | Yes | Yes | Older JS, generally avoided. |
| `let` | Block-scoped | No | Yes | Variables whose value might change. |
| `const` | Block-scoped | No | No | Variables whose value remains constant (must be initialized). |

**Example:**

```javascript
const PI = 3.14159;
let count = 0;
count = count + 1; // Re-assignment is allowed for 'let'
```

### 4\. Functions

Functions are blocks of code designed to perform a particular task.

  * **Function Declaration:**
    ```javascript
    function greet(name) {
      return "Hello, " + name;
    }
    ```
  * **Function Expression:**
    ```javascript
    const farewell = function(name) {
      return "Goodbye, " + name;
    };
    ```
  * **Arrow Functions (ES6):** Shorter syntax, different handling of `this`.
    ```javascript
    const multiply = (a, b) => a * b;
    ```

### 5\. Events in JavaScript & Propagation

An **event** is an action that happens in the system or on an HTML element (e.g., a mouse click, a keypress, a page load).

  * **Event Handling:** The mechanism to run a specific JavaScript function when an event occurs.

    ```html
    <button onclick="handleClick()">Click Me</button>
    ```

    ```javascript
    function handleClick() {
      alert("Button clicked!");
    }
    ```

  * **Event Propagation:** Describes the order in which elements receive the event. It has three phases:

    1.  **Capturing Phase:** The event travels **down** the DOM tree from the `window` to the target element.
    2.  **Target Phase:** The event reaches the actual target element.
    3.  **Bubbling Phase:** The event travels **up** the DOM tree from the target element back to the `window`.

    <!-- end list -->

      * **Bubbling** is the default behavior. If an inner element is clicked, its event handler runs, then its parent's, and so on up the hierarchy.

-----

## 🌳 II. Document Object Model (DOM)

### 1\. Explain DOM with Diagram

The **Document Object Model (DOM)** is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as a logical tree structure.

> **Crucial Point:** The DOM is *not* JavaScript. It is an API (Application Programming Interface) that JavaScript uses to interact with the HTML document.

### 2\. DOM Tree

The DOM structure is a **node tree**, where every element, attribute, and piece of text is a node.

  * **Document Node:** The root of the tree (the HTML document itself).
  * **Element Nodes:** HTML tags (`<body>`, `<h1>`, `<p>`, etc.).
  * **Text Nodes:** The actual content inside the elements.
  * **Attribute Nodes:** Attributes of the elements (e.g., `id="main"`).

### 3\. DOM Manipulation

**DOM manipulation** is the process of using JavaScript to change the structure, style, or content of the DOM tree.

#### A. Selecting Elements (Finding Nodes)

| Method | Description | Example |
| :--- | :--- | :--- |
| `getElementById()` | Selects one element by its unique `id`. | `document.getElementById('header')` |
| `getElementsByClassName()` | Selects multiple elements by their `class` name (returns an HTML Collection). | `document.getElementsByClassName('item')` |
| `querySelector()` | Selects the *first* element that matches a specified CSS selector. | `document.querySelector('#main p')` |
| `querySelectorAll()` | Selects *all* elements that match a specified CSS selector (returns a NodeList). | `document.querySelectorAll('.btn')` |

#### B. Updating Elements

| Action | Example |
| :--- | :--- |
| **Change Content** | `element.textContent = 'New Text';` or `element.innerHTML = '<strong>New HTML</strong>';` |
| **Change Style** | `element.style.color = 'blue';` |
| **Change Attributes** | `element.setAttribute('data-id', '123');` or `element.href = 'newlink.html';` |

#### C. Creating Elements

1.  **Create the element:**
    ```javascript
    const newDiv = document.createElement('div');
    ```
2.  **Add content/attributes:**
    ```javascript
    newDiv.textContent = 'A new element!';
    newDiv.classList.add('info');
    ```
3.  **Append to the DOM:**
    ```javascript
    const parent = document.getElementById('container');
    parent.appendChild(newDiv); // Inserts as the last child
    // parent.prepend(newDiv); // Inserts as the first child
    ```

-----

## 🧠 III. Modern JS Ideas

### 1\. What are Closures?

A **closure** is a feature in JavaScript where an inner function has access to the outer (enclosing) function's variables—*even after* the outer function has finished executing.

  * A closure "remembers" the environment in which it was created.
  * It allows for **data privacy** and creating function factories.

**Example:**

```javascript
function makeCounter() {
  let count = 0; // The outer function's variable

  return function() { // The inner function (the closure)
    count = count + 1; // Has access to 'count'
    return count;
  };
}

const counter1 = makeCounter();
console.log(counter1()); // Output: 1 (count is 'remembered')
console.log(counter1()); // Output: 2
// The 'count' variable is private and only accessible via 'counter1'.
```

### 2\. Callback Functions

A **callback function** is a function passed into another function as an argument, which is then executed inside the outer function at a later time.

  * They are fundamental to **asynchronous programming** in JavaScript.

**Example (Synchronous Callback - e.g., Array method):**

```javascript
function printItem(item) {
  console.log("Item:", item);
}

const names = ['Alice', 'Bob', 'Charlie'];
// printItem is the callback function, executed for each element
names.forEach(printItem);
```

**Example (Asynchronous Callback - e.g., setTimeout):**

```javascript
console.log("Start");

// The function inside setTimeout is the callback. It runs AFTER the delay.
setTimeout(function() {
  console.log("This runs after 2 seconds."); // Callback executes later
}, 2000);

console.log("End");
// Output order: Start -> End -> This runs after 2 seconds.
```

### 3\. Debugging Basics

  * **`console.log()`:** The most common tool. Used to inspect variable values at different points in the code.
  * **Breakpoints:** Using the browser's Developer Tools (Sources/Debugger tab) to pause code execution on a specific line, allowing inspection of the scope, variables, and call stack.
  * **`debugger;` statement:** Inserting this keyword into your JS code will automatically pause execution if the browser's DevTools are open.

-----

## 🔄 IV. AJAX (Asynchronous JavaScript and XML)

### 1\. What is AJAX?

**AJAX** is a set of web development techniques using various web technologies on the client-side to create asynchronous web applications.

  * It is **not** a technology itself, but a technique combining:
      * **HTML/CSS:** Presentation.
      * **JavaScript:** Interactivity and data fetching.
      * **`XMLHttpRequest`** (or more commonly, the modern **`fetch` API**): To exchange data asynchronously with a server.

### 2\. Need for AJAX: Updating Page Sections Without Reload

**Traditional Web Model (Synchronous):**
User clicks a link $\rightarrow$ Request sent to Server $\rightarrow$ Server processes $\rightarrow$ Server sends a **new, full HTML page** $\rightarrow$ Browser loads the entire page (page reload).

**AJAX Model (Asynchronous):**
User clicks a link $\rightarrow$ JS makes an AJAX request in the background $\rightarrow$ Server processes & sends **only the data** (usually JSON/XML) $\rightarrow$ JS receives data & uses DOM manipulation to **update only the required section** of the page $\rightarrow$ **No full page reload**.

### 3\. Synchronous vs Asynchronous

This distinction is crucial for understanding AJAX and modern JS.

| Feature | Synchronous | Asynchronous |
| :--- | :--- | :--- |
| **Execution Flow** | Tasks execute one after the other. The next task waits for the previous one to complete. | Tasks can run in parallel. A task can start without waiting for a previous task to finish. |
| **Blocking** | **Blocking** (The main thread/UI freezes until the task is done). | **Non-Blocking** (The main thread/UI remains responsive). |
| **Example** | Simple function calls, `alert()` (in some older contexts). | AJAX requests, `setTimeout()`, Promises (`fetch`), `async/await`. |

### 4\. AJAX Working Flow

1.  **User Event:** An event triggers (e.g., button click, page load).
2.  **JavaScript Call:** A JavaScript function calls the AJAX mechanism (`fetch` or `XMLHttpRequest`).
3.  **Request Sent:** An HTTP Request is sent to the server.
4.  **Server Processing:** The server processes the request (e.g., queries a database).
5.  **Response Sent:** The server sends a response back to the browser (e.g., JSON data).
6.  **JS Handles Response:** The JavaScript code's callback function receives the response data.
7.  **DOM Update:** JS uses the data to update the DOM (manipulate the page content) without a full refresh.

### 5\. AJAX Advantages & Disadvantages

#### ✅ Advantages

  * **Improved User Experience:** The page remains responsive, and the UI doesn't freeze.
  * **Faster Response Time:** Only necessary data is transferred, not the whole HTML page.
  * **Reduced Bandwidth Usage:** Less data is sent over the network.
  * **Decoupling:** Separation of data (server) and presentation (client).

#### ❌ Disadvantages

  * **Security Issues:** Increased exposure to client-side vulnerabilities.
  * **Debugging is Harder:** Asynchronous nature can make tracking the flow complex.
  * **Complexity:** Can increase code complexity compared to traditional request/response cycles.
  * **Browser History:** Dynamically updated content may not be recorded in the browser's history by default.

-----

## 📦 V. Lazy Loading (Conceptual)

### What is Lazy Loading?

**Lazy loading** is a design pattern used to defer the initialization of an object or resource until the point at which it is actually needed.

**In Web Development:** It is primarily used to load resources (like images, videos, or even sections of a page) only when the user scrolls them into the viewport.

  * **Conceptual Mechanism:** Instead of loading all images on page load, a placeholder image (or blank space) is shown. JavaScript monitors the user's scroll position, and once an image's position is near the visible area, JS changes the image source to load the actual image.

**Benefit:** Significant improvement in initial page load time and overall site performance, especially for content-heavy pages.

-----

Would you like a brief explanation of how the modern `fetch` API is used for making AJAX requests, or a quick-reference table for common DOM methods?

## Suggestions Sheet:

Absolutely\! Here are comprehensive study lecture notes on JavaScript and AJAX, formatted in Markdown for easy reading and study.

# 💻 CO3 — JAVASCRIPT & AJAX: Study Lecture Notes

These notes cover JavaScript fundamentals, DOM manipulation, closures, callbacks, and AJAX, drawing from common syllabus requirements and important concepts.

-----

## 🚀 I. JavaScript Fundamentals

### 1\. What is JavaScript?

JavaScript (JS) is a high-level, interpreted, dynamically-typed scripting language primarily used to make web pages **interactive**. Along with HTML and CSS, it is one of the three core technologies of the World Wide Web.

  * **HTML:** Defines the content and structure of web pages.
  * **CSS:** Controls the layout and presentation (style).
  * **JavaScript:** Provides the interactive behavior.

### 2\. Key JavaScript Features

  * **Interpreted:** Executes code line by line through an interpreter (unlike compiled languages).
  * **Object-Oriented:** Supports object-oriented programming (OOP) principles (e.g., objects, inheritance, polymorphism).
  * **Client-Side Execution:** Primarily runs on the user's web browser, reducing server load.
  * **Dynamically-Typed:** Variable types are checked during runtime, not compile-time.
  * **Asynchronous:** Capable of handling non-blocking operations, crucial for modern web apps (like AJAX).
  * **Prototypal Inheritance:** Uses prototypes for inheritance instead of classes (though ES6 introduced `class` syntax as syntactic sugar).
  * **Cross-Platform:** Runs in any browser on any OS.

### 3\. Variables

Variables are containers for storing data values.

| Keyword | Scope | Re-declaration | Re-assignment | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| `var` | Function-scoped | Yes | Yes | Older JS, generally avoided. |
| `let` | Block-scoped | No | Yes | Variables whose value might change. |
| `const` | Block-scoped | No | No | Variables whose value remains constant (must be initialized). |

**Example:**

```javascript
const PI = 3.14159;
let count = 0;
count = count + 1; // Re-assignment is allowed for 'let'
```

### 4\. Functions

Functions are blocks of code designed to perform a particular task.

  * **Function Declaration:**
    ```javascript
    function greet(name) {
      return "Hello, " + name;
    }
    ```
  * **Function Expression:**
    ```javascript
    const farewell = function(name) {
      return "Goodbye, " + name;
    };
    ```
  * **Arrow Functions (ES6):** Shorter syntax, different handling of `this`.
    ```javascript
    const multiply = (a, b) => a * b;
    ```

### 5\. Events in JavaScript & Propagation

An **event** is an action that happens in the system or on an HTML element (e.g., a mouse click, a keypress, a page load).

  * **Event Handling:** The mechanism to run a specific JavaScript function when an event occurs.

    ```html
    <button onclick="handleClick()">Click Me</button>
    ```

    ```javascript
    function handleClick() {
      alert("Button clicked!");
    }
    ```

  * **Event Propagation:** Describes the order in which elements receive the event. It has three phases:

    1.  **Capturing Phase:** The event travels **down** the DOM tree from the `window` to the target element.
    2.  **Target Phase:** The event reaches the actual target element.
    3.  **Bubbling Phase:** The event travels **up** the DOM tree from the target element back to the `window`.

    <!-- end list -->

      * **Bubbling** is the default behavior. If an inner element is clicked, its event handler runs, then its parent's, and so on up the hierarchy.

-----

## 🌳 II. Document Object Model (DOM)

### 1\. Explain DOM with Diagram

The **Document Object Model (DOM)** is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as a logical tree structure.

> **Crucial Point:** The DOM is *not* JavaScript. It is an API (Application Programming Interface) that JavaScript uses to interact with the HTML document.

### 2\. DOM Tree

The DOM structure is a **node tree**, where every element, attribute, and piece of text is a node.

  * **Document Node:** The root of the tree (the HTML document itself).
  * **Element Nodes:** HTML tags (`<body>`, `<h1>`, `<p>`, etc.).
  * **Text Nodes:** The actual content inside the elements.
  * **Attribute Nodes:** Attributes of the elements (e.g., `id="main"`).

### 3\. DOM Manipulation

**DOM manipulation** is the process of using JavaScript to change the structure, style, or content of the DOM tree.

#### A. Selecting Elements (Finding Nodes)

| Method | Description | Example |
| :--- | :--- | :--- |
| `getElementById()` | Selects one element by its unique `id`. | `document.getElementById('header')` |
| `getElementsByClassName()` | Selects multiple elements by their `class` name (returns an HTML Collection). | `document.getElementsByClassName('item')` |
| `querySelector()` | Selects the *first* element that matches a specified CSS selector. | `document.querySelector('#main p')` |
| `querySelectorAll()` | Selects *all* elements that match a specified CSS selector (returns a NodeList). | `document.querySelectorAll('.btn')` |

#### B. Updating Elements

| Action | Example |
| :--- | :--- |
| **Change Content** | `element.textContent = 'New Text';` or `element.innerHTML = '<strong>New HTML</strong>';` |
| **Change Style** | `element.style.color = 'blue';` |
| **Change Attributes** | `element.setAttribute('data-id', '123');` or `element.href = 'newlink.html';` |

#### C. Creating Elements

1.  **Create the element:**
    ```javascript
    const newDiv = document.createElement('div');
    ```
2.  **Add content/attributes:**
    ```javascript
    newDiv.textContent = 'A new element!';
    newDiv.classList.add('info');
    ```
3.  **Append to the DOM:**
    ```javascript
    const parent = document.getElementById('container');
    parent.appendChild(newDiv); // Inserts as the last child
    // parent.prepend(newDiv); // Inserts as the first child
    ```

-----

## 🧠 III. Modern JS Ideas

### 1\. What are Closures?

A **closure** is a feature in JavaScript where an inner function has access to the outer (enclosing) function's variables—*even after* the outer function has finished executing.

  * A closure "remembers" the environment in which it was created.
  * It allows for **data privacy** and creating function factories.

**Example:**

```javascript
function makeCounter() {
  let count = 0; // The outer function's variable

  return function() { // The inner function (the closure)
    count = count + 1; // Has access to 'count'
    return count;
  };
}

const counter1 = makeCounter();
console.log(counter1()); // Output: 1 (count is 'remembered')
console.log(counter1()); // Output: 2
// The 'count' variable is private and only accessible via 'counter1'.
```

### 2\. Callback Functions

A **callback function** is a function passed into another function as an argument, which is then executed inside the outer function at a later time.

  * They are fundamental to **asynchronous programming** in JavaScript.

**Example (Synchronous Callback - e.g., Array method):**

```javascript
function printItem(item) {
  console.log("Item:", item);
}

const names = ['Alice', 'Bob', 'Charlie'];
// printItem is the callback function, executed for each element
names.forEach(printItem);
```

**Example (Asynchronous Callback - e.g., setTimeout):**

```javascript
console.log("Start");

// The function inside setTimeout is the callback. It runs AFTER the delay.
setTimeout(function() {
  console.log("This runs after 2 seconds."); // Callback executes later
}, 2000);

console.log("End");
// Output order: Start -> End -> This runs after 2 seconds.
```

### 3\. Debugging Basics

  * **`console.log()`:** The most common tool. Used to inspect variable values at different points in the code.
  * **Breakpoints:** Using the browser's Developer Tools (Sources/Debugger tab) to pause code execution on a specific line, allowing inspection of the scope, variables, and call stack.
  * **`debugger;` statement:** Inserting this keyword into your JS code will automatically pause execution if the browser's DevTools are open.

-----

## 🔄 IV. AJAX (Asynchronous JavaScript and XML)

### 1\. What is AJAX?

**AJAX** is a set of web development techniques using various web technologies on the client-side to create asynchronous web applications.

  * It is **not** a technology itself, but a technique combining:
      * **HTML/CSS:** Presentation.
      * **JavaScript:** Interactivity and data fetching.
      * **`XMLHttpRequest`** (or more commonly, the modern **`fetch` API**): To exchange data asynchronously with a server.

### 2\. Need for AJAX: Updating Page Sections Without Reload

**Traditional Web Model (Synchronous):**
User clicks a link $\rightarrow$ Request sent to Server $\rightarrow$ Server processes $\rightarrow$ Server sends a **new, full HTML page** $\rightarrow$ Browser loads the entire page (page reload).

**AJAX Model (Asynchronous):**
User clicks a link $\rightarrow$ JS makes an AJAX request in the background $\rightarrow$ Server processes & sends **only the data** (usually JSON/XML) $\rightarrow$ JS receives data & uses DOM manipulation to **update only the required section** of the page $\rightarrow$ **No full page reload**.

### 3\. Synchronous vs Asynchronous

This distinction is crucial for understanding AJAX and modern JS.

| Feature | Synchronous | Asynchronous |
| :--- | :--- | :--- |
| **Execution Flow** | Tasks execute one after the other. The next task waits for the previous one to complete. | Tasks can run in parallel. A task can start without waiting for a previous task to finish. |
| **Blocking** | **Blocking** (The main thread/UI freezes until the task is done). | **Non-Blocking** (The main thread/UI remains responsive). |
| **Example** | Simple function calls, `alert()` (in some older contexts). | AJAX requests, `setTimeout()`, Promises (`fetch`), `async/await`. |

### 4\. AJAX Working Flow

1.  **User Event:** An event triggers (e.g., button click, page load).
2.  **JavaScript Call:** A JavaScript function calls the AJAX mechanism (`fetch` or `XMLHttpRequest`).
3.  **Request Sent:** An HTTP Request is sent to the server.
4.  **Server Processing:** The server processes the request (e.g., queries a database).
5.  **Response Sent:** The server sends a response back to the browser (e.g., JSON data).
6.  **JS Handles Response:** The JavaScript code's callback function receives the response data.
7.  **DOM Update:** JS uses the data to update the DOM (manipulate the page content) without a full refresh.

### 5\. AJAX Advantages & Disadvantages

#### ✅ Advantages

  * **Improved User Experience:** The page remains responsive, and the UI doesn't freeze.
  * **Faster Response Time:** Only necessary data is transferred, not the whole HTML page.
  * **Reduced Bandwidth Usage:** Less data is sent over the network.
  * **Decoupling:** Separation of data (server) and presentation (client).

#### ❌ Disadvantages

  * **Security Issues:** Increased exposure to client-side vulnerabilities.
  * **Debugging is Harder:** Asynchronous nature can make tracking the flow complex.
  * **Complexity:** Can increase code complexity compared to traditional request/response cycles.
  * **Browser History:** Dynamically updated content may not be recorded in the browser's history by default.

-----

## 📦 V. Lazy Loading (Conceptual)

### What is Lazy Loading?

**Lazy loading** is a design pattern used to defer the initialization of an object or resource until the point at which it is actually needed.

**In Web Development:** It is primarily used to load resources (like images, videos, or even sections of a page) only when the user scrolls them into the viewport.

  * **Conceptual Mechanism:** Instead of loading all images on page load, a placeholder image (or blank space) is shown. JavaScript monitors the user's scroll position, and once an image's position is near the visible area, JS changes the image source to load the actual image.

**Benefit:** Significant improvement in initial page load time and overall site performance, especially for content-heavy pages.

-----

## PYQ:

I'd be happy to provide detailed notes focused on those key topics, including descriptive diagrams where they add significant instructional value.

Here are the detailed study notes:

# 📘 Detailed Study Notes: JavaScript & AJAX

-----

## 🚀 I. JS Fundamentals

### 1\. Variables (`var`, `let`, `const`)

JavaScript variable keywords define the scope and mutability of data.

  * **`var`**: Function-scoped. Prone to hoisting issues and potential variable confusion, which is why it is generally avoided now.
  * **`let`**: **Block-scoped** ($\{...\}$). Can be re-assigned but not re-declared within the same scope. Best for mutable variables.
  * **`const`**: **Block-scoped**. Cannot be re-assigned or re-declared. Must be initialized upon declaration. Best for constants or references that should not change.

| Keyword | Scope | Re-assignment | Re-declaration |
| :--- | :--- | :--- | :--- |
| `var` | Function | Yes | Yes |
| `let` | Block | Yes | No |
| `const` | Block | No | No |

### 2\. Functions

Functions are the primary means of abstracting logic in JavaScript.

| Type | Syntax | `this` Binding | Use Case |
| :--- | :--- | :--- | :--- |
| **Declaration** | `function name() {...}` | Binds its own `this` | Standard, can be called before definition (hoisted). |
| **Expression** | `const name = function() {...}` | Binds its own `this` | Useful for passing as arguments (callbacks). |
| **Arrow (ES6)** | `const name = () => {...}` | Inherits `this` from the surrounding scope (lexical scope) | Concise syntax, especially for callbacks and preserving context. |

### 3\. Events and Propagation

An **Event** is something that happens to an HTML element (click, load, mouseover). **Event Handling** is the mechanism for executing code in response to these events.

#### Event Propagation

Event propagation is the order in which an event travels through the DOM tree. It occurs in three phases:

1.  **Capturing Phase:** The event travels **down** the DOM tree, from the `window` to the target element.
2.  **Target Phase:** The event reaches the actual element where it originated.
3.  **Bubbling Phase:** The event travels **up** the DOM tree, from the target element back to the `window`. **This is the default behavior.**

<!-- end list -->

  * **Event Delegation:** A common optimization technique that leverages bubbling. Instead of attaching a listener to every child element, a single listener is attached to a parent element. This listener checks the `event.target` property to determine which child triggered the event.

-----

## 🌳 II. DOM Manipulation

The **Document Object Model (DOM)** is a tree-structure interface that treats the HTML/XML document as a collection of programmable objects (nodes).

### 1\. Selecting Elements (Finding Nodes)

| Method | Selector Type | Returns |
| :--- | :--- | :--- |
| `getElementById()` | ID (`#myId`) | Single Element |
| `querySelector()` | CSS Selector (`#id` or `.class` or `tag`) | First matching Element |
| `querySelectorAll()` | CSS Selector | Non-live **NodeList** (iterable) |
| `getElementsByClassName()` | Class Name | Live **HTMLCollection** (must be converted to array for iteration) |

### 2\. Updating and Creating Elements

#### A. Updating Elements

| Action | Property/Method | Example |
| :--- | :--- | :--- |
| **Change Text** | `textContent` (secure) | `element.textContent = 'New text.';` |
| **Change HTML** | `innerHTML` (less secure; allows raw HTML injection) | `element.innerHTML = '<strong>New HTML</strong>';` |
| **Change Style** | `style` | `element.style.backgroundColor = 'blue';` |
| **Change Class** | `classList` | `element.classList.add('active');` / `.remove('old');` |
| **Change Attribute** | `setAttribute()` | `element.setAttribute('data-id', '123');` |

#### B. Creating Elements

Creating an element involves three main steps:

1.  **Creation:** `const newDiv = document.createElement('div');`
2.  **Configuration:** `newDiv.textContent = 'Created!';`
3.  **Insertion (Appending):** Finding a parent node and inserting the new node.
    ```javascript
    const parent = document.getElementById('container');
    parent.appendChild(newDiv); // Appends as the last child
    parent.prepend(newDiv); // Inserts as the first child
    ```
4.  **Removal:**
    ```javascript
    const childToRemove = document.getElementById('old');
    childToRemove.remove(); // Modern and simple way
    ```

-----

## 🧠 III. Modern JS Ideas

### 1\. Closures

A **closure** is a function that remembers and accesses variables from its immediate outer scope, even after the outer function has finished executing.

  * They are created when an inner function is defined inside another function.

**Concept:** The inner function maintains a hidden reference to the variables in its parent scope. This allows for **private variables** in JavaScript.

**Example:**

```javascript
function makeGreeter(greeting) { // Outer function
    // 'greeting' is the variable being closed over
    return function(name) { // Inner function (the closure)
        console.log(`${greeting}, ${name}!`);
    };
}

const sayHello = makeGreeter("Hello"); // 'sayHello' now permanently remembers "Hello"
const sayHi = makeGreeter("Hi");       // 'sayHi' remembers "Hi"

sayHello("Alice"); // Output: "Hello, Alice!"
sayHi("Bob");      // Output: "Hi, Bob!"
```

### 2\. Callback Functions

A **callback** is a function passed as an argument to another function, which is intended to be executed after some kind of operation has been completed.

  * They are fundamental for handling **asynchronous** operations (like timers, file reading, and AJAX).

**Example (Asynchronous):**

```javascript
console.log("A");

setTimeout(function() { // This function is the callback
    console.log("B");   // Executes only after the 2-second delay
}, 2000);

console.log("C");

// The output order is A, C, B (demonstrating non-blocking behavior)
```

### 3\. Debugging Basics

The most effective way to debug is using the browser's Developer Tools (F12 or Ctrl+Shift+I).

  * **`console.log()`:** Used for inspecting values and checking execution flow.
  * **Breakpoints:** Setting a breakpoint in the **Sources** tab of DevTools pauses the code execution at that exact line. This allows you to inspect:
      * **Scope:** Local and Global variables.
      * **Watch:** Specific variables you want to monitor.
      * **Call Stack:** The sequence of functions that led to the current pause.
  * **`debugger;` statement:** Inserting this into your code acts as a programmatic breakpoint.

-----

## 🔄 IV. AJAX (Asynchronous JavaScript and XML)

### 1\. AJAX Working: Updating Page Sections without Reload

**AJAX** (Asynchronous JavaScript and XML) is a technique for creating fast and dynamic web pages. It allows a web page to request small amounts of data from the server **asynchronously** (in the background) without disrupting the display and behavior of the current page.

| Traditional Method | AJAX Method |
| :--- | :--- |
| Full page refresh on every interaction. | Updates only the required section of the DOM. |
| Server sends back a full HTML document. | Server usually sends back a small data package (JSON/XML). |
| **Blocking** UI experience. | **Non-blocking** (responsive) UI experience. |

### 2\. Synchronous vs Asynchronous

The core distinction that makes AJAX possible is **Asynchronous** communication.

#### Synchronous

  * A task starts and must finish completely before the next task can begin.
  * **Blocking:** The browser thread is busy waiting for the response, which causes the UI to freeze ("Not Responding").

#### Asynchronous

  * A task (like an AJAX request) is started, and the browser can immediately move on to the next task (like updating the UI).
  * **Non-Blocking:** When the response comes back later, a callback function is executed to handle the result.

### 3\. AJAX Working Flow (Using Modern `fetch` API)

1.  **Trigger:** A user action (e.g., click) triggers a JavaScript function.
2.  **Request:** The JS function uses `fetch()` to send an HTTP request to the server in the background.
3.  **Concurrency:** The browser continues to render the page and respond to user input (non-blocking).
4.  **Server Processing:** The server processes the request and generates a response (usually JSON data).
5.  **Response Received:** The browser receives the response. The `fetch` promise is resolved.
6.  **Data Handling:** JavaScript processes the data (e.g., converts JSON into a JS object).
7.  **DOM Manipulation:** JS uses the data to update a specific element on the page (e.g., a comments section, a weather forecast) using DOM methods like `innerHTML` or `textContent`. **Crucially, the rest of the page remains untouched.**
