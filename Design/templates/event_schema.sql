-- schema.sql

-- Events database for calendar

-- Ability to import various calendars into this like US Holidays

create table usercal (
     id                    integer primary key autoincrement not null,
     user_id        ?,
     iday           integer,       --initial day of week Sunday =0 Monday=1 unix style
     cals           text,  --list of calendars in use
     ccals          text, --list of calendar colors in order?
     colors         ?
);

create table event (
     id                    integer primary key autoincrement not null,
     calendar       text,
     category       text,
     idate              date/time start
     fdate              date/time stop
     recurring     text,
     description    text,
     location       text
);
