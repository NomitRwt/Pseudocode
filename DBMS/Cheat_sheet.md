# DBMS SQL Cheat Sheet
The content here is specific to the coarse. Tries to cover elaborate exmples.

## DDL
### Create Table
```
create table table_name(
                        attribute_1 domain_1,
                        attribute_2 domain_2,
                        attribute_3 domain_3,
                        attribute_4 domain_4,
                        attribute_5 domain_5,
                        primary key (attribute1, attribute2),
                        foreign key (attribute3) references some_table
                        foreign key (attribute4, attribute5) references another_table);
```
### Insert
```
insert into table_name values ( alpha, beta, gamma);
```
Or
```
insert into table_name ( attribute_1, attribute_2, attribute_3) values ( alpha, bete, gamma);
```
### Delete (removing all tuples)
```
delete from table_name
```
### Drop Table
```
drop table r
```
### Alter
Adding new attribute
```
alter table_name add attribute_name domain
```
Dropping attribute
```
alter table_name drop attribute_name
```
