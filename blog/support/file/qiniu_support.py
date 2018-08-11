import qiniu.config
from qiniu import Auth, etag, put_file

# 需要填写你的 Access Key 和 Secret Key
access_key = 'LYgEIxfrKt7h6tf2ero1VrtwxxqUr1qmIuqhiV2n'
secret_key = 'PTihHOOPlnNDgoi25fo4x7JvSZ8lX2zAw3cqXuUX'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'image'
# 上传到七牛后保存的文件名
key = 'my-python-logo.jpeg'
# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
# 要上传文件的本地路径
localfile = '/Users/pengfei.you/Downloads/WechatIMG14560.jpeg'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
