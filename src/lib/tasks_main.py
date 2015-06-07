import importlib

taskheaders = {
  'nowplaying': {}
}

def run_tasks():
  for taskname in taskheaders:
   module = importlib.import_module('src.lib.tasks.%s' % taskname)
   task = getattr(module, taskname);
   task().start();