These detailed study notes cover all the Java Applet topics you requested, structured for clarity and easy review.

-----

# ☕ Java Applets: Detailed Study Notes

## 1\. Definition of Java Applet

  * A **Java Applet** is a small Java program that is designed to be embedded in an HTML web page and executed by a Java-enabled web browser or an Applet Viewer.
  * Applets were used to provide dynamic and interactive content on web pages.
  * They run on the client side, meaning the user's machine, which reduces the load on the web server.

## 2\. Features of Applet

  * **Platform Independent:** Applets are written in Java and compiled into bytecode, allowing them to run on any operating system (Windows, macOS, Linux, etc.) that has a Java Virtual Machine (JVM) installed in the browser.
  * **Web-Enabled:** They are embedded in HTML pages and run within the context of a web browser.
  * **Security Restricted (Sandbox Model):** Untrusted applets run in a restricted security environment (the "sandbox") to prevent them from damaging the user's system.
  * **No `main()` method:** Applets do not require a `main()` method for execution. Their lifecycle is managed by the browser's JVM.
  * **AWT/Swing Based:** They typically use the Abstract Window Toolkit (AWT) or Swing for creating a Graphical User Interface (GUI).

## 3\. Applet Architecture

The Applet architecture involves the following components:

1.  **Applet Class:** The core of the applet, which must extend the `java.applet.Applet` class (or `javax.swing.JApplet` for Swing).
2.  **Web Browser/Applet Viewer:** The container (or host) environment where the applet runs. It loads the applet's class file and manages its lifecycle.
3.  **Java Virtual Machine (JVM) / Java Plug-in:** The JVM within the browser or Applet Viewer is responsible for executing the Java bytecode and invoking the Applet lifecycle methods (`init()`, `start()`, `stop()`, `destroy()`, `paint()`).

## 4\. Applet Execution Environment

  * An Applet executes within the **Java Runtime Environment (JRE)** which is integrated into or accessed by the web browser or the dedicated **Applet Viewer** tool.
  * The browser's JVM loads the applet class file and initiates its execution, passing control through the defined lifecycle methods.
  * The browser provides the **Applet Context** (via the `AppletContext` interface), which allows the applet to interact with the environment, such as displaying messages in the browser status bar or accessing other applets on the same page.

## 5\. Applet Life Cycle: `init() → start() → paint() → stop() → destroy()`

The applet life cycle defines the path an applet takes from its creation to its termination. It is governed by five key methods, which are automatically invoked by the environment.

| Method | Invocation | Purpose |
| :--- | :--- | :--- |
| `init()` | Called **once** when the applet is first loaded. | Initialization, setting up UI, loading resources. (Equivalent to a constructor). |
| `start()`| Called after `init()`, and **every time** the applet becomes visible or resumes (e.g., when the user returns to the page). | Starting threads, animations, or other execution logic. |
| `paint(Graphics g)` | Called after `start()`, and **whenever** the applet needs to be redrawn (e.g., maximizing the window, repaint() call). | Drawing graphics, text, or components on the applet window. |
| `stop()` | Called **every time** the applet becomes invisible (e.g., user minimizes the window or navigates to another page). | Suspending threads or execution logic to save CPU cycles. |
| `destroy()` | Called **once** just before the applet is unloaded from memory. | Performing final cleanup, releasing system resources (closing files, database connections, etc.). |

## 6\. Applet vs Standalone Application

| Feature | Java Applet | Java Standalone Application |
| :--- | :--- | :--- |
| **Execution** | Runs within a **Web Browser** or **Applet Viewer**. | Runs independently on the **Operating System** with a JVM. |
| **Main Method** | **Does not** require a `main()` method. Execution is managed by lifecycle methods. | **Requires** a `main()` method as its entry point. |
| **Security** | Operates in a strict **"Sandbox"** model with heavy restrictions. | Generally has **full access** to the system resources (subject to OS permissions). |
| **Installation** | **No installation** required on the client machine (downloaded on demand). | Must be **installed** (or copied) on the client machine. |
| **Base Class** | Extends `java.applet.Applet` (or `JApplet`). | Typically uses `java.awt.Frame` or `javax.swing.JFrame` for GUI. |

## 7\. Applet Security (Sandbox Model)

The **Sandbox Model** is a security mechanism used by the JVM to run untrusted applets downloaded from the internet in a highly restricted environment. This is to protect the user's system from malicious code.

