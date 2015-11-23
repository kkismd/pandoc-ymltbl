pandoc-ymltbl
-------------

a Source block with language identifier `ymltbl`.

````ymltbl
-
  - A
  - False
  - False
  - False
-
  - B
  - True
  - False.
  - False
-
  - False
  - True
  - False
-
  - A and B
  - True
  - True
  - True
````

will converted to table notation.

| A     | B     | A and B |
|-------|-------|---------|
| False | False | False   |
| True  | False | False   |
| False | True  | False   |
| True  | True  | True    |
