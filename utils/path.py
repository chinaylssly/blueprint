#_*_ coding:utf-8 _*_
import os,sys
import json

if __name__=='__main__':

    sys.path.append(u'../')

from config import ROOT


'''
本模块用来获取图片的路径，对应url前缀为：image

'''
class Path(object):

    
    @classmethod
    def get_img_folder(self,root=u'd:/update'):

        folders=os.listdir(root)

        return folders


    @classmethod
    def get_img_path(self,root,folder):

        folder=u'%s/%s'%(root,folder)

        filenames=os.listdir(folder)


    @classmethod
    def get_category(self,):

        category={
                    u'qingchun':u'清纯',
                    u'meitui':u'美腿',
                    u'xinggan':u'性感',
                    u'update':u'最新',
                 }


        return category

    @classmethod
    def get_category_root(self,):

        root_dict={
             u'qingchun':u'd:/7mm_qingchun',
             u'meitui':u'd:/7mm_meitui',
             u'xinggan':u'd:/7mm_xinggan',
             u'update':u'd:/update',
        }

        return root_dict


    @classmethod
    def get_img_folder_by_category(self,):

        root_dict=self.get_category_root()
        for key,value in root_dict.items():

            folders=self.get_img_folder(root=value)

            root_dict[key]=dict(root=value,folders=folders)

        folder_dict=root_dict

        return folder_dict


    @classmethod
    def get_img_item_by_folder(self,):

        folder_dict=self.get_img_folder_by_category()
        item_dict={}

        for key,value in folder_dict.items():

            root=value.get('root')
            folders=value.get('folders')

            for folder in folders:

                full_folder=u'%s/%s'%(root,folder)

                filenames=os.listdir(full_folder)

                # path_list=[u'%s/%s'%(full_folder,filename) for filename in filenames]

                item_key=u'%s-%s'%(key,folder)

                # item_dict[item_key]=path_list
                item_dict[item_key]=filenames

        return item_dict


    @classmethod
    def write_dict_to_json(self,Dict,name):

        json_file=u'%s/%s.json'%(ROOT,name)

        with open(json_file,'w')as f:

            json_content=json.dumps(Dict,ensure_ascii=False)

            f.write(json_content.encode('utf-8','ignore'))

    @classmethod
    def read_json_to_dict(self,name):

        json_file=u'%s/%s.json'%(ROOT,name)

        with open(json_file,'r')as f:

            json_content=f.read()

        return json.loads(json_content)


    @classmethod
    def write_folder_dict_to_json(self,):

        folder_dict=self.get_img_folder_by_category()
        name=u'folder'

        self.write_dict_to_json(Dict=folder_dict,name=name)


    @classmethod
    def write_item_dict_to_json(self,):

        item_dict=self.get_img_item_by_folder()
        name=u'item'

        self.write_dict_to_json(Dict=item_dict,name=name)










def test():

    print Path.get_category_root()
    # print Path.get_img_folder_by_category()
    # print Path.get_img_item_by_folder()
    Path.write_folder_dict_to_json()
    # print Path.read_json_to_dict(name=u'folder')

    Path.write_item_dict_to_json()




if __name__ =='__main__':

    test()


