"""pytest Blocklist"""

from absl import app

collect_ignore = [
  "discussion/",
  "setup.py",
]

def pytest_addoption(parser):
  parser.addoption(
    "--absl-flag",
    action="append",
    help="pass flag to absl such as `--absl-flag='--vary_seed'`",
    default=[]
  )

def pytest_collection_finish(session):
  # `pytest`, unlike bazel doesn't run `tf.test.run()` (that parses flags) - external devs using pytest we parse flags directly
  absl_flags = session.config.getoption("absl_flag", default=[])
  app._register_and_parse_flags_with_usage(["test.py"] + absl_flags) # pylint: disable=protected-access