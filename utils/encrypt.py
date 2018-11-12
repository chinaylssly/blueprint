#_*_ coding:utf-8 _*_

import base64
import chardet

'''
本module用来加解密密码，图片base64加密

'''
class Encrypt(object):

    ##base64加密不要出现中文

    def __init__(self,salt=u'key'):

        assert isinstance(salt,unicode)
        self.salt=salt

    @classmethod
    def to_unicode(self,string):
        ##字符串转化为unicode编码
        if isinstance(string,unicode):
            return string
        else:
            result=chardet.detect(string)
            confidence=result.get('confidence')
            
            if confidence>0.9:
                encoding=result.get('encoding')

            else:

                print u'chardet结果不可靠，将使用utf-8解码'
                encoding='utf-8'
                
            return string.decode(encoding,'ignore')


    @classmethod
    def b64encode(self,s):
        #base加密

        s=self.to_unicode(s)
        return base64.b64encode(s)


    @classmethod
    def b64decode(self,m):
        #base64解密

        return base64.b64decode(m)



    def b64encode_with_salt(self,s):

        s=self.to_unicode(s)
        s=u'%s-%s'%(self.salt,s)
        return base64.b64encode(s)


    def b64decode_with_salt(self,m):

        return base64.b64decode(m).split('-',1)[1]


    @classmethod
    def img_b64encode(self,path):

        with open(path,'rb')as f:

            r=f.read()


        return base64.b64encode(r)








def test():

    s=u'qqqqqq'
    m=Encerpt.b64encode(s)
    ds=Encerpt.b64decode(m)

    print s
    print m
    print ds

    assert s==ds


def test_salt():

    s=u'qqqqqq'
    encrypt=Encerpt()
    salt=encrypt.salt
    m=encrypt.b64encode_with_salt(s)
    ds=encrypt.b64decode_with_salt(m)
    print s
    print m
    print ds
    print salt

    assert s==ds







if __name__ =='__main__':

    test()
    test_salt()