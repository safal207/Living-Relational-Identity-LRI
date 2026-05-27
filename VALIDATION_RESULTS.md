# LRI Validation Results

Tracked validation snapshot for the current LRI reference implementation and protocol assets.

## Summary

- Validation command: `python scripts/validate_project.py`
- Exit status: **PASS**

## Output

```text
[lri-reference pytest] status=PASS
................                                                         [100%]
============================== warnings summary ===============================
..\..\..\..\..\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\starlette\formparsers.py:12
  C:\Users\safal\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\starlette\formparsers.py:12: PendingDeprecationWarning: Please use `import python_multipart` instead.
    import multipart

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
16 passed, 1 warning in 5.57s
C:\Users\safal\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\_pytest\pathlib.py:98: PytestWarning: (rm_rf) error removing \\?\C:\Users\safal\AppData\Local\Temp\pytest-of-safal\garbage-c16460a2-350e-400d-859c-a4f5b0688c3c
<class 'OSError'>: [WinError 145] \u041f\u0430\u043f\u043a\u0430 \u043d\u0435 \u043f\u0443\u0441\u0442\u0430: '\\\\?\\C:\\Users\\safal\\AppData\\Local\\Temp\\pytest-of-safal\\garbage-c16460a2-350e-400d-859c-a4f5b0688c3c'
  warnings.warn(

Project validation passed.
```
