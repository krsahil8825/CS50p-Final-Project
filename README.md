# Billing.py

## Video Demo: [YouTube](https://youtu.be/-xUuBLr7_YY)

## Description:

- ### Project Idea: To Create simple CLI program to create bill's (CS50 Shop bills)

- ### What your project is and does

    **`Billing.py`** is a python **CLI** program help to create bill `pdf`.

    - When user execute the program menu will appear.

    - It have two option `Create Bill` or `exit`.

    - if user choose `Create Bill` then user will redirected to create bill function. Else If user choose exit then program close else user will prompted again for input.

    - After choosing `Create Bill` user can add "item name", "item price", "item quantity" and "total price" of each item i.e. `price x quantity` and "total payable amount" will be calculated dynamically.

    - If any error occur due to user input then user prompted a new menu new option menu where he have option to "exit the program", "reset the that row data", "get prompt of input again"

    - when user choose he don't want to add more product to bill he simply choose that option that option menu will appear just after adding each product. It user choose `y` yes then user need to add new bill items in that specific bill if user type any other character than `y` or `yes` then program will exit and pdf will be generated in same level directory where `project.py` is present.

- ### Project Structure
    ```bash
    project/
        |
        |___ project.py # it contain source code of program
        |
        |___ test_project.py # it contain test source code of project.py
        |
        |___ requirements.txt # it contain library info that is used in the project
        |
        |____README.md # it contains description of project
        |
        |___bill.pdf # it contains bill info and it over write again and again
    ```

- ### Python Library Used in Project

    - `fpdf`: It is a python library used to generate pdf using python code. Basically it provide some pre defined code and programmer can import these classes in order to use it functionality

    - `pytest`: It is a python library used to test our python code (function) i.e. Pytest provide some pre defined code and tools to test our program is it working properly or not

- ### Design Choices
    - Program is CLI Base UI (it is simple to use). I have use color to display different text in Command Line interface.

    - I have use Functions Rather than Class (OPPs) because i think my program is in just one file and do not too much feature so i used functions it decrease complexity and increase readability for small programs

    - I used fpdf python library to generate my pdf. I kept pdf as simple black and white theme

- ### Challenges Faced

    - I face problem while writing code for how to create table when i found this one more problem occur how to fix the coloum width for each cell ass needed and make table at center but i came up with idea to divide each column in equal parts as per page width and i use this in my code it is simple and almost centered my table.

    - I face problems while writing my test code because my function return value on the basic of input. I am searching for how to write test for this this type of function finally i found a random post on stackover flow i used that program after some error trial i wrote the code of my test function successfully.

## Author Info
- Name: Kumar Sahil
- GitHub: https://github.com/krsahil8825
- EdX Username: krsahil8825
- City & Country: Patna, Bihar, India
