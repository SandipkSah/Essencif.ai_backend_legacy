export PYTHONPATH=$(pwd)
pytest -sv . > ./results/result_$(date +"%Y%m%d_%H%M%S").txt
