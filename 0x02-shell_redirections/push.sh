#!/bin/bash

echo "What is the commit message?"
read commitMessage


git status 
git add .
git status
git commit -m commitMessage
git push origin master

