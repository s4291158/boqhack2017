import os


def load_local_env_vars():
    try:
        from env import vars
    except Exception:
        pass
    else:
        for var_name in dir(vars):
            if not var_name.startswith('__'):
                os.environ[var_name] = str(getattr(vars, var_name))
