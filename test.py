import yaml
import parser
def get_standard( path):
    '''
    :param path: 标准文件的路径
    '''
    f = open(path,'r',encoding='utf-8')
    standard = yaml.load(f, Loader=yaml.FullLoader)

    return standard
print(get_standard('cfg2.yml')['CHECK'])