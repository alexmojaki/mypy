# Stubs for sqlalchemy.sql.expression (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from . import functions
from . import elements
from . import base
from . import selectable
from . import dml

func = functions.func
modifier = functions.modifier
ClauseElement = elements.ClauseElement
ColumnElement = elements.ColumnElement
not_ = elements.not_
collate = elements.collate
literal_column = elements.literal_column
between = elements.between
literal = elements.literal
outparam = elements.outparam
type_coerce = elements.type_coerce
ColumnCollection = base.ColumnCollection
Alias = selectable.Alias
Join = selectable.Join
Select = selectable.Select
Selectable = selectable.Selectable
TableClause = selectable.TableClause
CompoundSelect = selectable.CompoundSelect
FromClause = selectable.FromClause
alias = selectable.alias
subquery = selectable.subquery
Insert = dml.Insert
Update = dml.Update
Delete = dml.Delete

and_ = ... # type: Any
or_ = ... # type: Any
bindparam = ... # type: Any
select = ... # type: Any
text = ... # type: Any
table = ... # type: Any
column = ... # type: Any
over = ... # type: Any
label = ... # type: Any
case = ... # type: Any
cast = ... # type: Any
extract = ... # type: Any
tuple_ = ... # type: Any
except_ = ... # type: Any
except_all = ... # type: Any
intersect = ... # type: Any
intersect_all = ... # type: Any
union = ... # type: Any
union_all = ... # type: Any
exists = ... # type: Any
nullsfirst = ... # type: Any
nullslast = ... # type: Any
asc = ... # type: Any
desc = ... # type: Any
distinct = ... # type: Any
null = ... # type: Any
join = ... # type: Any
outerjoin = ... # type: Any
insert = ... # type: Any
update = ... # type: Any
delete = ... # type: Any
