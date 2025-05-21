# `whenever-bug`

```console
.../whenever-bug on  dev [+] is 📦 v0.1.1 via 🐍 v3.13.0 (whenever-bug)
❯ pytest
=================================================================================== test session starts ===================================================================================
platform darwin -- Python 3.13.0, pytest-8.3.5, pluggy-1.6.0 -- /Users/derekwan/work/whenever-bug/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/derekwan/work/whenever-bug
configfile: pyproject.toml
testpaths: src/tests
collected 1 item

src/tests/test_main.py::test_main Fatal Python error: Aborted

Current thread 0x00000001f0661f00 (most recent call first):
  File "/Users/derekwan/work/whenever-bug/src/tests/test_main.py", line 7 in test_main
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/python.py", line 159 in pytest_pyfunc_call
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/python.py", line 1627 in runtest
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/runner.py", line 174 in pytest_runtest_call
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/runner.py", line 242 in <lambda>
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/runner.py", line 341 in from_call
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/runner.py", line 241 in call_and_report
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/runner.py", line 132 in runtestprotocol
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/runner.py", line 113 in pytest_runtest_protocol
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/main.py", line 362 in pytest_runtestloop
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/main.py", line 337 in _main
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/main.py", line 283 in wrap_session
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/main.py", line 330 in pytest_cmdline_main
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 175 in main
  File "/Users/derekwan/work/whenever-bug/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 201 in console_main
  File "/Users/derekwan/work/whenever-bug/.venv/bin/pytest", line 10 in <module>

Extension modules: whenever._whenever (total: 1)
[1]    68354 abort      pytest
```