**Key Restrictions in Untrusted Applets:**

  * **File I/O:** Cannot read or write files on the client's local disk.
  * **Network Access:** Can only establish network connections back to the host server from which it was downloaded (the **CodeBase**).
  * **System Access:** Cannot run local programs, load libraries, or access system properties like environment variables.
  * **Creating Windows:** Untrusted applets typically cannot create top-level windows that do not carry a warning label.

## 8\. Event Handling in Applets

Applets use the Java **Delegation Event Model** for handling user interactions (like button clicks, mouse movements, keyboard input).

  * **Source:** The component (e.g., a button) that generates the event.
  * **Listener:** An object that implements a specific event interface (e.g., `ActionListener`, `MouseListener`) and is registered with the source to receive notifications.

**Typical Process:**

1.  Implement the appropriate Listener interface in your Applet class (or a separate class).
2.  Override the required event-handling method (e.g., `actionPerformed()` for button clicks).
3.  **Register** the listener with the source component using a method like `addActionListener()`.

## 9\. Graphics & Painting

  * All drawing operations in an applet are performed within the **`paint(Graphics g)`** method.
  * The `Graphics` object (`g`) passed to the method provides the **graphics context**, which is the tool used for drawing.
  * The coordinate system starts at **(0, 0)** in the upper-left corner of the applet's display area.

| Common `Graphics` Methods | Description |
| :--- | :--- |
| `g.drawString(String s, int x, int y)` | Draws a string at the specified coordinates. |
| `g.setColor(Color c)` | Sets the current foreground color for subsequent drawing. |
| `g.setFont(Font f)` | Sets the current font. |
| `g.drawRect(int x, int y, int w, int h)` | Draws a rectangle outline. |
| `g.fillRect(int x, int y, int w, int h)` | Draws a solid (filled) rectangle. |

## 10\. Embedding Applet in HTML

A Java applet is embedded into an HTML page using the **`<APPLET>`** tag (or the more modern, but less supported, `<OBJECT>` tag).

**Syntax (using `<APPLET>` tag):**

```html
<APPLET CODE="MyApplet.class" WIDTH="300" HEIGHT="200" CODEBASE="classes/" ALT="Applet could not load.">
    <PARAM NAME="greeting" VALUE="Hello World!">
    
    If the browser cannot run the applet, this text will appear.
</APPLET>
```

| Attribute | Description |
| :--- | :--- |
| `CODE` | Specifies the name of the applet's main class file (e.g., `MyApplet.class`). |
| `WIDTH` | Defines the width of the applet's display area in pixels. |
| `HEIGHT` | Defines the height of the applet's display area in pixels. |
| `CODEBASE` | (Optional) Specifies the directory (relative to the HTML file) where the applet's class files are located. Default is the same directory as the HTML file. |
| `ALT` | (Optional) Text displayed if the browser recognizes the `<APPLET>` tag but cannot run the applet. |
| `<PARAM>` | Used to pass values (parameters) from the HTML file to the applet. |

## 11\. Applet Basics: Parameters and Context

### Passing Parameters:

Applets can read parameters defined in the HTML file using the `<PARAM>` tag.

  * The HTML: `<PARAM NAME="speed" VALUE="5">`
  * The Java code to retrieve it:

<!-- end list -->

```java
String paramValue = getParameter("speed");
int animationSpeed = 5; // Default value

if (paramValue != null) {
    try {
        animationSpeed = Integer.parseInt(paramValue);
    } catch (NumberFormatException e) {
        // Handle error or use default
    }
}
```

### Applet Context (`AppletContext`)

The `AppletContext` interface provides a way for an applet to communicate with the browser environment. You get an instance of it using `getAppletContext()`.

  * **Key uses:**
      * Displaying a message in the browser's status window: `getAppletContext().showStatus("Loading data...");`
      * Opening a new web page in the browser: `getAppletContext().showDocument(url);`
      * Finding other applets on the same HTML page: `getAppletContext().getApplets();`

### CodeBase and DocumentBase

These two methods are used to determine the location of the applet and its containing HTML file.

| Method | Returns | Description |
| :--- | :--- | :--- |
| `getDocumentBase()` | `URL` | The URL of the **HTML file** that loaded the applet. |
| `getCodeBase()` | `URL` | The URL of the **directory** from which the applet's class file was loaded (specified by `CODEBASE`). |

