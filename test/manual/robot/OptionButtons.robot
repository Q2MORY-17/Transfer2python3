*** Settings ***
Documentation           Dronelauncher tests regarding options for the automatic use
Library                 SeleniumLibrary
Library                 Process
Library                 ./library/UrlLibrary.py
Resource                ./../../keywords/keywords.robot
Resource                ./../../keywords/SSRS3keywords.robot
Test Setup              Begin web test
Test Teardown           End web test

*** Variables ***
${BROWSER}              headlesschrome

*** Test Cases ***
Home Button
    [Documentation]                         Testing if the right function is called when pressing button
    [Tags]                                  HBtest
    Given Server Is Up
    When User Clicks Home Button
    Then Verify Function Is Called          app_home


Reset Enconders Button
    [Documentation]                         Testing if the right function is called when pressing button
    [Tags]                                  REtest
    Given Server Is Up
    When User Clicks Reset Encoders Button
    Then Verify Function Is Called          app_reset_encoders

Battery Voltage Button
    [Documentation]                         Testing if the right function is called when pressing button
    [Tags]                                  BVtest
    Given Server Is Up
    When User Clicks Battery Voltage Button
    Then Verify Function Is Called          app_battery_voltage

