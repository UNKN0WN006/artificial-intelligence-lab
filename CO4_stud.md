# 📝 XML Study Notes

## 1\. Writing a Simple XML Document & XML Structure

XML (Extensible Markup Language) is a markup language designed to transport and store data. It is self-descriptive and has no predefined tags.

### Simple XML Document Structure

A basic XML document typically includes:

1.  **XML Declaration:** Specifies the XML version and character encoding.
2.  **Root Element:** The single, top-level element that encloses all other elements.
3.  **Other Elements and Attributes:** Data is stored within elements (tags) and attributes (name/value pairs inside start tags).

### Example: Simple XML Document (`book.xml`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book category="fiction">
        <title lang="en">The Great Novel</title>
        <author>J. Doe</author>
        <year>2023</year>
        <price>19.99</price>
    </book>
    <book category="nonfiction">
        <title lang="en">Data Structures 101</title>
        <author>A. Smith</author>
        <year>2022</year>
        <price>45.00</price>
    </book>
</bookstore>
```

-----

## 2\. Well-Formed XML

### Definition

A "Well-Formed" XML document adheres to the basic **syntactical rules** defined by the XML specification. If an XML document is not well-formed, it is simply **not considered XML**, and an XML parser will halt processing and report an error.

### Key Rules for Well-Formedness

| Rule | Example (Correct) | Example (Incorrect - Not Well-Formed) |
| :--- | :--- | :--- |
| **Single Root Element** | `<root>...</root>` | `<root1>...</root1><root2>...</root2>` (Two root elements) |
| **Proper Nesting** | `<A><B>text</B></A>` | `<A><B>text</A></B>` (Tags overlap) |
| **All Elements Closed** | `<element>...</element>` or `<element />` | `<element>...` (Missing closing tag) |
| **Case Sensitivity** | `<book>...</book>` | `<Book>...</book>` (Tags must match case) |
| **Quoted Attributes** | `<element attr="value">` | `<element attr=value>` (Attribute value not quoted) |
| **Reserved Character Escaping** | `&lt;` for `<` | `<text>` in content |
| **XML Declaration (Recommended)** | `<?xml version="1.0"?>` | (Missing declaration is technically allowed but discouraged) |

**Well-formed XML is a mandatory prerequisite for an XML document to be processed by a parser.**

-----

## 3\. Valid XML

### Definition

A "Valid" XML document is a document that is **Well-Formed** and also conforms to the rules specified in an associated **Schema** (like a DTD or XML Schema Definition (XSD)). The schema defines the document's structure, element names, permitted attributes, and the allowed sequence and nesting of elements.

### Requirement

To be valid, an XML document **must reference** an external definition (DTD or XSD) and then **comply with all its constraints**.

### Difference: Well-Formed vs. Valid (Summary Table)

| Feature | Well-Formed XML | Valid XML |
| :--- | :--- | :--- |
| **Syntax** | Follows all basic XML syntax rules. | Follows all basic XML syntax rules (must be well-formed first). |
| **Structure Rules** | Does NOT need an external schema definition. | **MUST** conform to a referenced DTD, XSD, or other schema. |
| **Processor Action** | An XML Parser can successfully read/parse the document. | A Validating Parser can successfully read/parse *and* verify structure/data types against the schema. |
| **Analogy** | Like writing a grammatically correct sentence. | Like writing a grammatically correct sentence that also follows the specific format rules of a report or letter. |

-----

## 4\. Document Type Definition (DTD)

### DTD Basics

A DTD is the oldest schema language for XML, inherited from SGML. It defines the legal building blocks of an XML document (elements and attributes).

### Writing a DTD for Given XML

To write a DTD, you need to declare the structure starting from the root element and moving down through its children.

**Given XML Example (Simple):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note date="2023-11-15">
    <to>George</to>
    <from>John</from>
    <heading>Reminder</heading>
    <body>Call the supplier.</body>
</note>
```

**Corresponding External DTD (`note.dtd`):**

```dtd
<!ELEMENT note (to, from, heading, body)> 
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>

<!ATTLIST note date CDATA #REQUIRED>
```

**Referencing the DTD (External Subset):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd"> 
<note date="2023-11-15">
    ... (content here) ...