## 12\. Write a Simple Applet Program

Here is a complete example of a simple Java Applet and the HTML file to run it.

### **`SimpleApplet.java`**

```java
import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Font;

/*
 * An applet to display "Hello Applet World!"
 */
public class SimpleApplet extends Applet {

    // A string variable to hold a parameter value
    private String message;

    // 1. Initialization: Called when the applet is first loaded
    public void init() {
        // Retrieve the 'greeting' parameter from the HTML
        message = getParameter("greeting");
        if (message == null) {
            message = "Hello Applet World!"; // Default message
        }
        
        // Set the background color
        setBackground(Color.lightGray);
    }

    // 2. Starting: Called after init() and every time the applet resumes
    public void start() {
        System.out.println("Applet started/resumed.");
    }

    // 3. Painting: Called to display output
    public void paint(Graphics g) {
        // Set the drawing color and font
        g.setColor(Color.BLUE);
        g.setFont(new Font("Arial", Font.BOLD, 20));
        
        // Draw the string (from the parameter) at position (50, 50)
        g.drawString(message, 50, 50);

        // Draw a simple rectangle
        g.drawRect(45, 25, 250, 40);
    }

    // 4. Stopping: Called when the applet is hidden or the user leaves the page
    public void stop() {
        System.out.println("Applet stopped.");
    }

    // 5. Destruction: Called when the applet is about to be unloaded
    public void destroy() {
        System.out.println("Applet destroyed/unloaded.");
    }
}
```

### **`SimpleApplet.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Java Applet Example</title>
</head>
<body>

    <h1>My First Java Applet</h1>

    <applet code="SimpleApplet.class" width="350" height="150">
        <param name="greeting" value="Welcome to Java Applets!">
        
        This text appears if the browser cannot display the applet.
    </applet>

