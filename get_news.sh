#/bin/bash

read -p 'Enter the keyword you want to get the news about that! ' keyword 

result=$(python3 news.py | grep $keyword) 

echo 'result is:' $result



