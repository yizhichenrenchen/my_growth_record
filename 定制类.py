class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self, path):
        if path == 'users':
            return lambda name:Chain('%s/users/:%s' % (self._path,name))
        else:
            return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__
#以上代码还需继续打磨，此处只抄写百人代码以便后续进行修改
#此处引出链式调用