</body>
</html>
```

### Steps to Run:

1.  Save the Java code as `SimpleApplet.java` and the HTML as `SimpleApplet.html` in the **same directory**.
2.  Compile the Java file: `javac SimpleApplet.java` (creates `SimpleApplet.class`).
3.  Run the applet using the Applet Viewer: `appletviewer SimpleApplet.html` (or load the HTML file in a Java-enabled web browser).


I can certainly provide detailed notes covering all the Java Applet topics you listed, focusing on the core concepts and their implementation.

-----

# ☕ Java Applet Core Concepts: Detailed Notes

## I. Applet Life Cycle

The Applet Life Cycle defines the sequence of method calls made by the browser's Java Virtual Machine (JVM) to manage the applet from loading to termination. All these methods are defined in the `java.applet.Applet` class.

| Method | Purpose | Invocation Timing |
| :--- | :--- | :--- |
| `public void init()` | **Initialization** | Called **once** when the applet is first loaded. Used for setting up the UI, loading initial resources, and processing HTML parameters. |
| `public void start()` | **Execution Start** | Called immediately after `init()`, and **every time** the applet becomes visible or resumes (e.g., when the user navigates back to the page). Used to start threads or animations. |
| `public void paint(Graphics g)` | **Display/Rendering**| Called after `start()`, and whenever the applet needs to be redrawn (e.g., window maximize, or explicit call to `repaint()`). Handles all output, graphics, and UI rendering. |
| `public void stop()` | **Execution Stop** | Called **every time** the applet becomes invisible (e.g., user minimizes the window or navigates to a new page). Used to pause threads and execution to conserve CPU. |
| `public void destroy()` | **Cleanup** | Called **once** just before the applet is unloaded from memory. Used to release system resources (like file handles or database connections). |

## II. Applet Basics: Embedding and Parameters

### A. Embedding an Applet

Applets are embedded into an HTML page using the `<applet>` tag.

  * **Syntax:**
    ```html
    <applet code="MyClass.class" width="300" height="200" codebase="classes/">
        </applet>
    ```
  * **Key Attributes:**
      * `code`: Specifies the name of the applet's main class file (e.g., `MyClass.class`).
      * `width`: The width of the applet display area in pixels.
      * `height`: The height of the applet display area in pixels.
      * `codebase`: (Optional) Specifies the directory relative to the HTML file where the class files are located.

### B. Passing and Retrieving Parameters (`getParameter()`)

The HTML `<param>` tag is used to pass user-defined configuration values to the applet from the web page.

1.  **HTML Side (Embedding):**

    ```html
    <applet code="ConfigApplet.class" width="100" height="100">
        <param name="message" value="Hello Applet User!">
        <param name="font_size" value="16">
    </applet>
    ```

2.  **Java Side (Retrieval):** The `getParameter(String name)` method, typically called in `init()`, is used to retrieve the value as a `String`.

    ```java
    public void init() {
        String msg = getParameter("message");
        if (msg == null) {
            msg = "Default Message";
        }
        
        // Parameter values must be converted if needed
        int size = 12;
        String sizeParam = getParameter("font_size");
        if (sizeParam != null) {
            try {
                size = Integer.parseInt(sizeParam);
            } catch (NumberFormatException e) {
                // Handle error
            }
        }
    }
    ```

## III. Event Handling and UI Interactions

Applets use the **Delegation Event Model** (DEM) to handle user interactions like mouse clicks, key presses, or button pushes.

  * **Source:** The component (e.g., a button) that generates the event.
  * **Event:** An object that describes the user interaction (e.g., `ActionEvent`, `MouseEvent`).
  * **Listener:** An object that implements a specific interface and waits for the event.

**Steps for Event Handling (e.g., a Button Click):**

1.  **Create/Instantiate** the GUI component (the Source):
    ```java
    Button b = new Button("Click Me");
    add(b); // Add to the applet
    ```
2.  **Implement** the appropriate Listener Interface (`ActionListener` for buttons) in the applet class.
3.  **Override** the required event method (`actionPerformed()`):
    ```java
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == b) {
            System.out.println("Button clicked!");
        }
    }
    ```
4.  **Register** the Listener with the Source:
    ```java
    b.addActionListener(this); // 'this' refers to the applet class instance
    ```

## IV. Basic Graphics and Painting

All rendering and drawing in an Applet must occur within the `paint(Graphics g)` method.

  * The `Graphics` object (`g`) is the device-context tool used for drawing shapes, text, and images.
  * The coordinate system starts at **(0, 0)** in the top-left corner of the applet area.

**Key `Graphics` Methods:**

| Method | Purpose | Example |
| :--- | :--- | :--- |
| `g.setColor(Color c)` | Sets the drawing color. | `g.setColor(Color.RED);` |
| `g.setFont(Font f)` | Sets the font for subsequent text. | `g.setFont(new Font("Serif", Font.BOLD, 18));` |
| `g.drawString(String s, int x, int y)` | Draws text at the specified coordinates. | `g.drawString("Java", 20, 40);` |
| `g.drawRect(x, y, w, h)` | Draws an outline rectangle. | `g.drawRect(10, 50, 80, 50);` |
| `g.fillRect(x, y, w, h)` | Draws a solid (filled) rectangle. | `g.fillRect(100, 50, 80, 50);` |

**Note on Repainting:** You never call `paint()` directly. To force the applet to redraw itself, you call the `repaint()` method, which schedules a call to the `update()` method, which in turn calls `paint()`.

## V. Context and Security Restrictions

### A. Applet Context, CodeBase, and DocumentBase

The `AppletContext` interface provides the applet with access to the browser environment where it is running.

| Method | Class | Return Value | Description |
| :--- | :--- | :--- | :--- |
| `getAppletContext()` | `Applet` | `AppletContext` | Returns the context of the applet container (browser/viewer). |
| `showStatus(String msg)`| `AppletContext` | `void` | Displays a message in the browser's status window. |
| `showDocument(URL u)` | `AppletContext` | `void` | Requests the browser to display a new web page. |
| `getCodeBase()` | `Applet` | `URL` | The **URL of the directory** from which the applet's class file was loaded. |
| `getDocumentBase()` | `Applet` | `URL` | The **URL of the HTML page** that loaded the applet. |

### B. Security Restrictions (Sandbox Model)

Untrusted applets downloaded from the internet run in a highly restricted **Sandbox Security Model** to prevent malicious code from harming the client machine.

| Restricted Action | Reason/Impact |
| :--- | :--- |
| **Local File I/O** | Cannot read, write, or delete files on the client's hard drive. |
| **System Properties** | Cannot access system properties or environment variables (e.g., user name, OS version). |
| **Network Connections** | Can only connect back to the **CodeBase** host (the server it came from). Cannot connect to third-party servers. |
| **Executable Calls** | Cannot run local programs, load local libraries, or execute system commands. |
| **Thread Control** | Cannot modify or create thread groups outside of its own execution group. |

These restrictions ensure that an untrusted applet can only interact with its own environment and the server it was downloaded from.

-----

## Given Notes:

I can provide detailed study notes based on the uploaded document, covering all the key aspects of Java Applets.

***

# ☕ Java Applets: Comprehensive Study Notes

## 1. Overview and Key Characteristics

[cite_start]A Java Applet is a Java program designed to be executed within a web-based environment[cite: 2]. [cite_start]Applets are embedded inside HTML documents and run by a Java-enabled browser or an applet viewer[cite: 3]. [cite_start]They were widely used for interactive web content, such as simulations, animations, and visual tools[cite: 9].

### Key Characteristics:
* [cite_start]**Client-side execution**[cite: 5].
* [cite_start]**Platform-independent**[cite: 6].
* [cite_start]**Event-driven and GUI-oriented**[cite: 7].
* [cite_start]Execution is **controlled** via the browser environment[cite: 8].

## 2. Applet Architecture and Execution Environment

[cite_start]The applet runs within an execution environment managed by the browser or Applet Viewer[cite: 31, 34]. 
### Components Involved:
* [cite_start]**HTML Page:** Embeds the applet using the `<applet>` tag[cite: 30].
* [cite_start]**Browser/Applet Viewer:** Loads and manages the applet[cite: 31, 35].
* [cite_start]**Java Virtual Machine (JVM):** Executes the applet's bytecode[cite: 32].
* [cite_start]**Applet Class:** Contains the applet's specific logic[cite: 33].

[cite_start]The browser controls applet loading, method invocation, and security enforcement[cite: 35, 36, 37].

## 3. Applet Life Cycle: `init()`, `start()`, `paint()`, `stop()`, `destroy()`

[cite_start]The applet's life cycle is managed by the execution environment and consists of well-defined phases[cite: 53]. 
### Conceptual Flow:
* [cite_start]Loaded $\rightarrow$ Initialized $\rightarrow$ Started $\rightarrow$ Painted $\rightarrow$ Stopped $\rightarrow$ Destroyed[cite: 72].

| Life Cycle Phase | Corresponding Method | Conceptual Flow | Purpose |
| :--- | :--- | :--- | :--- |
| **Initialization** | [cite_start]`init()` [cite: 39, 49] | [cite_start]Born State [cite: 40] | [cite_start]Memory allocation, reading parameters, and resource setup[cite: 56, 58, 60]. Called once when the applet is first loaded. |
| **Running/Idle** | [cite_start]`start()` $\leftrightarrow$ `stop()` [cite: 41, 42] | [cite_start]Running State $\leftrightarrow$ Idle State [cite: 44, 45] | [cite_start]Applet becomes active and executes continuously while visible[cite: 62, 63]. `start()` is called on resuming, and `stop()` is called when the applet becomes invisible. |
| **Painting** | [cite_start]`paint()` [cite: 47, 51] | Triggered from Running State | [cite_start]Responsible for rendering text and graphics[cite: 65]. [cite_start]Automatically triggered when display updates are required[cite: 66]. |
| **Termination** | [cite_start]`destroy()` [cite: 43, 52] | [cite_start]Idle State $\rightarrow$ Dead State [cite: 45, 46] | [cite_start]Resources are released, and the applet is removed from memory[cite: 69, 70]. Called once when the applet is being unloaded. |

## 4. Applet Security Model (Sandbox)

[cite_start]The Applet Sandbox is a security mechanism that protects users by ensuring that downloaded applets cannot compromise the host system[cite: 307, 314]. 
### Sandbox Restrictions:
* [cite_start]**No direct file system access**[cite: 310]. [cite_start]Applets cannot read from or write to files in the local computer[cite: 165, 167].
* [cite_start]**Limited network communication**[cite: 311]. [cite_start]Applets cannot communicate with other servers on the network (typically only back to the origin server)[cite: 172, 174].
* [cite_start]**No execution of local programs**[cite: 312]. [cite_start]Applets cannot run any program from the local computer[cite: 177, 178].
* [cite_start]**Controlled access** to system properties[cite: 313].
* [cite_start]Applets can only write to a **sandboxed area** within the computer's memory[cite: 288, 289].

## 5. Applets vs Standalone Java Applications

| Aspect | [cite_start]Applet [cite: 183] | [cite_start]Standalone Application [cite: 184] |
| :--- | :--- | :--- |
| **Execution** | [cite_start]Browser-controlled [cite: 186][cite_start]; cannot run independently[cite: 158, 159]. | [cite_start]OS-controlled [cite: 186][cite_start]; can run independently[cite: 160, 162]. |
| **Entry Point** | [cite_start]Life-cycle methods (`init()`)[cite: 187, 180]. | [cite_start]`main()` method[cite: 187, 180]. |
| **File I/O** | [cite_start]Cannot read from or write to files in local computer[cite: 165, 167]. | [cite_start]Can read from or write to files in local computer[cite: 166, 168]. |
| **Security** | [cite_start]Restricted (Sandbox)[cite: 189]. | [cite_start]Full access (subject to OS permissions)[cite: 190]. |
| **Deployment** | [cite_start]Embedded in HTML [cite: 193][cite_start]; part of a web page[cite: 180]. | [cite_start]Executed directly [cite: 193][cite_start]; standalone application[cite: 180]. |

## 6. Embedding and Parameter Passing

### Embedding Applets:
[cite_start]Applets are embedded using the HTML `<applet>` tag[cite: 130]. [cite_start]The tag specifies attributes such as `code` (the main class file), `width`, and `height`[cite: 117].

### Parameter Passing:
[cite_start]Applets can receive external values from HTML using the `<param>` tag[cite: 149].

* [cite_start]Parameters are passed as **name-value pairs** defined inside the HTML[cite: 151, 152].
* [cite_start]They are read during the **initialization** phase (i.e., inside `init()`)[cite: 153].
* [cite_start]Retrieval is done using the `getParameter("name")` method[cite: 115].
* [cite_start]This mechanism enables dynamic behavior without recompilation, allowing applets to adapt to page-level configuration[cite: 154, 155].

## 7. Applet Context, CodeBase, and DocumentBase

### AppletContext
[cite_start]The `AppletContext` interface provides communication between an applet and its environment (the browser or Applet Viewer)[cite: 233].

**Capabilities:**
* [cite_start]Interacting with other applets[cite: 235].
* [cite_start]Displaying browser status messages[cite: 236].
* [cite_start]Opening URLs or documents[cite: 237].
* [cite_start]Loading shared resources[cite: 238].

### CodeBase and DocumentBase
[cite_start]These are resource location concepts[cite: 268]:
* [cite_start]**CodeBase:** The location (URL) of the **compiled applet files**[cite: 269].
* [cite_start]**DocumentBase:** The location (URL) of the **embedding HTML page**[cite: 270].

[cite_start]These references are essential for loading images, reading files, and resolving relative paths, ensuring portability[cite: 271, 272, 273, 274, 275].

## 8. Event Handling in Applets

[cite_start]Applets respond to user interactions using the **Event Delegation Model**[cite: 348]. 
### Event Flow:
1.  [cite_start]**User performs an action** (e.g., button click)[cite: 350].
2.  [cite_start]**Event source** (the component) generates an **event object**[cite: 319, 325, 351].
3.  [cite_start]The **Listener object**, which implements a specific **Listener interface**, receives the event[cite: 320, 322, 352].
4.  [cite_start]A corresponding **handler method** (e.g., `actionPerformed()`) processes the event[cite: 353].

[cite_start]This model promotes loose coupling, better modularity, and cleaner program structure[cite: 355, 356, 357].

## 9. Graphics and Painting Mechanism

[cite_start]Applet graphics rely on the **Abstract Window Toolkit (AWT)**[cite: 87].

### Graphics Features:
* [cite_start]Drawing shapes (lines, rectangles, ovals)[cite: 89].
* [cite_start]Rendering text[cite: 90].
* [cite_start]Displaying images[cite: 91].
* [cite_start]Automatic **repainting** on resize or refresh[cite: 92].

[cite_start]Graphics rendering is **system-triggered** and **event-driven**[cite: 94, 95]. [cite_start]The `paint(Graphics g)` method is responsible for rendering text and graphics and is automatically triggered when display updates are required[cite: 65, 66].

### GUI Components:
Applets are based on AWT components. [cite_start]The `Applet` class is a subclass of `Panel`, which is a subclass of `Container`[cite: 371, 368, 366]. [cite_start] Common components include buttons, labels, text fields, and panels[cite: 388, 389, 390, 391].
