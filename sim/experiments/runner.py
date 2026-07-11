"""Run execution, multi-seed replication, parallelisation.

Each run's seed is derived from the hash of its config for full reproducibility;
results are written with the config embedded. Configs (one YAML per experiment,
E1-E6 and V1-V3) live in sim/experiments/configs/. See §3 and §4.
"""
