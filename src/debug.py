import sys, importlib.util, pkgutil, os

spec = importlib.util.find_spec("numpy")
print("找到了 numpy spec ->", spec)
for m in pkgutil.iter_modules():
    if m.name == "numpy":
        print("pkgutil 发现 numpy 来自:", m.module_finder)
