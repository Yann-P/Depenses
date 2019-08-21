# Dépenses.py

The purpose of this web app is to organize a budget within a group with shared expenditures.

*Live demo :* http://s.yann-p.fr:3031

## Features

 - Keep track of expenditures and reimbursements within groups
 - Calculates who owns money to who (takes expentidures and reimbursements in account)
 - Very easy to use
 - Translated in English and in French.

## Author
Yann Pellegrini \<mail ∀τ yann-p • fr\>

## Licence
GPLv3


## Dependencies

 - Python 3
 - MySQL
 - or docker + compose to run out of the box.


## Database

![schema](tables.png)


## Running

 - choose your port and database pw in docker-compose.yml
 - **WARNING : CHANGE THE APPLICATION SECRET KEY IN `app.py`**, otherwise the sessions are not secure.
 - docker-compose up -d

