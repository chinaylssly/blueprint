#_*_ coding:utf-8 _*_
import os


'''

获取不在项目目录下的book

'''
class Book(object):

    def __init__(self,):

        self.get_path()
        self.get_category()
        self.get_book()


    def get_path(self,):

        self.path_dict={'xp':u'f:/data/data',
                        'short':u'f:/data/books/class/putty',
                        'part':u'f:/data/books/putty',
                        # 'long':u'f/data/books/book/long'
                        }



    def get_category(self,):

        category_dict={}
        for key,value in self.path_dict.items():

            if 'long' not in key:

                folders=os.listdir(value)
                l=[]
                for folder in folders:
                    
                    if len(folder.split('.'))>1:
                        # print folder
                        folders.remove(folder)

                    else:
                        l.append(folder)


                category_dict[key]=l

        self.category_dict=category_dict



    def get_book(self,):

        book_dict={}

        for key,value in self.category_dict.items():
            folder_dict={}
            for folder in value:

                path=self.path_dict.get(key)
                full_folder=u'%s/%s'%(path,folder)

                filenames=os.listdir(full_folder)

                folder_dict[folder]=filenames
            book_dict[key]=folder_dict

        self.book_dict=book_dict


    @classmethod
    def read_book_to_lines(self,filepath):

        with open(filepath,'r')as f:
            r=f.read().decode('utf-8','ignore')

        lines=r.split('\n')

        return lines






def test():

    book=Book()
    import json

    category_dict=book.category_dict
    book_dict=book.book_dict
    print json.dumps(category_dict,ensure_ascii=False)
    print json.dumps(book_dict,ensure_ascii=False)


if __name__=='__main__':

    test()




        