# VIL-MASYS 
## Virtual Library Management System

Welcome to VIL-MASYS, the Virtual Library Management System designed to streamline the management of libraries by providing a robust, user-friendly platform. Whether you are a librarian or a book lover, VIL-MASYS is built to enhance your library experience by bringing all the essential functionalities online.

[Link to VIL-MASYS - Virtual Library Management System](https://librarysystem-4f4e1e02f356.herokuapp.com/)
![responsive](documentation/readme_images/features/responsive.jpg)

# Table of Contents

- [Project Overview](#project-overview)
  - [Purpose](#purpose)
  - [Existing Features](#existing-features)
- [Technical Design](#technical-design)
  - [WireFrames](#wireframes)
  - [Models Relationships](#models-relationships)
- [Technologies](#technologies)
- [Main Used Libraries](#main-used-libraries)
- [Testing and Fixing Bugs](#testing-and-fixing-bugs)
- [Deployment](#deployment)
  - [GitHub Forking](#github-forking)
  - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)

## Project Overview

### Purpose:

This project serves as an educational resource, demonstrating the application of Python development skills in building a comprehensive web-based book issuance system. The project showcases how Django can be leveraged to create a scalable and interactive application, with a focus on user experience, data management, and thorough testing. In general, this project exemplifies how Python, Django, Bootstrap, and Cloudinary can be combined to build a functional, secure, and visually appealing web application.

### Existing Features

#### Navigation bar

- The Navigation bar is customized for the three types of logins: Administrator, Registered user, and non-registered users.
        <details><summary>Administrator Navbar</summary><img src="documentation/readme_images/features/menu-adm.jpg"></details>
        <details><summary>Normal User NavBar</summary><img src="documentation/readme_images/features/menu-normal-user.jpg"></details>
        <details><summary>Not Logged-in NavBar</summary><img src="documentation/readme_images/features/menu-no-user.jpg"></details>

#### Main Page - Top 3 Books

- The "3 Most Issued Books" section enhances user engagement by showcasing popular titles and guiding users toward trending books, while also promoting the circulation of these frequently borrowed items.
        <details><summary>Top 5 Issued Books</summary><img src="documentation/readme_images/features/top-issued-books.jpg"></details>

#### Main Page - Website Introduction Features

- The "Why issue with us" section highlights the benefits of using the booking system on this online platform. 
- The "How to issue a book" section shows new users how simple it is to issue a book on our platform.
- The button to join the library, shown after the features are explained, encourages users to join the website.
        <details><summary>Main Page Features Introduction</summary><img src="documentation/readme_images/features/features.jpg"></details>

#### About Page

- The About page provides an overview of VIL-MASYS, our Virtual Library Management System, highlighting its purpose and key features.
        <details><summary>About Page</summary><img src="documentation/readme_images/features/about.jpg"></details>

#### Sign up/Login page

- Simple, quick signup.
        <details><summary>Signup</summary><img src="documentation/readme_images/features/signup.jpg"></details>

- The Login Page has a button to the signup page in case the person is not yet a user.
        <details><summary>Login</summary><img src="documentation/readme_images/features/login.jpg"></details>

#### Book Suggestions Forms

- Open the Suggestion book page in case anyone wants to suggest new books. 
        <details><summary>Book Suggestion Form</summary><img src="documentation/readme_images/features/suggest-book.jpg"></details>

- Thank you submission page.
        <details><summary>Thank you page</summary><img src="documentation/readme_images/features/suggest-book-thanks.jpg"></details>

- Easy and clean admin interface to view the book suggestions.
        <details><summary>Admin Interface</summary><img src="documentation/readme_images/features/suggest-book-adm.jpg"></details>

#### Book Issuance System

- Easy issuance when you click on a book cover, you will be directed to book details where, if logged in, it will show the option to book it; otherwise, it will show the login button.
        <details><summary>Book Detail No User</summary><img src="documentation/readme_images/features/book-detail-nouser.jpg"></details>
        <details><summary>Book Detail User Connected</summary><img src="documentation/readme_images/features/book-detail-user.jpg"></details>

- Confirmation screen showing the details of your issuance.
        <details><summary>Issuance Details</summary><img src="documentation/readme_images/features/issue-book-screen.jpg"></details>

- You can see your history and return the books on the My Issued Books Link on the Navigation bar.
        <details><summary>My Issued Books</summary><img src="documentation/readme_images/features/issued-book-history.jpg"></details>

- When returning a book, as a good practice, it has a confirmation.
        <details><summary>Return Book Confirmation</summary><img src="documentation/readme_images/features/returning-book-confirmation.jpg"></details>
        <details><summary>Book Return Notification</summary><img src="documentation/readme_images/features/book-return-notify.jpg"></details>

#### Book Collection

- The book collection has a search bar to search a title and shows the book cover and book name for easy visualization.
        <details><summary>Book Collection</summary><img src="documentation/readme_images/features/bookcolection.jpg"></details>

- When logged in as an admin, it shows the option at the top to add new books.
        <details><summary>Admin Book Collection Interface</summary><img src="documentation/readme_images/features/add-book.jpg"></details>

#### Administrator CRUD Function

- As a web administrator, it is possible to add, update, or delete books.
    - Adding a book:
        1. On the Book Collection page as an Administrator, a button labeled "Add book" will be shown.
                <details><summary>Add a book</summary><img src="documentation/readme_images/features/add-book.jpg"></details>
        2. The link will bring you to a page where you can fill out the form to add a book.
                <details><summary>Add a book form</summary><img src="documentation/readme_images/features/book-add-2.jpg"></details>
        3. If a book cover is not loaded, it will automatically add a placeholder image saying "Book image not available."
                <details><summary>Book Image not Available</summary><img src="documentation/readme_images/features/book-image-notavailable.jpg"></details>
- As a web administrator, when on book details, the buttons to update and delete the book will be visible.
            <details><summary>CRUD Options</summary><img src="documentation/readme_images/features/CRUD-edit-delete.jpg"></details>
    - Updating a book:
        1. Click on "Edit book."
        2. The "Update Book" page will open where you can change all book information.
                <details><summary>Update Book</summary><img src="documentation/readme_images/features/CRUD-edit.jpg"></details>
    - Deleting a book:
        1. Click on "Delete book."
        2. You will be directed to a deletion page for confirmation.
                <details><summary>Delete Book</summary><img src="documentation/readme_images/features/CRUD-delete.jpg"></details>

#### Footer with Social Media Links  

- The footer has social media links that open in a new page.
            <details><summary>Footer</summary><img src="documentation/readme_images/features/footer.jpg"></details>

#### Error Pages.

- Page not found 404.
        <details><summary>404 page</summary><img src="documentation/readme_images/features/404.jpg"></details>

- Internal Server Error 500 .
        <details><summary>500 page</summary><img src="documentation/readme_images/features/500.jpg"></details>        



#### Extra Functions

- Late fee function: If the book is not returned in 14 days, a $1 fee will be applied for each day of delay.
        <details><summary>Late Fee</summary><img src="documentation/readme_images/features/late-fee.jpg"></details>
- You cannot issue two copies of the same title at once.
        <details><summary>Book Already Issued Notification</summary><img src="documentation/readme_images/features/notification-book-already-issued.jpg"></details>
- You can only issue 3 books at once.
        <details><summary>Max Issue Notification</summary><img src="documentation/readme_images/features/max-issue.jpg"></details>
- Book out of stock.
        <details><summary>Book Out of Stock Notification</summary><img src="documentation/readme_images/features/out-of-stock.jpg"></details>

## Technical Design

### WireFrames

- When the VIL-MASYS project began, I created basic wireframes to outline the initial design and functionality of the application. These wireframes served as a starting point to visualize the core structure and user flow. However, as development progressed, significant changes were made to improve the user experience, functionality, and overall design.

- Initial WireFrame Design:
        <details><summary>Home</summary><img src="documentation/readme_images/wireframes/home.jpg"></details>
        <details><summary>Book Info</summary><img src="documentation/readme_images/wireframes/book-info.jpg"></details>
        <details><summary>Login</summary><img src="documentation/readme_images/wireframes/login.jpg"></details>
        <details><summary>Issued Book</summary><img src="documentation/readme_images/wireframes/issue-book-page.jpg"></details>
        <details><summary>About</summary><img src="documentation/readme_images/wireframes/about.jpg"></details>

- Key Changes:
    - Enhanced User Interface: The initial wireframes were simple and lacked the visual appeal needed for a modern web application. As the project evolved, I introduced a more polished and intuitive interface, incorporating feedback and best practices in UI/UX design.

    - Expanded Features: Originally, the wireframes focused on basic functionalities. During development, new features were added, such as personalized book recommendations, late fees, notifications, and advanced search capabilities, which were not part of the initial plan.

    - Improved Navigation and Layout: The initial wireframes had a straightforward but somewhat limited navigation structure. I restructured the layout to provide a more seamless and logical flow, making it easier for users to navigate between different sections of the application.

### Models Relationships

- Key Relationships:
    1. Book and IssuedBook Relationship
        - Relationship Type: One-to-Many (ForeignKey)
            Explanation:
            - The Book model represents each book in the library's collection.
            - The IssuedBook model keeps track of each instance where a book is issued to a user.
            - A single Book can be issued multiple times, hence the one-to-many relationship. This is implemented using a ForeignKey in the IssuedBook model that references the Book model.
            - The related_name='issued_books' allows you to access all issued records for a particular book using book.issued_books.all().
    2. User and IssuedBook Relationship
        - Relationship Type: One-to-Many (ForeignKey)
            Explanation:
            - The User model (from Django’s built-in authentication system) represents the users of the library system.
            - Each user can issue multiple books over time. Therefore, there is a one-to-many relationship between User and IssuedBook.
            - The ForeignKey in the IssuedBook model links each issued book to the specific user who has borrowed it.
            - The related_name='issued_books' allows you to retrieve all the books issued by a particular user using user.issued_books.all().
    3. BookSuggestion Model
    - Standalone Entity:
            - The BookSuggestion model is independent of the Book and IssuedBook models. It captures suggestions for new books that users want to see in the library.
            - This model contains information about the suggested book's title and author, as well as optional fields for the user’s name, email, and reason for suggesting the book.
            - While this model is not directly related to the Book or User models through foreign keys, it plays an important role in allowing users to contribute to the library’s growth.

    <details><summary>Relations</summary><img src="documentation/readme_images/relation.jpg"></details>

## Technologies

### Backend and Frameworks:

- **Python:** Core programming language used for the project.
- **Django:** Web framework for building the application's backend, handling models, views, and forms.
- **Django ORM:** For database interactions and queries.

### Frontend:

- **HTML/CSS:** For structuring and styling the web pages.
- **Bootstrap:** CSS framework for responsive design and UI components like the navbar and forms.

### Database:

- **SQLite:** Default database used by Django for development/tests.
- **PostgreSQL**:  Database for production.

### Storage:

-  **Cloudinary:** For managing and storing media files such as images.

### User Authentication:
- **Django's Authentication System:** For handling user registration, login, and permissions.

### Testing:
- **Django Test Framework:** For unit and integration testing of models, views, and forms.
- **Unittest:** Python's standard library for writing and running tests.

- **Visual Studio Code:** Local IDE.

### Tools and Utilities:
- **Git:** Version control system for tracking changes and collaborating.
- **GitHub:**  Platform for hosting the project repository.

### Deployment:
- **Heroku:** Cloud Deployment.

### Others:
- **Timezone and Date/Time Handling:** Managing timezones and datetime objects for accurate timestamps.
- **Coverage:** Generate automated test reports.

## Main used Libraries

- **Django:** The main web framework used to build your application.
- **Django Rest Framework (DRF):** for building APIs.
- **Bootstrap:** For frontend styling and responsive design.
- **Pillow:** For image handling in Django.
- **Cloudinary:** For storing and serving media files (images) in the cloud.
- **Unittest:** For writing and running tests in Django application.
- **Django Messages Framework:** For displaying flash messages to users.
- **Django Paginator:** For handling pagination in your views.
- **PostgreSQL:** As the database backend.
- **Django Crispy Forms:** To make Django forms more elegant and manageable.
- **Gunicorn:** As a Python WSGI HTTP Server for serving your application.
- **Whitenoise:** For serving static files in production.
- **Django Storage:** For managing storage in cloud environments.

## Testing and Fixing Bugs

### Debugging 

  - For debugging the python code, `print` statements were used together with debugging tools and console logs to help identify bugs, loops, and condition interactions. 

  **Debugging Tools**

   - [CI Python Linter - Code Institute](https://pep8ci.herokuapp.com/)  
   - [OpenAI Chat](https://chat.openai.com/)
   - [Perplexity AI](https://www.perplexity.ai/) 

## Testing 

- The page of tests can be found at the link below:
        [Project Test documentation](TESTING.md)

## Deployment

### Github Forking

- **Forking the GitHub Repository**
  - If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

  1. Find the relevant GitHub repository
  2. In the top right corner of the page, click the Fork button (under your account)
  3. Your repository has now been 'Forked' and you have a copy to work on

- **Cloning the GitHub Repository**
  - Cloning your repository will allow you to download a local version of the repository to work on. Cloning can also be a great way to backup your work.

  1. Find the relevant GitHub repository
  2. Press the arrow on the Code button
  3. Copy the link that is shown in the drop-down
  4. Open the terminal 
  5. Move to the folder where you want to clone it
  6. In the terminal type `git clone` and then paste the link you copied in GitHub
  7. Press enter and your local clone will be created.

- Live link: [GitHub Link](https://github.com/Volneirj/project_iv_ci)

### Heroku Deployment

- **Creating Requirements.txt**
    - For Heroku to be able to install the required dependencies, it is necessary to create a file where the needed dependencies are listed.

    1. Create a file named `requirements.txt`.
    2. Run the command: `pip3 freeze >requirements.txt`.
    3. Check if the file has been updated, as shown in the image below.

![Requirements.txt](documentation/readme_images/general_info/requirements.jpg)

- **Creating an Application with Heroku**
    - To deploy and run the application on the Heroku platform, it is necessary to follow a few steps:

    1. Login or create an account on the Heroku website.
    2. Click on "Create a new app."

![New app](documentation/readme_images/general_info/create-new-app.jpg)

3. After creating the new app, you need to configure the settings.
4. The first setting that needs to be done is to add your environment info to the platform so it will be able to access outside sources.

![Settings CREDS](documentation/readme_images/general_info/creds.jpg)

5. Add the Buildpacks necessary to run the application, in this case, Python and Node.js in this sequence.

![Buildpacks](documentation/readme_images/general_info/buildpacks.jpg)

6. After completing the settings, move to the deploy tab where you will configure the deployment setup.
7. Connect your GitHub.
8. Select your repository on GitHub.
9. Connect to the repository.

![Github](documentation/readme_images/general_info/github.jpg)

10. After all the settings above have been done, you can select to deploy automatically or manually.

![Deploy](documentation/readme_images/general_info/deploy.jpg)

11. After pressing deploy, if all settings are correct, you should see it building the application.

![Project being Deployed](documentation/readme_images/general_info/deployed.jpg)

12. After all steps of deployment, a button labeled "View" will be shown, where you can click to open a new tab with the application.


![Deploy done](documentation/readme_images/general_info/done.jpg)


## Credits

**Mentor:** [Harry Dhillon](https://github.com/Harry-Leepz/)

**Base template:** [Code Instutute: I Think Therefore I Blog](https://github.com/Code-Institute-Solutions/blog/)

**Book Covers:** Created Using [Canva](https://www.canva.com/)

**Book/Title Descriptions:** Generated with [ChatGPT](https://chatgpt.com/)