#### nginx

```yml
# 创建容器
docker run -d --name nginx_xv -p 82:80 --privileged=true nginx
# 复制配置文件以及数据目录
docker cp nginx_xv:/etc/nginx ./nginx
docker cp nginx_xv:/var/log/nginx ./nginx_logs
docker cp nginx_xv:/usr/share/nginx/html ./html
# 移除容器
docker rm -f <container_name>
# 使用 docker-compose 启动容器
docker-compose up -d
```

#### mysql

```yml
# 创建容器
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=888888 --name mysql_xv mysql

# 复制配置文件以及数据目录
docker cp mysql_xv:/var/lib/mysql ./data
docker cp mysql_xv:/etc/mysql/conf.d ./mysql.d

# 更新密码
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '888888';

# 移除容器
docker rm -f <container_name>

# 使用 docker-compose 启动容器
docker-compose up -d
```

#### gitea

```yml
docker pull gitea/gitea

docker run -d --name=gitea -p 10022:22 -p 10080:3000 -v /var/lib/gitea:/data gitea/gitea:latest
docker cp gitea:/data ./data

# 移除容器
docker rm -f gitea

docker-compose up -d
```