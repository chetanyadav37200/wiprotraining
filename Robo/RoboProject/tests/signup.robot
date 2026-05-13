*** Settings ***
Resource    ../resources/keywords/signup_keywords.robot

*** Test Cases ***
Verify User Can Signup Successfully
    Launch Demoblaze Application
    Click Signup Link
    Enter Username
    Enter Password
    Click Register Button
    Verify Signup Success Alert
    Close Application