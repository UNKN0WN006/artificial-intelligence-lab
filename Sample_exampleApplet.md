That's a great idea\! Seeing the concepts in code helps solidify the understanding.

Here is a complete example of a Java Applet program that demonstrates:

1.  **Life Cycle Methods** (via console output).
2.  **Parameter Retrieval** (`getParameter()`).
3.  **UI Interaction/Event Handling** (a Button).
4.  **Basic Graphics** (`paint()` method).

## 💻 Applet Example Program

### 1\. Java Source Code: `InteractionApplet.java`

This applet includes a button and updates a message based on the button clicks.

```java
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

/*
 * An applet demonstrating the lifecycle, parameters, 
 * event handling, and graphics.
 */
public class InteractionApplet extends Applet implements ActionListener {

    // UI Component
    private Button clickButton;
    
    // State Variables
    private int clickCount = 0;
    private String initialMessage;

    // --- 1. LIFE CYCLE METHOD: init() ---
    public void init() {
        System.out.println("--- Applet Life Cycle: init() called ---");
        
        // 1. Parameter Retrieval
        initialMessage = getParameter("Title");
        if (initialMessage == null) {
            initialMessage = "Click the Button Below";
        }

        // 2. UI Setup and Event Registration
        clickButton = new Button("Click Me!");
        
        // Register 'this' (the Applet) as the ActionListener for the button
        clickButton.addActionListener(this); 

        // Add the button to the Applet container
        add(clickButton); 
        
        // Set the background color
        setBackground(Color.cyan);
    }

    // --- 2. LIFE CYCLE METHOD: start() ---
    public void start() {
        System.out.println("--- Applet Life Cycle: start() called ---");
        // Often used to restart threads or animations
    }

    // --- 3. PAINTING METHOD: paint() ---
    public void paint(Graphics g) {
        // g is the Graphics context for drawing

        // 1. Draw Graphics/Text
        g.setColor(Color.BLUE);
        g.setFont(new Font("Arial", Font.BOLD, 18));
        
        // Display the initial parameter message
        g.drawString("Param Title: " + initialMessage, 20, 40);

        // Display the dynamic click count
        g.setColor(Color.RED);
        g.drawString("Clicks: " + clickCount, 20, 70);
        
        // 2. Simple Drawing
        g.setColor(Color.GREEN.darker());
        g.drawOval(10, 100, 150, 50); // Draw an oval
    }

    // --- 4. EVENT HANDLING METHOD: actionPerformed() ---
    // This is called when the registered event (button click) occurs
    public void actionPerformed(ActionEvent e) {
        // Check if the event source is our button
        if (e.getSource() == clickButton) {
            clickCount++;
            System.out.println("Button Clicked! Count: " + clickCount);
            
            // Forces the applet to call update() -> paint() to redraw the screen
            repaint(); 
        }
    }

    // --- 5. LIFE CYCLE METHOD: stop() ---
    public void stop() {
        System.out.println("--- Applet Life Cycle: stop() called ---");
        // Used to pause threads when the applet is not visible
    }

    // --- 6. LIFE CYCLE METHOD: destroy() ---
    public void destroy() {
        System.out.println("--- Applet Life Cycle: destroy() called ---");
        // Used to clean up resources
    }
}
```

### 2\. HTML Embedding File: `runApplet.html`

This file embeds the applet and passes a parameter to it.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Applet Interaction Demo</title>
</head>
<body>

    <h1>Java Applet Demonstration</h1>
    <p>Watch the console output for the lifecycle messages!</p>

    <applet code="InteractionApplet.class" width="300" height="200">
        <param name="Title" value="My Applet Interaction Demo">
        
        If you see this, your browser does not support Java Applets.
    </applet>

</body>
</html>
```

### 3\. Execution Steps

1.  **Save and Compile:** Save the Java code as `InteractionApplet.java` and the HTML code as `runApplet.html` in the **same directory**.
2.  **Compile:** Open a command prompt/terminal and run:
    ```bash
    javac InteractionApplet.java
    ```
    This creates the `InteractionApplet.class` file.
3.  **Run with Applet Viewer:** Use the utility to run the applet (as browsers no longer natively support them):
    ```bash
    appletviewer runApplet.html
    ```

### 4\. What You Will Observe

| Action | Result in Applet Window | Result in Console/Terminal | Concepts Demonstrated |
| :--- | :--- | :--- | :--- |
| **Applet Loads** | The background is Cyan. The text "Param Title: My Applet Interaction Demo" and the button are visible. | `init()` called, followed by `start()` called. | Life Cycle & Parameter Retrieval |
| **Click the Button** | The "Clicks: **0**" text immediately updates to "Clicks: **1**" (and so on). | "Button Clicked\! Count: 1" is printed. | Event Handling (`actionPerformed`) & Graphics Update (`repaint`) |
| **Close the Viewer**| Applet window closes. | `stop()` called, followed by `destroy()` called. | Life Cycle Termination |

This example demonstrates how all the core components—the automatic life cycle, passing configuration via parameters, handling user input, and updating the display—work together in a functional applet.
