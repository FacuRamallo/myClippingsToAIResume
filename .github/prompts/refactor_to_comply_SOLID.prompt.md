---
mode: agent
---
As a senior software engineer I want you to read the code base and identify areas where the code can be refactored to comply with SOLID principles.

The use-case we are working on now is, to read a txt file from a specific directory, process its content to go from a raw .txt file to a dto object that wraps a list of strings, each string representing a clipping block between "============" sparator characters. Then, from the dto a mapper generate a dommain object Clippings that wraps a listo of Books.
 Once  we have the Clipping object: 
 1. 2 files are generated for each book in a predefined folder named MyClippings and each file with the name of the book plus the current date at the moment the file is created or overwritten. One file will be a .json file and the other will be a .md file.
 2. The content of each file is populated with the corresponding clippings for that book, formatted as a json object or Markdown.

 There are 3 layers in this project to achieve an hexagonal architecture:

 1. The **Domain Layer** contains the business logic and domain entities, such as `Clippings`, `Book`, and `Clipping`. This layer is responsible for managing the core functionality of the application.

 2. The **Application Layer** acts as a bridge between the domain layer and the external world. It contains use cases and application services that orchestrate the flow of data between the domain layer and the presentation layer. This layer is responsible for handling user input, coordinating tasks, and managing application state.

 3. The **Infrastructure Layer** provides technical capabilities and external integrations, such as file system access, database connections, and third-party APIs. This layer is responsible for implementing the details of how the application interacts with the outside world, while keeping the domain and application layers decoupled from specific technologies.

 Focus on the separation of concerns between these layers to ensure a clean architecture.

 Ask questions to clarify the requirements and constraints of each layer.

Propose a Domain model and relationships between entities. 
What interfaces should be created to separate infrastructure implementations from the domain and application layers?
