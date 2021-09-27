def func_executor(*args, functions_returns=[]):
    for func in args:
        function,arguments = func[0],list(map(lambda x: x,func[1]))
        functions_returns.append(function(*arguments))
    return functions_returns