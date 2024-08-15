# Table of Contents

- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
- [Responsiveness and Device Testing](#responsiveness-and-device-testing)
- [Browser Testing](#browser-testing)
- [Manual and Automated Testing](#manual-and-automated-testing) 
  - [Automated Testing](#automated-testing)
  - [Manual Testing](#manual-testing)
- [Bugs and Errors](#bugs-and-errors)

### HTML

All HTML pages were validated using the [W3C HTML Validator](https://validator.w3.org/). One error was identified on the Signup page, which will be discussed in the bugs and errors section.
| Page                                                                                                               | Result            |
| ------------------------------------------------------------------------------------------------------------------ | ----------------- |
| <details><summary>Home</summary><img src="documentation/readme_images/testing/html-check-home.jpg"></details>        | <mark>PASS</mark> |
| <details><summary>Book Collection</summary><img src="documentation/readme_images/testing/html-check-books.jpg"></details> | <mark>PASS</mark> |
| <details><summary>Book Detail</summary><img src="documentation/readme_images/testing/html-check-books-detail.jpg"></details> | <mark>PASS</mark> |
| <details><summary>Suggestion Form</summary><img src="documentation/readme_images/testing/html-check-books-suggestion-form.jpg"></details> | <mark>PASS</mark> |
| <details><summary>My Issued List</summary><img src="documentation/readme_images/testing/html-check-issues-list.jpg"></details> | <mark>PASS</mark> |
| <details><summary>View Suggestions</summary><img src="documentation/readme_images/testing/html-check-view-suggestions.jpg"></details> | <mark>PASS</mark> |
| <details><summary>Signup</summary><img src="documentation/readme_images/testing/html-check-signup.jpg"></details>    | <mark>Error</mark> |
| <details><summary>Login</summary><img src="documentation/readme_images/testing/html-check-login.jpg"></details>      | <mark>PASS</mark> |
| <details><summary>About</summary><img src="documentation/readme_images/testing/html-check-about.jpg"></details>      | <mark>PASS</mark> |
| <details><summary>Confirm Book Return</summary><img src="documentation/readme_images/testing/html-check-creturn-book.jpg"></details> | <mark>PASS</mark> |

### CSS

- Using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), the CSS code was checked for errors using the direct input option.

![screenshot](documentation/readme_images/testing/css-validation.jpg)  

### Python

- Using the [CI Python Linter - Code Institute](https://pep8ci.herokuapp.com/), the Python code was inspected and validated. All `.py` files were checked, and most issues found were related to missing or extra blank lines and long lines. All issues were fixed.

## Responsiveness and Device Testing

Throughout the development process, the website was rigorously tested across a range of devices, including desktops, laptops, smartphones, and tablets. This testing ensured that the website displayed correctly on screens of various sizes and orientations, both portrait and landscape. Additionally, the responsive design was validated using Google Chrome's developer tools to confirm that the layout remained structurally sound and adaptable across different screen dimensions. No issues were noted, affirming that the site functions as expected across diverse environments.

## Browser Testing

The website was tested across Google Chrome, Safari, and Microsoft Edge, and no issues were found.

## Manual and Automated Testing

To ensure thorough testing, organization, and control throughout the development process, all testing activities were meticulously aligned with the requirements and acceptance criteria outlined in the epic and related user stories. This structured approach allowed us to systematically cover every aspect of the application, ensuring comprehensive test coverage and alignment with project goals.

[Epic - Comprehensive Testing for Library Management System](https://github.com/Volneirj/project_iv_ci/issues/36)

### Automated Testing

To achieve a robust and reliable application, a comprehensive testing strategy was implemented, combining both manual and automated methods. Leveraging Django's built-in testing framework, automated tests were meticulously developed to cover critical functionalities, including views and forms.

Each test was directly tied to specific user stories, ensuring that the application not only met technical requirements but also aligned with user needs and expectations. This approach provided thorough coverage, verifying that the application behaves as expected under various scenarios and that all features deliver the intended user experience.

To run the tests, I executed the following command in the terminal:

`python3 manage.py test`

Total Count of Automated Tests: 41

![screenshot](documentation/readme_images/testing/screen-terminal.jpg)  

To create the coverage report, I ran the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

Below are the reports on automated tests.

| App    | Screenshot                                                                 | 
| ------ | -------------------------------------------------------------------------- | 
| Home   | ![screenshot](documentation/readme_images/testing/report-home.jpg)           |
| Books  | ![screenshot](documentation/readme_images/testing/report-books.jpg)          |
| Issues | ![screenshot](documentation/readme_images/testing/report-issues.jpg)         |
| Users  | ![screenshot](documentation/readme_images/testing/report-users.jpg)          |
| About  | ![screenshot](documentation/readme_images/testing/report-about.jpg)          |

### Manual Testing

A comprehensive manual testing process was conducted to address areas that automated tests could not cover. Every test has been documented in the user stories below, where they are meticulously organized by application and test type to ensure complete coverage and clarity.

[User Story 23 - Tests About Page](https://github.com/Volneirj/project_iv_ci/issues/23)

[User Story 27 - Comprehensive Manual Testing of Book Management Features](https://github.com/Volneirj/project_iv_ci/issues/27)

[User Story 28 - Test Home App](https://github.com/Volneirj/project_iv_ci/issues/28)

[User Story 30 - Manual Tests Issuing and Returning Books](https://github.com/Volneirj/project_iv_ci/issues/30)

[User Story 31 - Manual Testing URL Issues App](https://github.com/Volneirj/project_iv_ci/issues/31)

[User Story 34 - Manual Testing URL Users App](https://github.com/Volneirj/project_iv_ci/issues/34)

### Bugs and Errors

Two issues were identified during testing: one related to time zone handling in the model and another concerning HTML form validation on the sign-up page. The first bug involved a conflict when calculating the return date due to time zone differences, which has been successfully resolved. The second issue, stemming from Crispy Forms, affected form validation. 

The resolution for the time zone bug is detailed in the stories below.

[User Story 36 - Handle Timezone-Related Issues in Book Issuance](https://github.com/Volneirj/project_iv_ci/issues/32)

Regarding the HTML validation error, I have chosen to leave it as is since it does not impact the application's functionality and is caused by Crispy Forms. Below, you can see the error encountered during validation testing with the [W3C HTML Validator](https://validator.w3.org/). The second image highlights the specific line where the error occurs, identified through page inspection.

![HTML check signup](documentation/readme_images/testing/html-check-signup.jpg)

![Signup error location HTML file](documentation/readme_images/testing/html-check-signup-error.jpg)
