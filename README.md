# Saige

Saige: A Python utility library and tool for deep exploration and understanding of large document sets and source code, making them accessible to an AI (Large Language Model) like those provided by OpenAI, for insightful analysis.

## Features

- **Interface to a Large Language Model (LLM)**: Saige serves as the primary, and ideally only, interface to such a system.
- **Support for multiple document types**: Saige supports at least PDF and text files out of the box. The library is designed to be extensible, allowing for support of additional document types such as Word or Excel without needing to modify the core Saige library.
- **Support for local and cloud-based vector data storage**: Saige supports a local storage mechanism for vector data (such as plain files or CSV) for debugging purposes, as well as at least one cloud-based vector database. The library is designed to be extensible, allowing for support of additional vector databases without needing to modify the core Saige library.
- **Usable within Jupyter or comparable notebooks**: Saige is implemented in Python and can be used within Jupyter or comparable notebooks.
- **CLI tool with two modes**: When used as a CLI tool, Saige can run in two modes: a batch command mode for indexing documents and storing vectors in the database, and a simple REPL mode for ad-hoc chat sessions with the LLM about the local data-set.
- **Fully configurable**: Whether used as a library or a CLI tool, Saige is fully configurable, allowing for customization of the data set, API key, vector database, and type of LLM.

![Saige: A Python utility library and tool for deep exploration and understanding of large document sets and source code](saige.png)

## Use Case: Understanding an Opaque Software System

Imagine you're a software engineer who has just joined a new team, and you're tasked with maintaining and enhancing a complex, legacy software system. The system is vast and somewhat opaque, with documentation scattered across various sources and the source code itself being dense and difficult to navigate. This is where Saige comes into play.

First, you would gather all available documentation related to the software system. This could include design documents, user manuals, API documentation, and more. You would also gather all the source code of the software system.

Next, you would use Saige's CLI tool in batch command mode to index all the gathered documents and source code. This process involves converting the text data into vector representations that can be understood by the LLM. These vectors are then stored in a database, which could be either local for debugging purposes or cloud-based for scalability and accessibility.

With the vectors stored in the database, you can now use Saige's CLI tool in REPL mode to have ad-hoc chat sessions with the LLM about the software system. You can ask questions about specific parts of the system, request explanations of complex code segments, or seek guidance on how to implement new features. The LLM, powered by the vector data, can provide insightful responses based on the comprehensive knowledge it has of the software system.

As you continue to work on the software system, you can keep updating the vector database with new documentation and code changes. This ensures that the LLM's knowledge stays up-to-date, allowing it to provide accurate and relevant responses.

By using Saige in this way, you can effectively open up and understand the opaque software system, making it easier to maintain and enhance over time.

## Installation

```bash
pip install saige
```

## Usage
```python
import saige
# code examples
```

## CLI Usage
```bash
saige --help
```

## Configuration
Detailed configuration instructions go here.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Copyright and license

Copyright © 2023 Iwan van der Kleijn

Licensed under the MIT License 
[MIT](https://choosealicense.com/licenses/mit/)




