use defaultdb;

create table fruit(
	id int primary key,
    name varchar(255),
    family varchar(255),
    orders varchar(255),
    genus varchar(255),
    calories int,
    fats float,
    sugar float,
    carbohydrates float,
    protein float
);

select * from fruit;
