# To Do List API

Proyektni ishga tushirish uchun loyiha root katalogidan quyidagi buyruqni ishlating:

```bash
uv run python -m uvicorn src.main:app --reload
```

Agar `uvicorn` paketini to'g'ridan-to'g'ri environment ichida ishlatsangiz, quyidagicha ham mumkin:

```bash
uvicorn src.main:app --reload
```

Eslatma:
- `uv run src.main:app --reload` xato, chunki `uv run` command emas, modul/skriptni bunday argument sifatida qabul qilmaydi.
- `uvicorn run src.main:app --reload` ham xato, chunki `uvicorn` buyruq nomi, `run` esa to'g'ri argument emas.
- `fastapi src.main:app` ham xato, chunki `fastapi` CLI `app`ni import qilish uchun `--app` yoki `python -m` usulini talab qiladi.
