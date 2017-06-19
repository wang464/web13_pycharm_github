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
service supervisor restart\

重启nginx
nginx -s reload