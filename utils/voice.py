#_*_ coding:utf-8 _*_
import os,sys
import json


root=u'e:/psftp/voice'

class Voice(object):

    @classmethod
    def read_folder_txt(self,):

        folder_Dict={}
        folder_txt=u'%s/floder.txt'%(root)
        with open(folder_txt,'r')as f:
            lines=f.readlines()

        for line in lines:

            num,title=line.strip().decode('utf-8','ignore').split(',')
            folder_Dict[num]=title

        return folder_Dict



    @classmethod
    def read_name_txt(self,folder):
        name_Dict={}
        full_folder=u'%s/%s'%(root,folder)


        try:
            int(folder)
            name_txt=u'%s/name.txt'%(full_folder)
            with open(name_txt,'r')as f:
                lines=f.readlines()

            for line in lines:

                title,num=line.strip().decode('utf-8','ignore').split(',')
                num_mp3=num.rsplit('/',1)[1]
                title_mp3=title.rsplit('/',1)[1]
                name_Dict[num_mp3]=title_mp3

            return name_Dict
                


        except:

            print u'folder do not need change'
            return {}


    @staticmethod
    def print_dict(Dict={}):

        print json.dumps(Dict,ensure_ascii=False)


    @classmethod
    def get_folder_list(self,):

        folders=os.listdir(root)

        for folder in folders:

            if u'.' in folder:
                folders.remove(folder)

        folder_List=folders
        return folder_List

    @classmethod
    def get_src(self,folder):

        full_folder=u'%s/%s'%(root,folder)
        name_Dict=self.read_name_txt(folder=folder)
        src_list=[]
        filenames=os.listdir(full_folder)

        for filename in filenames:
            

            if 'mp3' in filename:
                title=name_Dict.get(filename,filename)
                src='voice/%s/%s'%(folder,filename)
                t=(title,src)
                src_list.append(t)

        src=sorted(src_list)

        return src

        









def test():


    # print Voice.print_dict(Voice.read_folder_txt())
    # print Voice.print_dict(Voice.read_name_txt('1'))

    print Voice.print_dict(Voice.get_folder_list())
    print Voice.print_dict(Voice.get_src('1'))



if __name__ =='__main__':

    test()