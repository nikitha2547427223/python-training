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
      "contact nikki added\n",
      "contact vani added\n",
      "contact sush added\n"
     ]
    }
   ],
   "source": [
    "contacts={}\n",
    "def addcontact(name,phone):\n",
    "    if name not in contacts:\n",
    "        contacts[name]=phone\n",
    "        print(\"contact %s added\" % name)\n",
    "    else:\n",
    "        print(\"contact %s already exists\" % name)\n",
    "    return\n",
    "addcontact(\"nikki\",1234512345)\n",
    "addcontact(\"vani\",1234554321)\n",
    "addcontact(\"sush\",1122334455)\n"
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
      "nikki : 1234512345\n",
      " nikitha does not exists\n",
      "vani : 1234554321\n",
      "sush : 1122334455\n",
      " niki does not exists\n"
     ]
    }
   ],
   "source": [
    "def searchcontact(name):\n",
    "    if name in contacts:\n",
    "        print(name,\":\",contacts[name])\n",
    "    else:\n",
    "        print(\" %s does not exists\" % name)\n",
    "    return\n",
    "searchcontact(\"nikki\")\n",
    "searchcontact(\"nikitha\")\n",
    "searchcontact(\"vani\")\n",
    "searchcontact(\"sush\")\n",
    "searchcontact(\"niki\")"
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
      "2 contacts added successfully\n"
     ]
    }
   ],
   "source": [
    "def importcontacts(newcontacts):\n",
    "    contacts.update(newcontacts)\n",
    "    print(len(newcontacts.keys()),\"contacts added successfully\")\n",
    "    return\n",
    "newcontacts={\"arjun\":993618402,\"varun\":925197463}\n",
    "importcontacts(newcontacts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'arjun': 993618402, 'varun': 925197463}\n"
     ]
    }
   ],
   "source": [
    "print(contacts)"
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
      "vani is not exists in  the contacts\n",
      "varun is deleted from the contacts\n"
     ]
    }
   ],
   "source": [
    "def deletecontact(name):\n",
    "    if name in contacts:\n",
    "        del contacts[name]\n",
    "        print(name,\"is deleted from the contacts\")\n",
    "    else:\n",
    "         print(name,\"is not exists in  the contacts\")\n",
    "    return\n",
    "deletecontact(\"vani\")\n",
    "deletecontact(\"varun\")"
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
      "{'arjun': 993618402}\n"
     ]
    }
   ],
   "source": [
    "print(contacts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "arjun :updated with new phone number\n",
      "varun is not exists in  the contacts\n"
     ]
    }
   ],
   "source": [
    "def updatecontacts(name,phone):\n",
    "    if name in contacts:\n",
    "        print(name,\":updated with new phone number\")\n",
    "    else: \n",
    "        print(name,\"is not exists in  the contacts\")\n",
    "    return\n",
    "updatecontacts(\"arjun\",9966552211)\n",
    "updatecontacts(\"varun\",952197464)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'arjun': 993618402}\n"
     ]
    }
   ],
   "source": [
    "print(contacts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value at: {0} value at : {1} (1, 2)\n",
      "value at: {2} value at : {3} (3, 4)\n"
     ]
    }
   ],
   "source": [
    "lst=[1,2,3,4]\n",
    "print(\"value at: {0} value at : {1}\",format((lst[0],lst[1])))\n",
    "print(\"value at: {2} value at : {3}\",format((lst[2],lst[3])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import factorial as fact\n",
    "fact(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "123"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import floor as f1\n",
    "f1(123.46)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "math.factorial(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "103 114 83 109 76 51 36 115 17 105 "
     ]
    }
   ],
   "source": [
    "import random\n",
    "def generaterandomnumbers(n,lb,ub):\n",
    "    for i in range(0,n):\n",
    "        print(random.randint(lb,ub),end=\" \")\n",
    "    return\n",
    "generaterandomnumbers(10,12,120)    "
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
