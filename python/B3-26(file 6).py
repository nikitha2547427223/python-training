{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    1\n",
      "1    3\n",
      "2    4\n",
      "3    5\n",
      "4    6\n",
      "5    7\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "a=pd.Series([1,3,4,5,6,7])\n",
    "print(a)"
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
      "0    1.0\n",
      "1    2.0\n",
      "2    3.0\n",
      "3    4.0\n",
      "4    NaN\n",
      "5    5.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=pd.Series([1,2,3,4,np.nan,5])\n",
    "print(a1)"
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
      "DatetimeIndex(['2019-06-01', '2019-06-02', '2019-06-03', '2019-06-04',\n",
      "               '2019-06-05', '2019-06-06', '2019-06-07', '2019-06-08',\n",
      "               '2019-06-09', '2019-06-10', '2019-06-11', '2019-06-12',\n",
      "               '2019-06-13', '2019-06-14', '2019-06-15', '2019-06-16',\n",
      "               '2019-06-17', '2019-06-18', '2019-06-19', '2019-06-20'],\n",
      "              dtype='datetime64[ns]', freq='D')\n"
     ]
    }
   ],
   "source": [
    "dates=pd.date_range('20190601',periods=20)\n",
    "print(dates)"
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
      "     A          B    C  D      E    F\n",
      "0  1.0 2019-06-01  1.0  3   test  foo\n",
      "1  1.0 2019-06-01  1.0  3  train  foo\n",
      "2  1.0 2019-06-01  1.0  3   test  foo\n",
      "3  1.0 2019-06-01  1.0  3  train  foo\n"
     ]
    }
   ],
   "source": [
    "a2=pd.DataFrame({'A':1.,\n",
    "                'B':pd.Timestamp('20190601'),\n",
    "                'C':pd.Series(1,index=list(range(4)),dtype='float32'),\n",
    "                'D':np.array([3]*4,dtype='int32'),\n",
    "                'E':pd.Categorical([\"test\",\"train\",\"test\",\"train\"]),\n",
    "                'F':'foo'})\n",
    "print(a2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "tt.forward(100)\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "for x in range(40):\n",
    "    a1.forward(50)\n",
    "    a1.right(144)\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "for i in range(40):\n",
    "    a1.forward(i*10)\n",
    "    a1.right(144)\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Turtle' object has no attribute 'pencolour'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-721a77fc32b2>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mturtle\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mtt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0ma1\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTurtle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0ma1\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpencolour\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"blue\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m40\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0ma1\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mforward\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'Turtle' object has no attribute 'pencolour'"
     ]
    }
   ],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "a1.pencolour(\"blue\")\n",
    "for i in range(40):\n",
    "    a1.forward(i*10)\n",
    "    a1.right(144)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "c1=tt.Turtle()\n",
    "c1.pencolor(\"blue\")\n",
    "for i in range(50):\n",
    "    c1.forward(50)\n",
    "    c1.left(123)\n",
    "c1.pencolor(\"red\")\n",
    "for i in range(50):\n",
    "    c1.forward(100)\n",
    "    c1.left(123)\n",
    "tt.done()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "colours=['red','blue','orange','green','yellow','purple']\n",
    "c1=tt.Turtle()\n",
    "for x in range(360):\n",
    "    c1.pencolor(colours[x%6])\n",
    "    c1.width(x/100+1)\n",
    "    c1.forward(x)\n",
    "    c1.left(59)\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "colors=['red','blue','orange','green','yellow','purple']\n",
    "dot_distance=10\n",
    "width=10\n",
    "height=15\n",
    "a1.penup()\n",
    "for x in range(height):\n",
    "    a1.pencolor(colors[x%6])\n",
    "    for i in range(width):\n",
    "        a1.dot()\n",
    "        a1.forward(dot_distance)\n",
    "    a1.forward(dot_distance*width)\n",
    "    a1.right(90)\n",
    "    a1.forward(dot_distance)\n",
    "    a1.left(90)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from turtle import *\n",
    "import random\n",
    "for n in range(50):\n",
    "    penup()\n",
    "    goto(random.randint(-400,400),random.randint(-400,400))\n",
    "    pendown()\n",
    "    red_amount=random.randint(0,30)/100.0\n",
    "    blue_amount=random.randint(50,100)/100.0\n",
    "    green_amount=random.randint(0,30)/100.0\n",
    "    pencolor((red_amount,blue_amount,green_amount))\n",
    "    circle_size =random.randint(10,40)\n",
    "    pensize(random.randint(4,6))\n",
    "    for i in range(6):\n",
    "        circle(circle_size)\n",
    "        left(60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from turtle import *\n",
    "def main():\n",
    "    colors=['red','orange','yellow','seagreen4','orchid4','royalblue1','dodgerblue']\n",
    "    reset()\n",
    "    Screen()\n",
    "    up()\n",
    "    goto(-320,-195)\n",
    "    width(90)\n",
    "    for pcolor in colors:\n",
    "        color(pcolor)\n",
    "        down()\n",
    "        forward(640)\n",
    "        up()\n",
    "        backward(640)\n",
    "        left(90)\n",
    "        forward(66)\n",
    "        right(90)\n",
    "       \n",
    "    width(55)\n",
    "    color('white')\n",
    "    goto(0,-170)\n",
    "    down()\n",
    "   \n",
    "    circle(170)\n",
    "    left(90)\n",
    "    forward(340)\n",
    "    up()\n",
    "    left(180)\n",
    "    forward(170)\n",
    "    right(45)\n",
    "    down()\n",
    "    forward(170)\n",
    "    up()\n",
    "    backward(170)\n",
    "    left(90)\n",
    "    down()\n",
    "    forward(170)\n",
    "    up()\n",
    "    goto(0,300)\n",
    "   \n",
    "if __name__=='__main__':\n",
    "    main()\n",
    "    mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from turtle import *\n",
    "\n",
    "N=80\n",
    "\n",
    "def f(x):\n",
    "    return 3.9*x*(1-x)\n",
    "\n",
    "def g(x):\n",
    "    return 3.9*(x-x**2)\n",
    "\n",
    "def h(x):\n",
    "    return 3.9*x-3.9*x*x\n",
    "\n",
    "def jumpto(x,y):\n",
    "    penup()\n",
    "    goto(x,y)\n",
    "   \n",
    "def line(x1,y1,x2,y2):\n",
    "    jumpto(x1,y1)\n",
    "    pendown()\n",
    "    jumpto(x2,y2)\n",
    "   \n",
    "def coosys() :\n",
    "    line(-1,0,N+1,0)\n",
    "    line(0,-0-1,0,1.1)\n",
    "\n",
    "def plot(fun,start,color):\n",
    "    pencolor(color)\n",
    "    x=start\n",
    "    jumpto(0,x)\n",
    "    pendown()\n",
    "    dot(5)\n",
    "    for i in range(N):\n",
    "        x=fun(x)\n",
    "        goto(i+1,x)\n",
    "        dot(5)\n",
    "def main():\n",
    "    reset()\n",
    "    setworldcoordinates(-1.0,-1.0,N+1,1.1)\n",
    "    speed(0)\n",
    "    hideturtle()\n",
    "    coosys()\n",
    "    plot(f,0.35,\"blue\")\n",
    "    plot(g,0.35,\"green\")\n",
    "    plot(h,0.35,\"red\")\n",
    "   \n",
    "   \n",
    "    for s in range(100):\n",
    "        setworldcoordinates(0.5*s,-0.1,N+1,1.1)\n",
    "    return \"Done!!\"\n",
    "if __name__==\"__main__\":\n",
    "    main()\n",
    "    mainloop()"
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
