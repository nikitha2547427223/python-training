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
      "test()for the class and method\n"
     ]
    }
   ],
   "source": [
    "class demo:\n",
    "    def test(self):\n",
    "        print(\"test()for the class and method\")\n",
    "        return \n",
    "obj=demo()\n",
    "obj.test()"
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
      "test()for function\n"
     ]
    }
   ],
   "source": [
    "def test():\n",
    "        print(\"test()for function\")\n",
    "        return \n",
    "test()"
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
      "120\n"
     ]
    }
   ],
   "source": [
    "class demo1:\n",
    "    def fact(self,n):\n",
    "        fact=1\n",
    "        while(n!=0):\n",
    "            fact=fact*n\n",
    "            n=n-1\n",
    "        return fact\n",
    "p1=demo1()\n",
    "print(p1.fact(5))"
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
      "30\n"
     ]
    }
   ],
   "source": [
    "class demo2:\n",
    "    def _init_(self,p1,p2):\n",
    "        self.p1=p1\n",
    "        self.p2=p2\n",
    "    def add(self,p1,p2):\n",
    "        return p1+p2\n",
    "c1=demo2()\n",
    "print(c1.add(10,20))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "person() takes no arguments",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-8afd343ac2c9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0misemployee\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m \u001b[0memp\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mperson\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Anil\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0memp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetname\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0memp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0misemployee\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: person() takes no arguments"
     ]
    }
   ],
   "source": [
    "class person(object):\n",
    "    def _init_(self,name):\n",
    "        self.name=name\n",
    "    def getname(self):\n",
    "        return self.name\n",
    "    def isemployee(self):\n",
    "        return False\n",
    "class employee(person):\n",
    "    def isemployee(self):\n",
    "        return True\n",
    "emp=person(\"Anil\")\n",
    "print(emp.getname(),emp.isemployee())\n",
    "           \n",
    "emp1=person(\"Anvitha\")\n",
    "print(emp.getname(),emp.isemployee())\n",
    "           "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "lst=[1,2,3,4]\n",
    "print(lst)"
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
      "(4,)\n",
      "int64\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "lst=[1,2,3,4]\n",
    "array=np.array(lst)\n",
    "print(array.shape)\n",
    "print(array.dtype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "lst=[1,2,3,4]\n",
    "array=np.array(lst)\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([1,2,3])\n",
    "a2=np.array([4,5,6])\n",
    "print(np.hstack((a1,a2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([1,2,3])\n",
    "a2=np.array([4,5,6])\n",
    "print(np.vstack((a1,a2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4.19012864 4.95358409 5.19917599 4.75976347 4.57013263 4.98279431\n",
      " 5.06750293 5.27426154 4.3458372  4.95275312]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.random.normal(5,0.5,10)\n",
    "print(a1)"
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
       "array([[0., 0.],\n",
       "       [0., 0.]])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.zeros((2,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 0],\n",
       "       [0, 0]])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.zeros((2,2),dtype=np.int64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 1, 1],\n",
       "       [1, 1, 1],\n",
       "       [1, 1, 1],\n",
       "       [1, 1, 1]])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.ones((4,3),dtype=np.int64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 1 1 1]\n",
      " [1 1 1 1]\n",
      " [1 1 1 1]\n",
      " [1 1 1 1]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.matrix(np.ones((4,4),dtype=np.int64))\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 1 1 1]\n",
      " [1 1 1 1]\n",
      " [5 5 5 5]\n",
      " [1 1 1 1]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.matrix(np.ones((4,4),dtype=np.int64))\n",
    "np.asarray(A)[2]=5\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.arange(1,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.arange(1,100,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19, 21, 23])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.arange(1,20,2)\n",
    "np.arange(1,25,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first row: [1 2 3]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([(1,2,3),(4,5,6)])\n",
    "print(\"first row:\",a1[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "slicing column: [2 5]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([(1,2,3),(4,5,6)])\n",
    "print(\"slicing column:\",a1[:,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([(1,2,3),(4,5,6)])\n",
    "print (a1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "second row: [4 5 6]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([(1,2,3),(4,5,6)])\n",
    "print(\"second row:\",a1[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "slicing last column: [3 6]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([(1,2,3),(4,5,6)])\n",
    "print(\"slicing last column:\",a1[:,2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "slicing last column: [4]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=np.array([(1,2,3),(4,5,6)])\n",
    "print(\"slicing last column:\",a1[1,:1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3.67012727 3.67863718 3.76432291 5.04986583 6.37773202 5.59962722\n",
      " 6.16863148 2.28707418 5.46030007 5.65833158]\n",
      "min value= 2.2870741766515033\n",
      "max value= 6.377732017997909\n",
      "mean value= 4.771464972744714\n",
      "median value= 5.255082949826155\n"
     ]
    }
   ],
   "source": [
    "a1=np.random.normal(5,1,10)\n",
    "print(a1)\n",
    "print(\"min value=\",np.min(a1))\n",
    "print(\"max value=\",np.max(a1))\n",
    "print(\"mean value=\",np.mean(a1))\n",
    "print(\"median value=\",np.median(a1))\n",
    "\n"
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
      "      name            emailid  mobilenumber address\n",
      "0    arjun    arjun@gmail.com           999     hyd\n",
      "1    varun    varun@gmail.com           888     hyd\n",
      "2  goutham  goutham@gmail.com           777     hyd\n",
      "3    dolly    dolly@gmail.com           666     hyd\n",
      "4     sush     sush@gmail.com           555     hyd\n",
      "5     srav     srav@gmail.com           444     hyd\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "dict={\"name\":[\"arjun\",\"varun\",\"goutham\",\"dolly\",\"sush\",\"srav\"],\"emailid\":[\"arjun@gmail.com\",\"varun@gmail.com\",\"goutham@gmail.com\",\"dolly@gmail.com\",\"sush@gmail.com\",\"srav@gmail.com\"],\"mobilenumber\":[999,888,777,666,555,444],\"address\":[\"hyd\",\"hyd\",\"hyd\",\"hyd\",\"hyd\",\"hyd\"]}\n",
    "b=pd.DataFrame(dict)\n",
    "print(b)"
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
