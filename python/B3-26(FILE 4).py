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
    "createfile(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
   "execution_count": 3,
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
    "        f.write(\"Test %d line\\n\"% i)\n",
    "    print(\"file is created successfully and data is written\")\n",
    "    f.close()\n",
    "    return\n",
    "createfile(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Test 0 line\n",
      "Test 1 line\n",
      "Test 2 line\n",
      "Test 3 line\n",
      "Test 4 line\n",
      "Test 5 line\n",
      "Test 6 line\n",
      "Test 7 line\n",
      "Test 8 line\n",
      "Test 9 line\n",
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
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "foo={1:'1',2:'2',3:\"3\"}\n",
    "del foo[1]\n",
    "foo[1]='10'\n",
    "del foo[2]\n",
    "print(len(foo))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "def dataanalysiswordcount(filename,word):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=x.split()\n",
    "    cnt=lst.count(word)\n",
    "    return cnt\n",
    "print(dataanalysiswordcount(\"file1.txt\",\"rest\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "def countcharacter(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=list(x)\n",
    "    return len(lst)\n",
    "print(countcharacter(\"file1.txt\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def uppercasecount(filename):\n",
    "    cntupper=0\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=list(x)\n",
    "    for i in lst:\n",
    "        if i.isupper():\n",
    "            cntupper+=1\n",
    "    return cntupper\n",
    "uppercasecount(\"file1.txt\")"
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
       "['Test 0 line',\n",
       " 'Test 1 line',\n",
       " 'Test 2 line',\n",
       " 'Test 3 line',\n",
       " 'Test 4 line',\n",
       " 'Test 5 line',\n",
       " 'Test 6 line',\n",
       " 'Test 7 line',\n",
       " 'Test 8 line',\n",
       " 'Test 9 line',\n",
       " '']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def countoflines(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=x.split(\"\\n\")\n",
    "    return lst\n",
    "countoflines(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def countoflines(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=x.split(\"\\n\")\n",
    "    return len(lst)\n",
    "countoflines(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Test 0 line\r\n",
      "Test 1 line\r\n",
      "Test 2 line\r\n",
      "Test 3 line\r\n",
      "Test 4 line\r\n",
      "Test 5 line\r\n",
      "Test 6 line\r\n",
      "Test 7 line\r\n",
      "Test 8 line\r\n",
      "Test 9 line\r\n"
     ]
    }
   ],
   "source": [
    "cat file1.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
    "createfile(\"file1.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is 0 line\r\n",
      "this is 1 line\r\n",
      "this is 2 line\r\n",
      "this is 3 line\r\n",
      "this is 4 line\r\n",
      "this is 5 line\r\n",
      "this is 6 line\r\n",
      "this is 7 line\r\n",
      "this is 8 line\r\n",
      "this is 9 line\r\n"
     ]
    }
   ],
   "source": [
    "cat file1.txt"
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
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
