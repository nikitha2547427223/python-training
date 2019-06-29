{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "file is created successfully and data is written\n"
     ]
    }
   ],
   "source": [
    "def createfile(filename):\n",
    "    f=open(filename,\"w\")\n",
    "    for i in range(10):\n",
    "        f.write(\"this is %d line\\n\"% i)\n",
    "    print(\"file is created successfully and data is written\")\n",
    "    f.close()\n",
    "    return\n",
    "createfile(\"file1.txt\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def lowercasecount(filename):\n",
    "    cntlower=0\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=list(x)\n",
    "    for i in lst:\n",
    "        if i.islower():\n",
    "            cntlower+=1\n",
    "    return cntlower\n",
    "lowercasecount(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this 10\n",
      "is 10\n",
      "0 1\n",
      "line 10\n",
      "1 1\n",
      "2 1\n",
      "3 1\n",
      "4 1\n",
      "5 1\n",
      "6 1\n",
      "7 1\n",
      "8 1\n",
      "9 1\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import re \n",
    "def splcharacter(filename):\n",
    "    f = open(\"file1.txt\", \"r\") \n",
    "    wordcount={}\n",
    "    for word in f.read().split():\n",
    "        if word not in wordcount:\n",
    "            wordcount[word] = 1\n",
    "        else:\n",
    "            wordcount[word] += 1\n",
    "    for k,v in wordcount.items():\n",
    "        print(k, v)\n",
    "    return\n",
    "print(splcharacter(\"file1.txt\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is 0 line\n",
      "this is 1 line\n",
      "this is 2 line\n",
      "this is 3 line\n",
      "this is 4 line\n",
      "this is 5 line\n",
      "this is 6 line\n",
      "this is 7 line\n",
      "this is 8 line\n",
      "this is 9 line\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def readfile(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        print(x)\n",
    "    f.close()\n",
    "    return\n",
    "readfile(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def lowercasecount(filename):\n",
    "    cntlower=0\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=list(x)\n",
    "    for i in lst:\n",
    "        if i.islower():\n",
    "            cntlower+=1\n",
    "    return cntlower\n",
    "lowercasecount(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number of digits is:\n",
      "0\n",
      "The number of characters is:\n",
      "10\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def countofdigits(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    count1=0\n",
    "    count2=0\n",
    "    for i in f:\n",
    "        if(i.isdigit()):\n",
    "            count1=count1+1\n",
    "        count2=count2+1\n",
    "    print(\"The number of digits is:\")\n",
    "    print(count1)\n",
    "    print(\"The number of characters is:\")\n",
    "    print(count2)\n",
    "    return\n",
    "print(countofdigits(\"file1.txt\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