</note>
```

### DTD Element Content Models

| Model | Description | Example |
| :--- | :--- | :--- |
| **`(#PCDATA)`** | Element can contain character data (text). | `<!ELEMENT name (#PCDATA)>` |
| **`EMPTY`** | Element can have no content (self-closing). | `<!ELEMENT img EMPTY>` |
| **`ANY`** | Element can contain any mix of elements or text. | `<!ELEMENT mixed ANY>` |
| **Sequence** | Elements must appear in a specific order. | `<!ELEMENT person (first_name, last_name)>` |
| **Choice** | Elements must contain one of the elements listed. | `<!ELEMENT address (street | po_box)>` |

**Occurrence Indicators:**

  * `?`: Zero or one occurrence.
  * `+`: One or more occurrences.
  * `*`: Zero or more occurrences.

-----

## 5\. XML Schema Definition (XSD)

### Definition

XSD is the successor to DTD. It is an XML-based schema language (written in XML itself), offering far greater power and control over document structure and data types.

### Key Advantages of XSD over DTD:

  * **Data Types:** Supports a rich set of built-in data types (string, integer, date, boolean, etc.) and allows complex type creation, which DTD lacks.
  * **Namespaces:** Fully supports XML Namespaces (DTD does not).
  * **XML Syntax:** Written in XML, allowing standard XML parsers and editors to process schemas.
  * **Extensibility:** Easier to extend and reuse schemas.

### XSD Basics (Elements, Attributes, Types, Restrictions)

An XSD defines the structure using tags like `<xs:element>`, `<xs:attribute>`, `<xs:simpleType>`, and `<xs:complexType>`.

  * **Elements and Attributes:** Declared using their respective tags.
      * `<xs:element name="title" type="xs:string"/>`
      * `<xs:attribute name="lang" type="xs:language"/>`
  * **Simple Types:** Define constraints on text-only elements/attributes (e.g., specifying that a value must be an integer or a date).
  * **Complex Types:** Define elements that contain other elements and/or attributes.
  * **Restrictions (Facets):** Used within simple types to limit the value space (e.g., `maxLength`, `minInclusive`, `pattern` for regex).

-----

## 6\. XSLT for Transformation & XQuery for Filtering

### XSLT (Extensible Stylesheet Language Transformations)

  * **Purpose:** To transform XML documents into other formats, such as HTML, plain text, or other XML structures.
  * **Mechanism:** Uses XPath to navigate the XML document and XSLT templates (using `<xsl:template>`) to define how the matched nodes should be output.
  * **Process:** An XSLT processor takes the source XML document and the XSLT stylesheet as input and produces a result tree (the transformed output).

**Example:** Transforming XML data into an HTML table.

### XQuery

  * **Purpose:** A query language designed to retrieve, filter, and sort data from XML documents or XML data sources.
  * **Mechanism:** Uses the **FLWOR** expression (For, Let, Where, Order by, Return), which is similar to SQL but tailored for tree-structured data.
  * **Usage:** Ideal for querying large volumes of XML data or performing complex joins/aggregations.

**Example (Filtering):** Find the titles of books published after 2022.

```xquery
for $book in /bookstore/book
where $book/year > 2022
return $book/title
```

-----

## 7\. XML Namespaces

### Purpose

The primary purpose of XML Namespaces is to **avoid naming conflicts** when combining XML documents or vocabularies from different sources.

Imagine two XML documents, one for furniture and one for biology, both using a `<table/>` element. A parser needs to know if it's a **furniture table** or a **data table**.

### Usage

Namespaces are identified by a **URI** (Uniform Resource Identifier), which acts as a unique name for the vocabulary.

1.  **Declaration:** Declared using the `xmlns` attribute, usually in the root element.
2.  **Prefix:** An optional prefix is used to qualify elements and attributes belonging to that namespace.

**Example:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root 
    xmlns:f="http://www.example.com/furniture"
    xmlns:d="http://www.example.com/data"> 
    
    <f:table> <leg>4</leg>
    </f:table>
    
    <d:table> <row>Header</row>
    </d:table>
</root>
```

  * The prefix (`f:` or `d:`) tells the parser which vocabulary (namespace) the element belongs to, preventing conflicts.

-----

## SUggestions Sheet:

Absolutely\! Here are detailed study notes on the XML topics you listed, presented in a structured Markdown format.

-----

# 📝 XML Study Notes

## 1\. Writing a Simple XML Document & XML Structure

XML (Extensible Markup Language) is a markup language designed to transport and store data. It is self-descriptive and has no predefined tags.

### Simple XML Document Structure

A basic XML document typically includes:

1.  **XML Declaration:** Specifies the XML version and character encoding.
2.  **Root Element:** The single, top-level element that encloses all other elements.
3.  **Other Elements and Attributes:** Data is stored within elements (tags) and attributes (name/value pairs inside start tags).

### Example: Simple XML Document (`book.xml`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book category="fiction">
        <title lang="en">The Great Novel</title>
        <author>J. Doe</author>
        <year>2023</year>
        <price>19.99</price>
    </book>
    <book category="nonfiction">
        <title lang="en">Data Structures 101</title>
        <author>A. Smith</author>
        <year>2022</year>
        <price>45.00</price>
    </book>
</bookstore>
```

-----

## 2\. Well-Formed XML

### Definition

A "Well-Formed" XML document adheres to the basic **syntactical rules** defined by the XML specification. If an XML document is not well-formed, it is simply **not considered XML**, and an XML parser will halt processing and report an error.

### Key Rules for Well-Formedness

| Rule | Example (Correct) | Example (Incorrect - Not Well-Formed) |
| :--- | :--- | :--- |
| **Single Root Element** | `<root>...</root>` | `<root1>...</root1><root2>...</root2>` (Two root elements) |
| **Proper Nesting** | `<A><B>text</B></A>` | `<A><B>text</A></B>` (Tags overlap) |
| **All Elements Closed** | `<element>...</element>` or `<element />` | `<element>...` (Missing closing tag) |
| **Case Sensitivity** | `<book>...</book>` | `<Book>...</book>` (Tags must match case) |
| **Quoted Attributes** | `<element attr="value">` | `<element attr=value>` (Attribute value not quoted) |
| **Reserved Character Escaping** | `&lt;` for `<` | `<text>` in content |
| **XML Declaration (Recommended)** | `<?xml version="1.0"?>` | (Missing declaration is technically allowed but discouraged) |

**Well-formed XML is a mandatory prerequisite for an XML document to be processed by a parser.**

-----

## 3\. Valid XML

### Definition

A "Valid" XML document is a document that is **Well-Formed** and also conforms to the rules specified in an associated **Schema** (like a DTD or XML Schema Definition (XSD)). The schema defines the document's structure, element names, permitted attributes, and the allowed sequence and nesting of elements.

### Requirement

To be valid, an XML document **must reference** an external definition (DTD or XSD) and then **comply with all its constraints**.

### Difference: Well-Formed vs. Valid (Summary Table)

| Feature | Well-Formed XML | Valid XML |
| :--- | :--- | :--- |
| **Syntax** | Follows all basic XML syntax rules. | Follows all basic XML syntax rules (must be well-formed first). |
| **Structure Rules** | Does NOT need an external schema definition. | **MUST** conform to a referenced DTD, XSD, or other schema. |
| **Processor Action** | An XML Parser can successfully read/parse the document. | A Validating Parser can successfully read/parse *and* verify structure/data types against the schema. |
| **Analogy** | Like writing a grammatically correct sentence. | Like writing a grammatically correct sentence that also follows the specific format rules of a report or letter. |

-----

## 4\. Document Type Definition (DTD)

### DTD Basics

A DTD is the oldest schema language for XML, inherited from SGML. It defines the legal building blocks of an XML document (elements and attributes).

### Writing a DTD for Given XML

To write a DTD, you need to declare the structure starting from the root element and moving down through its children.

**Given XML Example (Simple):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note date="2023-11-15">
    <to>George</to>
    <from>John</from>
    <heading>Reminder</heading>
    <body>Call the supplier.</body>
</note>
```

**Corresponding External DTD (`note.dtd`):**

```dtd
<!ELEMENT note (to, from, heading, body)> 
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>

<!ATTLIST note date CDATA #REQUIRED>
```

**Referencing the DTD (External Subset):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd"> 
<note date="2023-11-15">
    ... (content here) ...
</note>
```

### DTD Element Content Models

| Model | Description | Example |
| :--- | :--- | :--- |
| **`(#PCDATA)`** | Element can contain character data (text). | `<!ELEMENT name (#PCDATA)>` |
| **`EMPTY`** | Element can have no content (self-closing). | `<!ELEMENT img EMPTY>` |
| **`ANY`** | Element can contain any mix of elements or text. | `<!ELEMENT mixed ANY>` |
| **Sequence** | Elements must appear in a specific order. | `<!ELEMENT person (first_name, last_name)>` |
| **Choice** | Elements must contain one of the elements listed. | `<!ELEMENT address (street | po_box)>` |

**Occurrence Indicators:**

  * `?`: Zero or one occurrence.
  * `+`: One or more occurrences.
  * `*`: Zero or more occurrences.

-----

## 5\. XML Schema Definition (XSD)

### Definition

XSD is the successor to DTD. It is an XML-based schema language (written in XML itself), offering far greater power and control over document structure and data types.

### Key Advantages of XSD over DTD:

  * **Data Types:** Supports a rich set of built-in data types (string, integer, date, boolean, etc.) and allows complex type creation, which DTD lacks.
  * **Namespaces:** Fully supports XML Namespaces (DTD does not).
  * **XML Syntax:** Written in XML, allowing standard XML parsers and editors to process schemas.
  * **Extensibility:** Easier to extend and reuse schemas.

### XSD Basics (Elements, Attributes, Types, Restrictions)

An XSD defines the structure using tags like `<xs:element>`, `<xs:attribute>`, `<xs:simpleType>`, and `<xs:complexType>`.

  * **Elements and Attributes:** Declared using their respective tags.
      * `<xs:element name="title" type="xs:string"/>`
      * `<xs:attribute name="lang" type="xs:language"/>`
  * **Simple Types:** Define constraints on text-only elements/attributes (e.g., specifying that a value must be an integer or a date).
  * **Complex Types:** Define elements that contain other elements and/or attributes.
  * **Restrictions (Facets):** Used within simple types to limit the value space (e.g., `maxLength`, `minInclusive`, `pattern` for regex).

-----

## 6\. XSLT for Transformation & XQuery for Filtering

### XSLT (Extensible Stylesheet Language Transformations)

  * **Purpose:** To transform XML documents into other formats, such as HTML, plain text, or other XML structures.
  * **Mechanism:** Uses XPath to navigate the XML document and XSLT templates (using `<xsl:template>`) to define how the matched nodes should be output.
  * **Process:** An XSLT processor takes the source XML document and the XSLT stylesheet as input and produces a result tree (the transformed output).

**Example:** Transforming XML data into an HTML table.

### XQuery

  * **Purpose:** A query language designed to retrieve, filter, and sort data from XML documents or XML data sources.
  * **Mechanism:** Uses the **FLWOR** expression (For, Let, Where, Order by, Return), which is similar to SQL but tailored for tree-structured data.
  * **Usage:** Ideal for querying large volumes of XML data or performing complex joins/aggregations.

**Example (Filtering):** Find the titles of books published after 2022.

```xquery
for $book in /bookstore/book
where $book/year > 2022
return $book/title
```

-----

## 7\. XML Namespaces

### Purpose

The primary purpose of XML Namespaces is to **avoid naming conflicts** when combining XML documents or vocabularies from different sources.

Imagine two XML documents, one for furniture and one for biology, both using a `<table/>` element. A parser needs to know if it's a **furniture table** or a **data table**.

### Usage

Namespaces are identified by a **URI** (Uniform Resource Identifier), which acts as a unique name for the vocabulary.

1.  **Declaration:** Declared using the `xmlns` attribute, usually in the root element.
2.  **Prefix:** An optional prefix is used to qualify elements and attributes belonging to that namespace.

**Example:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root 
    xmlns:f="http://www.example.com/furniture"
    xmlns:d="http://www.example.com/data"> 
    
    <f:table> <leg>4</leg>
    </f:table>
    
    <d:table> <row>Header</row>
    </d:table>
</root>
```

  * The prefix (`f:` or `d:`) tells the parser which vocabulary (namespace) the element belongs to, preventing conflicts.

-----

## PYQ:

Based on the images you provided, here are the detailed solutions to the XML-related questions.

## Solutions to XML Questions

### 1\. XQuery Expressions (Based on Image `image_4fdce5.png`)

The partial XML snippet implies a structure likely involving a root element (`<store>`) containing multiple `<monitor>` elements. The key information is that the `<monitor>` element has a child `<size>` and `<resolution>`. To answer the queries, we must assume a slightly more complete structure, similar to the snippet provided in `image_4fdfa9.jpg` (which shows `<make>LG</make>`).

**Assumed XML Structure (For Context):**

```xml
<store>
    <monitor type="LED">
        <make>Samsung</make>
        <size>27</size>
        <resolution>1920x1080</resolution>
    </monitor>
    <monitor type="LCD">
        <make>Dell</make>
        <size>15</size>
        <resolution>1280x800</resolution>
    </monitor>
    </store>
```

#### i. Find manufacturers that manufacture LED monitors

We need to iterate through all `<monitor>` elements, filter those where the `type` attribute is 'LED', and return the content of the `<make>` element.

```xquery
for $m in /store/monitor
where $m/@type = "LED"
return $m/make
```

*(Alternative XQuery using path navigation for simplicity):*

```xquery
/store/monitor[@type="LED"]/make
```

#### ii. Sort monitors by their size.

We need to iterate through all `<monitor>` elements, use the `order by` clause on the numerical value of the `<size>` child element, and return the monitor element itself (or key identifying data).

```xquery
for $m in /store/monitor
order by xs:integer($m/size) ascending
return $m
```

*(Note: `xs:integer()` is used to ensure sorting is numerical, not alphabetical, as XML data is stored as string by default.)*

-----

### 2\. DTD and Schema Questions (Based on Image `image_4fdfea.jpg`)

#### (a) i. Compare and contrast DTD and Schema

| Feature | DTD (Document Type Definition) | XSD (XML Schema Definition) |
| :--- | :--- | :--- |
| **Syntax** | Non-XML (SGML-like). | XML-based (written using XML tags). |
| **Data Typing** | Limited to basic types (`CDATA`, `ID`, `IDREF`, etc.). **Cannot define custom types** or complex data constraints (e.g., date, integer range). | **Extensive built-in data types** (e.g., `xs:integer`, `xs:date`, `xs:boolean`) and supports **custom type definition**. |
| **Namespaces** | **Does not support** XML Namespaces. | **Fully supports** XML Namespaces. |
| **Extensibility**| Difficult to reuse and extend components. | Highly modular and extensible (can import/include other schemas). |
| **Validation** | Less robust for complex data validation. | **More robust**; supports facets (restrictions) like `min/maxLength`, `pattern` (regex), etc. |

#### (a) ii. Write a DTD for the Book scenario

**Scenario:** A book has exactly one title, one or more chapters, one or more authors, a price, and an ISBN number (attribute). An author has a first name, an optional middle name, and a last name. A chapter consists of one or more paragraphs.

```dtd
<!ELEMENT book (title, chapter+, author+, price)>
<!ATTLIST book isbn ID #REQUIRED>

<!ELEMENT title (#PCDATA)>
<!ELEMENT price (#PCDATA)>

<!ELEMENT chapter (paragraph+)>

<!ELEMENT paragraph (#PCDATA)>

<!ELEMENT author (first_name, middle_name?, last_name)>

<!ELEMENT first_name (#PCDATA)>
<!ELEMENT middle_name (#PCDATA)>
<!ELEMENT last_name (#PCDATA)>
```

#### (a) iii. Write schema declaration for the element `<payment>`

**Scenario:** `<payment>` has one `<payee>`, one `<mode>` tag. `<mode>` tag having either `<cash>` or `<cheque>` tag. The `<cheque>` tag (if appears) contains one mandatory `chequeNo` attribute. The `<payment>` element itself is the element being defined.

**Assumptions Made:**

1.  All elements (`payee`, `cash`, `cheque`) have simple string content (`xs:string`).
2.  The `chequeNo` attribute is also a simple string (`xs:string`).

<!-- end list -->

```xml
<xs:element name="payment">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="payee" type="xs:string"/>
            
            <xs:element name="mode">
                <xs:complexType>
                    <xs:choice>
                        <xs:element name="cash" type="xs:string"/> 
                        
                        <xs:element name="cheque">
                            <xs:complexType>
                                <xs:simpleContent>
                                    <xs:extension base="xs:string">
                                        <xs:attribute name="chequeNo" type="xs:string" use="required"/>
                                    </xs:extension>
                                </xs:simpleContent>
                            </xs:complexType>
                        </xs:element>
                    </xs:choice>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

-----

### 3\. XML Concepts and Schema Questions (Based on Image `image_4fdfea.jpg` and `image_4fdfa9.jpg` (b))

#### (b) i. Compare and contrast well-formed and valid XML documents

| Feature | Well-Formed XML | Valid XML |
| :--- | :--- | :--- |
| **Definition** | Adheres to the basic, fundamental XML syntax rules (e.g., proper nesting, closed tags, single root). | Adheres to the rules defined in an associated external schema (DTD or XSD). |
| **Requirement** | **Mandatory** for a document to be considered XML. | **Optional**; depends on whether a schema is referenced and required for the application. |
| **Check Type** | Purely **syntactic** check. | **Structural and semantic** check (data types, element order, occurrence). |
| **Processing** | An XML Parser can successfully read and parse the document tree. | A **Validating Parser** must be used to ensure compliance with the schema. |
| **Analogy** | A program that follows the compiler's syntax rules (no compiler errors). | A program that follows the compiler's syntax rules **AND** the design specifications (no logical/structural errors). |

#### (b) ii. What is the difference between `value-of` and `copy-of` in XSLT?

Both are XSLT instructions used to output content from the source XML to the result tree, but they handle the structure differently.

| Instruction | XSLT Code | What it Outputs (Result Tree) |
| :--- | :--- | :--- |
| **`<xsl:value-of select="XPath"/>`** | Outputs the **text content** (string value) of the node(s) selected by the XPath expression. | The result is a simple text node. It discards all structure, elements, and attributes of the selected node(s). |
| **`<xsl:copy-of select="XPath"/>`** | Outputs the **complete node set** (all sub-trees) selected by the XPath expression. | The result is a copy of the selected nodes, including all their descendant elements, attributes, and text content. |

**Example:**
If the source XML is `<data><price currency="USD">100</price></data>`:

  * `<xsl:value-of select="data/price"/>` outputs: **`100`** (just the text).
  * `<xsl:copy-of select="data/price"/>` outputs: **`<price currency="USD">100</price>`** (the entire node and its content).

#### (b) iii. Create a data type for the element `<HDD>` in Schema

**Scenario:** `<HDD>` must have a mandatory `speed` attribute, an optional `unit` attribute. The element content is a non-negative integer.

**XML Example:** `<HDD speed="7200" unit="rpm">100</HDD>`

```xml
<xs:element name="HDD">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="xs:nonNegativeInteger"> 
                
                <xs:attribute name="speed" type="xs:string" use="required"/>
                
                <xs:attribute name="unit" type="xs:string" use="optional"/>
                
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
```

-----

### 4\. XQuery Expressions (Based on Image `image_4fdfa9.jpg`)

The XML snippet shows the structure for the `<HDD>` element.

**Assumed XML Structure (For Context):**

```xml
<store>
    <HDD type="ATA">
        <make>Samsung</make>
        <capacity>80</capacity>
        <speed>7200</speed>
        <price>1500</price>
    </HDD>
    <HDD type="SATA">
        <make>WD</make>
        <capacity>160</capacity>
        <speed>5400</speed>
        <price>2500</price>
    </HDD>
    </store>
```

#### i. Find manufacturers that manufacture 160 GB HDD

We need to filter `<HDD>` elements where the `<capacity>` is 160 and return the content of the corresponding `<make>` element.

```xquery
for $h in /store/HDD
where $h/capacity = 160
return $h/make
```

*(Alternative XQuery using path navigation for simplicity):*

```xquery
/store/HDD[capacity=160]/make
```

#### ii. Sort HDDs by their prices.

We need to iterate through all `<HDD>` elements, use the `order by` clause on the numerical value of the `<price>` child element, and return the HDD element itself (or key identifying data).

```xquery
for $h in /store/HDD
order by xs:integer($h/price) ascending
return $h
```

*(Note: `xs:integer()` is used to ensure numerical sorting.)*
