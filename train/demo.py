class Demo(object):
    def __init__(self,a=None,*args,**kwargs):
        self.a=a
        #import pdb;pdb.set_trace()
    def get_a(self):
        return self.a
    @property
    def b(self):
        b="b2b"
        return b

if __name__== '__main__':
    demo=Demo('int a','int b','int_c',d='init_d')
    print demo.get_a()
    print demo.b