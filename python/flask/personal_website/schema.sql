drop table if exists projects;
create table projects (
    id integer primary key autoincrement,
    name string not null,
    description string not null,
    url string
);
