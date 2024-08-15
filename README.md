# VIL-MASYS 
## Virtual Library Management System

Welcome to VIL-MASYS, the Virtual Library Management System designed to streamline the management of libraries by providing a robust, user-friendly platform. Whether you are a librarian or a book lover, VIL-MASYS is built to enhance your library experience by bringing all the essential functionalities online.

![Requirements.txt](static/media/readme_images/features/responsive.jpg)

[VIL-MASYS - Virtual Library Management System](https://librarysystem-4f4e1e02f356.herokuapp.com/)


## Project Overview

### Purpose:

This project serves as an educational resource, demonstrating the application of Python development skills in building a comprehensive web-based book issuance system. The project showcases how Django can be leveraged to create a scalable and interactive application, with a focus on user experience, data management, and thorough testing.In general this project exemplifies how Python, Django, Bootstrap, and Cloudinary can be combined to build a functional, secure, and visually appealing web application.

### Existing Features

#### Navigation bar

- The Navigation bar is customized for the three type of logins: Administrator, Registred user and no registered users.
        <details><summary>Administrator Navbar</summary><img src="static/media/readme_images/features/menu-adm.jpg"></details>
        <details><summary>Normal User NavBar</summary><img src="static/media/readme_images/features/menu-normal-user.jpg"></details>
        <details><summary>Not Logged-in NabBar</summary><img src="static/media/readme_images/features/menu-no-user.jpg"></details>


#### Main Page - Top 3 Books

- The "3 Most Issued Books" section enhances user engagement by showcasing popular titles and guiding users toward trending books, while also promoting the circulation of these frequently borrowed items.
        <details><summary>Top 5 Issued Books</summary><img src="static/media/readme_images/features/top-issued-books.jpg"></details>

#### Main Page - Website Introduction Features

- Why issue with us section brings the benefits of use the booking system in this online plataform. 
- How to issue a book, shows the new user how simple is to issue a book in our plataform.
- The button to join the library after the features explained is to encourage the user to join the website.
        <details><summary>Main Page Features Introduction</summary><img src="static/media/readme_images/features/features.jpg"></details>


#### About Page

- The About page provides an overview of VIL-MASYS, our Virtual Library Management System, highlighting its purpose and key features.
        <details><summary>About Page</summary><img src="static/media/readme_images/features/about.jpg"></details>

#### Sign up/Login page

- Simple quick signup.
        <details><summary>Signup</summary><img src="static/media/readme_images/features/signup.jpg"></details>

- Login Page has a button to signup page in case the person has not user yet.
        <details><summary>Login</summary><img src="static/media/readme_images/features/login.jpg"></details>

#### Book Suggestions Forms

- Open Suggestion book page, in case anyone want to suggest new books. 
        <details><summary>Book Suggestion Form</summary><img src="static/media/readme_images/features/suggest-book.jpg"></details>

- Thank you submition page.
        <details><summary>Thank you page</summary><img src="static/media/readme_images/features/suggest-book-thanks.jpg"></details>

- Easy and clean admin interface to see the book suggestions.
        <details><summary>Login</summary><img src="static/media/readme_images/features/suggest-book-adm.jpg"></details>

#### Book Issuance system

- Easy issuance when clicked in a book cover, you will be directed for book details where if logged will show the option to book it other wise will show the login button.
        <details><summary>Book Detail No user</summary><img src="static/media/readme_images/features/book-detail-nouser.jpg"></details>
        <details><summary>Book Detail user conected</summary><img src="static/media/readme_images/features/book-detail-user.jpg"></details>

- Confirmation screen showing the details of your issuance.
        <details><summary>Issuance Details</summary><img src="static/media/readme_images/features/issue-book-screen.jpg"></details>

- You can see your history and return the books on My issued Books Link on Navigation bar.
        <details><summary>My Issued Books</summary><img src="static/media/readme_images/features/issued-book-history.jpg"></details>

- When returned a book as good practice it has a confirmation. 
        <details><summary>Return Book Confirmation</summary><img src="static/media/readme_images/features/returning-book-confirmation.jpg"></details>
        <details><summary>Book Return Notification</summary><img src="static/media/readme_images/features/book-return-notify.jpg"></details>    


#### Book Collection

- The book collection has a search bar to search a title and shows the book cover and book name to easy visualization.
        <details><summary>Book Collection</summary><img src="static/media/readme_images/features/bookcolection.jpg"></details>

- When logged in with admin, shows the option on the top to add new books.
        <details><summary>Admin book collection interface</summary><img src="static/media/readme_images/features/add-book.jpg"></details>

#### Administrator CRUD Fucntion

- As web administrator is possible to add, update or delete books.
    - Adding a book:
        1. On book Collection page as Administrator will show a button Add book.
                <details><summary>Add a book</summary><img src="static/media/readme_images/features/add-book.jpg"></details>
        2. The link will bring you to a page where you can fill the form to add a book.
                <details><summary>Add a book form</summary><img src="static/media/readme_images/features/add-book-2.jpg"></details>
        3.  If not loaded a book cover, it automaticaly will add a placeholder image saying book image not available.
                <details><summary>Book Image not Available</summary><img src="static/media/readme_images/features/book-image-notavailable.jpg"></details>
- As web administrator when on book details will be visible the buttons to update and delete the book.
            <details><summary>CRUD options</summary><img src="static/media/readme_images/features/CRUD-edit-delete.jpg"></details>
    - Updating a book:
        1. Click on edit book.
        2. Will open the Update book page where you can change all book information.
                <details><summary>Update Book</summary><img src="static/media/readme_images/features/CRUD-edit.jpg"></details>
    - Deleting a book:
        1. Click on Delete book.
        2. You Will be directed to a deletion page confirmation.
                <details><summary>Delete Book</summary><img src="static/media/readme_images/features/CRUD-delete.jpg"></details>

#### Footer with social media.   

- Footer has the social media links opening in a new page.
            <details><summary>Footer</summary><img src="static/media/readme_images/features/footer.jpg"></details>

#### Extra Functions

- Late fee function, if the book is not returned in 14 days, will have a 1$ for every day delay.
        <details><summary>Late Fee</summary><img src="static/media/readme_images/features/late-fee.jpg"></details>
- You cannot issue 2 same title at once.
        <details><summary>Book already issued notification </summary><img src="static/media/readme_images/features/notification-book-already-issued.jpg"></details>
- You only can issue 3 books at once.
        <details><summary>Max issue notfication</summary><img src="static/media/readme_images/features/max-issue.jpg"></details>
- Book out of stock.
        <details><summary>Book out of stock notfication</summary><img src="static/media/readme_images/features/out-of-stock.jpg"></details>

## Technical Design

### WireFrames

- When the VIL-MASYS project began, I created basic wireframes to outline the initial design and functionality of the application. These wireframes served as a starting point to visualize the core structure and user flow. However, as development progressed, significant changes were made to improve the user experience, functionality, and overall design.

- Initial WireFrame Design:
        <details><summary>Home</summary><img src="static/media/readme_images/wireframes/home.jpg"></details>
        <details><summary>Book Info</summary><img src="static/media/readme_images/wireframes/book-info.jpg"></details>
        <details><summary>Login</summary><img src="static/media/readme_images/wireframes/login.jpg"></details>
        <details><summary>Issued Book</summary><img src="static/media/readme_images/wireframes/issue-book-page.jpg"></details>
        <details><summary>About</summary><img src="static/media/readme_images/wireframes/about.jpg"></details>

- Key Changes:
    - Enhanced User Interface: The initial wireframes were simple and lacked the visual appeal needed for a modern web application. As the project evolved, I introduced a more polished and intuitive interface, incorporating feedback and best practices in UI/UX design.

    - Expanded Features: Originally, the wireframes focused on basic functionalities. During development, new features were added, such as personalized book recommendations, late fee, notifications and advanced search capabilities, which were not part of the initial plan.

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

    <details><summary>Relations</summary><img src="static/media/readme_images/relation.jpg"></details>

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
- **Django Rest Framework (DRF)**: for building APIs.
- **Bootstrap:** For frontend styling and responsive design.
- **Pillow:** For image handling in Django.
- **Cloudinary:** For storing and serving media files (images) in the cloud.
- **Unittest:** For writing and running tests in  Django application.
- **Django Messages Framework:** For displaying flash messages to users.
- **Django Paginator:** For handling pagination in your views.
- **PostgreSQL:** As the database backend..
- **Django Crispy Forms:** To make Django forms more elegant and manageable.
- **Gunicorn:** As a Python WSGI HTTP Server for serving your application.
- **Whitenoise:** For serving static files in production.
- **Django Storage:** For managing storage in cloud environments.

## Testing and Fixing Bugs

### Debugging 

  - For debugging the python code has been used `print` together with debugging tools and the console logs to help identify bugs, loops, and condition interactions.. 

  **Debugging Tools**

   - [CI Python Linter - Code institute](https://pep8ci.herokuapp.com/)  
   - [OpenAI Chat](https://chat.openai.com/)
   - [Perplexity AI](https://www.perplexity.ai/) 


## Testing 

- The page of tests can be found in the link bellow.
    [Project Test documentation](TESTING.md) 

## Deployment

### Github Forking

- **Forking the GitHub Repository**
  - If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

  1. Find the relevant GitHub repository
  2. In the top right corner of the page, click the Fork button (under your account)
  3. Your repository has now been 'Forked' and you have a copy to work on

- **Cloning the GitHub Repository**
  - Cloning your repository will allow you to download a local version of the repository to be worked on. Cloning can also be a great way to backup your work.

  1. Find the relevant GitHub repository
  2. Press the arrow on the Code button
  3. Copy the link that is shown in the drop-down
  4. Open the terminal 
  5. Move to the folder you want clone it
  6. In the terminal type 'git clone' & then paste the link you copied in GitHub
  7. Press enter and your local clone will be created.
- Live link: [GitHub Link](https://github.com/Volneirj/project_iv_ci)

### Heroku Deployment

- **Creating Requirements.txt**
    - To heroku be able to install the required dependencies is necessary to create the file where will be listed what is needed to run the project.

    1. Create a file requirements.txt.
    2. Run the command: pip3 freeze >requirements.txt.
    3. Check if the file has been updated like the image bellow.

![Requirements.txt](static/media/readme_images/general_info/requirements.jpg)

- **Creating an Application with Heroku**
    - To be able to  deploy and run the application on heroku plataform, is necessary follow a few steps:

    1. Login or create an account on Heroku website.
    2. Click on create a new app.

![New app](static/media/readme_images/general_info/create-new-app.jpg)

3. After create the new app, you need to configure the settings.
4. The first setting which need to be done is add your enviroment info to the plataform so it will be able to access outside sources.

![Settings CREDS](static/media/readme_images/general_info/creds.jpg)

5. Add the Buildpacks necessary to run the application, in this case python and nodejs in this sequence.

![Buildpacks](static/media/readme_images/general_info/buildpacks.jpg)

6. After done the settings we move to the deploy tab where we will configure the deployment setup.
7. Connect your Github.
8. Select your repository on github.
9. Connect to the repository.

![Github](static/media/readme_images/general_info/github.jpg)

10. After all setting above been done you can select to deploy automatic or manual.

![Deploy](static/media/readme_images/general_info/deploy.jpg)

11. After press to deploy your project if all settings are working you should see it building the application.

![Project being Deployed](static/media/readme_images/general_info/deployed.jpg)

12. After all steps of deployment will show a button View, where you can click to open a new tab with the application.

![Deploy done](static/media/readme_images/general_info/done.jpg)


## Credits

