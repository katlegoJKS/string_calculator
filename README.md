STRING-CALCULATOR


INTRODUCTION

For raw project instructions see: https://umuzi-org.github.io/tech-department/projects/tdd/string-calculator/


REQUIREMENTS

Prerequisites: simple-calculator part 1 

This project requires the following modules:

pytest==4.6.11


INSTALLATION

Install the following modules from your terminal or visit their respective websites, for further assistance and information.

~$ pip install pytest

or visit: https://docs.pytest.org/en/stable/getting-started.html

NB! Make sure to Install these modules in your virtual environment. Check versions of modules to ensure they have been installed.


CONFIGURATION

After installations are completed, and have created a directory, do the following:

Make sure to work inside your virtual environment at all times. This is so that, your modules are recognised and will not be lost when working on a new terminal.

Your project is expected to be completed using pytest.


INSTRUCTIONS

Please note that this project should be done in a TDD manner.

    1. Create an add function that can handle up to two integers passed in as a string.
            
            add("")
            // should return 0

            add("1")
            // should return 1

            add("1,1")
            // should return 2

    2. Modify the add function to handle multiple integers.

            add("1,2,3,4")
            // should return 10

            add("")
            // should still return 0

            add("1")
            // should still return 1

            add("1,1")
            // should still return 2

        NB! As you keep adding more functionality to your code always make sure that the previous functionality you implemented still works flawlessly.
    
    3. Modify the add function so that it can handle new lines between integers.

            add("1\n2,3" )
            // should return 6

    4. Modify the add function so that it can handle different delimeters.

        Delimiters will be specified in the following manner:

        ”//[delimiter]\n[numbers…]”, the default delimiter will be in the beginning of the string just before a new line character (”\n”).For example:

            add("//;\n1;2")
            // should return 3

            add("//4\n142")
            // should return 3

        In the first case, the default delimiter is: “;”.

        In the second case, the default delimiter is: “4”.

    5. Modify the add function so that it can handle negative integers.

        If a negative number is passed into the add function it should throw this exception: "negatives not allowed"

        The exception should contain a list of all the negative integers that were passed into the add function.

        For example:

            add("-1,-2,3,4")
            // should throw the following:
                'ERROR: negatives not allowed -1,-2'

    6. Modify the add function so that it ignores integers greater than or equal to 1000.

            add("//;\n1000;1;2")
            // should return 3

    7. Modify the add function so that it can support delimiters of any length

        As long as the string passed in satisfies this format, “//[delimiter]\n[integers…]“, which was explained above. The add function should be able to handle it. For example:

            add("//***\n1***2***3")
            // should return 6

    8. Modify the add function so that it is able to support different delimiters of any length

        As long as the string passed into the add function follows this format, “//[delim1][delim2]\n[integers…]“, the add function should be able to handle it:

        For example:

            add("//[:D][%]\n1:D2%3")
            // should return 6

            add("//[***][%%%]\n1***2%%%3")
            // should return 6

            add("//[(-_-')][%]\n1(-_-')2%3")
            // should return 6

            add("//[abc][777][:(]\n1abc27773:(1")
            // should return 7

    9. Modify the add function so that it can handle invalid input.

        If the string passed in is invalid, your code should be able to detect this and throw an error.

        Hint: A valid string input follows these formats:

            - "integer,integer,integer" e.g "1,2" or "1,2,3,4"

            - "integer \n integer,integer e.g "1\n2,3"

            - "//delimiter \n integer delimiter integer" e.g "//;\n1;2"

            - "//[delimiter][delimiter]\n integer delimiter integer" e.g "//[\*][%]\n1\*2%3"

        If the string doesn’t abide by any of these formats, it should be considered invalid.

            add("//;\n1000;1;2;")
            // should throw the following:
                'ERROR: invalid input'

            add("   //;\n1000,1;2")
            // should throw the following:
                'ERROR: invalid input'

            add("1,2,3//;\n1000,1;2")
            // should throw the following:
                'ERROR: invalid input'


You are good to go.
