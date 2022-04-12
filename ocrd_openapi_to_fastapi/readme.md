Generate webservice skeleton from ocrd's openapi.yml

<https://github.com/koxudaxi/fastapi-code-generator>

### Install fastapi uvicorn and code generator
`sudo pacman -S python-fastapi uvicorn`
`pip install --user fastapi-code-generator`

### Download openapi from ocrd-spec
`wget https://raw.githubusercontent.com/OCR-D/spec/master/openapi.yml`

### generate stub
`fastapi-codegen --input openapi.yml --output app`
- error occurs. [For workaround](# Errors)

### first test-run
`
uvicorn app.main:app --host 0.0.0.0 --reload
`
- error occurs. [For workaround](# Errors)

### Errors:
- TypeError: unsupported operand type(s) for /: 'tuple' and 'str'
    - https://github.com/koxudaxi/fastapi-code-generator/issues/232
    - file ~/.local/lib/python3.10/site-packages/datamodel_code_generator/format.py
        - file maybe somewhere else depending on os, installation-method etc.
    - change line 45 from `path = root / "pyproject.toml"` to `path = root[0] / "pyproject.toml"`
- AssertionError: Path params must be of one of the supported types
    - just remove type for `executable` to workaround error:
    - sed 's/executable:\ [A-Za-z]*/executable/' app/main.py -i
