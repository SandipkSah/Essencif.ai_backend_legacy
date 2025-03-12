export PYTHONPATH=$(pwd)
pytest -sv tests/ > .tests/results/result_$(date +"%Y%m%d_%H%M%S").txt
