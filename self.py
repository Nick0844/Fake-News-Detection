class x:
    def __int__(self,a,b,c):
        self.a=public;
        self._b=protected;
        self.__c=private;
    def display(self):
        print("a is public: ",self.a);
        print("b is protected: ",self._b);
        print("c is private: ",self.__c);

y=x()
y.display
