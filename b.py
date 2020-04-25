# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:56:21 2020

@author: jaych
"""
import turtle

S=turtle.Turtle()
A=turtle.Screen()

A.title("window")

A.bgcolor("black")

S.color("green")
S.shape("turtle")
S.pensize(10)

F=0

while F<8:
    S.left(45)
    S.forward(100)
    F=F+1

turtle.done()