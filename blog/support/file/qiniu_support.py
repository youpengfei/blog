import qiniu.config
from qiniu import Auth, etag, put_file
from configparser import ConfigParser

cf = ConfigParser()
cf.read("/Users/pengfei.you/conf/config.ini")

# 需要填写你的 Access Key 和 Secret Key
access_key = cf.get("qiniu", "access_key")
secret_key = cf.get("qiniu", "secret_key")


def get_token(bucket_name, key, timeout):
    '''
    获取上传的token
    :param bucket_name: 上传未知
    :param key:  上传后的名称
    :param timeout: token 超时时间
    :return: 生成的token 给前端用
    '''
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, timeout)
    return token
