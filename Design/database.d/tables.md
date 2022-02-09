# Database Tables used in the Ed's Calendar Application

## List of Tables
|Table|Phase|Description|
|-----|-----|-----------|
|[calendar](#calendar-table)| initial |Information defining a calendar|
|[event](#event-table)| initial |Information defining an event|
|[calendarlist]| initial | events in a calendar |
|[category](#category-table)|initial|Type of event or task/project| 


## Table Definitions and Examples

### calendar Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|rowid |
|name  |text|Name of the calendar.  Examples; USHolidays, Liturgical, Personal, Family |
|type  |text| type of calendar Examples; Gregorian, Jewish, Shire |
|color|


#### Example Rows


### category Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|rowid|integer|
|title|text|
|color|text| border color for category|


#### Example Rows


### event Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|rowid |
|title |text| event title |
|e_start |datetime| date, time, timezone of initial start|
|e_stop   |datetime| date, time, timezone of initial end|
|location|text|
|category|enum

#### Example Rows

|rowid|title|e_start|e_stop|

### calendarlist Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|rowid |
|calendar|key||
|event|key||

#### Example Rows

|rowid|calendar|event|
|-----|--------|-----|



### x Table

#### Definition

|Column|Type|Description|
|------|----|-----------|

#### Example Rows
