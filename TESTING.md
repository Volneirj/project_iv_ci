# Table of Contents

- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
- [Responsiveness and Device Testing](#responsiveness-and-device-testing)
- [Browser Testing](#browser-testing)
- [Lighthouse Testing](#lighthouse-testing)
- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)


## Lighthouse Testing

Lighthouse validation was run on all pages (both mobile and desktop) in order to check performance, accessibility, best practices and CEO.

## Automated Testing

To achieve a robust and reliable application, a comprehensive testing strategy was implemented, combining both manual and automated methods. Leveraging Django's built-in testing framework, automated tests were meticulously developed to cover critical functionalities, including views and forms.

Each test was directly tied to specific user stories, ensuring that the application not only met technical requirements but also aligned with user needs and expectations. This approach provided thorough coverage, verifying that the application behaves as expected under various scenarios and that all features deliver the intended user experience.

To run the tests, I executed the following command in the terminal:

`python3 manage.py test`

Total Count of Automated Tests: 41

![screenshot](static/images/readme_images/testing/screen-terminal.jpg)  

To create the coverage report, I run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

Below are the reports on automated tests.