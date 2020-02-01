# ECE590_Project1

The first project requires the implementation of Continuous Delivery for a Flask Application on GCP.
The service is deployed on an app engine, and can accessed at following URL: https://ece590.appspot.com/

I have created an application called Interactive Dictionary.
The users can send a get request to server with the required word. The application returns an array of all meanings for that word.
Example: localhost/test will return the meaning of the word test. In case the application cannot find the entered word it will suggest possible words that would be similar to the entered word.
