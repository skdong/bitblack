create DATABASE test CHARACTER set utf8;

insert into test.people (name, age) values("李四", 19);

drop user straw;

CREATE USER 'straw'@'%' IDENTIFIED BY '123456';

GRANT ALL ON *.* TO 'straw'@'%';