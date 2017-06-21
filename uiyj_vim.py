'''
# web13-3_pycharm_1
## 设置软连接
### supervisor的配置和软连接
ln -s /root/web13_pycharm_github/web13_pycharm_github.conf /etc/supervisor/conf.d/web13_pycharm_github.conf
### 查看连接状态
ll /etc/supervisor/conf.d/web13_pycharm_github.conf
### Nginx软连接
ln -s /root/web13_pycharm_github/web13_pycharm_github.nginx /etc/nginx/sites-enabled/web13_pycharm_github.nginx
删除默认配置 rm /etc/nginx/sites-enabled/chat
### 查看软连接的内容和状态
内容:
cat /etc/nginx/sites-enabled/web13_pycharm_github.nginx
状态:
ll /etc/nginx/sites-enabled/web13_pycharm_github.nginx
删除默认:
rm /etc/nginx/sites-enabled/default
删除自己创建的
rm /etc/nginx/sites-enabled/web13_pycharm_github.nginx

启动
service supervisor restart

重启nginx
nginx -s reload

#### 6-20更新
增加了一个网页/fei. 一个小人可以跟着鼠标来回移动.

增加了一个bootstrap做的主页
这个里面的内容是用来记录变化的. 之前的内容有点问题. 现在首先要做好的事情是做出一个主页. 适配多端.
之后的内容就是找一个音乐播放器. 之后的内容呢? 暂时就这么多吧. .
#### 我也是醉了. 一个网页写那么多层的保护.我也是醉了. 算了自己写一个出来吧. 之后的内容呢? 以后再说吧.

#### 更新失败了? 还是因为更新的内容太多了?

'''
