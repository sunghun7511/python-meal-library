# Python meal library
## Introduce
This repository is a module that parse meals to Korean schools.  

## How to use
This module has only one function called `getMeal`.

```python
def getMeal(
        year="{:04d}".format(datetime.datetime.now().year),
        month="{:02d}".format(datetime.datetime.now().month),
        schoolcode="G100000170",
        schooltype="4")
```

### `year`
This field is year when you want parsing.
> ex) `2017`, `2016`
### `month`
This field is month when you want parsing.
> ex) `01`, `02`, `12`
### `schoolcode`
This field is school code what you want parsing.
You can find school code on [this site](https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do)
> ex) `G100000170`
### `schooltype`
This field is school type what you want parsing.
- 1 : kindergarden
- 2 : elementary school
- 3 : middle school
- 4 : high school