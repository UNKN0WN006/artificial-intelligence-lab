# 🟩 CO4 — XML / XML Schema (CT-Pattern Based Answers)

> Pattern followed:

* Definition
* Clear rules
* Syntax
* Example
* Key terms highlighted (VERY important for marks)

---

## ✅ Q1. What is a *well-formed XML document*? State any **two rules**

*(2–4 marks)*

### ✔ Answer:

A **well-formed XML document** is an XML document that strictly follows the **XML syntax rules** defined by W3C, so that it can be correctly processed by an XML parser.

### **Rules (any two):**

1. XML must have **exactly one root element**
2. Every start tag must have a **matching end tag**
3. XML tags are **case-sensitive**
4. Elements must be **properly nested**

### ✔ Example:

```xml
<book>
  <title>XML Basics</title>
</book>
```

📌 *Keywords to underline in exam:*
**XML parser, syntax rules, root element, properly nested**

---

## ✅ Q2. What is **DTD**? Differentiate between **Internal DTD** and **External DTD** with syntax

*(4–6 marks)*

### ✔ Answer:

**DTD (Document Type Definition)** defines the **structure, elements, attributes, and entities** of an XML document.

It ensures that the XML document is **valid**.

---

### 🔸 Internal DTD

* Defined **inside the XML document**
* Used for **small documents**

**Syntax:**

```xml
<!DOCTYPE book [
  <!ELEMENT book (title, author)>
  <!ELEMENT title (#PCDATA)>
  <!ELEMENT author (#PCDATA)>
]>
```

---

### 🔸 External DTD

* Defined in a **separate .dtd file**
* Used for **large or reusable documents**

**Syntax:**

```xml
<!DOCTYPE book SYSTEM "book.dtd">
```

---

### 📊 Difference Table (Very High-Scoring)

| Internal DTD            | External DTD            |
| ----------------------- | ----------------------- |
| Inside XML file         | Separate DTD file       |
| Not reusable            | Reusable                |
| Suitable for small docs | Suitable for large docs |

---

## ✅ Q3. What is **XML Schema (XSD)**? How is it better than DTD?

*(4–8 marks – VERY IMPORTANT)*

### ✔ Answer:

**XML Schema (XSD)** is a **W3C-recommended language** used to define the **structure, data types, and constraints** of an XML document.

---

### 🔥 Advantages over DTD:

1. Supports **data types** (int, string, date)
2. Written in **XML syntax**
3. Supports **namespaces**
4. Better validation and extensibility

---

### ✔ Example:

```xml
<xs:element name="price" type="xs:decimal"/>
```

📌 *Underline:*
**data types, namespaces, validation**

---

## ✅ Q4. Create a simple XML document and validate it using XML Schema

*(6–8 marks)*

### ✔ XML Document:

```xml
<book>
  <title>Web Tech</title>
  <price>450</price>
</book>
```

---

### ✔ XML Schema (XSD):

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="book">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="title" type="xs:string"/>
        <xs:element name="price" type="xs:integer"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

📌 *Mention in exam:*

> “The XML document is valid as it follows the schema.”

---

## ✅ Q5. Difference between **Well-formed XML** and **Valid XML**

*(4 marks)*

| Well-Formed XML        | Valid XML           |
| ---------------------- | ------------------- |
| Follows syntax rules   | Follows DTD/XSD     |
| No validation required | Validation required |
| Mandatory              | Optional            |
| Parser checks          | Validator checks    |

---

## ✅ Q6. Short Notes (2–3 marks each)

### 🔹 Namespace

Used to avoid **name conflicts** in XML.

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
```

---

### 🔹 Simple Type vs Complex Type

* **Simple Type**: No child elements
* **Complex Type**: Contains child elements or attributes

---

## 🧠 HOW TO SCORE FULL MARKS IN CO4

✔ Always write:

* **Definition**
* **Syntax**
* **One example**
* **Underline keywords**

✔ For long answers:

* Add **difference table**
* Mention **why it is used**
* Use **proper indentation**

Just say the word 👌
